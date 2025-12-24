import asyncio
import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Set, Optional, Any
import tornado.web
import tornado.websocket
import tornado.ioloop
import tornado.httpclient
from tornado.escape import json_encode


class CurrencyRateSubject:
    """Subject по паттерну Наблюдатель."""
    def __init__(self, test_mode: bool = False):
        self._observers: Set[tornado.websocket.WebSocketHandler] = set()
        self._rates: Dict[str, float] = {}
        self._last_update: Optional[datetime] = None
        self._test_mode = test_mode
        self._test_counter = 0

    def attach(self, observer: tornado.websocket.WebSocketHandler) -> None:
        self._observers.add(observer)

    def detach(self, observer: tornado.websocket.WebSocketHandler) -> None:
        self._observers.discard(observer)

    async def fetch_rates(self) -> Dict[str, float]:
        if self._test_mode:
            # имитация курсов, меняющихся каждые вызов
            self._test_counter += 1
            return {
                "USD": 75.0 + (self._test_counter % 5) * 0.1,
                "EUR": 82.0 + (self._test_counter % 7) * 0.05,
                "GBP": 95.0 + (self._test_counter % 3) * 0.3,
            }

        client = tornado.httpclient.AsyncHTTPClient()
        try:
            response = await client.fetch("https://www.cbr-xml-daily.ru/daily_json.js")
            data: Dict[str, Any] = json.loads(response.body.decode("utf-8"))
            valutes = data["Valute"]
            return {
                "USD": valutes["USD"]["Value"],
                "EUR": valutes["EUR"]["Value"],
                "GBP": valutes["GBP"]["Value"],
            }
        except Exception as e:
            print(f"❌ Ошибка загрузки курсов: {e}")
            return self._rates or {"USD": 75.0, "EUR": 82.0, "GBP": 95.0}

    async def check_and_notify(self) -> None:
        new_rates = await self.fetch_rates()
        changed = self._rates != new_rates
        if changed:
            self._rates = new_rates
            self._last_update = datetime.utcnow()
            await self._notify_observers()

    async def _notify_observers(self) -> None:
        message = {
            "type": "update",
            "timestamp": self._last_update.isoformat() if self._last_update else None,
            "rates": self._rates.copy(),
        }
        # Отправляем всем подключённым клиентам
        for observer in list(self._observers):
            try:
                observer.write_message(json_encode(message))
            except Exception as e:
                print(f"❌ Ошибка отправки клиенту {getattr(observer, 'client_id', '???')}: {e}")
                self.detach(observer)


class MainHandler(tornado.web.RequestHandler):
    def get(self) -> None:
        self.render("index.html")


class RateWebSocket(tornado.websocket.WebSocketHandler):
    subject: CurrencyRateSubject

    def initialize(self, subject: CurrencyRateSubject) -> None:
        self.subject = subject
        self.client_id: str = str(uuid.uuid4())

    def open(self) -> None:
        self.subject.attach(self)
        # Отправляем начальные данные
        self.write_message(json_encode({
            "type": "welcome",
            "client_id": self.client_id,
            "rates": self.subject._rates,
            "last_update": self.subject._last_update.isoformat() if self.subject._last_update else None,
        }))

    def on_close(self) -> None:
        self.subject.detach(self)

    def on_message(self, message: str) -> None:
        # Можно расширить для команд (например, "ping")
        pass


def make_app(test_mode: bool = False) -> tornado.web.Application:
    subject = CurrencyRateSubject(test_mode=test_mode)

    # Запускаем периодическую проверку каждые 5 сек (для теста) или 5 минут (для продакшена)
    interval_sec = 5 if test_mode else 5 * 60
    tornado.ioloop.PeriodicCallback(subject.check_and_notify, interval_sec * 1000).start()

    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/ws", RateWebSocket, dict(subject=subject)),
        ],
        template_path="templates",
        static_path="static",
        debug=True,
    )


if __name__ == "__main__":
    import sys
    test_mode = "--test" in sys.argv
    app = make_app(test_mode=test_mode)
    port = 8888
    app.listen(port)
    print(f"🚀 Сервер запущен на http://localhost:{port} (test_mode={test_mode})")
    tornado.ioloop.IOLoop.current().start()
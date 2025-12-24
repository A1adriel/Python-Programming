import sys
import requests
import importlib.abc
import importlib.util
from urllib.parse import urlparse

print("=" * 60)
print("СИСТЕМА УДАЛЕННОГО ИМПОРТА")
print("=" * 60)

class URLLoader(importlib.abc.Loader):
    """Загрузчик для модулей по URL"""
    
    def __init__(self, url):
        self.url = url
        print(f"[DEBUG] Создан URLLoader для {url}")
    
    def create_module(self, spec):
        # Python создаст модуль сам
        print(f"[DEBUG] create_module вызван для {spec.name}")
        return None
    
    def exec_module(self, module):
        print(f"[DEBUG] exec_module вызван для {module.__name__}")
        try:
            # Загружаем код по URL
            print(f"[DEBUG] Загружаю {self.url}")
            response = requests.get(self.url, timeout=5)
            response.raise_for_status()
            source_code = response.text
            print(f"[DEBUG] Загружено {len(source_code)} символов")
            
            # Устанавливаем атрибуты модуля
            module.__file__ = self.url
            module.__loader__ = self
            
            # Выполняем код
            exec(compile(source_code, self.url, 'exec'), module.__dict__)
            print(f"[DEBUG] Модуль {module.__name__} успешно загружен")
            
        except Exception as e:
            print(f"[DEBUG] Ошибка загрузки модуля: {e}")
            raise ImportError(f"Не удалось загрузить модуль: {e}")

class URLMetaFinder(importlib.abc.MetaPathFinder):
    """Поисковик модулей по URL в sys.meta_path"""
    
    def __init__(self):
        self.url_paths = []
        print("[DEBUG] URLMetaFinder создан")
    
    def add_url(self, url):
        """Добавить URL для поиска модулей"""
        url = url.rstrip('/')
        if url not in self.url_paths:
            self.url_paths.append(url)
            print(f"[DEBUG] Добавлен URL путь: {url}")
            print(f"[DEBUG] Все URL пути: {self.url_paths}")
    
    def find_spec(self, fullname, path, target=None):
        print(f"\n[DEBUG] find_spec вызван:")
        print(f"  fullname: {fullname}")
        print(f"  path: {path}")
        print(f"  target: {target}")
        print(f"  url_paths: {self.url_paths}")
        
        # Если path не None, значит это поиск внутри пакета
        # Нас интересуют только модули верхнего уровня
        if path is not None and path:
            print(f"[DEBUG] Пропускаем, т.к. это поиск внутри пакета")
            return None
        
        # Ищем модуль на всех добавленных URL
        for base_url in self.url_paths:
            module_url = f"{base_url}/{fullname}.py"
            print(f"[DEBUG] Проверяю {module_url}")
            
            try:
                # Проверяем, существует ли файл
                response = requests.head(module_url, timeout=2)
                print(f"[DEBUG] HTTP статус: {response.status_code}")
                
                if response.status_code == 200:
                    print(f"[DEBUG] Найден модуль {fullname} по адресу {module_url}")
                    
                    # Создаем загрузчик и спецификацию
                    loader = URLLoader(module_url)
                    spec = importlib.util.spec_from_loader(
                        fullname, 
                        loader, 
                        origin=module_url
                    )
                    spec.has_location = True
                    
                    print(f"[DEBUG] Создана спецификация: {spec}")
                    return spec
                    
            except Exception as e:
                print(f"[DEBUG] Ошибка при проверке {module_url}: {e}")
                continue
        
        print(f"[DEBUG] Модуль {fullname} не найден на URL путях")
        return None

# Создаем и устанавливаем глобальный поисковик
finder = URLMetaFinder()
sys.meta_path.insert(0, finder)
print(f"[DEBUG] URLMetaFinder установлен в sys.meta_path")
print(f"[DEBUG] Текущие мета-поисковики: {[type(m).__name__ for m in sys.meta_path]}")

def add_remote_path(url):
    """Добавить удаленный путь для импорта"""
    finder.add_url(url)
    
    # Также добавляем в sys.path для совместимости
    if url not in sys.path:
        sys.path.append(url)
        print(f"[DEBUG] Добавлен в sys.path: {url}")
    
    print(f"✓ Добавлен удаленный путь: {url}")
    return True

def show_status():
    """Показать текущее состояние"""
    print("\n" + "=" * 40)
    print("ТЕКУЩЕЕ СОСТОЯНИЕ:")
    print(f"  URL пути: {finder.url_paths}")
    print(f"  Sys.path URLs: {[p for p in sys.path if p.startswith('http')]}")
    print(f"  Мета-поисковики: {len(sys.meta_path)}")
    print("=" * 40)

# Инициализация
print("\nСистема готова к работе!")
print("Команды:")
print("  add_remote_path('http://localhost:8000')")
print("  show_status()")
print("  import myremotemodule")
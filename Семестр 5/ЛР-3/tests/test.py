import pytest
import sys
import os
from unittest.mock import Mock, patch, MagicMock

# Добавляем src в путь Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Импорты
from src.jamaspackage.app import app, currency_rates, db_controller
from src.jamaspackage.model import CurrencyRatesCRUD
from src.jamaspackage.main import CurrencyRates


def test_currency_rates_singleton():
    """Тест что CurrencyRates - синглтон"""
    instance1 = CurrencyRates()
    instance2 = CurrencyRates()
    assert instance1 is instance2


def test_fetch_rates():
    """Тест получения курсов валют"""
    with patch('jamaspackage.main.requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'Valute': {'USD': {'Value': 75.5}, 'EUR': {'Value': 85.3}}
        }
        mock_get.return_value = mock_response

        rates = CurrencyRates(['USD', 'EUR'])
        result = rates._fetch_rates()

        assert result is True
        assert rates.rates['USD'] == 75.5


def test_db_create_read():
    """Тест работы с БД"""
    mock_rates = Mock()
    mock_rates.values = [('USD', '01-01-2024 12:00', '75.5')]

    db = CurrencyRatesCRUD(mock_rates)
    result = db.create()

    assert result is True
    assert len(db.read()) == 1


def test_flask_app_creation():
    """Тест создания Flask приложения"""
    assert app is not None
    assert app.secret_key == 'your-secret-key'


def test_index_route():
    """Тест главной страницы"""
    with app.test_client() as client:
        with patch('jamaspackage.app.currency_rates._fetch_rates') as mock_fetch, \
                patch('jamaspackage.app.db_controller.read') as mock_read:
            mock_fetch.return_value = True
            mock_read.return_value = [('USD', '01-01-2024 12:00', '75.5')]

            response = client.get('/')
            assert response.status_code == 200


def test_update_route():
    """Тест страницы обновления"""
    with app.test_client() as client:
        response = client.get('/update')
        assert response.status_code == 200
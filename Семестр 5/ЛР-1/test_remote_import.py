#!/usr/bin/env python3

import sys
import os

# Добавляем текущую директорию в путь
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("=" * 60)
print("ТЕСТ УДАЛЕННОГО ИМПОРТА")
print("=" * 60)

# Шаг 0: Проверяем сервер
print("\n1. Проверка сервера...")
try:
    import requests
    response = requests.get("http://localhost:8000/myremotemodule.py", timeout=3)
    
    if response.status_code == 200:
        print(f"✓ Сервер доступен, модуль найден ({len(response.text)} символов)")
    else:
        print(f"✗ Ошибка: HTTP {response.status_code}")
        sys.exit(1)
        
except Exception as e:
    print(f"✗ Не удалось подключиться к серверу: {e}")
    print("\nЗапустите сервер:")
    print("  mkdir -p rootserver")
    print("  cd rootserver")
    print("  python -m http.server 8000")
    sys.exit(1)

# Шаг 1: Импортируем и активируем систему
print("\n2. Активация системы удаленного импорта...")
try:
    import activation_script as remote
    print("✓ Система импорта загружена")
except Exception as e:
    print(f"✗ Ошибка при загрузке системы импорта: {e}")
    sys.exit(1)

# Шаг 2: Добавляем URL
print("\n3. Добавление удаленного пути...")
remote.add_remote_path("http://localhost:8000")
remote.show_status()

# Шаг 3: Пробуем импортировать разными способами
print("\n4. Попытка импорта...")

# Способ 1: Через __import__
print("\nСпособ 1: __import__")
try:
    module = __import__('myremotemodule')
    print(f"✓ Успешно! Модуль: {module}")
    print(f"  __name__: {module.__name__}")
    print(f"  __file__: {getattr(module, '__file__', 'нет')}")
    
    if hasattr(module, 'myfoo'):
        result = module.myfoo()
        print(f"  myfoo(): {result}")
        
except Exception as e:
    print(f"✗ Ошибка: {e}")

# Способ 2: Через importlib
print("\nСпособ 2: importlib.import_module")
try:
    import importlib
    
    # Очищаем кеш если модуль уже был загружен
    if 'myremotemodule' in sys.modules:
        print("  Очищаю кеш...")
        del sys.modules['myremotemodule']
    
    module = importlib.import_module('myremotemodule')
    print(f"✓ Успешно! Модуль: {module}")
    
except Exception as e:
    print(f"✗ Ошибка: {e}")

# Шаг 4: Проверяем sys.modules
print("\n5. Проверка sys.modules...")
if 'myremotemodule' in sys.modules:
    module = sys.modules['myremotemodule']
    print(f"✓ Модуль в sys.modules")
    print(f"  Тип: {type(module)}")
    
    # Показываем все атрибуты модуля
    print("\n  Атрибуты модуля:")
    for attr in dir(module):
        if not attr.startswith('__'):
            value = getattr(module, attr)
            print(f"    {attr}: {type(value).__name__}")
else:
    print("✗ Модуль не найден в sys.modules")

print("\n" + "=" * 60)
print("ТЕСТ ЗАВЕРШЕН")
print("=" * 60)
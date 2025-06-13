import json
from typing import Dict, Any

def read_settings(file_path: str) -> Dict[str, Any]:
    """Чтение настроек из JSON-файла."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл {file_path} не найден.")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {file_path} содержит некорректный JSON.")

def write_to_file(file_path: str, content: str, mode: str = 'a') -> None:
    """Запись строки в файл."""
    with open(file_path, mode) as file:
        file.write(content + '\n')
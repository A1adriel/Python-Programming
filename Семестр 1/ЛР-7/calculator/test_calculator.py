import pytest
import json
import os
from calculator import read_settings, write_to_file

def test_read_settings_valid(tmpdir):
    """Проверка корректного чтения настроек из файла."""
    settings = {"theme": "dark", "precision": 4}
    file_path = tmpdir.join("settings.json")
    file_path.write(json.dumps(settings))
    assert read_settings(str(file_path)) == settings

def test_read_settings_file_not_found():
    """Проверка обработки отсутствующего файла."""
    with pytest.raises(FileNotFoundError):
        read_settings("nonexistent.json")

def test_read_settings_invalid_json(tmpdir):
    """Проверка обработки некорректного JSON."""
    file_path = tmpdir.join("invalid.json")
    file_path.write("{invalid}")
    with pytest.raises(ValueError):
        read_settings(str(file_path))

def test_write_to_file_new(tmpdir):
    """Проверка записи в новый файл."""
    file_path = tmpdir.join("output.txt")
    write_to_file(str(file_path), "Hello, World!")
    assert os.path.exists(str(file_path))
    with open(str(file_path), 'r') as file:
        assert file.read() == "Hello, World!\n"

def test_write_to_file_append(tmpdir):
    """Проверка добавления строк в существующий файл."""
    file_path = tmpdir.join("output.txt")
    file_path.write("First line\n")
    write_to_file(str(file_path), "Second line")
    with open(str(file_path), 'r') as file:
        content = file.readlines()
        assert content == ["First line\n", "Second line\n"]
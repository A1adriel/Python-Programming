import sqlite3
import os
from pathlib import Path

DB_PATH = Path("glossary.db")

def init_db():
    if DB_PATH.exists():
        return
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE terms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            term TEXT NOT NULL UNIQUE,
            definition TEXT NOT NULL
        )
    """)
    # Добавим несколько примеров
    initial_terms = [
        ("FastAPI", "Современный, быстрый (высокопроизводительный) веб-фреймворк для создания API с Python."),
        ("Pydantic", "Библиотека для валидации данных и настройки управления настройками с использованием аннотаций типов Python."),
        ("OpenAPI", "Стандарт описания RESTful API, позволяющий автоматически генерировать документацию и клиентские SDK."),
        ("Swagger", "Набор инструментов для работы с OpenAPI-спецификациями, включая интерактивную документацию."),
        ("Docker", "Платформа для разработки, доставки и запуска приложений в контейнерах.")
    ]
    cursor.executemany("INSERT INTO terms (term, definition) VALUES (?, ?)", initial_terms)
    conn.commit()
    conn.close()
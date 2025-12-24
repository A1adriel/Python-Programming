from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .database import init_db
from .schemas import TermCreate, TermUpdate, TermResponse
import sqlite3
from typing import List

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Python Glossary API",
    description="REST API для управления глоссарием терминов Python-экосистемы",
    version="1.0.0",
    lifespan=lifespan
)

# Разрешить CORS для демо
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect("glossary.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/terms", response_model=List[TermResponse], tags=["Термины"])
def get_all_terms():
    conn = get_db_connection()
    rows = conn.execute("SELECT id, term, definition FROM terms ORDER BY term").fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/terms/{term}", response_model=TermResponse, tags=["Термины"])
def get_term(term: str):
    conn = get_db_connection()
    row = conn.execute("SELECT id, term, definition FROM terms WHERE term = ?", (term,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return dict(row)

@app.post("/terms", response_model=TermResponse, status_code=201, tags=["Термины"])
def create_term(term_data: TermCreate):
    conn = get_db_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO terms (term, definition) VALUES (?, ?)",
            (term_data.term.strip(), term_data.definition.strip())
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return {"id": new_id, "term": term_data.term.strip(), "definition": term_data.definition.strip()}
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="Термин уже существует")

@app.put("/terms/{term}", response_model=TermResponse, tags=["Термины"])
def update_term(term: str, update_data: TermUpdate):
    conn = get_db_connection()
    cursor = conn.execute(
        "UPDATE terms SET definition = ? WHERE term = ?",
        (update_data.definition.strip(), term)
    )
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Термин не найден")
    conn.commit()
    updated = conn.execute("SELECT id, term, definition FROM terms WHERE term = ?", (term,)).fetchone()
    conn.close()
    return dict(updated)

@app.delete("/terms/{term}", status_code=204, tags=["Термины"])
def delete_term(term: str):
    conn = get_db_connection()
    cursor = conn.execute("DELETE FROM terms WHERE term = ?", (term,))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Термин не найден")
    conn.commit()
    conn.close()
    return
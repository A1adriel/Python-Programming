from pydantic import BaseModel, Field

class TermCreate(BaseModel):
    term: str = Field(..., min_length=1, max_length=100, description="Ключевое слово термина")
    definition: str = Field(..., min_length=1, max_length=2000, description="Определение термина")

class TermUpdate(BaseModel):
    definition: str = Field(..., min_length=1, max_length=2000, description="Новое определение термина")

class TermResponse(TermCreate):
    id: int

    class Config:
        from_attributes = True
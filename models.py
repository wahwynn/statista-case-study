from pydantic import BaseModel, HttpUrl
from datetime import date

class DocData(BaseModel):
    id: int
    title: str
    subject: str
    description: str
    link: HttpUrl
    date: date

class SearchResult(BaseModel):
    document: DocData
    score: float
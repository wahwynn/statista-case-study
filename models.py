from datetime import date
from pydantic import BaseModel, HttpUrl


class DocData(BaseModel):
    id: int
    title: str
    subject: str
    description: str
    link: HttpUrl
    date: date

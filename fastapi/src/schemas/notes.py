from datetime import datetime

from pydantic import BaseModel


class Note(BaseModel):
    id: int
    title: str
    text: str
    created_at: datetime
    updated_at: datetime


class CreateNote(BaseModel):
    title: str
    text: str

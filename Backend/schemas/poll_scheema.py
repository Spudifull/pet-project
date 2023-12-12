from pydantic import BaseModel
from typing import Optional, List
import re


class Question(BaseModel):
    text: str
    options: List[str]


class Poll(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: Optional[str]
    end_date: Optional[str]
    questions: List[Question] = []

class Answer(BaseModel):
    pass

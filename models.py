from typing import List

from pydantic import BaseModel


class MessageBody(BaseModel):
    phone_numbers: List[str]
    text: str

from pydantic import BaseModel


class MessageBody(BaseModel):
    phone_number: str
    text: str

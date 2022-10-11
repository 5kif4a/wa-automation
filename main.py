from fastapi import FastAPI

from celery_app.tasks import send_message
from models import MessageBody

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send_message_via_wa")
async def send_message_via_wa(body: MessageBody):
    send_message.delay(body.phone_number, body.text)
    return {"message": "Send message task created!"}


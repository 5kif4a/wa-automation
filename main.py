from celery import chain
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from celery_app.tasks import send_message
from models import MessageBody

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/send_message_via_wa")
async def send_message_via_wa(body: MessageBody):
    tasks = [send_message.si(phone_number, body.text) for phone_number in body.phone_numbers]
    chain_task = chain(*tasks)
    chain_task.delay()
    return {"message": "Send message task created!"}

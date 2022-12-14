from .celery import app
from .selenium import automatic_send_message


@app.task
def send_message(phone_number: str, text: str):
    return automatic_send_message(phone_number, text)

from threading import Thread
from flask_mail import Message
from flask import current_app

from .app import mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(data):
    msg = Message("New Form Fill", sender="drakemellone@gmail.com", recipients=["eli@jsdvs.com"])
    msg.body = f'First name: {data["first-name"]}, Last Name: {data["last-name"]}, Email: {data["email"]}, Message: {data["message"]}'
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
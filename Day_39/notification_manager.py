import os
from twilio.rest import Client
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())
class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ["TWILIO_VIRTUAL_NUMBER"],
            body=message_body,
            to=os.environ["MY_NUMBER"]
        )
        print(message.sid)
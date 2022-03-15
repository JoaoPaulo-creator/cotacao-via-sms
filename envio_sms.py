from twilio.rest import Client
from constants import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_PHONE_NUMBER


def client_():
    return Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def message_sms(client_msg, destination_number):
    return client_().messages.create(
        body=client_msg,
        from_=TWILIO_PHONE_NUMBER,
        to=destination_number
    )

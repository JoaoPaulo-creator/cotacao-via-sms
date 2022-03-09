from twilio.rest import Client
from constants import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_WHATSAPP_PHONE_NUMBER


def client_whats():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    return client


def message_whats(client_msg, destination_number):
    client_message_sender = client_whats().messages.create(
        body=client_msg,
        from_=TWILIO_WHATSAPP_PHONE_NUMBER,
        to=destination_number
    )
    return client_message_sender

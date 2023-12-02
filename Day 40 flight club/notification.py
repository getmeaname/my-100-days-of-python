import smtplib
from twilio.rest import Client

TWILIO_SID = YOURTWILIOACCOUNTSID
TWILIO_AUTH_TOKEN = YOURTWILIOAUTHTOKEN
TWILIO_VIRTUAL_NUMBER = YOURTWILIOVIRTUALNUMBER
TWILIO_VERIFIED_NUMBER = YOURTWILIOVERIFIEDNUMBER
MAIL_PROVIDER_SMTP_ADDRESS = YOUREMAILPROVIDERSMTPADDRESS #"smtp.gmail.com"
MY_EMAIL = YOUREMAIL
MY_PASSWORD = YOURPASSWORD

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
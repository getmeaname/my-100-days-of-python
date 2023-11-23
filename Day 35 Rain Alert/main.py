import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "Generate your own api key here: https://openweathermap.org/api"

# visit twilio and get your account_sid and auth_token

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Use https://www.latlong.net/ to find out your latitude and longitude.

parameters = {
    "lat": "Your latitude",
    "lon": "Your longitude",
    "appid": api_key,
    "exclude": "currently,minutely,daily"
}

# One call api requires you to pay for their service use any other free hourly forecast api service that is free
# https://openweathermap.org/api/one-call-3
# Free api: https://openweathermap.org/price

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    condition = hour["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True

# If the above block of code triggered the will_rain will initiate the api call to twilio which will send a message
# reminding us to bring an umbrella.

if will_rain:
    # This can be found here in this doc: https://www.twilio.com/docs/messaging/quickstart/python
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella.",
        from_='+15017122661',  #From the twilio provided no
        to='Your verified number'  #To your mobile number
    )

    print(message.status)

# You can host your code in Pythonanywhere.
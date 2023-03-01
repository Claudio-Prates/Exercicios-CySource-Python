import requests
import time
from twilio.rest import Client


url = "http://127.0.0.1:1337/index.html"
site_antigo = ""
r = requests.get(url)
site_antigo = r.text


while True:
    time.sleep(1)
    r = requests.get(url)
    if site_antigo != r.text:
        # Download the helper library from https://www.twilio.com/docs/python/install
         # Set environment variables for your credentials
        # Read more at http://twil.io/secure
        account_sid = "ACd9781f5ccf1c81b923d4ed4a0ca1ec91"
        auth_token = "f88eabe1e6eda02cc379e33819e64f83"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Hello from Twilio",
            from_="+12762778468",
            to="+5519991234019"
        )

        print(message.sid)
        break


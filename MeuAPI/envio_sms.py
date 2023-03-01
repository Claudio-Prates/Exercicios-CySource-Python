# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

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
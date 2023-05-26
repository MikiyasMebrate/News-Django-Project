# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC68448056174902f81acbebdbe949d68c"
auth_token = "86c76068701f1ba2ad6ac3b098936469"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello Mike",
  from_="+13159291943",
  to="+251942274410"
)
print(message.sid)
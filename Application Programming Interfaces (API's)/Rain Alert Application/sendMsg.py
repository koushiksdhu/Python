import os
from twilio.rest import Client
# acc_sid = os.environ['TWILIO_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']

acc_sid = 'AC256cc84490b3cee802aa0eb214e440b6'
auth_token = '7885c66fa6bde4f1472f6bb5e3ff3ec9'

client = Client(acc_sid, auth_token)

message = client.messages \
    .create(
        body=input("Enter the message: "),
        from_='+18143249126',
        to='+917992321676'
    )
    
print(message.sid)
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2e469a5de8716251fa8542992e3634da"
# Your Auth Token from twilio.com/console
auth_token  = "0f73afe3c04da01ac2ce33177b7dc18f"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+13472911141", 
    from_="+16463928575",
    body="Hello from Python!")

print(message.sid)

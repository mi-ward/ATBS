#! python3
#textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string

import os

# Preset values:
accountSID = os.environ['TWILIO_SID']
authToken = os.environ['TWILIO_AUTH_TOKEN']
myNumber = os.environ['TWILIO_MY_NUMBER']
twilioNumber = os.environ['TWILIO_NUMBER']
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)

# If twilio could actually text you and didn't require a virtual phone
# you could enter the following to have it send a text to you when your task is done

# import textMyself
# textMyself.textmyself('The boring task is finished.')
from twilio.rest import Client

client = Client("XX", "XX")


num=[
"+123456789",
"+123456789",
"+123456789",
"+123456789",
"+123456789"
]




for i in num:
    client.messages.create(to=i, 
                        from_="+123456789", 
                        body="Reminder: MLab-Onlinestudie, morgen um 14:30 Uhr. Der Zoom-Link wurde per E-Mail zugesandt. Wir freuen uns auf Sie!")
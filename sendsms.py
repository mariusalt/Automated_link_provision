from twilio.rest import Client

client = Client("AC3a59d1287e0b5eda97371ba0ac23ec2f", "a7437027a342f3118d59311607db228b")


num=[
"+4915731109072",
"+491717818776",
"+4917655285817",
"+491756224910",
"+4915226882005"
]




for i in num:
    client.messages.create(to=i, 
                        from_="+17044626748", 
                        body="Reminder: MLab-Onlinestudie, morgen um 14:30 Uhr. Der Zoom-Link wurde per E-Mail zugesandt. Wir freuen uns auf Sie!")
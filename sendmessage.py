import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import requests
import csv

subject = "hello"
msg = "hello"


def mail2textmsg(phone_num, msgtype="sms"):
#    gateway = gatewaylookup(carrier=carrier, typ=msgtype)
    ph = phone_num.replace("-","")
    ph = ph.replace("(","")
    ph = ph.replace(")","")
    to = '%s@vodafone-sms.de' % (ph)
    try:
        sender = "UMFRAGE@zew.de"
#        recipients = address # could be list
        header = 'To:' + ph + '\n' + 'From:  ' + sender + '\n' + 'Subject:%s \n' % (subject)
        print(header)
#        mesg = "\n".join([header, "RE: %s" % subject, ' %s \n\n' % msg])
        m="this is message"
        msg = MIMEText("""From: %s
        To: %s
        Subject: text-message
        %s""" % (sender, to, m))
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = to
        # Make sure you add a new line in the subject
        msg['Subject'] = "You can insert anything\n"
        # Make sure you also add new lines to your body
        body = "You can insert message here\n"
        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, 'plain'))

        sms = msg.as_string()
        c = smtplib.SMTP('hermes.zew-private.de',timeout=4)
        c.sendmail(sender, ph, sms)
        print('mail sent!')
        c.quit()
    except Exception as e:
        print("Exception while sending Email")
        print(traceback.format_exc(2))



def gatewaylookup(carrier, typ):
    gatewaylist = "https://cdn.rawgit.com/just-dantastic/blog/d20dbeab/data/textmsg_carriers.ls"
    fields = ["provider","sms","mms","other"]
    req = requests.get(gatewaylist)
    readr = csv.DictReader(req.text, fieldnames=fields)
    if carrier.lower() in [p.lower() for p in row["provider"]]:
        for row in readr:
            if carrier.lower() == row["provider"].lower():
                return row[typ]
            else:
                pass
    else:
        print("Carrier Name is Invalid. Please be sure to remove all not alphanumeric characters.")

mail2textmsg("+491743119138")
import smtplib
from email.mime.text import MIMEText


def sendEmail(subj, msgBody,address):
    try:
        sender = "xx@yy.de"
        recipients = address # could be list
        body = '%s' % (msgBody)
        msg = MIMEText(body) # string to email body - ascii only
        msg['Subject'] = subj
        msg['From'] = sender
        msg['To'] = recipients
        c = smtplib.SMTP('xx',timeout=4)
        c.sendmail(sender, [recipients], msg.as_string())
        c.quit()
    except Exception as e:
        print("Exception while sending Email")
        print(traceback.format_exc(2))

# for i in mails:
#     sendEmail(hello,hello1,i)



# def sendEmail(subj, msgBody, address):
    
#     sender = "marius.alt@zew.de"
#     recipients = address # could be list
#     body = '%s\n(end of message body)\n' % (msgBody)
#     msg = MIMEText(body) # string to email body - ascii only
#     msg['Subject'] = '%s (subject line)' % (subj[:40])
#     msg['From'] = sender
#     msg['To'] = recipients

#     c = smtplib.SMTP('email.zew.de',timeout=4)
# #        c.login("zew\mat", "209am!zw")
#     c.sendmail(sender, [recipients], msg.as_string())
#     c.quit()


# hello="hello how are you"
# hello1="this is random content"
# ad="marius_alt@web.de"
# sendEmail(hello,hello1,ad)
#smtp server

# SERVER = "hermes.zew-private.de"
# FROM = "marius.alt@zew.de"
# TO = ["marius_alt@web.de"] # must be a list

# SUBJECT = "Hello!"
# TEXT = "This is a test of emailing through smtp of example.com."

# # Prepare actual message
# message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

# %s
# """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

# # Send the mail
# import smtplib
# server = smtplib.SMTP(SERVER,443)
# server.login("ZEW\mat", "209am!zw")
# server.sendmail(FROM, TO, message)
# server.quit()




# to = 'marius_alt@web.de'
# gmail_user = 'ZEW\mat'
# gmail_pwd = '209am!zw'
# smtpserver = smtplib.SMTP("email.zew.de",443)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo
# smtpserver.login(gmail_user, gmail_pwd)
# header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
# print(header)
# msg = header + '\n this is test msg from m \n\n'
# smtpserver.sendmail("marius.alt@zew.de", to, msg)
# print('done!')
# smtpserver.close()
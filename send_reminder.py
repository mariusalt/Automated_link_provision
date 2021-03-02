import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np 
import csv
import smtplib
from email.mime.text import MIMEText
import sendlink



#mail.1.player.mail
Uhrzeit = "14:30 Uhr"
remind="Sehr geehrte Teilnehmerin, sehr geehrter Teilnehmer,\n \nwir würden Sie gerne freundlich darauf hinweisen, dass morgen um %s der zweite Teil der MLab Studie, an der Sie letzte Woche teilgenommen haben, stattfindet. \nÜber Ihre erneute Teilnahme würden wir uns sehr freuen." % (Uhrzeit)

df = pd.read_excel('C:/Users/mat/Desktop/Policy tools as commitment devices/Experiment/Session2 (23.07. 1430)/Daten/all_apps_wide_2020-07-23.xlsx', sheet_name='Sheet1')
hello = "Reminder: MLab Onlinestudie, morgen 14:30 Uhr"


for k,i in enumerate(df['mail.1.player.reminder']):
    if i==0:
        print(df['mail.1.player.mail'][k])
        n=df['mail.1.player.mail'][k]
        sendlink.sendEmail(hello,remind,n)
        if pd.isnull(df['mail.1.player.mail2'][k])==False and df['mail.1.player.mail2'][k]!=df['mail.1.player.mail'][k]:
            f=df['mail.1.player.mail2'][k]
            sendlink.sendEmail(hello,remind,f)
            print(df['mail.1.player.mail2'][k])




# def sendEmail(subj, msgBody,address):
#     try:
#         sender = "UMFRAGE@zew.de"
#         recipients = address # could be list
#         body = '%s' % (msgBody)
#         msg = MIMEText(body) # string to email body - ascii only
#         msg['Subject'] = 'Link_Experiment_MLab'
#         msg['From'] = sender
#         msg['To'] = recipients
#         c = smtplib.SMTP('hermes.zew-private.de',timeout=4)
#         c.sendmail(sender, [recipients], msg.as_string())
#         c.quit()
#     except Exception as e:
#         print("Exception while sending Email")
#         print(traceback.format_exc(2))
# links=[
# "http://mat.zew.de/InitializeParticipant/zqrmm8jf",
# "http://mat.zew.de/InitializeParticipant/xp6dxc21",
# "http://mat.zew.de/InitializeParticipant/zvai65mx",
# "http://mat.zew.de/InitializeParticipant/dnq3l913",
# "http://mat.zew.de/InitializeParticipant/93fxfr1b",
# "http://mat.zew.de/InitializeParticipant/pabl0cpt",
# "http://mat.zew.de/InitializeParticipant/268iufup",
# "http://mat.zew.de/InitializeParticipant/ojivgq3d",
# "http://mat.zew.de/InitializeParticipant/r33wqjfm",
# "http://mat.zew.de/InitializeParticipant/owymnvvw",
# "http://mat.zew.de/InitializeParticipant/42y0arg2",
# "http://mat.zew.de/InitializeParticipant/ib4p389u",
# "http://mat.zew.de/InitializeParticipant/3uq79e2x",
# "http://mat.zew.de/InitializeParticipant/oyl974nv",
# "http://mat.zew.de/InitializeParticipant/b5fo2zvi",
# "http://mat.zew.de/InitializeParticipant/rjrxj5qi",
# "http://mat.zew.de/InitializeParticipant/tujfbwst",
# "http://mat.zew.de/InitializeParticipant/b8je2d5g",
# ]
# mails=[

# ]
# hello="Experiment MLab"
# hello1="https://hs-aalen-de.zoom.us/j/3889527092"
# ad="marius_alt@web.de"
# #for k,i in enumerate(mails):
# #    sendEmail(hello,links[k],i)
# carriers = {
# 	'att':    '@mms.att.net',
# 	'tmobile':' @tmomail.net',
# 	'verizon':  '@vtext.com',
# 	'sprint':   '@page.nextel.com'
# }
# sms='+491743119138{}'.format(carriers['sprint'])
# sendEmail(hello,hello,"marius_alt@web.de")
# getmail.py - By Mason Fisher
# A Python script that gets emails via the Internet Message Access Protocol
# This is mostly just a simple script but should be expanded on!
# This script only gets emails from the GMail server for now and you will need an app password.
# https://myaccount.google.com/apppasswords

import getpass
from imap_tools import MailBox as email
from imap_tools import Q as query

def getemail(user, password):
    host = 'imap.gmail.com' # Gmail IMAP servers

    server = email(host)
    try:
        server.login(user, password, initial_folder='INBOX')
    except Exception:
        print("Login failure, did you type in email and password correctly and are you using an app password?")
        exit()

    mail = []
    tmail = []

    for msg in server.fetch(query(all=True)):
        tmail.append(msg.subject)
        tmail.append(msg.html)
        mail.append(tuple(tmail))
        tmail = []

    server.logout()
    return(tuple(mail))

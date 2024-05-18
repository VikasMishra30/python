from email.message import EmailMessage, EmailID
from app2 import password
import ssl
import smtplib

email_sender = EmailID
email_password = password
email_receiver = input('Enter Email: ')

subject = 'Dont forgot to follow Know The Facts'
body = """
Follow Know the Facts on Instagram (@knowthefactsorg) and Twitter (@KnowTheFactsOrg) and also subscribe on YouTube (@knowthefactsorg)
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

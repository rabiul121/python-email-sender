from email.message import EmailMessage
from multiprocessing import context
from email_details import password
import ssl
import smtplib


email_sender = 'mrobiulislam.robi@gmail.com'
email_password = password

email_receiver = 'robiulislam649@gmail.com'

subject = 'Sending Message from Python Code'
body = """
Hello Robi! I'm sending this message from Python code....
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

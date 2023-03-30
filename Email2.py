from email.message import EmailMessage
from PassEmail2 import password
import ssl
import smtplib

email_sender = 'tarungaikwad8@gmail.com'
email_password = password

email_receiver = 'yoraje3089@areosur.com'

Subject = 'Email send using Python'
Body = """
When You Watch This I am Glad to Say that i make it
"""

em = EmailMessage()
em['from'] = email_sender
em['To'] = email_receiver
em['Subject'] = Subject
em.set_content(Body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
    
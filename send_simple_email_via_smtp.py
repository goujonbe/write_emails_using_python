import smtplib
import ssl
import getpass

port = 587
smtp_server = 'smtp.gmail.com'
sender_email = 'test.emetteur1@gmail.com'
receiver_email = 'test.destinataire2@gmail.com'
password = getpass.getpass('Password:')
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()

with smtplib.SMTP(host=smtp_server, port=port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
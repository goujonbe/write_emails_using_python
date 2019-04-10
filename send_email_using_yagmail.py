import yagmail
import getpass

receiver = "test.destinataire2@gmail.com"
body = "Hello there from Yagmail"

yag = yagmail.SMTP("test.emetteur1@gmail.com", getpass.getpass('Password:'))
yag.send(
    to=receiver,
    subject="Yagmail test",
    contents=body
)
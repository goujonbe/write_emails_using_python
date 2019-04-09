# How to send e-mails using Python
This repository contains code examples that explain how to send e-mails using Python.

## SMTP

**SMTP** stands for Simple Mail Transfer Protocol. It is a **communication protocol** for send e-mails transmission. Although it is quite old (first defined in 1982), it has been updated and is used by most of the mail servers.

## Security

It is tempting to allow less secure apps on gmail and hard code passwords directly in the code.
Solutions:
* at least use [getpass](https://docs.python.org/3/library/getpass.html) a built-in python library that will ask for your password at runtime.
* more sophisticated you can store your password using [keyring](https://pypi.org/project/keyring/), it avoids you the pain to type your password each time you want to send an e-mail.
* best solution but quite complicated, use OAuth2 authentication. This [tutorial](http://blog.macuyiko.com/post/2016/how-to-send-html-mails-with-oauth2-and-gmail-in-python.html) or this [one](https://developers.google.com/gmail/api/quickstart/python) may help.

import smtplib, ssl
import os

# tafkbjmvzlbdrzdy

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "nikolaykorbut@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "nikolaykorbut@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

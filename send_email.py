import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "saurabh11308@gmail.com"
    password = "uxmf sdkr asyy ycis"

    receiver = "saurabh.shashank@capgemini.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        


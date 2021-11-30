import os
import smtplib


Email_id = os.environ.get('email_id')
Email_pass = os.environ.get('email_pass')

#PASSWORD IS THE APP PASSWORD THAT YOU NEED TO CREATE

def sendto(reciever):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(Email_id,Email_pass)

        subject = 'You are now REGISTERED'
        body = 'Thank You for Registering!!\n\nRegards,\ndp-login'

        msg = f'Subject:{subject}\n\n{body}'

        smtp.sendmail(Email_id,reciever,msg)
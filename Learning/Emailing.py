__author__ = "Ashad Nadeem Mahmudi"
__date__ = "9/5/2020"

from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass

email = EmailMessage()

#Sender
sender = "asadek009@gmail.com"
email["From"] = sender
#Receiver
recipient = "ashadnadeem@gmail.com"
email["To"] = recipient
#Subject Line
email["Subject"] = "Test Email Using Python"
#Write Body to a variable
body = """To whom it may concern,
This is just a test email.
Regards,
Ashad"""
#Assign Body Variable to Email Message Object
email.set_content(body)

#Attatchment
attachment_path = os.path.join(os.getcwd(),"email_atatch.jpg")
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/')
with open(attachment_path, 'rb') as img:
    email.add_attachment(img.read(),
                        maintype=mime_type,
                        subtype=mime_subtype,
                        filename=os.path.basename(attachment_path)
                        )
# print(email)

#Login into Email Server and send Email from it
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
# mail_pass = getpass.getpass('Password? ')
mail_pass = input("Enter password for {} to send email...".format(sender))
code = mail_server.login(sender, mail_pass)
print(code)
mail_server.send_message(email, to_addrs= recipient)
print("Email Sent to {} : successfull".format(recipient))
mail_server.quit()
print("Logging Out")
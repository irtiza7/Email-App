import smtplib
from getpass import getpass
from email.message import EmailMessage
import os


# Printing the Menu heading.
print(("\n" + "_" * 13) + "MENU" + ("_" * 13 + "\n"))

# Taking user credentials and other required stuff.
USER_EMAIL_ADDRESS = input("Sender's Email Address> ")
USER_EMAIL_PASSWORD = getpass("Sender's Password> ")
RECEIVER_EMAIL_ADDRESS = input("Receiver's Email Address> ")

EMAIL_SUBJECT = input("\nEmail Subject> ")
EMAIL_BODY = input("Email Body> ")

print("\n[ SENDING ] \n.\n.\n.\n.")

# "r" converts normal string into raw string.
FILE_PATH = r"C:\Users\Irtiza\Projects\Test.pdf"



# Using EmailMessage object to store all required information i.e. credentials, subject and body.
msg = EmailMessage()

msg["Subject"] = EMAIL_SUBJECT
msg["From"] = USER_EMAIL_ADDRESS 
msg["To"] = RECEIVER_EMAIL_ADDRESS

msg.set_content(EMAIL_BODY) # Setting email contents to whatever user entered for email body.

# Adding attachment(s) to the email message.
# Read the file from local machine and get the file to be attached.
with open(FILE_PATH, "rb") as f:
    fileData = f.read()

    # If your file is not in CWD, then you have to use file's path. To extract file name from path, you cannot use f.name as it produces logical error.
    # Solution: I used OS module's path.basename() method. There might be other ways too.
    fileName = os.path.basename(FILE_PATH) # Getting file name to display what is the name of the attached file.

# Attaching a file to the email.
# add_attachment() takes file contents, type of file, a subtype (extension) and file name to be displayed on attachment.
# For an image, maintype = "image", subtype = "jpg"
# For a PDF, maintyep = "application", subtype = "octet-stream"
msg.add_attachment(fileData, maintype = "application", subtype = "octet-stream", filename = fileName)



# Adding context manager to establish a server.
# SMTP_SLL() here takes 2 arguments i.e. your email servive name and a port number to run the server. 456 is default.
# SMTP_SSL class is a better way of doing things instead of simple SMTP (SMTP lib). 
# We wont have to call methods like ehlo() and starttls().
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

    smtp.login(USER_EMAIL_ADDRESS, USER_EMAIL_PASSWORD) # Login method is used to login to our mail server and it takes 2 arguments i.e. email address and password.
    smtp.send_message(msg) # Takes an object containing all the information needed i.e. sender's and receiver's mail, and the message to be sent.

print("[ EMAIL SENT SUCCESSFULLY ]\n")
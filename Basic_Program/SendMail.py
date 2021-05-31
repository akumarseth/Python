import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security  
s.starttls()

# Authentication
s.login("svcxyzz@gmail.com", "Abhishek@123")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("svcxyzz@gmail.com", "abhishekseth989@gmail.com", message)

# terminating the session
s.quit()
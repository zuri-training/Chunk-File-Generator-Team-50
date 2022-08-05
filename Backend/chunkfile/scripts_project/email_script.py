import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# Explore yagmail smtp client https://pypi.org/project/yagmail/

def sendHTMLMail(): # HTML Email
    # Define the transport variables
    ctx = ssl.create_default_context()
    password = "vtcqmmzzbafvidvy"    # Your app password goes here
    sender = "tersooahire21@gmail.com"    # Your e-mail address
    receiver = "tersooahire15@gmail.com" # Recipient's address
    
    # Create the message
    message = MIMEMultipart("alternative")
    message["Subject"] = "GitHub Profile"
    message["From"] = sender
    message["To"] = receiver
    
    # HTML Version
    html = """\
    <html>
    <body>
        <p>Hey Tersoo,</p>
        <p>Kindly find my<a href="https://github.com/tersoo-ahire">GitHub Profile</a> and CV attached below.</p>
        <p>Warm regards,</p>
        <p>Tersoo from Savannah Labs.</p>
    </body>
    </html>
    """
    
    # Plain text alternative version
    plain = """\
    Hey Tersoo,
    Kindly find attached my GitHub Profile and CV attached below.</a>.
    Warm regards
    Tersoo from Savannah Labs.
    """
    
    # Add the different alternative parts in order of increasing complexity
    # starting with the simplest first, i.e. the plain text version first.
    message.attach(MIMEText(plain, "plain"))
    message.attach(MIMEText(html, "html"))
    
    # Attach a file
    filename = "python-emails/CV_AHIRE_TERSOO_2022.docx"
    with open(filename, "rb") as f:
        file = MIMEApplication(f.read())
    disposition = f"attachment; filename={filename}"
    file.add_header("Content-Disposition", disposition)
    message.attach(file)
    
    # Connect with server and send the message
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
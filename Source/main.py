from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from enum import Enum
import smtplib
import time
import ssl

from message_dictionary import phishingLevelDict as PLD
from email_dictionary import emailList


class Status(Enum):
    ERROR = -1


class SmtpPackage(object):
    def __init__(self, **kwargs):
        self.smtp_server = kwargs['server']
        self.sender_email = kwargs['senderEmail']
        self.receiver_email = kwargs['recipientEmail']
        self.port = kwargs['port']
        if self.sender_email == "supp0rt.my.phish@gmail.com":
            self.password = "khdjwzwslrzudlue"
        else:
            input(f'Type your password for user: {self.sender_email}, and press enter: ')
            self.password = kwargs['password']
        self.message = None

    def smtpExecuteSend(self, amount=1):

        # Create a secure SSL context
        context = ssl.create_default_context()

        print('Sending ', end="", flush=True)
        for i in range(abs(amount)):
            try:
                server = smtplib.SMTP(self.smtp_server, self.port)
                server.ehlo()  # Can be omitted
                server.starttls(context=context)  # Secure the connection
                server.ehlo()  # Can be omitted
                server.login(self.sender_email, self.password)
                server.send_message(self.message)
                print('.', end="", flush=True)

            except Exception as e:
                print(f'This exception occured: {e}')

            finally:
                server.quit()

            if abs(amount) > 1 and i != abs(amount) - 1:
                time.sleep(10)  # sleep 3 seconds

        print('Your messages have been delivered')

    # Multipurpose Internet Mail Extensions
    def mimeMessageBuilder(self, name, level=1):

        self.message = MIMEMultipart("alternative")
        self.message["From"] = self.sender_email
        if level == 2:
            answer = input('Please verify that the emailDictionary in email_dictionary.py is correct (Y/N): ')
            if answer.lower() != 'y':
                return Status.ERROR
            self.message["To"] = ", ".join(emailList)
        else:
            self.message["To"] = self.receiver_email

        # Create the plain-text and HTML version of your message
        text = f"""\
        Hi {name}, How are you?

        This message will populate if you allow only incoming, plain text emails.
        Options like this will keep you more secure from phishing attacks, great job
        """

        html = self.messageBuilderHelper(name=name, level=level)
        if html == Status.ERROR:
            return html

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(part1)
        self.message.attach(part2)

    # This method should pull a html email template from a dictionary based on how advanced the phishing attack is
    def messageBuilderHelper(self, name, level=1):
        if level in range(1, 4):
            if level == 2:
                name = 'Team Name'

            self.message["Subject"] = PLD[level]['subject']
            message = PLD[level]['beforeName'] + name + PLD[level]['afterName'] + PLD[level]['linkHTML'] + PLD[level]['afterLink']
        elif level == 4:
            self.message["Subject"] = PLD[level]['subject']
            message = PLD[level]['body1'] + PLD[level]['body2']
        else:
            print('This level is not yet configured in the messageBuilderHelper method')
            return Status.ERROR
        return message


def main():

    # TODO You need to create an email account and replace it here as well as the recipient email
    #  Also update the RETURN_EMAIL in message_dictionary.py
    sender_email = "supp0rt.my.phish@gmail.com"  # This is a working sample
    # sender_email = "<create_new_email@gmail.com>"
    recipient_email = "<recipient_email@gmail.com>"

    # Port 465 for SSL || 587 for TLS || 1025 for local
    smtp_package = SmtpPackage(server="smtp.gmail.com",
                               senderEmail=sender_email, recipientEmail=recipient_email, port=587)
    
    # TODO Update the recipient name (if the email requires it) and choose the email level
    status = smtp_package.mimeMessageBuilder(name='Recipient Name', level=4)
    if status != Status.ERROR:
        smtp_package.smtpExecuteSend(amount=1)


if __name__ == '__main__':
    main()

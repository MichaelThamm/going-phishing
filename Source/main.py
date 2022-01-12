import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from message_dictionary import phishingLevelDict as PLD
from email_dictionary import emailList

"""
Background: The goal is to simulate attack vectors in the form of phishing emails.
            This script will automate the sending of suspicious emails to see if targets are aware
            and if Gmail can filter these incoming emails

Reference:  https://realpython.com/python-send-email/
            https://docs.python.org/3/library/smtplib.html#module-smtplib
            https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
            https://accounts.google.com/DisplayUnlockCaptcha
            
Thoughts:   I can try to target the company with different types of phishing attacks which can be done in levels:
            lvl1 - Pretend to be a generic company to see if people will click a link
            lvl2 - Pretend to be Anne sending out a specific announcement e.g. COVID-19 update
            lvl3 - Pretend to be Anne and send out personal emails to each individual
            
Psychology: https://www.campaignmonitor.com/blog/email-marketing/improve-email-click-through-rate-psychology/

Make Google Accounts Without Phone Number: https://www.quora.com/How-can-I-create-a-Google-account-without-a-phone-number-during-the-registration-process
Note: This requires an android phone, I needed this since my phone number was used for too many Google accounts
"""


class SmtpPackage(object):
    def __init__(self, **kwargs):
        self.smtp_server = kwargs['server']
        self.sender_email = kwargs['senderEmail']
        self.receiver_email = kwargs['recipientEmail']
        self.port = kwargs['port']
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
            if answer != 'Y':
                return
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

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(part1)
        self.message.attach(part2)

    # This method should pull a html email template from a dictionary based on how advanced the phishing attack is
    def messageBuilderHelper(self, name, level=1):
        if level == 2:
            name = 'TEAM_NAME'

        self.message["Subject"] = PLD[level]['subject']
        message = PLD[level]['beforeName'] + name + PLD[level]['afterName'] + PLD[level]['linkHTML'] + PLD[level]['afterLink']
        return message


def main():

    sender_email = "create_new_email@gmail.com"  # You need to create an email account and replace it here
    # Also update the RETURN_EMAIL in message_dictionary.py

    # Port 465 for SSL || 587 for TLS || 1025 for local
    smtp_package = SmtpPackage(server="smtp.gmail.com",
                               senderEmail=sender_email, recipientEmail="person1@gmail.com", port=587,
                               password=input(f'Type your password for user: {sender_email}, and press enter: '))

    smtp_package.mimeMessageBuilder(name='RECIPIENT_NAME', level=1)
    smtp_package.smtpExecuteSend(amount=1)


if __name__ == '__main__':
    main()

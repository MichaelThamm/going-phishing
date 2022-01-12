Welcome, your mission is to test the awareness of the company staff to spot phishing emails.


# Summary
This project was created as a point and click phishing attack with the intent to
create interesting emails to get employees to click links. Once a link is pressed a return email will be sent to the
RETURN_EMAIL in the Source.message_dictionary.py file.


# Message Contents
To change the contents of the messages, edit the string constants found in Source.message_dictionary.py where the
variables end in _P1, _P2, _P3 for each level/phase.


# Recipients
To change the recipient of the email, change the recipientEmail parameter of the SmtpPackage constructor.
If you want to send out a mass email, update the dictionary in Source.email_dictionary.py, all of which will
receive the email.


# Send Email
In Source.main.py, the sender emails can be set in addition to the name of the target e.g. John Doe. In
the mimeMessageBuilder() method, define the name and level parameters which must match for a given
recipient email. Example, name='Mike', level=1 where recipientEmail='person1@gmail.com'


# Gmail Accounts
Before sending an email, a valid Gmail account must exist that has these settings enabled:
https://www.google.com/settings/security/lesssecureapps
https://accounts.google.com/DisplayUnlockCaptcha

Make Google Accounts Without Phone Number:
https://www.quora.com/How-can-I-create-a-Google-account-without-a-phone-number-during-the-registration-process


# Conclusion
Now you can use the Gmail account and password to send emails. Once you run the main.py file, you will be prompted for
the password for the sender_email account and hit Enter. The console will log that you have sent the messages and you
are done.

Happy phishing!
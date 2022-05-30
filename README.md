Welcome, your mission is to test the awareness of the company staff to spot phishing emails.

_Note: There are no dependencies for this project, just run the code_

# Summary
This project was created as a point and click phishing attack with the intent to
create interesting emails to get employees to click links. Once a link is pressed a return email will be sent to the
RETURN_EMAIL in the Source.message_dictionary.py file.


# Message Contents
To change the contents of the messages, edit the string constants found in Source.message_dictionary.py where the
variables end in _P1, _P2, _P3, _P4 for each level/phase.


# Recipients
To change the recipient of the email, change the recipientEmail parameter of the SmtpPackage constructor.
If you want to send out a mass email, update the dictionary in Source.email_dictionary.py, all of which will
receive the email.


# Send Email
In Source.main.py, the sender emails can be set in addition to the name of the target e.g. John Doe. In
the mimeMessageBuilder() method, define the name and level parameters which must match for a given
recipient email. Example, name='person1', level=1 where recipientEmail='person1@gmail.com'


# Gmail Accounts
Before sending an email, a valid Gmail account must exist that has these settings enabled:

_Note: "To help keep your account secure, starting May 30, 2022, Google will no longer support the use of third-party apps or devices which ask you to sign in to your Google Account using only your username and password." [Link](https://support.google.com/accounts/answer/6010255?hl=en)_
- [lesssecureapps](https://www.google.com/settings/security/lesssecureapps)
- [DisplayUnlockCaptcha](https://accounts.google.com/DisplayUnlockCaptcha)

[Make Google Accounts Without Phone Number](https://www.quora.com/How-can-I-create-a-Google-account-without-a-phone-number-during-the-registration-process)
Note: This requires an android phone, I needed this since my phone number was used for too many Google accounts

# Conclusion
Now you can use the Gmail account and password to send emails. Once you run the main.py file, you will be prompted for
the password for the sender_email account and hit Enter. The console will log that you have sent the messages and you
are done.

Happy phishing!



# Supporting References
[Tutorial](https://realpython.com/python-send-email/)
[smtplib](https://docs.python.org/3/library/smtplib.html#module-smtplib)
[AuthenticationError](https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python)
            
Thoughts:   Try to target the company with different types of phishing attacks which can be done in levels:
            lvl1 - Pretend to be a generic company to see if people will click a link
            lvl2 - Pretend to be a manager sending out a specific announcement e.g. COVID-19 update
            lvl3 - Pretend to be a manager and send out personal emails to each individual
            lvl4 - Use more embedded html content to see what is filtered 
            
[Psychology of phishing](https://www.campaignmonitor.com/blog/email-marketing/improve-email-click-through-rate-psychology/)

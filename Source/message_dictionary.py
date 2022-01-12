RETURN_EMAIL = "create_new_email@gmail.com"

REPLY_EMAIL_BODY = """Hey MY_NAME,

I would like to speak with you regarding phishing attacks and cybersecurity. I understand that having clicked this link will not get me in trouble and will instead be used as a learning experience.
I look forward to working with you to improve our security!

Regards,
"""


# ________________LEVEL 1________________ #
SUBJECT_P1 = 'Response Required'

LINK_HTML_P1 = f"""<a href="mailto:{RETURN_EMAIL}?subject=Re: I Should Not Click Suspicious Links&body={REPLY_EMAIL_BODY}">log in</a>"""

BEFORE_NAME_P1 = """
                <html>
                <body>
                <p>
                Dear 
                """

AFTER_NAME_P1 = """,<br><br>
                We emailed your a little while ago to ask for your help resolving an issue with your Microsoft Teams account.<br>
                Your account is still temporarily limited because we haven't heard from you.<br><br>
                We noticed some unusual log in activity with your account. Please check that no one has logged in to your account without permission.<br><br>
                To help us with this and to see what you can and can't do with your account until this issue is resolved, 
                """

AFTER_LINK_P1 = """ to your account and go to the Resolution Center.<br><br>
                As always, if you need help or have any questions, feel free to contact us. We're always here to help.<br><br>
                Thank you for being a Microsoft customer.<br><br>
                Regards,<br><br>
                Microsoft Teams
                </p>
                </body>
                </html>
                """

# ________________LEVEL 2________________ #
SUBJECT_P2 = 'Important: Summary of Workplace COVID Restrictions'

LINK_HTML_P2 = f"""<a href="mailto:{RETURN_EMAIL}?subject=Re: I Should Not Click Suspicious Links&body={REPLY_EMAIL_BODY}">Document</a>"""

BEFORE_NAME_P2 = """
                <html>
                <body>
                <p>
                Hi 
                """

AFTER_NAME_P2 = """,<br><br>
                I have (almost) finalized our Pandemic Plan and have changed our current status. With everyone's help, this page: 
                """

AFTER_LINK_P2 = """ is now a great resource for up-to-date COVID-19 variant information and will act as the penultimate resource for the company in the near future. The Rapid Test Kits are serving their purpose so do not hesitate to continue to use them. Masks remain mandatory throughout common areas.
                <br><br>
                This level of enforcement is not pleasant for anyone but is required by the city. Please do your part in keeping us and the community safe.
                <br><br>
                MY_NAME,
                </p>
                </body>
                </html>
                """

# ________________LEVEL 3________________ #
SUBJECT_P3 = 'Important: Work Directive for the New Year'

LINK_HTML_P3 = f"""<a href="mailto:{RETURN_EMAIL}?subject=Re: I Should Not Click Suspicious Links&body={REPLY_EMAIL_BODY}">Document</a>"""

BEFORE_NAME_P3 = """
                <html>
                <body>
                <p>
                Hi 
                """

AFTER_NAME_P3 = """,<br><br>
                I made a document for Friday's meeting and I think your input would help keep the content concise. I tried to segment the information into sections that align with the usual Friday meeting order. I will make a final review of the document by tomorrow afternoon and am excited to see your contributions.
                <br><br>
                """

AFTER_LINK_P3 = """<br><br>
                MY_NAME,
                </p>
                </body>
                </html>
                """

phishingLevelDict = {1: {'subject': SUBJECT_P1, 'beforeName': BEFORE_NAME_P1, 'afterName': AFTER_NAME_P1, 'afterLink': AFTER_LINK_P1, 'linkHTML': LINK_HTML_P1},
                     2: {'subject': SUBJECT_P2, 'beforeName': BEFORE_NAME_P2, 'afterName': AFTER_NAME_P2, 'afterLink': AFTER_LINK_P2, 'linkHTML': LINK_HTML_P2},
                     3: {'subject': SUBJECT_P3, 'beforeName': BEFORE_NAME_P3, 'afterName': AFTER_NAME_P3, 'afterLink': AFTER_LINK_P3, 'linkHTML': LINK_HTML_P3}}

# TODO Update the return email if an embedded link is clicked
RETURN_EMAIL = "enter_return_email@gmail.com"
# TODO Update your name here
REPLY_EMAIL_BODY = """Hey Name,

I would like to speak with you regarding phishing attacks and cybersecurity. I understand that having clicked this link will not get me in trouble and will instead be used as a learning experience.
I look forward to working with you to improve our company's security!

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
                We emailed you a little while ago to ask for your help resolving an issue with your Microsoft Teams account.<br>
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
                I have (almost) finalized our Pandemic Plan and have changed our current status. With everyone's help, the confluence page: 
                """

AFTER_LINK_P2 = """ is now a great resource for up-to-date COVID-19 variant information and will act as the penultimate resource for the company in the near future. The Rapid Test Kits are serving their purpose so do not hesitate to continue to use them. Masks remain mandatory throughout common areas.
                <br><br>
                This level of enforcement is not pleasant for anyone but is required by the city. Please do your part in keeping us and the community safe.
                <br><br>
                Sincerely,
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
                Sincerely,
                </p>
                </body>
                </html>
                """

# ________________LEVEL 4________________ #
LINK_HTML1_P4 = f"""<a href="mailto:{RETURN_EMAIL}?subject=Re: I Should Not Click Suspicious Links&body={REPLY_EMAIL_BODY}">Here Is What's New!</a>"""
LINK_HTML2_P4 = f"""<a href="mailto:{RETURN_EMAIL}?subject=Re: I Should Not Click Suspicious Links&body={REPLY_EMAIL_BODY}">Pricing Calculator</a>"""
LINK_HTML3_P4 = f"""<a href="mailto:{RETURN_EMAIL}?subject=Re: I Should Not Click Suspicious Links&body={REPLY_EMAIL_BODY}" class="btn-primary">Renew Your Subscription</a>"""

SUBJECT_P4 = """It Is Time To Move Up"""

BODY1_HTML_P4 = """
<html xmlns="http://www.w3.org/1999/xhtml">
<head> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"> 
<title>Atlassian</title> 
<style type="text/css">
      TD { vertical-align: top; } .intro h3{margin: 0;font-size: 16px;} .data{margin: 3px 0 9px 0;line-height: 1.2em;} a{color: #348eda; text-decoration: underline;}
</style> 
<style type="text/css">
      .btn-primary {text-decoration: none; color: #FFF; background-color: #2379bf; border: solid #2379bf; border-width: 10px 20px; line-height: 2em; font-weight: bold; text-align: center; cursor: pointer; display: inline-block; border-radius: 5px; text-transform: capitalize; margin-right: 16px;}
</style> 
</head> 
<body style="background-color:#AFC4D5; margin:30px; font-family:tahoma,arial,helvetica,sans-serif;font-size:12px;"> 
<style type="text/css">
      TD { vertical-align: top; } .intro h3{margin: 0;font-size: 16px;} .data{margin: 3px 0 9px 0;line-height: 1.2em;}
</style> 
<table style="width:600px; background-color:#fff; margin:0 auto;border:1px solid #b5d7e6;" cellpadding="0" cellspacing="0" summary="outerWrapper"> 
<tbody> 
<tr> 
<td><a href="https://www.atlassian.com/" target="_blank"><img style="border:0; margin-left:30px; margin-top:15px; margin-bottom:15px" src="https://github.com/MichaelThamm/LetsGo-Phishing/blob/main/AtlassianImages/atlassian-blue-logo_small.png?raw=true" alt="Atlassian"></a></td> 
</tr> 
<tr> 
<td style="padding-left:30px;padding-right:30px"> 
<table id="emailbody" style="width:100%" cellpadding="0" cellspacing="0" summary="configurable"> 
<tbody> 
<tr> 
<td class="intro" colspan="3"> <h3>It is time to move to the cloud<img style="border:0; margin-left:10px; margin-top:0px; margin-bottom:0px" src="https://github.com/MichaelThamm/LetsGo-Phishing/blob/main/AtlassianImages/At-Cloud_smaller.png?raw=true" alt="Atlassian"></h3> </td> 
</tr> 
<tr> 
<td colspan="3"> 
<hr style="margin-bottom:15px;"> </td> 
</tr> 
<tr> 
<td style="width:40%"> <p class="data">End Date</p> </td> 
<td>&nbsp;</td> 
<td> <p class="data">30-06-2022</p> </td> 
</tr> 
<tr> 
<td> <p class="data">Should I Stay?</p> </td> 
<td>&nbsp;</td> 
<td>"""

BODY2_HTML_P4 = f"""{LINK_HTML1_P4}
</td> 
</tr> 
<tr> 
<td> <p class="data">Or Should I Go?</p> </td> 
<td>&nbsp;</td> 
<td> <p class="data">No Steps Required Until The Expiry Date</p> </td> 
</tr> 
<tr> 
<td> <p class="data">Find What Suits Your Needs</p> </td> 
<td>&nbsp;</td> 
<td> {LINK_HTML2_P4} </td> 
</tr> 
</tbody> 
</table> </td> 
</tr> 
<tr> 
<td style="padding-left:30px;padding-right:30px;padding-bottom:15px;padding-top:10px;"> 
<table style="width:100%"> 
<tbody> 
<tr> 
<td style="border:none;padding:3.75pt 3.75pt 3.75pt 3.75pt"> <p><b>{LINK_HTML3_P4}</b></p> </td> 
</tr> 
</tbody> 
</table> </td> 
</tr> 
</tbody> 
</table>  
</body>
</html>
"""


phishingLevelDict = {1: {'subject': SUBJECT_P1, 'beforeName': BEFORE_NAME_P1, 'afterName': AFTER_NAME_P1, 'afterLink': AFTER_LINK_P1, 'linkHTML': LINK_HTML_P1},
                     2: {'subject': SUBJECT_P2, 'beforeName': BEFORE_NAME_P2, 'afterName': AFTER_NAME_P2, 'afterLink': AFTER_LINK_P2, 'linkHTML': LINK_HTML_P2},
                     3: {'subject': SUBJECT_P3, 'beforeName': BEFORE_NAME_P3, 'afterName': AFTER_NAME_P3, 'afterLink': AFTER_LINK_P3, 'linkHTML': LINK_HTML_P3},
                     4: {'subject': SUBJECT_P4, 'body1': BODY1_HTML_P4, 'body2': BODY2_HTML_P4}}

#!/usr/bin/python

import smtplib

message = """From: From Person <udayan.guha@cotiviti.com>
To: To Person <udayan.guha@cotiviti.com>
MIME-Version: 1.0
Content-type: text/html
Subject: E-mail notification from Feature Library Team
<p>
Hi All,
<br />
<br />
This is a notification email after successful execution of <b>Step 1.</b>
<br />
<br />
Thanks,<br />
Feature Library Team<br />
</p>
"""
sender = 'udayan.guha@cotiviti.com'
receiver = 'udayan.guha@cotiviti.com'
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, sender, message)
   print "Successfully sent email"
except smtplib.SMTPException:
   print "Error: unable to send email"



=================


# import smtplib
#
# message = """From: From Person <udayan.guha@cotiviti.com>
# To: To Person <udayan.guha@cotiviti.com>
# MIME-Version: 1.0
# Content-type: text/html
# Subject: SMTP HTML e-mail test
#
# This is an e-mail message to be sent in HTML format
#
# <b>This is HTML message.</b>
# <h1>This is headline.</h1>
# """
#
# try:
#    smtpObj = smtplib.SMTP('localhost')
#    smtpObj.sendmail(sender, receivers, message)
#    print "Successfully sent email"
# except SMTPException:
#    print "Error: unable to send email"

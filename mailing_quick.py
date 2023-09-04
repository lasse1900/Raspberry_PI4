import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("YAGMAIL_PASS")

import time
from datetime import datetime as dt
# https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
# https://www.pythonanywhere.com/

sender = 'lauri.kyttala@gmail.com'
receiver = 'lauri.kyttala@gmail.com'

subject = "This is the subject!"
# token = 'check token from primary gmail account, until hidden'


contents = """
Here is the content of the email! 
Hi!
"""

yag = yagmail.SMTP(user=sender, password=token)
yag.send(to=receiver, subject=subject, contents=contents, attachments="attachment.txt")
print("Email Sent!")


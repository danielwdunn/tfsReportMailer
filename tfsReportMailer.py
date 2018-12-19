import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import os
import globalconfig as cfg
import json
import time
from datetime import datetime, date, time, timedelta

#Cleanup existing files
if os.path.exists("email_body.txt"):
  os.remove("email_body.txt")
else:
  print("The file does not exist")
if os.path.exists("table_data.txt"):
  os.remove("table_data.txt")
else:
  print("The file does not exist")

collection = "/" + cfg.tfs['collection']
project = "/" + cfg.tfs['project']
repo_type = "/tfvc/changesets"

# TFS Basic Auth Url with login values as username and password
url = cfg.tfs['url'] + collection + project + "/_apis" + repo_type
user = cfg.tfs['username']
passwd = cfg.tfs['password']

# GET request to REST API using basic auth and TFS private key
auth_values = (user, passwd)
requestget = requests.get(url, auth=auth_values)


full_request = requestget.json()
values = (full_request["value"])

def get_changeset_data():
    values = (full_request["value"])
    for changeset_data in values:
        changeset_id = changeset_data['changesetId']
        changeset_comment = changeset_data['comment']
        # Transform UTC Zulu datetime format TFS uses
        changeset_longdate = changeset_data['createdDate']
        changeset_strdate = changeset_longdate[0:16]
        changeset_date = datetime.strptime(changeset_strdate, '%Y-%m-%dT%H:%M')
        # Get current data and date to compare. This will get data 1 week out from current system time.
        today = datetime.today()
        tdelta = timedelta(days=7)
        compareto = today - tdelta
        # Create Table Rows
        if changeset_date > compareto:
                rows = "<tr><td>" + str(changeset_date) + "</td><td>" + str(changeset_comment) + "</td></tr>"
                file = open('table_data.txt', 'a')
                file.write(rows)
get_changeset_data()

#Concatenate header, body, and footer files.
filenames = ['header.txt','table_data.txt','footer.txt']
with open('email_body.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = cfg.mail['subject']
msg['From'] = cfg.mail['from']
msg['To'] = cfg.mail['to']


with open("email_body.txt","r") as body:
    email_body = body.read()


# Create the body of the message (a plain-text and an HTML version).
text = email_body
html = email_body

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP(cfg.mail['smtp_server'], cfg.mail['port'])

mail.ehlo()

mail.starttls()

mail.login(cfg.mail['username'], cfg.mail['password'])
mail.sendmail(msg['From'], msg['To'], msg.as_string())
mail.quit()

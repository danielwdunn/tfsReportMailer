# TFS Report Mailer
This script gets changeset data from a TFS project for the last 7 days via the REST API , generates an HTML formatted email, then sends it to the address specified.

##Prerequisites
Python 3.0
TFS REST API endpoint information, personal access key, and user membership to TFS project team.
An email account and SMTP server information. 

##Setup
Modify the globalconfig_sample.py file.
Rename globalconfig_sample.py to globalconfig.py
Schedule using Windows task scheduler or CRON job.

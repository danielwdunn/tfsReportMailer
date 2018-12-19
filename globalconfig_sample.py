#Rename this file to globalconfig.py once you've modified it.
tfs = {  'url': 'http://example.com:8080/tfs/',
         'username': 'uname',
		 #You must use a TFS personal access token as the password and have access to the relevant project/collection. See: https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts
         'password': '55537776example6633373gp3bkzbgvwv3jg5dsxi3uq37fmnsdpbinkwz4oq', 
         'collection': 'CollectionName',
         'project': 'ProjectName'}

#The below example uses a gmail account and SMTP server. You must allow unsecure access to your gmail account, or if using 2-factor authentication, you must create an app specific password. See: https://myaccount.google.com/apppasswords
mail = { 'username': 'example@gmail.com',
         'password': 'exampleqaqxytzxi',
         'subject': 'HTML Formatted Report from TFS',
         'from': 'example@gmail.com',
         'to': 'example@company.com',
         'smtp_server': 'smtp.gmail.com',
         'port': 587}
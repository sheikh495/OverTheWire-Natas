#!/user/bin/env python
import requests
import  re
username = 'natas1'
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'
url ='http://%s.natas.labs.overthewire.org' % username
#url ='http://%s.natas.labs.overthewire.org/files/users.txt' % username
reponse = requests.get(url, auth=(username, password))
content = reponse.text

print (content)

#!/user/bin/env python
import requests
import  re
import base64
import urllib

username = 'natas11'
password = '1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg'

url ='http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
cookies={"data" : "MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz"}
reponse = session.get(url , auth = (username, password),cookies=cookies)

content = reponse.text
print(content)
print (re.findall('The password for natas12 is(.*)',content)[0])


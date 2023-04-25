#!/user/bin/env python
import requests
import  re
username = 'natas8'
password = 'a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB'



url ='http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
#reponse = requests.get(url , auth = (username, password))
reponse = session.post(url ,data={"secret":"oubWYf2kBq", "submit" :"submit"} , auth = (username, password))


content = reponse.text

print (content)
print (re.findall(' The password for natas9 is(.*)',content)[0])

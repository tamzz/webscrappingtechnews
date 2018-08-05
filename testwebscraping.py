# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 22:33:16 2018

@author: tammy_000
"""

import requests
import sys
#This URL will be the URL that your login form points to with the "action" tag.
POST-LOGIN-URL = "https://github.com/login"

#This URL is the page you actually want to pull down with requests.
REQUEST-URL = "https://github.com/"


payload = {"login": "tammy18tam@gmail.com","password": "github000"}


with requests.Session() as session:
    post = session.post(POST-LOGIN-URL, data=payload)
    r = session.get(REQUEST-URL)
    print(r.text)   #or whatever else you want to do with the request data!
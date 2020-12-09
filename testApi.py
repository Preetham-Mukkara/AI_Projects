#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 14:36:12 2020

@author: preetham
"""


import http.client

conn = http.client.HTTPSConnection("grammarbot.p.rapidapi.com")

payload = "language=en-US&text=Susan%20go%20to%20the%20store%20everyday"

headers = {
    'x-rapidapi-host': "grammarbot.p.rapidapi.com",
    'x-rapidapi-key': "d947322c46msh6b7d16cb6320125p1264bdjsn2d550af6021b",
    'content-type': "application/x-www-form-urlencoded"
    }

conn.request("POST", "/check", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
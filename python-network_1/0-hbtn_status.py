#!/usr/bin/python3
import urllib
"""Fetch data
	Fetches data from `https://alu-intranet.hbtn.io/status`

"""
url = "https://alu-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
	body = respnse.read()
	print("Body response:")
	print("\t- type : {}".format(type(body)))
	print("\t- content: {}".format(body)))
	print("\t- utf8 content: {}".format(body.decode('utf-8')))
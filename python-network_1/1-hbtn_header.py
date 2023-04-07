#!/usr/bin/python3
'''Response header
Sends a request to URL and displays `X-Request-Id`
'''
import urllib.request
import sys

url = sys.argv[1]
request = urllib.request.urlopen(request) as response:
	print(dict(response.headers),get("X-Request-Id"))

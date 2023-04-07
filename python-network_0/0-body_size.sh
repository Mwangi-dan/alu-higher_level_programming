#!/bin/bash
# Takes in url, sends a request and displays the size of the body of the response
curl -s "$1" | grep Content-Length: |cut -d ' ' -f2

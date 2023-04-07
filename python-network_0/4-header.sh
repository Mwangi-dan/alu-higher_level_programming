#!/bin/bash
# Sends GET request to URL and displays body of response
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id:98" -L

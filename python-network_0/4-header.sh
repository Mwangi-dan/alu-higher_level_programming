#!/bin/bash
# Sends GET request to URL and displays body of response
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"

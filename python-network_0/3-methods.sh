#!/bin/bash
# Displays a;; HTTP methods the server will accept
curl -sI | grep Allow | cut -d ":" | cut -c 2-

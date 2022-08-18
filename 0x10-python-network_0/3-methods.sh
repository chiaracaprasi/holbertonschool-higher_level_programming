#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -X -L PUT -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"

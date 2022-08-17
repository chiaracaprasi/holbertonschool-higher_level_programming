#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -I -X OPTIONS 0.0.0.0:5000/route_4 | grep 'Allow:' | cut -f2 -d' '
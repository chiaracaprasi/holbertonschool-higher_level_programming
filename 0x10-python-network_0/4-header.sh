#!/bin/bash
# Script  takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
RequestHeader set X-HolbertonSchool-User-Id "98"
curl -s -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"

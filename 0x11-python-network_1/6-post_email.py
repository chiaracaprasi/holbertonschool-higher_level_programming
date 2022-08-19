#!/usr/bin/python3
""" Sript that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response """
import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    email = {'email': argv[2]}
    # data = urllib.parse.urlencode(values)
    # data = data.encode('ascii')
    r = requests.post(url, data=email)
    print(r.text)

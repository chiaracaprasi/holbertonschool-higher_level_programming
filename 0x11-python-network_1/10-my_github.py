#!/usr/bin/python3
""" Sript that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response """
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":

    api = 'https://api.github.com/user'
    username = argv[1]
    token = argv[2]
    basic = HTTPBasicAuth(username, token)
    r = requests.get(api, auth=basic)
    print(r.json().get('id'))

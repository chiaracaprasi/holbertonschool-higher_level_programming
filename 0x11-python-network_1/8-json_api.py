#!/usr/bin/python3
""" Sript that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response """
import requests
from sys import argv


if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    letter = argv[1]
    r = requests.get(url)
    print(r.json())

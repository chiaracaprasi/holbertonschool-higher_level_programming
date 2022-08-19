#!/usr/bin/python3
""" Sript that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response """
import requests
from sys import argv


if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    r = requests.post(url, data={'q': q})
    try:
        r_dict = r.json()
        if r_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    except ValueError:
        print("Not a valid JSON")
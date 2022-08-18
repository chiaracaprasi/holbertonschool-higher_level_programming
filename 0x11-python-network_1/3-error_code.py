#!/usr/bin/python3
""" Sript that takes in a URL and an email,
sends a request to the URL and
displays the body of the response (decoded in utf-8). """
import urllib.request
import urllib.parse
import urllib.error
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            message_body = response.read().decode('utf-8')
            print(message_body)
    except url.error.URLError as e:
        print("Error code: {}".format(e.code))

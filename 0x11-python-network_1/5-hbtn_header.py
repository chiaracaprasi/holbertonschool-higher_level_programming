#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status """
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = get(url)
    print(r.headers.get('X-Request-Id'))

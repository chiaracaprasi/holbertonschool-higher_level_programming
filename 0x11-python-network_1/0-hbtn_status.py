#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
    
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        resp = response.read()
        html = resp.decode("UTF-8")
        typ = type(resp)
        print('Body response:')
        print(f'\t- type: {typ}')
        print(f'\t- content: {resp}')
        print(f'\t- utf8 content: {html}')

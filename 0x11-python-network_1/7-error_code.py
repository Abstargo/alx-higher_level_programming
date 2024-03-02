#!/usr/bin/python3
"""
given URL, sends a request, displays response (utf-8).
usage: ./7-error_code.py http://0.0.0.0:5000/status_401
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)

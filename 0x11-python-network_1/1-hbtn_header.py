#!/usr/bin/python3
"""
given URL as parameter, fetch URL and display value from response header
usage: ./1-hbtn_header https://intranet.hbtn.io
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))

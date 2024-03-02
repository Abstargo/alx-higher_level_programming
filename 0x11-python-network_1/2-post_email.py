#!/usr/bin/python3
"""
given URL & email as params, send POST req to URL, display response body utf-8
usage: ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""
import urllib.request
from sys import argv
import urllib.parse


if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())

#!/usr/bin/python3
"""
 takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request

try:
    with urllib.request.urlopen(sys.argv[1]) as response:
            pass
except urllib.error.HTTPError as e:
            print(e.code)
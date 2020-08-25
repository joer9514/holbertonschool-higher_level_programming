#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    usrna = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = (usrna, token)
    r = requests.get(url, auth=auth)
    print(r.json().get("id"))

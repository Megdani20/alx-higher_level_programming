#!/usr/bin/python3
"""6-hbtn_header module"""
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
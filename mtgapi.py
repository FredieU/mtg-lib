#! /usr/bin/python3

import requests
import json
from sys import argv
from urllib.parse import quote_plus

baseURL = 'https://api.magicthegathering.io/v1/'

def getRequest(path, params = None):
    """GET from path"""

    if params:
        response = requests.get(url = baseURL + path + str(params))
    else:
        response = requests.get(url = baseURL + path)
    
    response.raise_for_status()

    return response.json()

def search(path, key, value):
    """Change element value"""

    q = getRequest(
        path = path, 
        params = "/?" + key + "=" + value)

    return q   

if __name__ == "__main__":

    response = search(
        path = argv[1], 
        key = argv[2], 
        value = quote_plus(argv[3]))

    print(json.dumps(response, sort_keys = True, indent = 4))
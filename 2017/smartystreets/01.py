#!/usr/bin/env python3

import requests

# Solving - https://smartystreets.com/landing/mission
# This task was an advert on the advent website

valid = 0
AUTH_ID = '7e96ed57-bbac-2c98-1ccd-711a68da25fc'
AUTH_TOKEN = '5UoElE1hdLxb1Y19IUGw'
with open('input.txt') as fp:
    for line in fp:
        address = line.strip()
        payload = {'auth-id': AUTH_ID, 'auth-token': AUTH_TOKEN, 'street': address}
        url = 'https://us-street.api.smartystreets.com/street-address'
        r = requests.get(url, payload)
        if len(r.json()) > 0:
            valid += 1
print(valid)

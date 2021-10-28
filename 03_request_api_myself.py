#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os
import requests
import json


def request_api_myself():
    load_dotenv()

    backlog_url = os.getenv('BACKLOG_URL')
    api_key = os.getenv('BACKLOG_API_KEY')

    r = requests.get(
        backlog_url + '/api/v2/users/myself',
        params={
            'apiKey': api_key
        })

    print(json.dumps(r.json(), indent=4))


if __name__ == '__main__':
    request_api_myself()

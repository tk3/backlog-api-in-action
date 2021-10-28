#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os
import requests
import datetime


def print_api_limit_2():
    backlog_url = os.getenv('BACKLOG_URL')
    api_key = os.getenv('BACKLOG_API_KEY')

    r = requests.get(
        backlog_url + '/api/v2/users/myself',
        params={
            'apiKey': api_key
        })

    print('X-RateLimit-Limit: ' + r.headers['X-RateLimit-Limit'])
    print('X-RateLimit-Remaining: ' + r.headers.get('X-RateLimit-Remaining'))
    print('X-RateLimit-Reset: ' + r.headers.get('X-RateLimit-Reset'))

    x_rate_limit_reset = r.headers.get('X-RateLimit-Reset')
    date = datetime.datetime.fromtimestamp(int(x_rate_limit_reset))
    print('RateLimit Reset: ' + str(date))


if __name__ == '__main__':
    load_dotenv()
    print_api_limit_2()

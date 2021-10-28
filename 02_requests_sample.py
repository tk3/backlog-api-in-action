#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def request_http():
    r = requests.get('Http://localhost:10080/')

    print('status_code: %d' % r.status_code)

    print('headers')
    for k in r.headers:
        print(k + ': ' + r.headers[k])

    print('header')
    print('Content-Type: ' + r.headers['content-type'])
    print('Content-Type: ' + r.headers.get('content-type'))


if __name__ == '__main__':
    request_http()

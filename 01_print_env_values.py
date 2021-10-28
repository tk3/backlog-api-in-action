#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os


def print_env_values():
    load_dotenv()

    backlog_url = os.getenv('BACKLOG_URL')
    api_key = os.getenv('BACKLOG_API_KEY')

    print('BACKLOG_URL: ' + (backlog_url or ''))
    print('BACKLOG_API_KEY: ' + (api_key or ''))


if __name__ == '__main__':
    print_env_values()

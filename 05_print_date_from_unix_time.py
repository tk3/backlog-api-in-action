#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import datetime


def print_date_from_unix_time(unix_time):
    date = datetime.datetime.fromtimestamp(unix_time)

    print(date)


if __name__ == '__main__':
    now = time.time()
    print_date_from_unix_time(now)

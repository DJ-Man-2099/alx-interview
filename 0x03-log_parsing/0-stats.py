#!/usr/bin/python3
"""4th Project Module"""


import re
from signal import SIGINT, signal
import sys


status_count = {}
ip_regex = r'^(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})'
dash_regex = r'-'
date_regex = r'\[(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d+\.\d+)\]'
request_regex = r'"GET \/projects\/260 HTTP\/1.1"'
status_regex = r'(200|301|400|401|403|404|405|500)'
file_size_regex = r'(\d+)$'
regexes = [ip_regex, dash_regex, date_regex,
           request_regex, status_regex, file_size_regex]
log_regex = re.compile(r'{} {} {} {} {} {}'.format(*regexes))
total_file_size = 0
count = 0


def print_summary(status_count, total_file_size):
    print(f"File size: {total_file_size}")
    sorted_keys = sorted(status_count.keys())
    for key in sorted_keys:
        print(f"{key}: {status_count[key]}")


signal(SIGINT, lambda signum, frame: print_summary(
    status_count, total_file_size))

for line in sys.stdin:
    if log_regex.match(line):
        ip, date, status, file_size = log_regex.match(line).groups()
        total_file_size += int(file_size)
        if status in status_count:
            status_count[status] += 1
        else:
            status_count[status] = 1
        count += 1
        if count == 10:
            print_summary(status_count, total_file_size)
            count = 0

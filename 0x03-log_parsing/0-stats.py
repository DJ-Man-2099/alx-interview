#!/usr/bin/python3
"""4th Project Module"""


ip_regex = r'^(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})'
dash_regex = r'-'
date_regex = r'\[(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d+\.\d+)\]'
request_regex = r'"GET \/projects\/260 HTTP\/1.1"'
status_regex = r'(200|301|400|401|403|404|405|500)'
file_size_regex = r'(\d+)$'
regexes = [ip_regex, dash_regex, date_regex,
           request_regex, status_regex, file_size_regex]


def print_summary(status_count, total_file_size):
    """Prints the summary of the log parsing."""
    print(f"File size: {total_file_size}")
    sorted_keys = sorted(status_count.keys())
    for key in sorted_keys:
        print(f"{key}: {status_count[key]}")


if __name__ == "__main__":
    import sys
    import re

    status_count = {}
    total_file_size = 0
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_summary(status_count, total_file_size)
                count = 1
            else:
                count += 1
            line = line.split()
            try:
                file_size = line[-1]
                total_file_size += int(file_size)
            except (IndexError, ValueError):
                pass
            try:
                status = line[-2]
                if status in ["200", "301", "400", "401", "403",
                              "404", "405", "500"]:
                    if status in status_count.keys():
                        status_count[status] += 1
                    else:
                        status_count[status] = 1
            except IndexError:
                pass

        print_summary(status_count, total_file_size)
    except KeyboardInterrupt:
        print_summary(status_count, total_file_size)
        raise

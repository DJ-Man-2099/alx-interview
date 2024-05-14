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
    print("File size: {}".format(total_file_size))
    sorted_keys = sorted(status_count.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, status_count[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_summary(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_summary(size, status_codes)

    except KeyboardInterrupt:
        print_summary(size, status_codes)
        raise

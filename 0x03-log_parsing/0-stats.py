#!/usr/bin/python3
"""
This module reads from standard input
and computes metrics from the input
"""


import sys


def print_stats(total_size, status_codes):
    """Prints the accumulated file size and status code counts"""
    print(f"File size: {total_size}")
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print(f"{code}: {count}")


def parse_line(line):
    """
    Parses a single line of input
    and extracts the file size and status code
    """
    try:
        parts = line.split()
        if len(parts) < 2:
            return None, None
        file_size = int(parts[-1])
        status_code = int(parts[-2])
        return file_size, status_code
    except (ValueError, IndexError):
        return None, None


def main():
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size is None or status_code is None:
                continue

            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    finally:
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()

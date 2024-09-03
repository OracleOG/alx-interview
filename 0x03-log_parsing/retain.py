#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics:'''
# try reading inoputs from stdin
# match with regex
# track various metrics in each line of text
# construct an outputing logic
# handle interuptions with ctrl c.

import sys
import re
import signal

log_pattern = re.compile(r'''
    ^\s*                             # Optional leading whitespace
    (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) # IP address
    \s-\s                            # Separator
    \[(.*?)\]                        # Date in square brackets
    \s"GET /projects/260 HTTP/1\.1"\s  # HTTP request
    (\d{3})                          # Status code
    \s(\d+)                          # File size
    $
''', re.VERBOSE)

status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0


def prt_status(st_code, f_size):
    '''prints out status code as st_code
    and file_size as f_size'''
    print(f"File size: {f_size}")
    for key in sorted(st_code.keys()):
        if st_code[key] > 0:
            print(f"{key}: {st_code[key]}")


def signal_handler(sig, frame):
    '''Handles the SIGINT signal to print the metrics before exiting'''
    prt_status(status_code, file_size)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for lines in sys.stdin:
    lines = lines.strip()
    #print(f"Processing line: {lines}")  # Debug print statement
    match = log_pattern.match(lines)
    if match:
        status_codex = match.group(3)
        file_sizex = int(match.group(4))

        if status_codex in status_code:
            file_size += file_sizex
            status_code[status_codex] += 1

        count += 1

        prt_status(status_code, file_size)

        if count == 10:
            prt_status(status_code, file_size)
            count = 0
if count > 0:
    prt_status(status_code, file_size)
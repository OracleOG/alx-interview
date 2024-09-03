#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics.'''

import sys
import re
import signal

log_pattern = re.compile(r'''
    ^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) # IP address
    \s-\s                                # Separator
    \[(.*?)\]                            # Date and time in square brackets
    \s"GET\s/projects/260\sHTTP/1\.1"\s  # HTTP request
    (\d{3})                              # Status code
    \s(\d+)$                             # File size
''', re.VERBOSE)


status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}

file_size = 0
count = 0

def print_metrics():
    '''Prints the accumulated metrics.'''
    print(f"File size: {file_size}")
    for code in sorted(status_code.keys()):
        if status_code[code] > 0:
            print(f"{code}: {status_code[code]}")
    sys.stdout.flush()  # Ensure output is flushed immediately

def handle_signal(sig, frame):
    '''Handles the SIGINT signal to print the metrics before exiting.'''
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)

for line in sys.stdin:
    line = line.strip()
    match = log_pattern.match(line)
    if match:
        print("Line matched!")  # Debugging statement
        status_codex = match.group(3)
        file_sizex = int(match.group(4))

        if status_codex in status_code:
            file_size += file_sizex
            status_code[status_codex] += 1

        count += 1

        print_metrics()  # Print metrics after processing the line

        if count == 10:
            print_metrics()
            count = 0
    else:
        print("Line did not match!")  # Debugging statement

# Print remaining metrics if the script ends before reaching 10 lines.
if count > 0:
    print_metrics()

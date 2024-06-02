#!/usr/bin/python3
"""A script for parsing HTTP request logs."""
import re


def extract_input(input_line):
    """Extracts sections of a line of an HTTP request log."""
    pattern = (
        r'(?P<ip>\S+)\s+'                          # IP address
        r'\[(?P<date>[^\]]+)\]\s+'                 # Date
        r'"(?P<request>[^"]*)"\s+'                 # Request
        r'(?P<status_code>\d+)\s+'                 # Status code
        r'(?P<file_size>\d+)'                      # File size
    )
    match = re.match(pattern, input_line)
    if match:
        return {
            "status_code": match.group("status_code"),
            "file_size": int(match.group("file_size")),
        }
    return {"status_code": "0", "file_size": 0}


def print_statistics(total_file_size, status_codes_stats):
    """Prints the accumulated statistics of the HTTP request log."""
    print(f"File size: {total_file_size}", flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats[status_code]
        if num > 0:
            print(f"{status_code}: {num}", flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the metrics from a given HTTP request log.

    Args:
        line (str): The line of input from which to retrieve the metrics.

    Returns:
        int: The new total file size.
    """
    line_info = extract_input(line)
    status_code = line_info["status_code"]
    if status_code not in status_codes_stats:
        status_codes_stats[status_code] = 0
    status_codes_stats[status_code] += 1
    return total_file_size + line_info["file_size"]


def run():
    """Starts the log parser."""
    line_num = 0
    total_file_size = 0
    status_codes_stats = {}

    try:
        while True:
            line = input()
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == "__main__":
    run()

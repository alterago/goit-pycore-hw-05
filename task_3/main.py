"""Task 3: log file analyser.

Usage:
    python main.py /path/to/logfile.log [level]

Prints the number of records for each log level and, when a level is given
(e.g. "error"), all records of that level.
"""

import sys
from collections import Counter
from pathlib import Path

ENCODING = "utf-8"
LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")


def parse_log_line(line: str) -> dict:
    """Split a log line into date, time, level and message.

    Raises ValueError when the line does not look like
    'YYYY-MM-DD HH:MM:SS LEVEL message'.
    """
    parts = line.strip().split(" ", 3)
    if len(parts) < 4 or parts[2].upper() not in LEVELS:
        raise ValueError(f"malformed log line: {line.strip()!r}")
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level.upper(), "message": message}


def load_logs(file_path: str) -> list:
    """Read the file and return the parsed records; malformed lines are skipped."""
    logs = []
    with open(file_path, encoding=ENCODING) as file:
        for line_number, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                logs.append(parse_log_line(line))
            except ValueError as error:
                print(f"Line {line_number} skipped: {error}", file=sys.stderr)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Return the records of the given level (case-insensitive)."""
    return list(filter(lambda log: log["level"] == level.upper(), logs))


def count_logs_by_level(logs: list) -> dict:
    """Return the number of records for each level found in the logs."""
    return dict(Counter(log["level"] for log in logs))


def display_log_counts(counts: dict) -> None:
    """Print the counts as a table."""
    print(f"{'Log level':<17}| Count")
    print(f"{'-' * 17}|{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")


def display_log_details(logs: list, level: str) -> None:
    """Print every record of one level."""
    print(f"\nLog details for level '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main() -> None:
    if len(sys.argv) not in (2, 3):
        print("Usage: python main.py /path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level = sys.argv[2] if len(sys.argv) == 3 else None
    if level is not None and level.upper() not in LEVELS:
        print(f"Unknown level '{level}'. Use one of: {', '.join(LEVELS).lower()}")
        sys.exit(1)

    try:
        logs = load_logs(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except (OSError, UnicodeDecodeError) as error:
        print(f"Cannot read file {file_path}: {error}")
        sys.exit(1)

    if not logs:
        print("No valid log records found.")
        sys.exit(1)

    display_log_counts(count_logs_by_level(logs))
    if level is not None:
        display_log_details(filter_logs_by_level(logs, level), level)


if __name__ == "__main__":
    main()

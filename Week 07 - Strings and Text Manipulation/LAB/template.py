"""
RECORD CHECK  -  my version
===========================

Name  : Habimana Rugwiro Herve
Lane  :  IT
Date  : 7/11/2026

Run it:   python template.py
"""

import os


def parse_line(raw_line):
    """Clean and parse one messy IT record into a dictionary."""
    text = raw_line.strip().lower()
    if not text:
        return {}

    record = {}

    for piece in text.split(","):
        part = piece.strip()
        if not part:
            continue

        if "=" in part:
            key, value = part.split("=", 1)
            record[key.strip()] = float(value.strip())
        else:
            record["hostname"] = part

    return record


def status_of(record):
    """Return OK, WARNING, or OVER LIMIT for a cleaned IT record."""
    used = record.get("used", 0)
    total = record.get("total", 0)

    if total == 0:
        return "OK"

    usage = used / total
    if usage >= 1.0:
        return "OVER LIMIT"
    if usage >= 0.9:
        return "WARNING"
    return "OK"


def main():
    """Read messy server records from a file, process each, and print a summary."""
    script_dir = os.path.dirname(__file__)
    data_file = os.path.join(script_dir, "raw_records.txt")
    raw_records = []

    with open(data_file, "r") as file:
        for line in file:
            if line.strip():
                raw_records.append(line)

    flagged_count = 0

    for raw_record in raw_records:
        record = parse_line(raw_record)
        status = status_of(record)
        print(f"{record['hostname']} {status}")

        if status != "OK":
            flagged_count += 1

    print(f"Summary: {len(raw_records)} records, {flagged_count} flagged.")


main()

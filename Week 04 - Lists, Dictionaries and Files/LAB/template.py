"""
RECORD CHECK  -  my version
===========================

Name  : Habimana Rugwiro Herve
Lane  :  AI / Cyber / IT      (delete two)
Date  :  17/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


"""Load, check, report, and save a collection of records."""


def check_record(value, limit):
    """Return the difference, percentage, and status for a record."""
    difference = value - limit
    percent = (value / limit) * 100

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report for one record."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"Value      : {value:>10.2f}")
    print(f"Limit      : {limit:>10.2f}")
    print(f"Difference : {difference:>+10.2f}")
    print(f"Percent    : {percent:>10.2f}%")
    print(f"Status     : {status:>10}")
    print("=" * 34)


def load_records(path):
    """Load label , value, limit from file"""
    records = []
    try:
        with open(path) as file:
            for line in file:
                label, value, limit = line.strip().split(",")
                records.append({
                    "label" : label,
                    "value" : float(value),
                    "limit" : float(limit)
                })
    except FileNotFoundError:
        print("file not found: ",path)

    return records
records =load_records("records_sample.txt")



over_limit_count= 0

with open("results.txt", "w") as results_file:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_report(label=record["label"],value=record["value"],limit=record["limit"],difference=difference,percent=percent,status=status)
        results_file.write(f'{record["label"]},{status}\n')
        if status == "OVER LIMIT":
            over_limit_count += 1

print(f"Checked {len(records)} records. {over_limit_count} were over limit.")

with open("results.txt") as results_file:
    print(results_file.read(), end="")



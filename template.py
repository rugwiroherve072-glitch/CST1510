"""
RECORD CHECK  -  my version
===========================

Name  : HABIMANA RUGWIRO HERVE
Lane  :  AI     (delete two)
Date  : 9/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def check(value, limit):
    """Calculate the difference and percentage of value against limit."""
    difference = value - limit
    percent = (value / limit) * 100 if limit != 0 else 0
    return difference, percent

def status_of(percent, warning_at = 90):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report of the record check."""

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

# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
over_limit_count = 0  # Counter for records that are over the limit
while True:
    label = str(input("Enter a dataset name(or quit): "))       # replace with an input() call
    if label == "quit":
        break
    value = float(str(input("Enter the row loaded: ")))    # replace with an input() call, converted with float()
    limit = float(str(input("Enter the row expected: ")))

    difference, percent = check(value, limit)
    status = status_of(percent)
    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)



print(f"Records over limit: {over_limit_count}")


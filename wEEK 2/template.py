"""
RECORD CHECK  -  my version
===========================

Name  : Habimana Rugwiro Herve
Lane  :  AI       (delete two)
Date  : 01/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
over_limit_count = 0  # Initialize a counter for OVER LIMIT records
while True:
    label = str(input("Enter a dataset name(or quit): "))       # replace with an input() call
    if label == "quit":
        break
    value = float(str(input("Enter the row loaded: ")))    # replace with an input() call, converted with float()
    limit = float(str(input("Enter the row expected: ")))     # replace with an input() call, converted with float()


# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

    difference = limit - value   # replace with your calculation
    percent = (difference / limit * 100) if limit != 0 else 0       # replace with your calculation
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

# your report lines go here

    print("=" * 34)
    print(f"Row loaded   : {value:>15.2f}")
    print(f"Row expected : {limit:>15.2f}")
    print(f"Difference   : {difference:>+15.2f}")
    print(f"Percent      : {percent:>15.2f}%")

    print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
print(f"OVER LIMIT records: {over_limit_count}")
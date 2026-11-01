"""
RECORD CHECK - AI / Data Science lane
====================================

Run it: python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# Read the CSV we created for this mini-project.
df = pd.read_csv("records.csv")

# ================================================================= PROCESS
# Add percent and status columns.
df["percent"] = (df["rows_loaded"] / df["rows_expected"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# ================================================================== OUTPUT
# Print full DataFrame.
print("Full dataset:")
print(df)

# Print only non-OK rows using a boolean filter.
print("\nRows needing attention:")
print(df[df["status"] != "OK"][["dataset", "rows_loaded", "rows_expected", "percent", "status"]])

# Group by status and print a count per group.
print("\nCounts by status:")
print(df.groupby("status").size())

# Save the full DataFrame and chart.
df.to_csv("records_report.csv", index=False)
print("\nSaved records_report.csv")

df["status"].value_counts().plot(kind="bar")
plt.title("Status Counts")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_counts.png")
plt.show()

# ==========================================================================
# Check the percent and status values by hand, review the column names, and
# verify you used a boolean filter rather than a loop.

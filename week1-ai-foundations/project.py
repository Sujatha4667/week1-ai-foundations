import pandas as pd
import numpy as np

# Read CSV file
df = pd.read_csv("students.csv")

print("Student Data:")
print(df)

# Calculate statistics
average = np.mean(df["Marks"])
highest = np.max(df["Marks"])
lowest = np.min(df["Marks"])

print("\nStatistics:")
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# Add Pass/Fail Status
df["Status"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Save new CSV
df.to_csv("final_output.csv", index=False)

print("\nOutput saved to final_output.csv")
#Question 1
import csv
from statistics import mean, median, stdev

# Required variables to keep (in same order as given)
required_columns = [
    'interest rate', 'verified income', 'debt to income', 'total credit utilised',
    'total credit limit', 'public record bankrupt', 'loan purpose', 'term',
    'inquiries last 12m', 'issue month', 'annual income', 'loan amount',
    'grade', 'emp length', 'homeownership'
]

# Read the dataset
with open('loans_dataset.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    all_rows = list(reader)

# Count observations before cleaning
observations_before = len(all_rows)

# Filter and clean rows (retain only required columns and drop rows with missing values)
cleaned_rows = []
for row in all_rows:
    if all(row.get(col, '').strip() != '' for col in required_columns):
        cleaned_row = {col: row[col] for col in required_columns}
        cleaned_rows.append(cleaned_row)

# Rename 'inquiries last 12m' to 'credit checks'
for row in cleaned_rows:
    row['credit checks'] = row.pop('inquiries last 12m')

# Count observations after cleaning
observations_after = len(cleaned_rows)

# Prepare summary statistics for numerical fields
numerical_fields = [
    'interest rate', 'annual income', 'debt to income', 'loan amount',
    'total credit utilised', 'total credit limit', 'credit checks',
    'emp length', 'public record bankrupt'
]

# Convert text values to floats
summary_data = {field: [] for field in numerical_fields}
for row in cleaned_rows:
    for field in numerical_fields:
        try:
            summary_data[field].append(float(row[field]))
        except ValueError:
            pass  # Skip invalid numbers

# Print results
print(f"Number of observations before cleaning: {observations_before}")
print(f"Number of observations after cleaning: {observations_after}")
print("\nSummary Statistics (numeric columns only):")
for field in summary_data:
    values = summary_data[field]
    if len(values) >= 2:
        print(f"\n{field}:")
        print(f"  Count: {len(values)}")
        print(f"  Mean: {mean(values):.2f}")
        print(f"  Median: {median(values):.2f}")
        print(f"  Standard Deviation: {stdev(values):.2f}")
        print(f"  Minimum: {min(values):.2f}")
        print(f"  Maximum: {max(values):.2f}")

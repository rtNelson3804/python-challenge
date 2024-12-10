# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 1
total_net = 0
# Add more variables to track other necessary financial data
greatest_increase = -999999
greatest_decrease = 999999
greatest_decrease_month = ""
greatest_increase_month = ""
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')
    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    opening_month = next(reader)
    prev_month = int(opening_month[1])
    
    # Track the total and net change
    total_net = int(opening_month[1])
    total_net_change = 0
    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        total_net += int(row[1])
        
        # Track the net change
        net_change = int(row[1]) - int(prev_month)
        total_net_change += net_change
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]
        
        # Calculate the greatest decrease in losses (month and amount)
        elif net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]
        
        prev_month = int(row[1])

# Calculate the average net change across the months
average_net_raw = total_net_change / (total_months - 1)
average_net = round(average_net_raw, 2)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)


# Print the output

print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

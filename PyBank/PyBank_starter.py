# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Defining total months and total_net to use later.
total_months = 1
total_net = 0

# Setting variables for our greastest increases and decreases in net change.
greatest_increase = -999999
greatest_decrease = 999999
greatest_decrease_month = ""
greatest_increase_month = ""

# Opening and reading budget_data
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=',')
    
    # Skipping the header row
    header = next(reader)

    # Extracting the first row to setup our initial data.
    opening_month = next(reader)
    prev_month = int(opening_month[1])
    
    # Tracking the total and net change.
    total_net = int(opening_month[1])
    total_net_change = 0
    
    # Reading through each row.
    for row in reader:

        # Tracking the total months and total dollars.
        total_months += 1
        total_net += int(row[1])
        
        # Tracking the net change and total net change.
        net_change = int(row[1]) - int(prev_month)
        total_net_change += net_change
        
        # Calculating the greatest increase in profits and saving the month each time it finds a greater value.
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]
        
        # Calculating the greatest decrease in profits and saving the month each time it finds a lesser value.
        elif net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]
        
        prev_month = int(row[1])

# Calculating the average net change across the months and rounding to the nearest cent.
average_net_raw = total_net_change / (total_months - 1)
average_net = round(average_net_raw, 2)

# Generating an output summary.
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# Printing the output summary.
print(output)

# Writing the results to the text file.
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

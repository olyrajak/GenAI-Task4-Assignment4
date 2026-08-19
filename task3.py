
# Task 3: Append New Sales
# 1. Append these new sales to the same file:
# 5000, 2500, 1700
# 2. After appending, reopen and print the entire updated file.
# Extra (optional): Print the total number of lines after appending.

# Task 3: Append New Sales

# Append new sales to the existing file
sales = [5000, 2500, 1700]

with open('sales_data.txt', 'a') as file:
    for sale in sales:
        file.write(f"{sale}\n")


# Read and print the updated file
with open('sales_data.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())

    # Optional: Print total number of lines
    print(f"Total number of lines: {len(lines)}")
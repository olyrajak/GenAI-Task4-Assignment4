
# Task 2: Read File in Different Ways
# Using the same sales_data.txt:
# 1. Read the entire file using .read() and print it.
# 2. Read the first line using .readline().
# 3. Read all lines using .readlines() and convert them into a list of integers.
# Ensure proper formatting and cleanup of newline characters.

with open('sales_data.txt','r') as file:
    # Read file using .read()
    content=file.read()
    print("Using .read():")
    print(content)
    file.close()

with open('sales_data.txt','r') as file:
    # Read first line using .readline()
    first_line=file.readline()
    print("Using .readline():")
    print(first_line)
    file.close()

with open('sales_data.txt','r') as file:
    # Read all lines using .readlines()
    all_lines=file.readlines()
    # Convert lines to a list of integers, stripping newline characters
    sales_list = [int(line.strip()) for line in all_lines]
    print("Using .readlines():")
    print(sales_list)
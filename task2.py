
# Task 2: Read File in Different Ways
# Using the same sales_data.txt:
# 1. Read the entire file using .read() and print it.
# 2. Read the first line using .readline().
# 3. Read all lines using .readlines() and convert them into a list of integers.
# Ensure proper formatting and cleanup of newline characters.

# Task 2: Read File in Different Ways

# 1. Read the entire file using .read()
with open('sales_data.txt', 'r') as file:
    content = file.read()
    print("Using .read():")
    print(content)


# 2. Read the first line using .readline()
with open('sales_data.txt', 'r') as file:
    first_line = file.readline()
    print("Using .readline():")
    print(first_line.strip())


# 3. Read all lines using .readlines()
with open('sales_data.txt', 'r') as file:
    all_lines = file.readlines()

    # Remove newline characters and convert to integers
    sales_list = [int(line.strip()) for line in all_lines]

    print("Using .readlines():")
    print(sales_list)
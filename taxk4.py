
# Task 4: Generate Summary Report from File
# Using only file reading operations:
# 1. Read all sales values from sales_data.txt.
# 2. Convert them into integers.
# 3. Calculate and print:
#    o Total Sales
#    o Highest Sale
#    o Lowest Sale
#    o Average Sale
# Do not use any advanced libraries.
# Task 4: Generate Summary Report from File

# Open and read all lines from the file
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

# Convert each line into an integer (strip removes newline/whitespace)
sales = [int(line.strip()) for line in lines if line.strip() != ""]

# Calculate required values
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

# Print the summary report
print("----- Sales Summary Report -----")
print("Total Sales   :", total_sales)
print("Highest Sale  :", highest_sale)
print("Lowest Sale   :", lowest_sale)
print("Average Sale  :", round(average_sale, 2))
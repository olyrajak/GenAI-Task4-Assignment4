

# Task 7: Mini Project - Export Discounted Prices
# Create a dictionary:
# prices = {
# "Mouse": 500,
# "Keyboard": 800,
# "Monitor": 7000,
# "Pendrive": 400,
# "Camera": 5000
# }
# Ask the user for a discount percentage.
# Write discounted prices into discount_report.txt using:
# Product | Original Price | Discounted Price
# After writing, read the file and print it to the terminal.
# Extra (optional): Write a summary at the bottom of the file:
# Total Items: X
# Average Discounted Price: Y

import os

folder_path = "discounted_prices"
file_path = os.path.join(folder_path, "discount_report.txt")


# Create the FOLDER (not the file path) if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount_percentage = float(input("Enter the discount percentage: "))
if discount_percentage < 0 or discount_percentage > 100:
    print("Invalid discount percentage. Please enter a value between 0 and 100.")
    exit()

discounted_prices = {}
for product, price in prices.items():
    discounted_price = price - (price * discount_percentage / 100)
    discounted_prices[product] = discounted_price

with open(file_path, 'w') as file:
    file.write("Product | Original Price | Discounted Price\n")
    for product, price in prices.items():
        discounted_price = discounted_prices[product]
        file.write(f"{product} | {price} | {discounted_price:.2f}\n")

    total_items = len(prices)
    average_discounted_price = sum(discounted_prices.values()) / total_items
    file.write(f"\nTotal Items: {total_items}\n")
    file.write(f"Average Discounted Price: {average_discounted_price:.2f}\n")

# Read the file  and print it to the terminal
with open(file_path, 'r') as file:
    content = file.read()
    print(content)
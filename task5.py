
# Task 5: Create Product Info File (User Input)
# 1. Ask the user for 3 product names & their prices.
# 2. Write them into a new file products.txt in this format:
# 3. ProductName | Price
# 4. Read the file and print each line with proper formatting.

def main():
    # Open the file in write mode
    with open("products.txt", "w") as file:
        for i in range(3):
            product_name = input(f"Enter the name of product {i + 1}: ")
            price = input(f"Enter the price of {product_name}: ")
            # Write to the file in the specified format
            file.write(f"{product_name} | {price}\n")

    # Read and print the contents of the file
    print("\n----- Product Information -----")
    with open("products.txt", "r") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    main()

Assignment 4: File Handling (Read, Write, Append, Modes)

Problem Statement
You are working as a Python Developer for a small retail analytics team. The company wants
to store sales data, read stored files, extract reports, and append new records. Your task is
to build simple utilities using file handling operations in Python.

This assignment covers:
- Opening files in different modes (r, w, a, r+, w+)
- Reading using .read(), .readline(), .readlines()
- Writing and appending to files
- Basic data extraction from text files
- Ensuring safe file operations using with blocks
- No advanced libraries should be used.

(Solve each task clearly and separately)

Restrictions:
- Do not use pandas, csv module, or any external tools.
- Stick strictly to Python file handling features.
- Use with open() wherever possible.

--------------------------------------------------------------------------------

Task 1: Write Sales Records to a File
1. Create a list of sales amounts:
2. sales = [1200, 450, 980, 1500, 3000]
3. Open a file named sales_data.txt in write mode.
4. Write each sale on a new line in the file.
5. Close the file, then reopen it and print its contents.
Extra (optional): Write the data in comma-separated format instead of separate lines.

Task 2: Read File in Different Ways
Using the same sales_data.txt:
1. Read the entire file using .read() and print it.
2. Read the first line using .readline().
3. Read all lines using .readlines() and convert them into a list of integers.
Ensure proper formatting and cleanup of newline characters.

Task 3: Append New Sales
1. Append these new sales to the same file:
5000, 2500, 1700
2. After appending, reopen and print the entire updated file.
Extra (optional): Print the total number of lines after appending.

Put all Tasks code files in a single folder (or a single notebook) and upload in a
GitHub repo link or a Google Drive folder and submit the link

Task 4: Generate Summary Report from File
Using only file reading operations:
1. Read all sales values from sales_data.txt.
2. Convert them into integers.
3. Calculate and print:
   o Total Sales
   o Highest Sale
   o Lowest Sale
   o Average Sale
Do not use any advanced libraries.

Task 5: Create Product Info File (User Input)
1. Ask the user for 3 product names & their prices.
2. Write them into a new file products.txt in this format:
3. ProductName | Price
4. Read the file and print each line with proper formatting.

Task 6: Read File Safely (Error Handling Inside File Handling Only)
You must not use exceptions beyond file-related safeguards here.
1. Ask the user for a filename to open.
2. If the file exists, read and print it.
3. If it does not exist, print:
"File not found. Please check the filename."
Use simple condition checks with os.path.exists() (allowed).

Task 7: Mini Project - Export Discounted Prices
Create a dictionary:
prices = {
"Mouse": 500,
"Keyboard": 800,
"Monitor": 7000,
"Pendrive": 400,
"Camera": 5000
}
Ask the user for a discount percentage.
Write discounted prices into discount_report.txt using:
Product | Original Price | Discounted Price
After writing, read the file and print it to the terminal.
Extra (optional): Write a summary at the bottom of the file:
Total Items: X
Average Discounted Price: Y

Put all Tasks code files in a single folder (or a single notebook) and upload in a
GitHub repo link or a Google Drive folder and submit the link
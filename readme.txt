Sales Data Processing Project
Overview
This Python-based project processes sales data by reading from a CSV file, performing calculations (total sales and discounted sales), and writing results to an output CSV file. The program is designed to be executed via command line or batch script. The output includes processed data with additional columns for total sales and discounted sales after applying a 10% discount.

Features
Reads sales data from a CSV file (sales.csv).

Calculates total sales (quantity * price) and discounted sales (10% discount).

Outputs results to a new CSV file (summary.csv).

Includes error handling for file-related issues.

Installation
Ensure Python is installed on your system. Check by running python --version in the command prompt.

Download or clone the project folder.

Navigate to the project directory using cd command in Command Prompt.

Running the Program
Command Prompt: Run the following command to execute the program:


python sales_processor.py sales.csv
This processes sales.csv and generates summary.csv with the calculated data.

Batch Script: Simply double-click the run_sales_processor.bat file to run the program automatically.

Input/Output Format
Input: CSV file with item name, quantity, and price.

Output: CSV file with item name, quantity, price, total sales, and discounted sales.

Error Handling
The program includes basic error handling for missing files and invalid formats.




import csv
import sys
import os

def process_sales_data(input_file, output_file):
    total_sum = 0.0
    results = []

    try:
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    item = row['item']
                    quantity = float(row['quantity'])
                    price = float(row['price'])

                    # Calculation 1: Total cost
                    total_cost = quantity * price

                    # Calculation 2: Apply 10% discount if quantity > 5
                    if quantity > 5:
                        discounted_cost = total_cost * 0.9  # 10% off
                    else:
                        discounted_cost = total_cost

                    total_sum += discounted_cost
                    results.append((item, round(total_cost, 2), round(discounted_cost, 2)))
                except ValueError:
                    print(f"Warning: Skipping invalid row: {row}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing column {e} in the input file.")
        sys.exit(1)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['item', 'total_cost', 'discounted_cost'])
        for item, cost, discounted in results:
            writer.writerow([item, cost, discounted])
        writer.writerow(['Grand Total', '', round(total_sum, 2)])

    print(f"Processing complete. Output written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sales_processor.py <input_file>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = os.path.join("output", "summary.csv")
    process_sales_data(input_path, output_path)

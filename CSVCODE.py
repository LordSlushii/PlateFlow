import csv
import os

# Path to the CSV file
csv_file = 'orders.csv'

# Function to add or update an order in the CSV
def update_order(license_plate, current_order):
    # Check if file exists, if not, initialize it
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["License Plate", "Current Order", "Previous Orders"])  # Write header if file is new
    
    # Load existing data
    rows = []
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Check if license plate exists
    license_found = False
    for row in rows:
        if row[0] == license_plate:
            # If found, update current and previous orders
            row[2] = f"{row[2]}; {row[1]}" if row[2] else row[1]  # Move current order to previous orders
            row[1] = current_order           # Update with new current order
            license_found = True
            break
    
    # If not found, add a new entry
    if not license_found:
        rows.append([license_plate, current_order, ""])

    # Write updated data back to the CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Function to read the data from the CSV
def read_orders():
    if not os.path.exists(csv_file):
        print("No orders found.")
        return
    
    with open(csv_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"License Plate: {row[0]}, Current Order: {row[1]}, Previous Orders: {row[2]}")
read_orders()
update_order()

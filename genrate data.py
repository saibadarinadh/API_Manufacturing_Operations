import csv
import random
import os

# Generate sample data
data = [
    ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"]
]

for i in range(100):
    machine_id = random.randint(1, 5)
    temperature = round(random.uniform(60, 100), 2)
    run_time = round(random.uniform(50, 250), 2)
    downtime_flag = 1 if temperature > 85 or run_time > 200 else 0
    data.append([machine_id, temperature, run_time, downtime_flag])

# Debug: Print data and directory
print("Generated Data:", data[:5])  # Print the first 5 rows for debugging
print("Current Directory:", os.getcwd())

# Write to CSV file
file_path = 'uploaded_data.csv'
try:
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Sample data has been generated and saved to '{file_path}'")
except Exception as e:
    print(f"An error occurred: {e}")

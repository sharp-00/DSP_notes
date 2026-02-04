import csv
import json
from collections import defaultdict

def calculate_column_stats(input_csv, output_json):
    # This dictionary will store lists of numbers for each column name
    column_data = defaultdict(list)
    
    try:
        # 1. Read the CSV file using csv.DictReader
        with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # 2. Dynamically determine the column names and collect values
            for row in reader:
                for column_name, value in row.items():
                    try:
                        # Convert string value to float for calculations
                        column_data[column_name].append(float(value))
                    except ValueError:
                        # Skip non-numeric data if present
                        continue

        # 3. Compute stats for each column
        stats_summary = {}
        for column, values in column_data.items():
            if not values:
                continue
                
            # Perform calculations
            count = len(values)
            minimum = min(values)
            maximum = max(values)
            mean = sum(values) / count
            
            # 4. Store in a nested dictionary
            stats_summary[column] = {
                "count": count,
                "mean": mean,
                "minimum": minimum,
                "maximum": maximum
            }

        # 5. Write the computed statistics to a JSON file
        with open(output_json, 'w', encoding='utf-8') as json_file:
            json.dump(stats_summary, json_file, indent=4)
            
        print(f"Statistics successfully saved to {output_json}")

    except FileNotFoundError:
        print(f"Error: The file '{input_csv}' was not found.")

# Usage
calculate_column_stats('data.csv', 'stats_summary.json')

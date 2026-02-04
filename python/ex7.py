import csv
import json
from collections import defaultdict

def analyze_ledger(input_file, output_file):
    # 1. & 2. Read ledger and map account_id to a list of transaction amounts
    # Structure: { 'acc1': [100.0, -40.0, -60.0], ... }
    account_history = defaultdict(list)

    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    # Unpacking transaction_id, account_id, amount
                    _, account_id, amount = row
                    account_history[account_id.strip()].append(float(amount.strip()))

        # 3. & 4. Compute statistics and build the summary dictionary
        summary = {}
        for account_id, amounts in account_history.items():
            running_balance = 0
            ever_negative = False
            
            # Check for negative balance at any point in the history
            for transaction in amounts:
                running_balance += transaction
                if running_balance < 0:
                    ever_negative = True
            
            summary[account_id] = {
                "final_balance": running_balance,
                "ever_negative": ever_negative,
                "transaction_count": len(amounts)
            }

        # 5. Write the final summary to a JSON file
        with open(output_file, 'w', encoding='utf-8') as json_out:
            json.dump(summary, json_out, indent=4)
            
        print(f"Ledger analysis complete. Results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError:
        print("Error: Found non-numeric data in the amount column.")

# Usage
analyze_ledger('ledger.txt', 'ledger_summary.json')

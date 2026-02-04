#ex5

import csv
import json

def analyze_log_file(input_filename, output_filename):
    # Standard dictionary mapping user_id to list of events
    user_events = {}

    with open(input_filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                _, user_id, event_type = [item.strip() for item in row]
                
                # Manual initialization instead of defaultdict
                if user_id not in user_events:
                    user_events[user_id] = []
                user_events[user_id].append(event_type)
    
    summary = {}
    for user_id, events in user_events.items():
        summary[user_id] = {
            "event_count": len(events), #
            "has_logout": "logout" in events #
        }

    with open(output_filename, 'w') as json_file:
        json.dump(summary, json_file, indent=4) #




#ex 6

import csv
import json

def calculate_column_stats(input_csv, output_json):
    column_data = {}
    
    with open(input_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            for col_name, value in row.items():
                # Initialize column list if it's the first time seeing it
                if col_name not in column_data:
                    column_data[col_name] = []
                try:
                    column_data[col_name].append(float(value))
                except ValueError:
                    continue

    stats_summary = {}
    for col, values in column_data.items():
        if values:
            stats_summary[col] = {
                "count": len(values), #
                "mean": sum(values) / len(values), #
                "minimum": min(values), #
                "maximum": max(values) #
            }

    with open(output_json, 'w') as json_file:
        json.dump(stats_summary, json_file, indent=4) #



#ex7

import csv
import json

def analyze_ledger(input_file, output_file):
    account_history = {}

    with open(input_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                _, acc_id, amount = [item.strip() for item in row]
                
                # Manual key check
                if acc_id not in account_history:
                    account_history[acc_id] = []
                account_history[acc_id].append(float(amount))

    summary = {}
    for acc_id, amounts in account_history.items():
        balance = 0
        ever_neg = False
        for amt in amounts:
            balance += amt
            if balance < 0:
                ever_neg = True #
        
        summary[acc_id] = {
            "final_balance": balance, #
            "ever_negative": ever_neg, #
            "transaction_count": len(amounts) #
        }

    with open(output_file, 'w') as json_out:
        json.dump(summary, json_out, indent=4) #

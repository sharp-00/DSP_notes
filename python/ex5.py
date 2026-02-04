import csv
import json
from collections import defaultdict

def analyze_log_file(input_filename, output_filename):
    # 1. & 2. Read log file line by line and build the initial mapping
    # Maps user_id -> [list of event_types]
    user_events = defaultdict(list)

    try:
        with open(input_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    # Unpacking the columns
                    _, user_id, event_type = row
                    # Stripping spaces to ensure clean IDs and types
                    user_events[user_id.strip()].append(event_type.strip())
        
        # 3. & 4. Determine stats and create the summary dictionary
        summary = {}
        for user_id, events in user_events.items():
            summary[user_id] = {
                "event_count": len(events),
                "has_logout": "logout" in events
            }

        # 5. Write the summary to a JSON file
        with open(output_filename, 'w', encoding='utf-8') as json_file:
            json.dump(summary, json_file, indent=4)
            
        print(f"Successfully created summary in {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")

# Execute the analysis
analyze_log_file('activity.log', 'summary.json')

import csv



with open("events.log") as f:
    reader = csv.reader(f)
    rows = list(reader)
    
    timestamp = []

    for rows in f:
        timpestamp.append(timestamp)
    print(timestamp)
        

import csv

Headers = ['timestamp','user_id', 'event_type']

with open("events.log", mode ='r') as file:
    reader = csv.DictReader(file, fieldnames=Headers)
    rows = list(reader)

    timestamp = []

   # for row in rows:
        # timestamp.append(rows[0])    
        # print(timestamp)
    print(rows)

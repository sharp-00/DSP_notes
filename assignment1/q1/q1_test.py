def load_accounts(filename):
    accounts = {}
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("File not found.")
        return {}

    for line in file:
        try:
            parts = line.strip().split(",")
            acc_no = parts[0]
            name = parts[1]
            balance = float(parts[2])
            
            accounts[acc_no] = {
                "name": name,
                "balance": balance,
                "transactions": []
            }
        except (IndexError, ValueError) as e:
            print("Skipping a bad line.", e)
            continue
        
        file.close()
        return accounts

re = load_accounts('res.csv')


def save_accounts(filename, accounts):
    try:
        file = open(filename, "w")
    except FileNotFoundError as e:
        print("File not found.", e)

        for acc in accounts:
            acc_data = accounts[acc]
            line = acc + "," + acc_data["name"] + "," + str(acc_data["balance"])
            file.write(line + "\n")

        file.close()

re = save_accounts(re, 'new')

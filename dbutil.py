import json

data_file_path = './data.txt'
#Initializing the db to an empty json.
def db_initialize():
    records = {}
    with open(data_file_path, 'w') as f:
        f.write(json.dumps(records, indent=2))

#Reading the customer name from the db
def db_read_records(name):
    with open(data_file_path, 'r') as f:
        file_data = f.read()
        records = json.loads(file_data)
        if name in records.keys():
            return {name: records[name]}
        return None

#Creating a new customer and writing it to the db
def db_create_records(name, purchase_count=0):
    with open(data_file_path, 'r') as f:
        file_data = f.read()
        new_records = json.loads(file_data)
        if name in new_records.keys():
            return None
        new_records[name] = purchase_count

    with open(data_file_path, 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return {name: new_records[name]}

#Updating the purchase_count of a customer and writing it to db
def db_update_records(name, count):
    with open(data_file_path, 'r') as f:
        file_data = f.read()
    if not file_data:
        return None
    else:
        new_records = json.loads(file_data)
        if name in new_records.keys():
            new_records[name] = count

    with open(data_file_path, 'w') as f:
        f.write(json.dumps(new_records, indent=2))
    return {name: count}

#Deleting the customer form the db
def db_delete_records(name):
    # print(f"------------{name}")
    with open(data_file_path, 'r') as f:
        file_data = f.read()
    if not file_data:
        print("Record not found")
    else:
        records = json.loads(file_data)
        del records[name]

    with open(data_file_path, 'w') as f:
        f.write(json.dumps(records, indent=2))
    return {"deleted": name}
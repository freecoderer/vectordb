import os
import json
from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient('XXXXXXXXXXXXXXXXXX')

# Specify the database and the collection
db = client['playlist']
collection = db['mycollection']

# Specify the directory containing the JSON files
directory = 'localdb'

# Loop over all JSON files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        filepath = os.path.join(directory, filename)

        # Open the JSON file and load the data
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Check the type of the data
        if isinstance(data, list):
            # If data is a list, insert all items into the MongoDB collection
            collection.insert_many(data)
        elif isinstance(data, dict):
            # If data is a dictionary, insert it into the MongoDB collection
            collection.insert_one(data)
        else:
            print(f"Unexpected data type in file {filepath}: {type(data)}")
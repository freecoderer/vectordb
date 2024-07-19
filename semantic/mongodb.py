from pymongo import MongoClient

# Establish a connection to the MongoDB server
client = MongoClient('XXXXXXXXXXXXXXXXX')

# Select the database
db = client['playlist']

# Select the collection
collection = db['mycollection']

# Define the data you want to insert
data = [
{
    "person_name": "Tim",
    "person_id": 4,
    "songs": [
        {
            "title": "I CAN'T STOP ME",
            "artist": "TWICE"
        },
        {
            "title": "Don't Call Me",
            "artist": "SHINee"
        },
        {
            "title": "Panorama",
            "artist": "IZ*ONE"
        },
        {
            "title": "HIP",
            "artist": "MAMAMOO"
        }
    ]
}

]

# Insert the data into the collection
collection.insert_many(data)
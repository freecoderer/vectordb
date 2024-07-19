from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
# Establish a connection to the MongoDB server
client = MongoClient('XXXXXXXXXXXXXX')

# Select the database
db = client['playlist']

# Select the collection
collection = db['mycollection']

# Get the count of unique person_id in the collection
unique_person_ids = collection.distinct("person_id")

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')
# Set the id to a variable
original_person_id = 1  # Change this to the id of the person you want to fetch data for

# Fetch the document for the original person
original_person_document = collection.find_one({"person_id": original_person_id})

# Iterate over the songs and format them into a sentence
original_sentence = ""
for song in original_person_document['songs']:
    original_sentence += f"{song['title']} {song['artist']} "

print(original_sentence)

# Fetch the documents for all other users and convert the cursor to a list
other_users_documents = list(collection.find({"person_id": {"$ne": original_person_id}}))

# Get the total number of other users
total_other_users = len(other_users_documents)

for counter, document in enumerate(other_users_documents):
    if counter < total_other_users:
        comparison_sentence = ""
        for song in document['songs']:
            comparison_sentence += f"{song['title']} {song['artist']} "

        print(f"Comparison sentence for person_id {document['person_id']}, {document['person_name']}: {comparison_sentence}")

        # Encode the sentences
        original_sentence_embedding = model.encode([original_sentence])
        comparison_sentence_embedding = model.encode([comparison_sentence])

        # Calculate the cosine similarity
        similarity = cosine_similarity(
            original_sentence_embedding.reshape(1, -1),
            comparison_sentence_embedding.reshape(1, -1)
        )[0][0]
        print(f"The similarity between the original sentence and the comparison sentence is: {similarity}")
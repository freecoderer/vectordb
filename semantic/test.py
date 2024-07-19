# Fetch the document for "Kim Min-Ji"
from mongodb import collection

kim_min_ji_document = collection.find_one({"person_name": "Kim Min-Ji"})

# Iterate over the songs and format them into a sentence
original_sentence = ""
for song in kim_min_ji_document['songs']:
    original_sentence += f"{song['title']} {song['artist']} "

print(original_sentence)
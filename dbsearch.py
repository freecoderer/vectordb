from pymongo import MongoClient
import os
import sys
import requests
import json

def send_api(path, method, body):
	API_HOST = "XXXXXXXXXXXXXXXXXXX"
	url = API_HOST + path
	headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}

	try:
		if method == 'GET':
			response = requests.get(url, headers=headers)
		elif method == 'POST':
			response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
		#print("response status %r" % response.status_code)
		#print("response text %r" % response.text)
		return response
	except Exception as ex:
		print(ex)


def search_by_username(username, client_name, db_name, form_data_collection_name):
	# Establish a connection to the MongoDB server
	client = MongoClient(client_name)

	# Specify the database and the collection
	db = client[db_name]
	form_data_collection = db[form_data_collection_name]

	# Print the total number of documents in the collection
	print(f"전체 DB내의 form 데이터 개수: {form_data_collection.count_documents({})} 명")

	# Find the person's age and gender from the database
	person = form_data_collection.find_one({"username": username})
	if person is None:
		print(f"일치하는 사용자가 없습니다 프로그램을 종료합니다 {username}")
		return False
	sex = person['sex']

	print(f"대상자: {person['username']}, 성별: {sex}")

	# Perform the query
	query = { "sex": { "$ne": sex }}   # Not the person's original gender

	results = list(form_data_collection.find(query))

	# Check if the query returned any results
	result_count = form_data_collection.count_documents(query)
	if result_count == 0:
		print("조건에 맞는 대상자 존재하지 아니함 조건:(성별이 반대).")
		return False
	else:
		# Create a list to store the results
		result_list = []

		# Add the person's data to the list
		result_list.append(person)

		# Add the results of the query to the list
		for result in results:
			result_list.append(result)

		# Print the results and the number of results
		print(f"조건 검색 결과: {result_count} 명")

		# Ensure the samples directory exists
		if not os.path.exists('samples'):
			os.makedirs('samples')

		# Open a single file to write all the results
		with open('samples/data.txt', 'w+', encoding='utf-8') as f:
			# Iterate over each result
			for i, result in enumerate(result_list):
				# Extract the name and songs data
				username = result.get('username')
				if username == None:
					continue

				# 사용자의 모든 플레이리스트 조회
				response1 = send_api(f"/api/v1/playlist/user/{username}", 'GET', None).json()
				if (response1['status'] != 200):
					print(f"사용자 {username}의 플레이리스트 조회 실패")
					continue
				data_list = response1['data']

				song_list = []
				for data in data_list:
					#print(data)
					playlistId = data.get('id')
					response2 = send_api(f"/api/v1/music/{playlistId}", 'GET', None).json()
					if (response2['status'] != 200):
						print(f"플레이리스트 {playlistId}의 음악 조회 실패")
						continue
					music_list = response2['data']
					for music in music_list:
						artist = music.get('artist')
						title = music.get('title')
						song_list.append(f"{artist} - {title}")
						#print(f"{artist} - {title}")

				if (len(song_list) == 0):
					print(f"사용자 {username}의 플레이리스트가 존재하지 않습니다")
					continue
				# Format the data into a string
				data_str = f"username: {username}, playlist: [{', '.join(song_list)}]\n"

				# Write the string into the file
				f.write(data_str)
		return True

#def check_username_in_mariaDB(username, client_name, db_name, form_data_collection_name):
#	# Establish a connection to the MongoDB server
#	client = MongoClient(client_name)

#	# Specify the database and the collection
#	db = client[db_name]
#	form_data_collection = db[form_data_collection_name]

#	# Print the total number of documents in the collection
#	print(f"전체 DB내의 form 데이터 개수: {form_data_collection.count_documents({})} 명")

#	# Find the person's age and gender from the database
#	person = form_data_collection.find_one({"username": username})
#	if person is None:
#		print(f"일치하는 사용자가 없습니다 프로그램을 종료합니다 {username}")
#		return False

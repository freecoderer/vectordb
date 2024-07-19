import mysql.connector
from mysql.connector import Error
from pymongo import MongoClient

def connect_to_mariadb(host_name, user_name, user_password, db_name):
	connection = None
	try:
		connection = mysql.connector.connect(
			host=host_name,
			user=user_name,
			passwd=user_password,
			database=db_name
		)
		print("MariaDB에 성공적으로 연결되었습니다.")
	except Error as e:
		print(f"데이터베이스 연결 오류: {e}")
	return connection

# mariaDB 쿼리 실행 함수
def execute_query(connection, query):
	cursor = connection.cursor(buffered=True)
	res = None
	try:
		cursor.execute(query)
		#connection.commit()
		res = cursor.fetchall()
		#for row in res:
		#	print(row, end=" ")
		#print("쿼리 실행 성공!")
	except Error as e:
		print(f"쿼리 실행 오류: {e}")
	finally:
		cursor.close()
		return res

def connect_to_mongodb(url, mongodb_name, collection_name):
	client = MongoClient(url)
	db = client[mongodb_name]
	collection = db[collection_name]
	return collection

# mongoDB 데이터 삽입 함수
def insert_data(collection, data):
	try:
		collection.insert_one(data)
		print("데이터 삽입 성공!")
	except Error as e:
		print(f"데이터 삽입 오류: {e}")


# 연결 설정 정보 - 자신의 데이터베이스 정보로 대체하세요
host_name = "XXXXXXXXXXXXXXXX"
db_username = "XXXXXXXXXX"
user_password = "XXXXXXXXXXXXXXXXXXXXXXXXX"
db_name = "XXXXXXXX"

## MongoDB 연결 정보
url = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
mongodb_name = "XXXXXXX"
collection_name = "XXXXXXXXXX"

# 데이터베이스 연결
mariaDB_conn = connect_to_mariadb(host_name, db_username, user_password, db_name)
mongoDB_conn = connect_to_mongodb(url, mongodb_name, collection_name)

# username이 일치하지 않는 사용자
warning_member = []

# mongoDB에 username이 mariaDB에 있는지 확인
try:
	# mongoDB에 있는 데이터를 가져옴
	all_documents = mongoDB_conn.find();

	for document in all_documents:
		if 'username' not in document:
			warning_member.append(document)
			#print(f"username이 없는 사용자: {document}")
			continue
		username = document['username']
		query = f"select * from member where username = '{username}';"
		mariaDB_member = execute_query(mariaDB_conn, query)
	if mariaDB_member == None:
		warning_member.append(document)
		#print(f"mariaDB에 없는 사용자: {document}")
	else:
		print(f"mariaDB에 있는 사용자: {document}")

except Error as e:
	print(f"쿼리 실행 오류: {e}")

for member in warning_member:
	print(f"mariaDB에 없는 사용자2: {member}")
#	mongoDB_conn.delete_one(member)
#	print(f"mongoDB에서 삭제된 사용자: {member}")

# 쿼리 실행
#if mariaDB_conn:
#	try:
#		member_list = execute_query(mariaDB_conn, "select * from member;")
#		for member in member_list:
#			id = member[0]
#			name = member[4]
#			username = member[6]
#			if username == None:
#				continue
#			sex = "male" if random.randint(0, 1) == 0 else "female"
#			insert_data(mongoDB_conn, {"name":name, "sex":sex, "username": username, "phone" : "010-1234-5678"})



#	except Error as e:
#		print(f"쿼리 실행 오류: {e}")
#	finally:
#		mariaDB_conn.close()




def invoke_db_original():
    global dbname_origin
    global collection_origin
    dbname_origin = input("오리지널 데이터베이스 이름을 입력해주세요: ")
    collection_origin = input("데이터베이스 내의 콜렉션을 입력해주세요: ")

def invoke_db_atlas():
    global dbname_atlas
    global collection_atlas
    dbname_atlas = input("개인 아틀라스 데이터베이스 이름을 입력해주세요: ")
    collection_atlas = input("아틀라스데이터베이스 내의 콜렉션을 입력해주세요: ")
def invoke_script():
    # Import the necessary modules and functions
    import time
    from dbsearch import search_by_username
    from load_data import load_data
    from extract_information import query_data
    from droptable import delete_all_documents

    # Record the start time
    start_time = time.time()
    # Specify the database and collection names
    client_name_origin = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    dbname_origin = 'mylist'
    form_data_collection_origin = 'form_data'

    dbname_atlas = 'XXXXXXXXX'
    collection_atlas = 'XXXXXXXXXXX'

    # Get the username to search as an input from the user
    username = input("매칭 사용자명을 입력해주세요: ").strip()  # Remove leading and trailing whitespace
    print("                                                            ")
    # Call the search_by_name_and_age function
    try:
        if not search_by_username(username, client_name_origin, dbname_origin, form_data_collection_origin):
            return False
    except Exception as e:
        print(f"search_by_link_and_age에 오류 발생: {e}")
        print("                                                            ")
        return False

    # Call the load_data function
    load_data(dbname_atlas, collection_atlas)

    # Call the function with your query
    try:
        output = query_data(f"{username}의 playlist와 가장 음악 취향이 비슷한 username은 뭐야? 이유도 알려줘", dbname_atlas, collection_atlas)
    except Exception as e:
        print(f"query_data 함수에 오류 발생: {e}")
        return False
    print("                                                            ")
    print("매칭 결과")
    # Check if output is a list or a tuple
    if isinstance(output, (list, tuple)):
        # Print each item on a different row
        for item in output:
            print(item)
            print("                                                            ")
    else:
        # If output is not a list or a tuple, just print it
        print(output)

    delete_all_documents(dbname_atlas, collection_atlas)

    # Record the end time
    end_time = time.time()

    # Calculate the runtime
    runtime = end_time - start_time
    print("                                                            ")
    print(f" 매칭 검색에 {runtime} 초가 걸렸습니다.")
    print("                                                            ")
    return True

import matching

while True:
    try:
        print("---------------------------------------------------------------------")
        print("플레이리스트 매칭프로그램 v0.1 with Python 3.12")
        print("                                                                                   ")
        print("안녕하세요 플레이리스트 매칭 프로그램입니다")
        print("이 프로그램은 플레이리스트를 기반으로 가장 유사한 사람을 찾아주는 프로그램입니다")
        print("실행하기 앞서서 폴더 안에 있는 requirements.txt를 pip install -r requirements.txt로 설치해주세요")
        print("                                                                                   ")
        print("조건: 성별이 반대")
        print("만약 매칭 결과가 이상하게 나오면 (혹은 이름이 나오지 않는 경우) 프로그램을 껐다가 다시 실행시켜주세요")
        print("                                                                                   ")
        print("1번을 누르시면 이름을 입력하시면 매칭을 시작합니다")
        print("2번을 누르시면 오리지널 데이터베이스를 설정합니다")
        print("3번을 누르시면 개인 아틀라스 데이터베이스를 설정합니다")
        print("4번을 누르시면 프로그램을 종료합니다")
        print("made by mylist")
        print("---------------------------------------------------------------------")

        choice = input("번호를 입력해주세요: ")

        if choice == '1':
            if not matching.invoke_script():  # Replace run.run_script() with run.invoke_script()
                print("오류 발생, 프로그램을 재시작합니다")
                continue
            with open('samples/data.txt', 'r', encoding='utf-8') as file:
                print("조건 필터링 결과")
                #print(file.read())

        elif choice == '2':
            matching.invoke_db_original()  # Replace run.set_db_original() with run.invoke_db_original()
        elif choice == '3':
            matching.invoke_db_atlas()  # Replace run.set_db_atlas() with run.invoke_db_atlas()
        elif choice == '4':
            print("프로그램을 종료합니다...")
            break
        else:
            print("잘못된 입력입니다. 1번과 4번사이로 다시 입력해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")
        continue  # Restart the script

from flask import Flask, request, redirect
import requests

app = Flask(__name__)

# 카카오 개발자 콘솔에서 얻은 정보를 입력하세요.
CLIENT_ID = "XXXXXXXXXXXXXXXXXXXXXXX"
CLIENT_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
REDIRECT_URI = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
FRIEND_UUIDS = ["XXXXXXXX"]

# 사용자를 카카오 로그인 페이지로 리다이렉트하는 엔드포인트
@app.route("XXXXXXX")
def login():
	return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code")

# 카카오로부터 리다이렉트 되는 엔드포인트, 인증 코드를 받고 액세스 토큰 요청
@app.route("XXXXXXXXXXXXXXXXXX")
def oauth():
	code = request.args.get("code")
	token = get_access_token(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, code)
	if token:
		return send_message(token, FRIEND_UUIDS, "My List 테스트")
	else:
		return "액세스 토큰을 획득할 수 없습니다."

# 인증 코드를 사용해 액세스 토큰을 획득하는 함수
def get_access_token(client_id, client_secret, redirect_uri, code):
	url = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	payload = {
		"grant_type": "authorization_code",
		"client_id": client_id,
		"client_secret": client_secret,
		"redirect_uri": redirect_uri,
		"code": code
	}
	response = requests.post(url, data=payload)
	print(response.json())
	if response.status_code == 200:
		return response.json()["access_token"]
	else:
		return None

def send_message(access_token, friend_uuids, message):
	headers = {
		"Authorization": f"Bearer {access_token}",
		"Content-Type": "application/json",
	}

	data = {
		"receiver_uuids": friend_uuids, # 수신자 UUID 리스트
		"template_object": { # 메시지 내용
			"object_type": "text",
			"text": message,
			"link": {
				"web_url": "https://match.mylist.im",
				"mobile_web_url": "https://match.mylist.im"
			},
			"button_title": "매칭 다시 신청하기"
		}
	}

	response = requests.post('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', headers=headers, json=data)

	print("[STATUS]: " , response.status_code)
	print(response.json())

	return "메시지 전송 성공!"

if __name__ == "__main__":
	app.run(debug=True)

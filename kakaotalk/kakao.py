import requests
import json


class Kakaotalk():

    def kakao_login(self):
        url = 'https://kauth.kakao.com/oauth/token'
        rest_api_key = 'e4ec918cd4f0c0110c7ea1de7face491'
        redirect_uri = 'https://example.com/oauth'
        authorize_code = "" # 보안상 삭제

        data = {
            'grant_type': 'authorization_code',
            'client_id': rest_api_key,
            'redirect_uri': redirect_uri,
            'code': authorize_code,
        }

        response = requests.post(url, data=data)
        tokens = response.json()
        print(tokens)

        with open("kakao_code.json", "w") as fp:
            json.dump(tokens, fp)

    def send_message(self, a, b):
        with open("kakaotalk/kakao_code.json", "r") as fp:
            tokens = json.load(fp)

        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

        headers = {
            "Authorization": "Bearer " + tokens["access_token"]
        }

        cheating_message = "{0} {1} 학생의 부정행위가 의심됩니다. 확인해주세요.".format(a, b)

        # 카카오톡 측에서 로컬에 저장된 이미지는 카카오톡 메세지로 저장하는 기능을 제공하지 않고 있음
        # 만약 kakao api를 통해 메세지를 보낸다면, 1. 웹 서버에 사진을 저장하거나 / 2. 텍스트만 전송
        # 만약 text만 전송한다면, feed message 대신 text message가 나을까?
        template = {
            "object_type": "feed",
            "content":
                {
                    "title": "Stop_Cheating",
                    "description": cheating_message,
                    "image_url": "https://image.shutterstock.com/image-photo/cheating-on-test-young-bearded-600w-270696500.jpg",
                    "link": {
                        "web_url": "www.naver.com",
                        "mobile_web_url": "www.naver.com"
                    }
                }
        }

        data = {
            "template_object": json.dumps(template)
        }

        response = requests.post(url, headers=headers, data=data)
        print("Response Status Code: {0}".format(response.status_code))
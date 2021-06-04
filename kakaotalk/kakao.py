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

        data = {
            "template_object": json.dumps({
                "object_type": "text",
                "text": cheating_message,
                "link": {
                    "web_url": "www.naver.com"
                }
            })
        }

        response = requests.post(url, headers=headers, data=data)
        print("Response Status Code: {0}".format(response.status_code))
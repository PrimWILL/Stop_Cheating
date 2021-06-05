import requests
import json


class Kakaotalk():

    def send_message(self, a, b, date, hour, cheating_code):
        with open("kakaotalk/kakao_code.json", "r") as fp:
            tokens = json.load(fp)

        cheat_string = ""

        if cheating_code == 1:
            cheat_string = "2인 이상 감지"
        elif cheating_code == 2:
            cheat_string = "휴대폰 검출"
        elif cheating_code == 3:
            cheat_string = "응시자 자리이탈"
        elif cheating_code == 4:
            cheat_string = "시험지,답안지 미포착"

        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

        headers = {
            "Authorization": "Bearer " + tokens["access_token"]
        }

        cheating_message = "{0} {1} 학생의 부정행위가 의심됩니다. 확인부탁드립니다. / 일시: {2}_{3} / 사유: {4}".format(a, b, date, hour, cheat_string)

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
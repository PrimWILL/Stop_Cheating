import requests
import json

with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

template = {
    "object_type" : "feed",
    "content" :
    {
        "title" : "Stop_Cheating",
        "description" : "부정행위가 의심됩니다. 확인해주세요.",
        # 카카오톡 측에서 로컬에 저장된 이미지는 카카오톡 메세지로 저장하는 기능을 제공하지 않고 있음
        # 만약 kakao api를 통해 메세지를 보낸다면, 1. 웹 서버에 사진을 저장하거나 / 2. 텍스트만 전송
        "image_url" : "https://image.shutterstock.com/image-photo/cheating-on-test-young-bearded-600w-270696500.jpg",
        "link" : {
            "web_url" : "www.naver.com",
            "mobile_web_url" : "www.naver.com"
        }
    }
}

data={
    "template_object": json.dumps(template)
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
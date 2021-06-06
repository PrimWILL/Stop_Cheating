import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '405fae226d8dc36b6815206762d946f9' #'e4ec918cd4f0c0110c7ea1de7face491'
redirect_uri = 'https://example.com/oauth'
authorize_code = 's_mjnZhjB_a8-6zWBU1YNYLTCxyrm57xp0qQjrud2sGeQxaBFJzEjHDCT4MIvTq4q5Fi3AorDKgAAAF54JDKGA' # 보안상 삭제

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

#2.
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)



import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '405fae226d8dc36b6815206762d946f9'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'LByddgcRpcjZvWCebnVSEMxzaJfkC1m1JsTNGtgJ4g61rgTz8oTq5I6DDEn1tiuxBwcFWwopyNoAAAF54IHGBQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)
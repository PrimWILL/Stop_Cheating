import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'e4ec918cd4f0c0110c7ea1de7face491'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'XKVjyOif1sEk1RV64i43_EaFMOafLCRtDhw5kWE7yHBT50ZJ6crhb_ZDtde6ww0pyIfNzwo9dJgAAAF53YHxtg'

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


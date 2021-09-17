import requests
import json

user_key = "ZnlyREhhbDZqSnFmS0V1dy9HVzRIZz09"
url = "https://api.signupgenius.com/v2/k/user/profile/?user_key=" + user_key
response = requests.get(url)

print (response.status_code)
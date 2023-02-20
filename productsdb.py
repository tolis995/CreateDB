# import requests
# import json
# url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"
#
# headers = {
# 	"X-RapidAPI-Key": "6fe1701727mshd5868d60c5d69d7p1e9f2bjsnddd3997b6fc9",
# 	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
# }
#
# response = requests.request("GET", url, headers=headers)
# print(response)
# print(response.text)
#
# data = json.load(response.text)
# print(data)
# print(data['data'])


import http.client
import json

headers = {
    'X-RapidAPI-Key': "6fe1701727mshd5868d60c5d69d7p1e9f2bjsnddd3997b6fc9",
    'X-RapidAPI-Host': "wft-geo-db.p.rapidapi.com"
    }

conn.request("GET", "/v1/geo/adminDivisions", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
data2 = json.load(data.decode("utf-8"))
print(data2)
print(data2['data'])

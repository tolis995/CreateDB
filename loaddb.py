#f = open("users.csv", "r",  encoding="utf8")
#print(f.read())
import csv

import null as null

# f=open("users.csv", 'r', encoding="utf8")
# header=f.readline()
# fields=header.split(";")
# print("Αριθμός πεδίων:", len(fields))
# c=1
# for x in fields:
#     print(c,x)
#     c=c+1

# with open("users.csv", 'r', encoding="utf8") as file:
#   csvreader = csv.reader(file)
#   for row in csvreader:
#       fields=row[0].split(";")
#       print(fields)

# import pandas as pd
# data = pd.read_csv("users.csv",error_bad_lines=False)
import requests

url = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"

headers = {
	"X-RapidAPI-Key": "6fe1701727mshd5868d60c5d69d7p1e9f2bjsnddd3997b6fc9",
	"X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

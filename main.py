#import the library
import sqlite3

#creating connection
conn = sqlite3.connect(
  host="https://integrationrabbit.methodoos.com",
  user="testuser",
  password="testuser@#$",
  database ="integrationrabbit"
)

mycursor = db.cursor()

sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
# iterate over the result
# for row in cursor:


# we close the cursor and conn both
cursor.close()
conn.close()

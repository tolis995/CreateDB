import mysql.connector
#import pyodbc
# creating connection
db = mysql.connector.connect(
  host="integrationrabbit.methodoos.com",
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

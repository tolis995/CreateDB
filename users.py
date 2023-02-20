import sqlite3

db = sqlite3.connect("users.db")
db.execute("CREATE TABLE if not exists users (_id INTEGER PRIMARY KEY AUTOINCREMENT, uid integer, username text, phone_number text, email text, password text, last_login text, first_name text, last_name text, is_email_verified boolean, is_superuser boolean, is_staff boolean, is_active boolean, date_joined date, language text, timezone text, hubspot_contact_id text, email_notifications boolean)")

insert_string="insert "

cursor=db.execute("select * from users")

for x in cursor:
    print(x)

cursor.close()
db.commit()
db.close()



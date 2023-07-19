import mysql.connector as mysql

db = mysql.connect(host="localhost",
                   user="root",
                   passwd="naskevich8",
                   database="test_db_2")
cursor = db.cursor()
cursor.execute("ALTER TABLE usersADD PRIMARY KEY(column_name)")
cursor.execute("DESC users")
print(cursor.fetchall())

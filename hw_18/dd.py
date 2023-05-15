import mysql.connector as mysql

db = mysql.connect(host="localhost",
                   user="root",
                   passwd="naskevich8")

cursor = db.cursor()
cursor.execute("CREATE DATABASE test_db_2")

cursor.execute("SHOW DATABASES")
print(cursor.fetchall())
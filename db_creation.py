import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilon135792468"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE example_db")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

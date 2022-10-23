import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilon135792468",
    database="example_db"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students(name VARCHAR(255), age INTEGER)")
sql = "SHOW TABLES"
mycursor.execute(sql)
for tb in mycursor:
    print(tb)

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilon135792468",
    database="example_db"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * From students WHERE name Like 'A%'")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilon135792468",
    database="example_db"
)
mycursor = mydb.cursor()
sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
student = [('Alex', 27), ("Adi", 26)]
mycursor.executemany(sqlFormula, student)
mydb.commit()

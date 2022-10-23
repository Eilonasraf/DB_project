import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilon135792468",
    database="primary_db"
)
mycursor = mydb.cursor()
sql = "SELECT customers.name AS user, products.name AS favorite FROM customers INNER JOIN products ON customers.fav = products.id"
mycursor.execute(sql)
myresault = mycursor.fetchall()
for user in myresault:
    print(user)
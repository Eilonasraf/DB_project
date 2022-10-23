import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Eilon135792468",
    database="primary_db"
)
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE primary_db")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE workers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
#
# sql_formula = "INSERT INTO workers (name, address) VALUES (%s, %s)"
# workers = [("Alex", "Mandes"), ("Alex", "Mandes"), ("Adi", "Dankner")]
# mycursor.executemany(sql_formula, workers)
# mydb.commit()

#Delete
mycursor = mydb.cursor()
# sql_formula = "DELETE FROM workers WHERE name='Alex' and id = 1"
# # workers = [("Alex", "Mandes"), ("Alex", "Mandes"), ("Adi", "Dankner")]
# mycursor.execute(sql_formula)
# mydb.commit()

# Add columns
# sql_formula = "ALTER TABLE workers ADD COLUMN age INT"
# mycursor.execute(sql_formula)
# mydb.commit()

# Two Tables
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")
# mycursor.execute("CREATE TABLE products (id INT, name VARCHAR(255))")
sql_formula_cust = "INSERT INTO customers (name, fav) VALUES (%s, %s)"
sql_formula_prod = "INSERT INTO products (id, name) VALUES (%s, %s)"
customers = [("John", 154), ("Peter", 154), ("Amy", 155)]
products = [(154, "Twix"), (155, "Milky way"), (156, "Mars")]
mycursor.executemany(sql_formula_cust, customers)
mycursor.executemany(sql_formula_prod, products)
mydb.commit()
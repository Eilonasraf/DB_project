import sqlite3
# Connect to DB
connection = sqlite3.connect('users')
cursor = connection.cursor()
# Create table
# sql = 'CREATE TABLE users (username varchar(30), admin boolean, password varchar(30))'
# cursor.execute(sql)
# Populate table
# sql = 'INSERT INTO users (username, admin, password) VALUES ("David", true, "1234"), ("Moshe", false, "5678")'
# cursor.execute(sql)
# connection.commit()
# cursor.execute("SELECT * From users")
# myresult = cursor.fetchall()
# for row in myresult:
#     print(row)

def get_user(username, password, cursor):
    cursor.execute("SELECT * FROM users WHERE username = '%s' AND password = '%s'" % (username, password))
    result = cursor.fetchone()

    if result is None:
    # User does not exist
        return False

    return result

print(get_user("' OR 'a'='a';--,'", '1234', cursor))

def safely_get_user(username, password, cursor):
    cursor.execute("SELECT * FROM users WHERE username= ? AND password = ?", (username, password))
    result = cursor.fetchone()
    if result is None:
        # User does not exist
        return False

    return result

print(safely_get_user("' OR 'a'='a';--,'", '1234', cursor))
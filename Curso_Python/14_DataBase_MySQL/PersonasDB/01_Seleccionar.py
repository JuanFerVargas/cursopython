import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas")
result = cursor.fetchall()
for persona in result:
    print(persona)
cursor.close()
personas_db.close()

import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

cursor = personas_db.cursor()
# Insertar una persona
sentencia_sql = "INSERT INTO personas (nombre, apellido , edad) VALUES (%s, %s, %s)"
valores = ("Carlos", "Perez", 55)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(cursor.rowcount, "registro insertado.")
cursor.close()
personas_db.close()
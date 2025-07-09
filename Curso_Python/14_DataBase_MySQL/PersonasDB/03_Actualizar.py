import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

cursor = personas_db.cursor()
sentencia_sql = "UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s"
valores = ("Victoria", "Florez", 45, 4)  # Actualizar el registro con id = 1
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(cursor.rowcount, "registro(s) actualizado(s).")
cursor.close()
personas_db.close()
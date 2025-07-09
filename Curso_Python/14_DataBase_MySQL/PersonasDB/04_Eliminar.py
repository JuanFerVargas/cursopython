import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

cursor = personas_db.cursor()
cursor.execute("DELETE FROM personas WHERE id = 5")  # Cambia el ID según el registro que quieras eliminar
personas_db.commit()  # Asegúrate de hacer commit para guardar los cambios
print(cursor.rowcount, "registro(s) eliminado(s).")
cursor.close()
personas_db.close()

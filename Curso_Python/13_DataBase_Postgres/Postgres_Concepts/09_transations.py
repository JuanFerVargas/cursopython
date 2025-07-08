import psycopg2 as bd

conexion = bd.connect("dbname=test_db user=postgres password=admin host=localhost port=5432")

try:
    with conexion:              # Crea un contexto de conexión
        with conexion.cursor() as cursor:       # Crea un cursor para ejecutar consultas
            sentencia_sql = "INSERT INTO PERSONA (NOMBRE, APELLIDO, EMAIL) VALUES (%s, %s, %s)"
            valores = ('Alex','Rojas','arojas@mail.com')
            cursor.execute(sentencia_sql, valores)

            sentencia_sql = "UPDATE PERSONA SET NOMBRE = %s, APELLIDO = %s, EMAIL = %s WHERE ID_PERSONA = %s"
            valores = ('Juan', 'Perez', 'jperez@mail.com','1')  
            cursor.execute(sentencia_sql, valores)

            registros_insertados = cursor.rowcount  # Obtiene el número de registros afectados
            print("Número de registros Insertados:", registros_insertados)
except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")
finally:
    if conexion:        # Cierra la conexión si está abierta
        conexion.close()  
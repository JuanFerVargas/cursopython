import psycopg2

def connect_to_db():
    try:
        # Connect to your postgres DB
        conexion = psycopg2.connect("dbname=test_db user=postgres password=admin host=localhost port=5432")
        print("Conexión exitosa a la base de datos")   
        return conexion
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None 
    
print("Conectando a la base de datos...")
conexion = connect_to_db()
try:
    with conexion:
        with conexion.cursor()  as cursor:
            sentencia_sql = "UPDATE PERSONA SET NOMBRE = %s, APELLIDO = %s, EMAIL = %s WHERE ID_PERSONA = %s"
            valores = (
                ('Carol', 'Herrera', 'cherrera@mail.com','6'),  
                ('Camilo', 'Bustos', 'cbustos@mail.com','7')  
            )
            cursor.executemany(sentencia_sql, valores)
            registros_actualizados = cursor.rowcount  # Obtiene el número de registros afectados
            print("Número de registros actualizados:", registros_actualizados)
except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")
finally:
    if conexion:
        conexion.close()
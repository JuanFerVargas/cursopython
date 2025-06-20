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
            sentencia_sql = "INSERT INTO PERSONA (NOMBRE, APELLIDO, EMAIL) VALUES (%s, %s, %s)"
            valores = (
                    ('Carlos','Lara','clara@mail.com'),  
                    ('Ana','Gómez','agomez@mail.com'),
                    ('Luis','Pérez','lperez@mail.com')
            )
            cursor.executemany(sentencia_sql, valores)
            registros_afectados = cursor.rowcount  # Obtiene el número de registros afectados
            print("Número de registros insertados:", registros_afectados)
except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")
finally:
    if conexion:
        conexion.close()
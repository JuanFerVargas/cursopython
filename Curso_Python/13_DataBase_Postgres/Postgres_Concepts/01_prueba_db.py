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
try:
    conexion = connect_to_db()
except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")
finally:
    if conexion:
        conexion.close()
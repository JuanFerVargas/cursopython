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
            sentencia_sql = "SELECT * FROM PERSONA WHERE ID_PERSONA IN %s"
            entrada = input("Introduce los IDs de las personas que quieres consultar (separado por comas): ")
            llaves_primarias = (tuple(entrada.split(',')),)  # Convierte la entrada a una tupla
            # id_persona = 2  # Cambia este valor según el ID que quieras consultar
            cursor.execute(sentencia_sql, llaves_primarias)
            resultados = cursor.fetchall() # Obtiene todos los resultados de la consulta
            # resultado = cursor.fetchone() #  Obtiene un solo resultado de la consulta
            print("Resultados de la consulta:")
            for fila in resultados:
                print(fila)
except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")
finally:
    if conexion:
        conexion.close()
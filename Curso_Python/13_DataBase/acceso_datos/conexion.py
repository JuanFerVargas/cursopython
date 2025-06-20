from logger_base import log
import psycopg2 as bd
class Conexion:

    _DATABASE = "test_db"
    _HOST = 'localhost'
    _DB_PORT = 5432
    _USERNAME = "postgres"
    _PASSWORD = "admin"
    _conexion = None
    _cursor = None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None:
            try:
                
                cls._conexion = bd.connect(
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE,
                    user=cls._USERNAME,
                    password=cls._PASSWORD                  
                )
                log.debug(f"Conexión exitosa a la base de datos: {cls._conexion} ")
            except Exception as e:
                log.error(f"Error al conectar a la base de datos: {e}")
        else:
            return cls._conexion
    
    @classmethod
    def obtener_cursor(cls):
        if cls._conexion is None:
            cls.obtener_conexion()
        if cls._cursor is None:
            try:
                cls._cursor = cls._conexion.cursor()
                log.debug(f"Cursor obtenido: {cls._cursor}")
            except Exception as e:
                log.error(f"Error al obtener el cursor: {e}")
        return cls._cursor
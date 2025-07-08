from logger_base import log
from psycopg2 import pool
from os import sys

class Conexion:

    _DATABASE = 'postgres'
    _USER = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _PORT = '5432'
    _MIN_CON=1
    _MAX_CON=5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON,cls._MAX_CON, host=cls._HOST, port=cls._PORT, dbname=cls._DATABASE, user=cls._USER, password=cls._PASSWORD)
                log.debug(f'Pool de conexiones creado: id={id(cls._pool)}')
                log.debug(f'Creación del Pool exitosa: {cls._pool}')
            except Exception as e:
                log.error(f'Ocurrió un error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            log.debug(f'Pool de conexiones ya creado: id={id(cls._pool)}')
        return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: id={id(conexion)}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        log.debug('Pool de conexiones cerrado.')

if __name__ == '__main__':

    conexion1=Conexion.obtenerConexion()
    conexion1=Conexion.liberarConexion(conexion1)

    # conexion2=Conexion.obtenerConexion()
    # conexion2=Conexion.liberarConexion(conexion2)

    # conexion3=Conexion.obtenerConexion()
    # conexion3=Conexion.liberarConexion(conexion3)

    # conexion4=Conexion.obtenerConexion()
    # conexion4=Conexion.liberarConexion(conexion4)

    # conexion5=Conexion.obtenerConexion()
    # conexion5=Conexion.liberarConexion(conexion5)

    # conexion6=Conexion.obtenerConexion()
    # conexion6=Conexion.liberarConexion(conexion6)

    # conexion7=Conexion.obtenerConexion()
    # conexion8=Conexion.obtenerConexion()
    # conexion9=Conexion.obtenerConexion()
    # conexion10=Conexion.obtenerConexion()
    # conexion11=Conexion.obtenerConexion()



    


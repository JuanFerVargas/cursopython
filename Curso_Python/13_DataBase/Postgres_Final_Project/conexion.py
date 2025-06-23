from logger_base import log
from psycopg2 import pool


class Conexion:
    _pool = ConnectionPool(
        conninfo="host=127.0.0.1 port=5432 dbname=test_db user=postgres password=admin",
        min_size=1,
        max_size=5,
        timeout=5
    )

    @classmethod
    def obtener_pool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls.min_size,cls.max_size, host=cls.host, port=cls.port, dbname=cls.dbname, user=cls.user, password=cls.password)
                log.debug(f'Pool de conexiones creado: id={id(cls._pool)}')
            except Exception as e:
                log.error(f'Ocurrió un error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            log.debug(f'Pool de conexiones ya creado: id={id(cls._pool)}')
        return cls._pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls._pool.getconn()
        log.debug(f'Conexión obtenida del pool: id={id(conexion)}')
        return conexion

    @classmethod
    def liberar_conexion(cls, conexion):
        cls._pool.putconn(conexion)
        log.debug(f'Conexión liberada al pool: id={id(conexion)}')

    @classmethod
    def cerrar_conexion(cls):
        cls._pool.closeall()
        log.debug('Pool de conexiones cerrado.')

if __name__ == '__main__':
    Conexion._pool.check()
    log.debug('Pool de conexiones verificado correctamente.')

    # Caso con with, donde se reutilizan las conexiones
    for i in range(10):  # Pide 10 conexiones, pero se liberan automáticamente
        with Conexion.obtener_conexion() as conexion:
            log.debug(f'Conexión #{i + 1} abierta y cerrada: id={id(conexion)}')

    Conexion._pool.close()
    log.debug('Pool de conexiones cerrado correctamente.')

    # Las conexiones de liberar de manera automatica al user with
    # y el metodo _pool.connection()
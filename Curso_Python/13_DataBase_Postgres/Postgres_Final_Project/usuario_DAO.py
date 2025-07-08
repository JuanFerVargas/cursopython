import logging
from cursor_del_pool import CursorDelPool
from usuario import Usuario

log = logging.getLogger(__name__)

class UsuarioDAO:
    # Data Access Object (DAO) para a tabla de usuarios
    
    _SELECT='SELECT * FROM usuarios ORDER BY 1'
    _INSERTAR='INSERT INTO usuarios (username, password) VALUES (%s, %s)'
    _ACTUALIZAR='UPDATE usuarios SET username = %s, password = %s WHERE id_usuario = %s'
    _ELIMINAR='DELETE FROM usuarios WHERE id_usuario = %s'


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(id_usuario=registro[0], username=registro[1], password=registro[2])
                log.debug(f'Usuario recuperado: {usuario}')
                usuarios.append(usuario)
            return usuarios
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a Insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount  # Retorna el número de filas afectadas

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a Actualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount  # Retorna el número de filas afectadas
    
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a Eliminar: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':

    UsuarioDAO.seleccionar()

    # Insertar un registro
    # usuario1 = Usuario(username='admin1', password='12456')
    # UsuarioDAO.insertar(usuario1)

    # Actualizar un registro
    # usuario2 = Usuario(id_usuario=1, username='siname', password='87654')
    # UsuarioDAO.actualizar(usuario2)

    # Eliminar un registro
    # usuario3 = Usuario(id_usuario=1)
    # UsuarioDAO.eliminar(usuario3)
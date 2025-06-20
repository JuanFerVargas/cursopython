import logging as log
import os

# Asegura que la ruta exista
log_dir = os.path.join('Curso_Python', '13_DataBase', 'acceso_datos')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'capa_datos_persona.log')

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)s]- %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        log.FileHandler(log_file, encoding='utf-8'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('Mensaje de depuración')
    log.info('Mensaje informativo')
    log.warning('Mensaje de advertencia')
    log.error('Mensaje de error')
    log.critical('Mensaje crítico')
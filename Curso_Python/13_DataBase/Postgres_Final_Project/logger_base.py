import logging as log
import os

# Asegura que la ruta exista
log_dir = os.path.join('Curso_Python', '13_DataBase', 'Postgres_Final_Project')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'capa_datos_persona.log')

log.basicConfig(
                level=log.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)s]- %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                handlers=[
                    log.FileHandler(log_file, encoding='utf-8'),
                    log.StreamHandler()
                ]
)

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')
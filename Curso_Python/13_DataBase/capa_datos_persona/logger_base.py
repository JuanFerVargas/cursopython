import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)s]- %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S', 
                handlers=[
                    log.FileHandler(f'Curso_Python\{13}_DataBase\capa_datos_persona\capa_datos_persona.log', encoding='utf-8'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje de depuración')
    log.info('Mensaje informativo')
    log.warning('Mensaje de advertencia')
    log.error('Mensaje de error')
    log.critical('Mensaje crítico')
    # logger_base.py
import os

class CatalogoPeliculas:

    ruta_archivo = '/home/user/cursopython/Curso_Python/12_Archivos/catalogo_peliculas/servicio/peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as archivo:
            print('Catálogo de Películas'.center(50,'-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
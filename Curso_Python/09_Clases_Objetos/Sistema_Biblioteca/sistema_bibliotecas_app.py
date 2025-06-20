from biblioteca import Biblioteca
from libro import Libro

bibiotecaNacional=Biblioteca('Biblioteca Nacional')
print(f'Bienvenidos a la {bibiotecaNacional.nombre}')

# Definicion de libros

libro1=Libro('Harry Potter y la piedra filosofal','J.K. Rowling','Fantasia')
libro2=Libro('Harry Potter y la camara secreta','J.K. Rowling','Fantasia')
libro3=Libro('Maldito karma','David Safier','comedia')


# Agregar libros biblioteca
bibiotecaNacional.agregar_libro(libro1)
bibiotecaNacional.agregar_libro(libro2)
bibiotecaNacional.agregar_libro(libro3)


# buscar libros por autor
autor='J.K. Rowling'
print(f'\nLos libros de {autor} son:')
bibiotecaNacional.buscar_libro(autor)

# buscar libros por genero
genero='comedia'
print(f'\nLos libros de {genero} son:')
bibiotecaNacional.buscar_libro_por_genero(genero)

# mostrar todos los libros de la biblioteca
bibiotecaNacional.mostrar_todos_los_libros()
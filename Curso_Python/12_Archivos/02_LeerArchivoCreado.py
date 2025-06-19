# archivo = open('c:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
archivo = open('//home//user//cursopython//Curso_Python//12_Archivos//prueba.txt', 'r', encoding='utf8')
# print(archivo.read())

# leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# leer lineas completas
# print(archivo.readline())
# print(archivo.readline())


# Iterar cada una de las lineas
# for linea in archivo:
#     print(linea)

# leer todas las lineas
# print(archivo.readlines())
# print(archivo.readlines())

# Abrirmos un nuevo archivo
# a - Anexar información
archivo2=open('//home//user//cursopython//Curso_Python//12_Archivos//copia.txt','a',encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha terminado el proceso de leer archivos')


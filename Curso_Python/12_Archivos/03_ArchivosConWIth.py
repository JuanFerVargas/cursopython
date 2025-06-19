# with open('//home//user//cursopython//Curso_Python//12_Archivos//prueba.txt', 'r', encoding='utf8') as archivo:

from ManejoArchivos import ManejoArchivos

with ManejoArchivos('//home//user//cursopython//Curso_Python//12_Archivos//prueba.txt') as archivo:
    print(archivo.read())
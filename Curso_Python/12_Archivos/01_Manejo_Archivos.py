try:
    archivo=open('//home//user//cursopython//Curso_Python//12_Archivos//prueba.txt','w',encoding='utf8')      #
    
    archivo.write('Esto es una prueba\n')
    archivo.write('Está es una prueba\n')

except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Se ha finalizado la prueba')
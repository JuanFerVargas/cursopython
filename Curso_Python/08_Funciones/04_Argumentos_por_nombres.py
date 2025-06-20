print('*** Funcion con argumentos por nombre ***')

def imprimir_persona(nombre,apellido='',edad=0):
    print(f'Persona: Nombre: {nombre} Apellido: {apellido} Edad: {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Juan','Perez',32)

# Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Carlos',apellido='Rojas',edad=28)

# Llamar la funcion usando argumentos intercambiando el orden
imprimir_persona(edad=28,apellido='Rojas',nombre='Carlos')

# Argumentos con valor por default
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Carlos',apellido='Rojas')
imprimir_persona(apellido='Rojas', nombre='Carlos')
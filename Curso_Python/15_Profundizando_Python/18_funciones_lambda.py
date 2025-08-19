# Funciones Lambda
# Son funciones anónimas que se definen con la palabra clave lambda.

def sumar(a,b):
    return a + b

# Con una funcion lambda (anonima, sin nombre, y una sola linea de codigo)
# No se necesita definirla con la palabra clave def ni parentesis
# No se necesita usar la palabra clave return

mi_funcion_lambda = lambda a, b: a + b
# Se puede llamar a la funcion lambda como cualquier otra funcion
resultado_lambda = mi_funcion_lambda(4, 6)
print(f"Resultado de la función lambda: {resultado_lambda}")  # Resultado de la función lambda: 8

# Funcion lambda que no recibe argumentos

mi_funcion_lambda = lambda: "Hola, soy una función lambda sin argumentos"
print(f'Llamar la funcion lambda sin argumentos: {mi_funcion_lambda()}')

# Funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Llamar la funcion lambda con valores por default: {mi_funcion_lambda()}')
print(f'Llamar la funcion lambda con un argumento: {mi_funcion_lambda(10)}')
print(f'Llamar la funcion lambda con dos argumentos: {mi_funcion_lambda(10, 20)}')

# Funcion lambda con argumentos variables *args y *kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Llamar la funcion lambda con *args y **kwargs: {mi_funcion_lambda(1, 2, 3, a=5, b=6)}') 

# Funciones lambda con argumentos, argumentos variables y valores por default.
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a + b + c + len(args) + len(kwargs)
print(f'Llamar la funcion lambda con argumentos, *args, **kwargs y valores por default: {mi_funcion_lambda(1, 2, 4, 5, 6, 7, e=6, f=7)}')
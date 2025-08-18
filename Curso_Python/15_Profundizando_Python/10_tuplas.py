# Profundizando en tuplas

# Declarar variables
a,b='Hola','Adios'
print(a,b)

# Swap (Intercambio)
a,b = b,a
print(a,b)

# Regresar multiples valores en una funcion
def minmax(elementos):
    return min(elementos), max(elementos)

minimo, maximo = minmax([1, 2, 3, 4, 5])
print(f'Valor minimo {minimo} y valor maximo {maximo}')

# Regresar la suma de una tupla

resultado = sum((1, 2, 3, 4, 5))
print(f'Suma de la tupla: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1, 2, 3, 4, 5)
print(f'Suma de los argumentos: {resultado}')

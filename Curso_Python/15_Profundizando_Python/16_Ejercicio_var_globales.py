# Definicion de variables globales
contador=0

def mostrar_contador():
    print(f'Contador: {contador}')

def incrementar_contador(*args):
    global contador
    contador += sum(args)

incrementar_contador(5)
mostrar_contador()

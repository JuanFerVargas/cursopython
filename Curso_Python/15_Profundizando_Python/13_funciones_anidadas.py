# Funciones anidadas

def calculadora(a,b,operacion='sumar'):

    # 1. Definir Funcion anidada
    def sumar(a,b):
        return a + b

    def restar(a,b):
        return a - b
    
    def multiplicar(a,b):
        return a * b
    
    def dividir(a,b):
        return a / b

    # 2. llamamos a la funcion anidada
    if operacion == 'sumar':
        print(f'Resultado de sumar: {sumar(a,b)}' )
    elif operacion == 'restar':
        print(f'Resultado de restar: {restar(a,b)}' )
    elif operacion == 'multiplicar':
        print(f'Resultado de multiplicar: {multiplicar(a,b)}' )
    elif operacion == 'dividir':
        print(f'Resultado de dividir: {dividir(a,b)}' )

calculadora(5,6,)
calculadora(4,3, 'restar')
calculadora(2,3, 'multiplicar')
calculadora(8,2, 'dividir')

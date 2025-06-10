class Aritmetica:

    """
    Clase Aritmetica para realizar las operacoones de sumar, restar, etc
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        resultado= self.operandoA + self.operandoB
        print(f'Resultado Suma: {resultado}')

    def restar(self):
        resultado= self.operandoA - self.operandoB
        print(f'Resultado Resta: {resultado}')
        
    def multiplicar(self):
        resultado= self.operandoA * self.operandoB
        print(f'Resultado Multiplicacion: {resultado}')

    def dividir(self):
        resultado= self.operandoA / self.operandoB
        print(f'Resultado Division: {resultado}')
    
# Creacion de Objeto
if __name__ == '__main__':
    print('*** Clase Aritmetica ***')

    aritmetica1 = Aritmetica(5,7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    print()
    aritmetica2 = Aritmetica(12,16)
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
    aritmetica2.dividir()
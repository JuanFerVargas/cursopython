from teclado import Teclado
from raton import Raton
from monitor import Monitor

class Computadora:
    contador_computadoras =0

    def __init__(self, nombre, monitor,teclado,raton):
        Computadora.contador_computadoras +=1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
    
    def __str__(self):
        return f"""
        id: {self.id_computadora}
        nombre: {self.nombre}
        monitor: {self.monitor}
        teclado: {self.teclado}
        raton: {self.raton}
        """

if __name__ == '__main__':
    # Importamos las clases y las llamamos
    monitor = Monitor('HP', '24 Pulgadas')
    teclado = Teclado('Logitech', 'Bluetooth')
    raton = Raton('Logitech', 'Bluetooth')

    computadora1 = Computadora('HP', monitor, teclado, raton)
    print(computadora1)

    monitor2 = Monitor('Lenovo', '17 Pulgadas')
    teclado2 = Teclado('Red Dragon', 'USB')
    raton2 = Raton('Red Dragon', 'USB')

    computadora2 = Computadora('Lenovo', monitor2, teclado2, raton2)
    print(computadora2)
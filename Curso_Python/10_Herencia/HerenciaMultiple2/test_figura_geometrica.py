from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

if __name__ == "__main__":

    print("Herencia Multiple")
    print("Creación Objeto Cuadrado".center(50,'-'))
    cuadrado1 = Cuadrado(lado=5, color="rojo")
    cuadrado1.alto=-10
    print(cuadrado1)
    print(f"El area del cuadrado es: {cuadrado1.calcular_area()}\n")

    print("Creación Objeto Rectangulo".center(50,'-'))
    rectangulo1 = Rectangulo(ancho=9, alto=8, color="verde")
    rectangulo1.ancho=15
    print(rectangulo1)
    print(f"El area del rectangulo es: {rectangulo1.calcular_area()}")
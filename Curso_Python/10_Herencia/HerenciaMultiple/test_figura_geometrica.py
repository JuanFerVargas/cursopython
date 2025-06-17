from Cuadrado import Cuadrado

cuadrado1= Cuadrado(5, "rojo")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'El area del cuadrado es: {cuadrado1.calcular_area()}')
print(f'El area del perimetro es: {cuadrado1.calcular_perimetro()}')

# Method Resolution Order
print(Cuadrado.mro())
# Polimorfismo

class Animal:
    def hacer_sonido(self):
        print("Hago un pitido")

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau")

# Funcion polimorfica
def hacer_sonido_animal(animal):    # duck typing
    animal.hacer_sonido()


print('*** Ejemplo Polimorfismo ***')
print('\nClase Padre Animal')
animal1=Animal()
# animal1.hacer_sonido()
hacer_sonido_animal(animal1)

print('\nClase Hija Perro')
perro1=Perro()
# perro1.hacer_sonido()
hacer_sonido_animal(perro1)

print('\nClase Hija Gato')
gato1=Gato()
# gato1.hacer_sonido()
hacer_sonido_animal(gato1)


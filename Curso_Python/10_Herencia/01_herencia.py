class Animal:

    def comer(self):
        print("Estoy comiendo")

    def dormir(self):
        print("Estoy durmiendo")

class Perro(Animal):

    def hacer_sonido(self):
        print("Estoy ladrando")


# Programa Principal
print('*** Programa de herencia en Python ***')
print('\nClase Padre, Soy un animal')
animal1=Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, Soy un perro')
perro1=Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()
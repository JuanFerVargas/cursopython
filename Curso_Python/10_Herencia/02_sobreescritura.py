class Animal:

    def comer(self):
        print("Estoy comiendo")

    def dormir(self):
        print("Duermo Muchas Horas")



class Perro(Animal):

    def hacer_sonido(self):
        print("Estoy ladrando")

    # Sobreescritura del metodo dormir
    def dormir(self):
        print("Duermo 15 horas al dia")




# Programa Principal
print('*** Programa de herencia en Python ***')
print('\nClase Padre, Soy un animal')
animal1=Animal()
animal1.comer()
animal1.dormir()

print('\nClase Hija, Soy un perro')
perro1=Perro()
perro1.comer()
perro1.dormir()     # Se ejecuta el metodo de la clase perro
perro1.hacer_sonido()
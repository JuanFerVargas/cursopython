class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def __add__(self,other):
        return f'{self.nombre} {other.nombre}'


persona1='Juan'
persona2='Perez'

print(persona1+persona2)


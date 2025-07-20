class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Persona(nombre={self.nombre}, apellido={self.apellido}, ID={hex(id(self)).upper()})'

if __name__ == '__main__':
    # Crear una instancia de Persona
    persona1 = Persona('Juan', 'Vargas')
    print(persona1)
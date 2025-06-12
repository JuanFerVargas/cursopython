class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # Sobreescribir el metodo str
    def __str__(self):
        return f"Nombre: {self.nombre}, apellido: {self.apellido}, Direccion de memoria: {super.__str__(self)}"

# Codigo principal
persona1 = Persona("Juan", "Perez")
print(persona1)                 # El metodo __str__ se ejecuta automaticamente
# print(persona1.__str__())       # Metodo Opcional


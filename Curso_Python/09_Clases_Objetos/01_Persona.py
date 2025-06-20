# Definicio de una clase
class Persona:

    # Constructor
    def __init__(self,nombre, apellido):
        # Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    # def inicializar_persona(self,nombre, apellido):
    #     # Creamos los atributos de la clase
    #     self.nombre = nombre
    #     self.apellido = apellido

    def mostrar_persona(self):
        print(f''' Persona:
        Nombre: {self.nombre} 
        Apellido: {self.apellido}''')
        print(f'Dir. mem self: {id(self)}')
        print(f'Dir. mem hex self: {hex(id(self))}')
        

# Creacion de Objeto
if __name__ == '__main__':
    # Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta') # Se crea un objeto vacio en memoria
    # persona1.inicializar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()
    print(f'Dir. mem persona1: {id(persona1)}')
    print(f'Dir. mem hex persona1: {hex(id(persona1))}')


    # Creamos segunto objeto
    persona2 = Persona('Ian', 'Sanchez')
    # persona2.inicializar_persona('Ian', 'Sanchez')
    persona2.mostrar_persona()
    print(f'Dir. mem persona2: {id(persona2)}')
    print(f'Dir. mem hex persona2: {hex(id(persona2))}')
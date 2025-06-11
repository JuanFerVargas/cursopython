class Persona:

    atributo_clase=0

    def __init__(self, atributo_instancia):
        self.atributo_instancia=atributo_instancia
    
# Programa Principal

if __name__ == '__main__':
    print('*** Atributos de Clase ***')
    print(f'atributo de clase: {Persona.atributo_clase}')
    
    # Moficamos el atributo de clase
    Persona.atributo_clase=10
    print(f'atributo de clase: {Persona.atributo_clase}')

    # Creamos el objeto de persona1
    persona1=Persona(15)
    print(f'atributo de instancia desde persona1: {persona1.atributo_instancia}')
    print(f'atributo de clase desde persona1: {persona1.atributo_clase}')

    # Creamos un objeto persona2
    persona2=Persona(30)
    print(f'atributo de instancia desde persona2: {persona2.atributo_instancia}')
    print(f'atributo de clase desde persona2: {persona2.atributo_clase}')
class Persona:
    # Atributo de clase
    contador_personas=0

    def __init__(self,nombre,apellido):
        # Incrementamos el valor del atributo de clase
        Persona.contador_personas+=1
        self.id_persona=Persona.contador_personas
        self.nombre=nombre
        self.apellido=apellido
    
    def mostrar_persona(self):
        print(f'Persona: {self.id_persona} - {self.nombre} - {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo Estatico')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print('Metodo de Clase')
        return cls.contador_personas

if __name__=='__main__':
    print('*** Ejemplo Contador de Objetos de Tipo Persona****')
    persona1=Persona('Gerardo','Perez')
    persona1.mostrar_persona()

    persona2=Persona('Maria','Lopez')
    persona2.mostrar_persona()
    
    persona3=Persona('Carlos','Garcia')
    persona3.mostrar_persona()

    # Imprimir el valor del contador de objetos de personas
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')

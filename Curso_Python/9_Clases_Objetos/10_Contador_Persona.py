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

if __name__=='__main__':
    print('*** Ejemplo Contador de Objetos de Tipo Persona****')
    persona1=Persona('Gerardo','Perez')
    persona1.mostrar_persona()

    persona2=Persona('Maria','Lopez')
    persona2.mostrar_persona()
    
    persona3=Persona('Carlos','Garcia')
    persona3.mostrar_persona()


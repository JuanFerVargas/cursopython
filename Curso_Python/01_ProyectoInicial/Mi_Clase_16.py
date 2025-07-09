class MiClase:
    '''
    Esta es una clase de ejemplo que representa un objeto simple.
    '''
    def __init__(self, atributo1, atributo2):
        '''
        Inicializa los atributos de la clase.
        
        :param atributo1: Primer atributo de la clase.
        :param atributo2: Segundo atributo de la clase.
        '''
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def metodo1(self):
        '''
        Este es un método1 de ejemplo que realiza una acción simple.
        '''
        return self.atributo1 + self.atributo2

    def metodo2(self,parametro1, parametro2):
        '''
        Este es un método2 de ejemplo que realiza una acción diferente.
        '''
        return self.atributo1 * self.atributo2 * parametro1 * parametro2
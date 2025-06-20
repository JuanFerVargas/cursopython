class Libro:

    # Inicializo los atributos de la clase Libro
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

    # Getters de los atributos de la clase Libro
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def genero(self):
        return self._genero
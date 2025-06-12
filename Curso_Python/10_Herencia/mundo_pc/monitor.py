class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanho):
        Monitor.contador_monitores += 1
        self.id_monitor=Monitor.contador_monitores
        self.marca = marca
        self.tamanho = tamanho

    def __str__(self):
        return f'Id: {self.id_monitor}, Marca: {self.marca}, Tamaño: {self.tamanho}'

# Prueba de clase
if __name__ == '__main__':
    monitor1 = Monitor('Samsung', 15)
    monitor2 = Monitor('LG', 17)
    print(monitor1)
    print(monitor2)
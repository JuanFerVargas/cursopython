from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f"Id: {self.id_raton}, Marca: {self.marca}, Tipo entrada: {self.tipo_entrada}"

# Codigo Principal
if __name__ == "__main__":
    raton1 = Raton("HP", "USB")
    raton2 = Raton("Acer", "Bluetooth")
    print(raton1)
    print(raton2)
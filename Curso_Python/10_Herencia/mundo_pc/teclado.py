from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return f"Id: {self.id_teclado}, Marca: {self.marca}, Tipo entrada: {self.tipo_entrada}"

# Prueba en funcion principal
if __name__ == "__main__":
    teclado1 = Teclado("HP", "USB")
    teclado2 = Teclado("Dell", "Bluetooth")
    print(teclado1)
    print(teclado2)
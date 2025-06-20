# Creación de la Clase HolaMundo
# Crea una clase llamada HolaMundo con un método llamado saludar(). Este método debe imprimir el mensaje
# "Saludos desde Python"
# Nota: Sólo debe crearse la clase y el método, no hay necesidad de crear objetos ni realizar ninguna otra prueba, ya que sólo se está evaluando la creación de clases y métodos de la clase. La salida que debe arrojar el método saludar programa debe ser idéntico al mostrado, respetando acentos, no agregar espacios, textos o saltos de línea innecesarios, solo los mostrados, de lo contrario la prueba a ejecutar podría fallar.
# Instrucciones de Ejecución:
# 1. Deben presionar el botón de "Ejecutar código" para ver su resultado,
# 2. Finalmente presionar el botón de "Ejecutar pruebas" para que quede resuelto el ejercicio.
# 3. Nota: Tu código podría estar correcto, pero recuerda que lo importante es el resultado de ejecutar la prueba, así que revisa nuevamente las instrucciones del ejercicio y respétalas por completo.

class HolaMundo:
    def saludar(self):
        print("Saludos desde Python")

if __name__ == "__main__":
    hola_mundo = HolaMundo()
    hola_mundo.saludar()
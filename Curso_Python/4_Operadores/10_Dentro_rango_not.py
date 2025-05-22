# Revisar si una variable se encuentra dentro de rango 1 y 10
dato=int(input("Proporciona un dato entero: "))

# Revisar si esta dentro de rango
# esta_dentro_rango = 1 <= dato <= 10
esta_dentro_rango = not(1 <= dato <= 10)
print(f"El dato {dato} esta dentro de rango? {esta_dentro_rango}")
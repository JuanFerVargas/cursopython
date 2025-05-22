# Valor dentro del rango
print("*** Valor dentro del rango ***")

VALOR_MINIMO=0
VALOR_MAXIMO=5

valor=input("Ingrese el valor a evaluar: ")
valor=int(valor.strip())
#is_valid=valor>=VALOR_MINIMO and valor<=VALOR_MAXIMO
is_valid=VALOR_MINIMO<= valor<= VALOR_MAXIMO
print(f"El valor {valor} esta dentro del rango?: {is_valid}")
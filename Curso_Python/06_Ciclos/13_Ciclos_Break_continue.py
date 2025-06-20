print('*** Break y Continue ***')

# Ejemplo con Break
print('palabra Break')
for numero in range(1,10):
    if numero % 2==0:
        print(numero)
        break               # Salimos del ciclo inmediatamente



# Ejemplo con continue
print('\nPalabra Continue')
for numero in range(1,10):
    if numero % 2==1:       # Es un numero impar
        continue            # Volvemos al inicio del ciclo
    print(numero)           # Solo numeros pares
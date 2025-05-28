from random import randint

print('*** Welcome to Guess the Number! ***')
SECRET_NUMBER=randint(1,50)
LIMIT_TRY=0
adivinanza=None
INTENTOS_MAXIMOS=5

while adivinanza!=SECRET_NUMBER and LIMIT_TRY<INTENTOS_MAXIMOS:
    adivinanza=int(input('Adivina el numero secreto (1-50): '))
# Agregamos una ayuda al jugador
    if adivinanza<SECRET_NUMBER:
        print('El numero secreto es mayor')
    elif adivinanza>SECRET_NUMBER:
        print('El numero secreto es menor')
    LIMIT_TRY+=1
# Conclusion del juego
if adivinanza==SECRET_NUMBER:
    print(f'Felicidades, adivinaste el numero secreto era {SECRET_NUMBER} en {LIMIT_TRY} intentos')
elif LIMIT_TRY==INTENTOS_MAXIMOS:
    print(f'Lo siento, has agotado tus intentos. {INTENTOS_MAXIMOS}')
    print(f'El numero secreto era {SECRET_NUMBER}')
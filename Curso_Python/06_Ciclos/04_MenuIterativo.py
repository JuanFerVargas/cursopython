import os
import time

print('*** Sistema de Administración de Cuentas ***')

salir = False
while not salir:
    print(f'''Menu:
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print('Creando tu cuenta...\n')
    elif opcion == 2:
        print('Eliminado tu cuenta...\n')
    elif opcion == 3:
        print('Saliendo del sistema. Hasta pronto!\n')
        salir = True
    else:
        print('Opción inválida, proporciona otra opción...\n')
    
    time.sleep(5)
    if os.name == 'nt':
        os.system('cls')
    # Limpia la pantalla en POSIX (Linux, macOS)
    else:
        os.system('clear')
else:
    print('Terminando el sistema de Administración de Cuentas')
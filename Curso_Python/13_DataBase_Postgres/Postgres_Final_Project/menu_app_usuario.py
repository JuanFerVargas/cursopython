from usuario_DAO import UsuarioDAO
from logger_base import log
from usuario import Usuario  # Import the Usuario class
opcion=None
while opcion != 5:
    print("Seleccione una opción:")
    print("1. Listar usuarios")
    print("2. Agregar usuario")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")
    try:
        opcion = int(input("Escribe tu opción (1-5): "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opcion == 2:
        username_var = input("Ingrese el nombre de usuario: ")
        password_var = input("Ingrese la contraseña: ")
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertados=UsuarioDAO.insertar(usuario)
        log.info(f"Usuarios insertados: {usuarios_insertados}")

    elif opcion == 3:
        usuario_id = input("Ingrese el ID del usuario a actualizar: ")
        username_var = input("Ingrese el nuevo nombre de usuario: ")
        password_var = input("Ingrese la nueva contraseña: ")
        usuario = Usuario(usuario_id, username_var, password_var)
        usuarios_actualizados=UsuarioDAO.actualizar(usuario)
        log.info(f"Usuarios actualizados: {usuarios_actualizados}")

    elif opcion == 4:
        usuario_id = input("Ingrese el ID del usuario a eliminar: ")
        usuario=Usuario(usuario_id)
        usuarios_eliminados =UsuarioDAO.eliminar(usuario)
        log.info(f"Usuarios eliminados: {usuarios_eliminados}")
else:
    print("Salimos de la aplicación.")
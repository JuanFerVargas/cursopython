# Alcance de variables (scope)

var_global = "Variable global"

def imprimir():
    global var_global
    # Acceder a una variable global
    print(f'Variable Global desde funcion: {var_global}')

    # Definir una variable local
    var_local = "Variable local"
    print(f'Variable Local desde funcion: {var_local}')
    var_global='Nuevo Valor Var Global'

    def funcion_anidada():
        print(f'Variable Global desde funcion anidada: {var_global}')
        print(f'Variable Local desde funcion anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Variable Global desde fuera de la funcion: {var_global}')
# Acceso a la variable local desde fuera de la funcion
try:
    print(f'Variable Local desde fuera de la funcion: {var_local}')
except NameError:
    print('No se puede acceder a la variable local desde fuera de la funcion')


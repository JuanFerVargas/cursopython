# Las funciones en python son ciudadanos de primera clase
# First Class Citizens

# Definicion de funciones
def suma(a, b):
    return a + b

# 1. Asignar una función a una variable (no se usan parentesis)
operacion_suma = suma

# Verificar el tipo de variable
# print(type(operacion_suma))  # <class 'function'>

# Llamamos la función a través de la variable
resultado_suma = operacion_suma(5, 3)
print(f"Resultado de la suma: {resultado_suma}")  # Resultado de la suma: 8

# 2. Pasar una función como argumento
def ejecutar_operacion(a, b, operacion):
    return operacion(a, b)

# resultado = ejecutar_operacion(5, 3, suma)

# 3. Retornar una función
def obtener_operacion():
    # Retornamos la función de suma
    return suma

mi_funcion = obtener_operacion()
resultado_retorno = mi_funcion(10, 20)
print(f"Resultado de la función retornada: {resultado_retorno}")  # Resultado de la función retornada: 30
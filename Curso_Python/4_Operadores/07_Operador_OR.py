# Operador logico or
print("Operador logico or")
condicion1=False
condicion2=False
# El operador or retorna True si cualquiera de los operandos es True
resultado=condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2} es: {resultado}")

condicion1=True
condicion2=False
resultado=condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2} es: {resultado}")

condicion1=False
condicion2=True
resultado=condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2} es: {resultado}")

condicion1=True
condicion2=True
resultado=condicion1 or condicion2
print(f"Resultado {condicion1} or {condicion2} es: {resultado}")


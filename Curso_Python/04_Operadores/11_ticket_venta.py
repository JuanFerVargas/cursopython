print("*** Generacion Ticket de Venta ***")
precio_leche=float(input("Precio Leche: "))
precio_pan=float(input("Precio Pan: "))
precio_lechuga=float(input("Precio Lechuga: "))
precio_platanos=float(input("Precio platanos: "))
discount=int(input("Digite el % de descuento: "))
# Calculo del subtotal (sin impuesto)
subtotal=precio_leche+precio_pan+precio_lechuga+precio_platanos

# Calculo del descuento
subtotal-=(subtotal*(discount/100))

# Calculo del impuesto 16%
impuesto=subtotal*0.16

# Calculo total de la compra (con impuesto)
costo_total_compra=subtotal+impuesto

print(f'''
Subtotal: {subtotal:.2f}
Descuento Aplicado: {discount:.2f} %
Subtotal con descuento: {subtotal:.2f}
Impuesto: {impuesto:.2f}
Costo Total: {costo_total_compra:.2f}
''')
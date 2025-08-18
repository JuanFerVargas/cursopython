# Profundizar en set
# Un set es una colección desordenada de elementos únicos
# Los elementos de un set deben ser inmutables

# conjunto={[1,2],[3,4]}
conjunto={'Juan',True,18.0}
print(conjunto)

# Set vacio
conjunto={} # Esto no es un set, es un diccionario
print(type(conjunto))

# Set Vacio correcto
conjunto = set()
print(conjunto)
print(type(conjunto))

# Mutable
conjunto.add('Juan')
print(conjunto)

# Contiene valores unicos
conjunto.add('Juan')
conjunto.add('Juan')
print(conjunto)

# Crear un set a partir de un iterable
conjunto = set([4,5,7,8])
print(conjunto)

# Agregar mas elementos o incluso otro set al set ya definido
conjunto2={100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (Copia poco profunda, solo copia la referencia)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

# Verificar la igualdad
print(f'Es igual en contenido? conjunto == conjunto_copia: {conjunto == conjunto_copia}')
print(f'Es la misma referencia? conjunto is conjunto_copia: {conjunto is conjunto_copia}')

# Operaciones de conjuntos utilizando Sets
# Personas con distintas caracteristicas

pelo_negro={'Juan','Maria','Pedro','Karla'}
pelo_rubio={'Ana','Luis','Pedro','Sofia'}
ojos_cafes={'Karla','Sofia'}
menores_30={'Juan','Karla','Luis'}

# (Union) Todos los ojos cafes y pelo rubio (No se repiten los elementos)
print(ojos_cafes.union(pelo_rubio))

# (Union) Invertir el orden con el mismo resultado (Conmutativa)
print(pelo_rubio.union(ojos_cafes))

# (Interseccion) Solo las personas con ojos cafes y pelo rubio
print(pelo_rubio.intersection(ojos_cafes))

# (Diferencia) Solo las personas con pelo negro y sin ojos cafes
print(pelo_negro.difference(ojos_cafes))


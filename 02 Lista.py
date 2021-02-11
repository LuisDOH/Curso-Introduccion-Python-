# Listas, arreglos, vectores
variable = 10
variable1 = ""
variablebool = True

vNum = [10,15,5,20,88]
vStr = ["Manzana", "Arbol", "Nombre","Texto"]
vBool = [True, False, True, False, False]
vMix = [True, "Manzana", 88, False, 50.3]
#         0      1       2     3      4
#         -5    -4      -3    -2     -1
# impresion
print(vMix)
# Imprimir un elemento
print(vMix[4])
print(vMix[1:4])
print(vMix[1:]) # Desde el indice 1 hasta el ultimo indice
print(vMix[-3]) # - :Imprime el indice partiendo del ultimo elemento
print(vMix[-4:-1])

print("==================================")
vBool = [True, False, True, False, False]
print(vBool)
# Modificar los elementos de una lista
vBool[1] = "Hola"
print(vBool)
vBool[1:4] = ["mundo"]
print(vBool)
vBool[1:2] = ["mundo","hola", 53, 80]
print(vBool)

print("==================================")
# ******Prints en una sola linea
print("Hola",end = " ")
print("mundo",end = "-")
print("Adicional")
print("Hola","Esto es","un texto","Separado",sep = "_")

# Elimiar un dato de un inidice
#=> [True, 'mundo', 'hola', 53, 80, False]
del vBool[0]
#=> ['mundo', 'hola', 53, 80, False]

# Eliminar utilizando el valor del dato
vBool.remove("mundo")
#=> ['hola', 53, 80, False]

# Longitud de un vector
len(vBool) # Me da la longitud de la lista vBool

# Crear una lista vacia
listaNum = []
listaNum.append(valor_nuevo)

#Agregar un elemento a la lista
vBool.append(10)
#=> ['hola', 53, 80, False,10]

dimension = len(vBool)
# Recorrer una lista en python
for iterador in range(dimension):
    print(vBool[iterador])

# Forma secundaria de recorrer el vector es
#=> ['hola', 53, 80, False, 10]

for iterador in vBool:
    print(iterador)

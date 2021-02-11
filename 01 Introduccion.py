print("Hola Mundo")
# esto es un comentario
'''
    Esto es un comentario
    multilinea
'''
# Declaracion de variables
variable1 = 10 # Numerica
variable2 = 15.5 # Real (punto decimal)
VariableNula = None # Variable nula
VariableBool = False # Variable booleana
VariableString = "Cadena de caracteres" # String

print(variable1)
# Concatenacion
print(variable1, variable2)
nombre  = "Aurora"
print("Hola mi nombre es", nombre)
print("variable 1 = %s y variable2 = %s." %(variable1,variable2))
print("Variable 1 =",variable1,"y variable 2 =", variable2,".")


# Operaciones Aritmeticas (+, -,*,/)
suma = variable1 + variable2
resta = variable1 - variable2
multiplicacion = variable1 * variable2
division = variable1/variable2
residuo = variable1%variable2  # si division exacta = 0
elevacion = 5 ** 3
print(suma)

# Operadores de asignacion
a = 7
a = a + 5
a += 5 # Incrementa el valor de a en 5 unidades
a -= 1 # Disminuye el valor de a en 1 unidad
a /= 2 # Divide el valor de a entre 2
a *= 3 # Mutiplica el valor de a por 3

# Operadores de comparacion
10 > 5 # Mayor que
1 < 3 # Menor que

10>=5 # Mayor o igual
5>=5 # Mayor o igual

2<=7 # Menor o igual
7<=7 # Menor o igual

105 != 40 # Diferente de
5 == 5 # Identico a

# Datos de entrada
variable = 25
variable = "Nombre"
variable = float(input("Ingresa tu nombre"))

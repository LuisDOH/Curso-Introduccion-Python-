# Funciones
def nombre():
    print("Este texto es parte de una funcion")
    print("Este tambien es parte de una funcio")



def operacion(arg1, arg2, arg3):
    suma = arg1 + arg2 + arg3
    print("El resultado de la suma es", suma)
    return suma

# Inicio de nuestro codigo principal
print("==== Inicio del programa ====")
nombre()
variable1 = 10
variable2 = 55
variable3 = 15
#operacion = 10

r_operacion = operacion(variable1,variable2,variable3)
print(r_operacion + 5)

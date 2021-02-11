'''
    El programa debe solicitar dos vectores, cuyos valores seran
    ingresados uno a uno.

    Posteriomente el programa debe identificar cual es el valor
    maximo de cada uno de los vectores, compararlos
    y mostrar por consola cual de esos dos valores fue el mas alto.

    Finalmente el programa debe mostrar por pantalla la suma de los
    valores de cada vector.

    *Al inicio del programa el usuario le indicara al programa
    cuantos valores contendra cada vector
'''


def operaciones(vect1, vect2):
    suma1 = 0
    suma2 = 0

    for i in vect1:
        suma1 += i

    for i in vect2:
        suma2 += i

    vector_soluciones = [suma1, suma2]
    return vector_soluciones

v1 = [1,2,3]
v2 = [4,5,6]
Vresultado = operaciones(v1,v2)
Vresultado[0]
Vresultado[1]

[r1, r2] = operaciones(v1,v2)
print(r1, r2)



vectorA = [10,5,80,23]

for i in range(len(vectorA)):
    print(i)

print("----------------------")

for i in vectorA:
    print(i)



'''
    vector = [5,7,10,88]
    vector1 = [10,3,5,48]

    vector_vectores = [vector, vector1]

    return vector_vectores


* - Retorno de los valores de una funcion
  - Aurora
'''

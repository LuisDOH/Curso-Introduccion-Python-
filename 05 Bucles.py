
# Bucle por parametro
for iterador in range(2):
    x = 10
    print("Hola mundo")
    print(iterador)
    print("--------")

# Bucle con intervalo definido
for iterador in range(2,10): #iterador =2; iterador < 10
    print(iterador)

print("--------")
for iterador in range(2,10,2):
    print(iterador)

print("--------")
for iterador in range(10,-1,-5):
    print(iterador)

print("------------")


# Bucle por condicion
temperatura = 30
bateria = 100

while temperatura > 25 and bateria>0:
    print("Hace calor")
    temperatura -= 0.2
    bateria -= 10
    print("Temperatura %s, bateria = %s " %(round(temperatura,2), bateria))

print("Me he apagado")

# Bucle infinito
contador = 0
while True:
    print("Bucle infinito")

    if contador > 1000:
        break # => Frena totalmente el ciclo

    contador +=1
print(" Me he detenido")

'''
Vamos a hacer un programa que diferencie si eres un chico, una chica
un joven o una joven
'''

genero = input("Introduce tu genero [hombre/mujer]: ")
edad = int(input("Introduce tu edad: "))

#genero.lower() minusculas

if (genero == "mujer") or (genero == "Mujer"):
    # Si la condicion es verdadera
    if edad < 18:
        # Si la condicion es verdadera
        print("Eres una chica")
    else:
        print("Eres una joven")

elif genero == "hombre" or genero == "Hombre":
    if edad < 18:
        print("Eres un chico")
    else:
        print("Eres un joven")
else:
    print("Error en el genero")

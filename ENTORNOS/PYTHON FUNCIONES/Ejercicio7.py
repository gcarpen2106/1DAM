#Gonzalo Carretero Peñalosa

#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.

#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

from Funciones_Ejercicio7 import login

intentos_carretero = 0

while intentos_carretero < 3 :
    nombre_carretero = input("Ingrese nombre de usuario: ")
    print("")
    contraseña_carretero = input("Ingrese contraseña: ")
    print("")

    respuesta_carretero = login(nombre_carretero,contraseña_carretero,intentos_carretero)

    if respuesta_carretero == True:
        break

    else:
        intentos_carretero = intentos_carretero + 1

if intentos_carretero >= 3:
    print("")
    print("Has alcanzado el numero maximo de intentos. Acceso Denegado")
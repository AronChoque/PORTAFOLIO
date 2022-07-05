# -*- coding: utf-8 -*-

"Desarrollo"
"1. Estructura excepciones"
"Validación de números:"
while True:
    try:
        f = int(input("Ingrese un número cualquiera: "))
        print("Correcto karnal, si le sabes")
        break
    except ValueError:
        print("El número que usted a ingresado no es válido")
        
        
"Validación de números y otra condición:"
while True:
    try:
        f = int(input("Ingrese un número positivo: "))
        print("Correcto karnal, si le sabes")
    except ValueError:
        print("El número que usted a ingresado no es válido")
        continue
    if f < 0:
        print("\t Que ingrese un número positivo")
        continue
    break

"2. Estructura Funciones"
"Función Principal  main"
def one():
    print("Iniciando el programa")

def two():
    print("A medias del programa")

def three():
    print("\n Fin del programa :(")
#función principal main

if __name__ == "__main__":
    one()
    two()
    one()
    two()
    three()
    three()
    
    
"Hacer un programa que solicite ingreso de DNI correctamente:"
def n_dni():
    while True:
        try:
            dni = int(input("Ingrese su número de DNI: "))
            if len(str(dni)) == 8:
                print("Muy bien, DNI válido")
                break
            else:
                print("Longitud de DNI no válido, vuelva a intentarlo")
                continue
        
        except ValueError:
            print("ERROR!!! DNI no válido, intenta de nuevo")
    return dni
    

#programa MAIN principal
if __name__ == "__main__":
    titulo = (" Bono COVID-19 para todos")
    print(titulo.center(50,"*"))
    print("\n\n")
    number_dni = n_dni()
    print("\nEl número ingresado es:  ",number_dni)
    
"FIN DEL DESARROLLO"



"INICIO DE LOS O EL EJEMPLO XD"
"Hacerun programa que imprima un menú deopciones y que valide correctamente los ingresos:"
import os

def minu():
    """
    FUnción que limpia la pantalla y muestra nuevamente el menu
    """
    os.system("clear") 
    titule= ("Menu Genral")
    print(titule.center(50,"*"))
    print("\n\n")
    print("Seleciione una opción ")
    print("\t1 - Primera opción")
    print("\t2 - Segunda opción")
    print("\t3 - Tercera opción")
    print("\t9 - Salir")
    
def vali():
    while True:
        minu()
        
        opcionesmin = input("Inserte un número válido ")
        
        if opcionesmin == "1":
            print("")
            input("Has elegido la opción 1 \npulsa unsa tecla para continuar ")
        elif opcionesmin == "2":
            print("")
            input("Has elegido la opción 2 \npulsa unsa tecla para continuar ")
        elif opcionesmin == "3":
            print("")
            input("Has elegido la opción 3 \npulsa unsa tecla para continuar ")
        elif opcionesmin == "9":
            break
        else:
            print("")
            input("No has elegido una opción válida \npulsa una tecla para continuar")
            
    return opcionesmin


if __name__ == "__main__":
    vali()
    print("A finalizado el programa!!")
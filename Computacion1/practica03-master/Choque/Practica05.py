#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"1. Estructura iterativa - bucle while"
"Usamos while"
"Hacer un programa que imprima la tabla del 5"

contadora = 0
print("Tabla del número 5")
#bucle while
while contadora <=10:
    print(f"5 x {contadora} ==> {contadora*5}")
    contadora += 1
print("Fin de la tabla de multiplicar")



"Hacer un programa que repita una frase las veces que desee, use funciones"
frase = "Debo de llegar temprano a las clase de Cómputo 1, si no el teacher se enoja"
contadora = 0
def repetir(n,contadora):
    while contadora < n:
        print(frase)
        contadora +=1
        
numero=int(input("Ingrese el número de veces que quiere repetir la frase: "))
print("\n\n")
repetir(numero,contadora)



" Hacer un programa que solicite ingreso de contraseña"
contra = ""
while contra != "666":
    print("Porfis entre con su contraseña")
    contra = input()
print("Al fin xd")


"Modificando la finalización del bucle while: break y continue"
"Uso de break:"
"Hacer un programa que valide ingreso nombre Chiviktor:"
while True:
    print("Ingrese su nombre ")
    name = input()
    if name.lower() == "chiviktor":
        break
        
print("Nos vemos luego viejo")


"Uso de continue:"
"Hacer un programa que valide nombre y contraseña de dos listas respectivamente"
name =["pepe", "marti", "vi", "floyd", "otto"]
contra = ["zzzz", "303", "badaga", "gozu", "edgy"]
while True:
    nom = input("Escriba su nombre: ")
    if nom not in name:
        continue
    print(f"\nHola {nom.title()}, escribe tu contraseña: ")
    password = input()
    if password in contra:
        print("\nBienvenido a su cuenta de Fornite")
        break
    else:
        print("\nUsuario no existente")
        break


"Fin de desarrollo de clase"
"Inicio de ejemplos:"
"Estructura iterativa while"
"Hacer un programa que busque el número 8 dentro de una lista de números, si se encuentra, que imprima el índice dentro de la lista"
numeros = [2, 3, 9, 6, 8, 1]
hallado = False
indice = 0
longitud = len(numeros)
while not hallado and indice < longitud:
    numero = numeros[indice]
    if numero == 8:
        hallado = True
    else:
        indice += 1
if hallado:
    print(f"El número 8 fue encontrado en el indice {indice}")
else:
    print("El número 8 no está en la lista de números")
    
    
    
"Hacer un programa que solicite el ingreso de contraseña con intentos limitados"
contra = ""
conta = 0
while contra != "heil hitler":
    conta += 1
    print("Escriba su contraseña \nSolo tiene 2 intentos: ")
    contra = input()
    if conta == 2:
        print("Sus intentos han finalizado, bay Hitler :( ")
        break
if conta !=2:
    print(" GOD NAZI")
    
    
    
" Imprime la secuencia 3x+1 desde un número X, terminando cundo llegue a 1."
def numerogod(x):
    while x != 1:
        print(x, end=", ")
        if x % 2 ==0:
            x = x // 2
        else:
            x = x * 3 + 1
    print(x, end=".\n")
num = int(input("Ingrese numero de inicio x: "))
numerogod(num)



"Hacer un programa con función que cuenta el número de dígitos que son 2 o 7 en un entero o positivo:"
def nudi(f):
    count = 0
    while f > 0:
        digito = f % 10
        if digito == 2 or digito == 7:
            count = count + 1
        f = f // 10 
    return count
num = int(input('Ingrese un numero que contenga los digitos "2" y "7" : ==> '))
cantidad =nudi(num)  
print('\n\n\tLa cantidad de digitos "2" y "7" en el numero ',num,'es: ==>',cantidad)
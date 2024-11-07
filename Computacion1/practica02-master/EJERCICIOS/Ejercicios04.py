#!/usr/bin/env python3
# -*- coding: utf-8 -*-


################################################## * EJERCICIOS * #######################################


##### EJERCICIO 1: Hacer un programa que ingrese por teclado un número inicial y un número final para generar un rango (una la lista consecutiva de números que inicia y termina de acuerdo a los números ingresados):
   #Imprimir de cada número si es par o impar (recorrer la lista)
   #Utilizando el operador %
   #Utilizar for y funciones de verificación
   
n = int(input("Ingrese un número entero inicial:"))
m = int(input("Ingrese un número entero final:"))
print("\n")

def verificar(i) :
        if i == 0:
            print(" no es un par ni tampoco impar")   
for i in range(n, m+1):
    if i % 2 != 0:       
        print(i, "es un numero impar ")
    
    else:
        if i != 0:
            print(i, "es un numero par")
        
    if i == 0:
        print(verificar(i), i) 




##### EJERCICIO 2: Hacer un programa que imprima la tabla completa de multiplicar de un número que se ingresa por teclado:
   #Primero se debe solicitar un número
   #Que imprima por pantalla las tablas de multiplicar del 1 al 10 de dicho número ingreado por teclado
   #Utilizar for y funciones
   
#Primero solicitamos un numero para lo cual digitamos lo siguiente:
numero = int(input('Digite un numero entero: '))

#Luego realizamos la funcion 
def tabl():
        if numero > 0:
            for w in range(0, 11):
                print(f'{w} x {numero} = {w * numero}')
        else:
            print("El numero ingresado no es correcto.Intentelo nuevamente.")
tabl()
   
##### EJERCICIO 3: Hacer un programa que solicite el ingreso de un nombre y apellido:
   #Que verifique que el nombre y/o apellido no contenga ningun numero
   #Que verifique que el nombre y/o apellido no contenga ningun simbolo extraño
   #Si detecta que el nombre y/o apellido que no es un válido, que solicite que vuelva a ingresar su nombre y/o apellido
   #Utilizar for y funciones

b=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","¿","#","&","+","-","*","$","¬","|","°","@","!","¡","?","%","()","{}","[]","/","<",">","_","-","^",";",":"]

print("Buenos días, escriba sus datos y evite usar símbolos y números  ")

#Utilizamos una primera función para el nombre
def nombre(name):
    for f in name:
        if f in b:
            print("Hay un número o símbolo no permitido \nVuelva a intentarlo")
            return plb()
    else:
        print("Continue")
             
        
def apell(lst):            #Utilizamos una funcion para el apellido
    for a in lst:
        if a in b:
            print("Hay un número o símbolo no permitido \nVuelva a intentar ")
            return apl()   
    else:
        print("GRACIAS")
             
        
def plb():
    nom=input("Ingrese su nombre ")
    nombre(nom)
plb()

def apl():
    waa=input("Ingrese su Apellido: ")
    apell(waa)      
apl()




#####EJERCICIO 4: Hacer un programa que genere una lista aleatoria de hasta 60 numeros:
   #Subdidivir en listas pequeñas: lista multiplos de 2, lista multiplos de 3 y lista multiplos de 5
   #Utilizar for para recorrer la lista
   #utilizar listas y funciones
    
print('\n')
# Importaremos la biblioteca "random"

from random import randint
numeros = [randint(1,100) for _ in range(1,59)]
    
print("TENEMOS:\n60 números aleatorios del 1 hasta el 100:")
print('\n')
print(numeros)

#Ahora haremos las función para sacar múltiplos de 2, 3 y 5 de los 60 números random.
numeros_2 = []
numeros_3 = []
numeros_5 = []

# El modulo "%" nos indica el residuo entre dos números, por está razón 
#dividimos el número entre 2 y si nos sale igual a 0, es porque es múltiplo

def dos_numeros(x):
    for x in numeros:
        div = x%2
        if div == 0:
            numeros_2.append(x)
            
#ividimos el número entre 3 y  si nos sale igual a 0, es porque es múltiplo            
def tres_numeros(x):
    for x in numeros:
        div = x%3
        if div == 0:
            numeros_3.append(x)
            
#ividimos el número entre 5 y   si nos sale igual a 0, es porque es múltiplo         
def cinco_numeros(x):
    for x in numeros:
        div = x%5
        if div == 0:
            numeros_5.append(x)

#Llamamos a las funciones

dos_numeros(numeros)
tres_numeros(numeros)
cinco_numeros(numeros)

print("\n-----------------------------------------\n ")
print("MULTIPLOS DE 2 \n",numeros_2)
print("MULTIPLOS DE 3 \n",numeros_3)
print("MULTIPLOS DE 5 \n",numeros_5)

print('\n')


##### EJERCICIO 5: Hacer un programa que ingrese por teclado un número inicial de 3 cifras y un número final de 4 cifras para generar un rango (una la lista consecutiva de números que inicia y termina de acuerdo a los números ingresados):
   #Imprimir de cada número si Capicúa (recorrer la lista)
   #Utilizar for y funciones de verificación
    
print("Hola. Por favor: ")

#Numero minimo de 3 cifras
a = int(input("Ingrese un numero (min) de 3 cifras: "))


#Numero maximo de 4 cifras
b = int(input("Ingrese un numero (max) de 4 cifras: "))


# para poder hallar los numeros capicuos del intervalo que se ha formado existen varias maneras. Una de ellas
# es convertir los numeros del intervalo a formato tipo string para luego separarlos en sus digitos 
# correspondientes. Una vez hecho eso, invertiremos los elementos de la lista para luego compararlo con la lista
# original (orden de los digitos original).

# num = numeros comprendidos en el intervalo establecido.
# ln = lista de numeros

def cap():
    for i in range(a,b+1):
        num = str(i)
        ln = list(num)
        if ln == ln [::-1]:
            capicua =''.join(ln)
       
            print(capicua,"", end="")
cap()       
print('Muchas gracias, que tenga un buen dia!')

# Nota: se ha usado "[::-1]" para facilitar y abreviar el codigo al momento de que querer invertir los elementos
# de la lista de numeros. El codigo omite el inicio y el fin del iterable, y añadiendo un paso -1, se nos devuelve
# los elementos del iterable comenzando por el ultimo y terminando con el primero, invertiendo el orden original.
        



##### EJERCICIO 6: Hacer un programa que solicite el ingreso del DNI de un ciudadano:
   #Que verifique que el DNI no contenga letras del abecedario
   #Que verifique que el DNI no contenga ningun simbolo extraño
   #Que verifique que el DNI solo tenga 8 números
   #Si detecta que el DNI no es válido, que solicite que vuelva a ingresar su DNI
   #Utilizar for y funciones
   
b= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",'?','!','$','%','&','/','ª','º', '-',"-", "_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

print("Buen día")

def validar_dni(numero):
    for r in numero:
        if r in b:
            print("  Entrada digitada incorrecta, recuerde que solo son 8 números, intente de nuevo")
            return numdni()
    if len(numero) == 8:
        pass
    else:
        print("  No válido, recuerde que tiene que digitar 8 NÚMEROS intente de nuevo")
        return numdni()
    
def numdni():
    numero = input("Ingrese su número de DNI: ")
    validar_dni(numero)

numdni()

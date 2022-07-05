#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"DESARROLLO"
"1. Estructura Iterativa - Bucle for"
"Usamos for"
num = [10,20,30,60]
for n in num:
    print(n)
    
    
nom = "Thanos"
for t in nom:
    print(t)    
    
    
for nombres in ["Carlitos", "Pepito", "Chavito", "Chiviktor"]:
    print("Hola {0}, la longitud de tu nombre es de: {1} caracteres." .format(nombres,len(nombres)))
    
    

"Hacer un programa que itere a lo largo de una lista que contenga colores y añada(appends) todos los colores que contengan la letra "r" a una nueva lista."
colores = ["morado", "plomo", "azul", "marrón", "negro", "rosado", "verde", "naranja"]
colores_con_m = []
for t in colores:
    if "m" in t:
        colores_con_m.append(t)
print(colores_con_m) 


"Función range()" 
for v in range(9):
    print(v)
    
" Hacer un programa que imprima los números del 1 al 13"   
for i in range(13):
    print(i+1, "", end="")   
    
    
    
for m in range(1,13):
    print(m, "", end="")
    
    
"Ejemplos de función range"
for v in range(2,20,4):
    print(v, "", end="")
    
    
for l in range(10,0,-1):
    print(l, "", end="")
    
    
    
for k in range(60,-10,-10):
    print(k, "", end="")
    
    
    
for f in range(10,-5,-2):
    print(f, "", end="")
    
    
    
"Modificando la iteración del bucle for: break y continue"
"Uso de break:"
" Hacer un programa que de una lista de números imprima la posición del número 9:"
lista = [8,6,9,12,2,7,1]
contar = -1
for b in lista:
    contar = contar+1
    if b ==9:
        break
print(contar)



contador = 3
contador *=7
print(contador)



lista = [3,8,6,12,15]
contar = -3
for f in lista:
    contar += 3
    if m == 9:
        break
else:
    contar =-3
    print("No hay el número 9")
if contar>= 0:
    print(contar)
    
    
    
"Uso de continue:"
"Hacer un programa que de una lista de números imprima solo los números pares:"
lista = [ 3, 7, 29, 48, 101, 666]
for h in lista:
    if h %2 !=0:
        continue
    print(h)
    
"Hacer un programa que imprima los múltiplos de 3:"    
lista = [ 21, 88, 67, 453, 303]
for o in lista:
    if o %3 !=0:
        continue
    print(o)   
    
    
    
"Iniciando EJEMPLOS:"
"Estructura iterativa for:"
"Hacer un programa mostrar por pantalla los números pares del 0 al 18:"
for num in range(0,17,2):
    print(num)
    
    
    
"Hacer un programa que permita ingresar nombres a una lista, utilizando funciones:"
names = []
def entrada(ele):
    for f in range(0,ele):
        z= input("Ingresar Nombre de la posición {0} : ".format(f))
        names.append(z)
        
l=int(input("De cuantos elementos crearemos la lista de nombres : "))

entrada(l)
print("\nla lista completa de nombres es: \n",names)
    


" Método2: Hacer u programa que de una lista de números imprima la posición del número 8, utilizando función enumerate"
lista=[3, 7, 18, 21, 6]
for f,z in enumerate(lista):
    if z==9:
        break
else:
    f = -1
    print("No hay el número 9")
if f >=0:
    print(z)
    
    
"Hacer un programa que lea la lista de relatos de H.P. Lovecraft e indique el nombre de los libros:"
relatos_hpl=["Dagón", "La tumba", "Aire frío","El alquimista"]
orden=["primer","segundo","tercero","cuarto"]
for r, relato in enumerate(relatos_hpl):
    print("\nEl " + orden[r] +" libro de H.P.Lovecraft es: " +relato)
    
    
"Hacer un programa que haga invitaciones de una lista de nombres"
for z in ["Pepe", "Tito", "Chino", "Kriko", "Keiko"]:
    invitacion = "Hello " + z + ". ¡ Plis, caigan a mi quino el lunes!!!"
    print(invitacion)

"Hacer un programa que sume los elementos de una lista, utilizar funciones y for"
def mimi(xd):
    """Suma todos los números de la lista xd, y devuelve el total."""
    running_total=0
    for x in xd:
        running_total = running_total + x
    return running_total

print(mimi([2,3,4]))
print(mimi([12,4,564,654]))
print(mimi([5.9,36.4,2.1]))
print(mimi([303,666,121]))
print(mimi(range(5,9)))



"Hacer un programa que sume los elementos de una lista, usando función sum"
f = [1,9,6,8]
sum(f)


"Hacer un programa que imprima los múltiplos hasta el número 10 de cualquier número"
def multi(f):
    for z in range(1,20):
        print(f * z, end="  ")
    print()
    
m = int(input("Ingrese un número: "))
print("\nLos múltiplos de ", m, "son: ")
multi(m)



"Ejemplo de for anidado: Creación de tablas"
for f in range(0,6):
    for z in range(0,2):
        for m in range(0,2):
            print(f,z,m)
            
            

"Hacer un programa que permita hallar la raíz enésima de un número que se ingresaea por teclado:"
number = float(input("Ingrese un número: "))
for n in range(2, 51):
    print("La raíz {0}-ésima de {1} es {2}".format(n, number, number**(1/n)))
    
    
    
num=["1", "2", "3", "4", "5", "6"]
sim=["¿","#","&","$","¬"]
def validar(nomap):
    for x in nomap:
        if x in num:
            print("Nombre no válido!!!!")
        elif x in sim:
            print("Nombre no vpalido!!!!!!!!")
        else:
            print("Nombre correcto :D")
            
nom = input("Ingrese su nombre: ")
validar(nom)
apell = input("Ingrese su apellido: ")
validar(apell)


"Fin de los ejemplos"
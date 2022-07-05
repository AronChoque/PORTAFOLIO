#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################## * EJERCICIOS * #######################################

#####EJERCICIO 1: Hacer un programa que verifique la lista existente de compras de una Jugería, si se compro:
   #"manzanas" o "peras" y si es Lunes, debera indicar que se puede desayunar jugo de dichas frutas.
   #"platano" o "fresa" y "leche" y siendo Martes, debera indicar que se puede desayunar jugo de leche de dichas frutas.
   #yogurt" y "cereales" y siendo Miercoles, debera indicar que se tomara dicho desayuno.
   #Si es del Jueves al Domingo verificar si hay papaya, debera indicar que se puede desayuinar dicha fruta. (Utilizar listas y funciones)

print('\n')
print("¡¡¡BIENVENIDO A NUESTRA JUGUERÍA!!!")
print("\n")
print("Tenemos estás opciones... \n")
Lunes = ["manzana", "pera"]
Martes = ["platano", "fresa", "leche"]
Miercoles = ["yogurt", "cereales"]
JuevesaDomingo = ["papaya"]

print("Desayunos: ")
print("\nLunes:" + str(Lunes))
print("\nMartes:" + str(Martes))
print("\nMiercoles:" + str(Miercoles))
print("\nJueves a Domingo:" + str(JuevesaDomingo))
print("\n")


print("Digite, para preparar:")
desayuno1 = input("\nPrimer Desayuno:  ")
desayuno2 = input("\nSegundo Desayuno: ")


#Menú
print("\nSeleccione una opción: ")
print("\n")
print("a) Lunes ")
print("b) Martes ")
print("c) Miercoles ")
print("d) Jueves a Domingo")

opcion = input("Digita a, b, c o d y presiona enter:")
print('\n')

if opcion == "a":
    if desayuno1 in Lunes:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    elif desayuno2 in Lunes:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    else:
        print("Lo sentimos, no disponemos de esa fruta hoy. \nElija otra fruta o vuelva otro día")
elif opcion == "b":
    if desayuno1 in Martes:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    elif desayuno2 in Martes:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    else:
        print("Lo sentimos, no disponemos de esa fruta hoy. \nElija otra fruta o vuelva otro día")
elif opcion == "c":
    if desayuno1 in Miercoles:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    elif desayuno2 in Miercoles:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    else:
        print("Lo sentimos, no disponemos de ese desayuno hoy. \nElija otra fruta o vuelva otro día")
elif opcion == "d":
    if desayuno1 in JuevesaDomingo:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    elif desayuno2 in JuevesaDomingo:
        print("Sí disponemos de esa fruta, enseguida sale su jugo!")
    else:
        print("Lo sentimos, no disponemos de ese desayuno hoy. \nElija otra fruta/desayuno o vuelva otro día")
print('\n')
print(" GRACIAS!!!")
print('\n')

#####EJERCICIO 2: Hacer un programa que ingrese por teclado 20 numeros y luego visualizar un menu de opciones para hallar los valores estadisticos: media, mediana y frecuencia. Utilizar listas y funciones .

print("*RECOMENDACIÓN*: Al escribir un número entero escríbalo usando el punto decimal (ejm: 4.0 )")

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
n4 = float(input("Ingrese el cuarto número: "))
n5 = float(input("Ingrese el quinto número: "))
n6 = float(input("Ingrese el sexto número: "))
n7 = float(input("Ingrese el séptimo número: "))
n8 = float(input("Ingrese el octavo número: "))
n9 = float(input("Ingrese el noveno número: "))
n10 = float(input("Ingrese el décimo número: "))
n11 = float(input("Ingrese el onceavo número: "))
n12 = float(input("Ingrese el doceavo número: "))
n13 = float(input("Ingrese el treceavo número: "))
n14 = float(input("Ingrese el catorceavo número: "))
n15 = float(input("Ingrese el quinceavo número: "))
n16 = float(input("Ingrese el dieciseisavo número: "))
n17 = float(input("Ingrese el diecisieteavo número: "))
n18 = float(input("Ingrese el dieciochoavo número: "))
n19 = float(input("Ingrese el diecinueveavo número: "))
n20 = float(input("Ingrese el veinteavo número: "))

a=[(n1),(n2),(n3),(n4),(n5),(n6),(n7),(n8),(n9),(n10),(n11),(n12),(n13),(n14),(n15),(n16),(n17),(n18),(n19),(n20)]

from statistics import mode
from statistics import median

#MENÚ
print("Seleccione una opción: ")
print("a) Calcular la Media Aritmética.")
print("b) Calcular la Frecuencia.")
print("c) Calcular la Mediana.")
opcion = input("Escoja su opción; digitando a, b, o c y presione enter: ")
if opcion == "a":
    media = ((n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12+n13+n14+n15+n16+n17+n18+n19+n20) / 20)
    print("\nLa media aritmética es {0}.".format(media))
else:
    if opcion == "b":
        print("\nLa Frecuencia es:")
        print(float(mode(a)))
    else:
        if opcion == "c":
            a.sort()
            print("\nLa mediana es.")
            print(float(median(a)))
        else:
            print("\nSolo hay tres opciones: a, b, c.")
            print('Usted ha tecleado "{0}".'.format(opcion))

print('\n')
#####EJERCICIO 3: Hacer un programa que ingrese por teclado 10 objetos de casa, luego visualizar un menu de opciones para ordenar la lista e imprimir de forma:
 #ordenar de forma ascendente
 #ordenar de forma descendente. (Utilizar listas y funciones)

print ("LISTA DE OBJETOS DEL HOGAR : ") 
 
o1 = input( "Ingrese el primer objeto: " ) 
o2 = input( "Ingrese el segundo objeto: " )
o3 = input( "Ingrese el tercer objeto: " ) 
o4 = input( "Ingrese el cuarto objeto: " ) 
o5 = input( "Ingrese el quinto objeto: " ) 
o6 = input( "Ingrese el sexto objeto: " ) 
o7 = input( "Ingrese el séptimo objeto: " ) 
o8 = input( "Ingrese el octavo objeto: " ) 
o9 = input( "Ingrese el noveno objeto: " ) 
o10 = input( "Ingrese el décimo objeto: " )

OBJETOS = [ o1, o2, o3, o4, o5, o6, o7, o8, o9, o10 ] 

print( "Seleccione una opción :" ) 
print( "a): Lista Ordenada de manera Ascendente" )
print( "b): Lista Ordenada de manera Descendente" )
opcion = input( "Escoja su opción; digitando a) o b) y presione enter:" )
if opcion ==  "a" : 
    print('\nLista Ordenada de manera Ascendente')
    OBJETOS.sort()                 
    print(OBJETOS)

else:
    if opcion ==  "b" : 
        print('\nLista Ordenada de manera Descendente')
        OBJETOS.sort()
        OBJETOS.reverse()              
        print(OBJETOS)


print('\n')
#####EJERCICIO 4: Hacer un programa que ingrese por teclado una contraseña con un nombre, si el nombre y contraseña ingresada se encuentra en la lista de contraseñas y en la lista de nombres, Les da la bienvenida el sistema y te reconoce como Trabajador de la empresa MicroSecret . Si la contraseña o nombre es incorrecta te rechaza el acceso. Utilizar listas y funciones
print("Buenos días,para ingresar a la empresa realice los siguientes pasos: ")
def usuario(name):
    if name in nombre:
           
        def contraseña(pase):
            if pase in contra:
                print(f"\nBienvenido(a) {nombre1.upper()}, trabajador(a) de la empresa MicroSecret. ")
            else:
                print("Acceso Denegado" "\nNo es trabajador de la empresa MicroSecret.")
                
        contra = ["Barrera", "Canazas", "Choque", "Cruz", "Gomez", "Palma", "Rosas"]
        contra1 = input("Escriba su contraseña(apellido): ")
        
        contraseña(contra1)
        
    else:
        print("El nombre que usted a ingresado es incorrecto." "\nNo es trabajador de la empresa MicroSecret.")
               
nombre = ["Alvaro", "Aron", "Axel", "Derek", "Jhair", "Raquel", "Yadira"]
nombre1 = input("Escriba su usuario(nombre): ")

usuario(nombre1)




print('\n')
#####EJERCICIO 5: Hacer un programa que verifique una lista de almacen de una Carpintería:
 #Si tiene clavos y madera se puede construir una ventana.
 #Si tiene plancha metal y soldadura se puede construir puerta metalica.
 #Si tiene plancha de madera y madera se puede construir una puerta.
 #Si no tiene ninguna de las anteriores, solicitar compra de materiales. (Utilizar listas y funciones)

print("MATERIALES DE LA CARPINTERÍA")
print("\n")
almacen = ['clavos', 'madera', 'plancha de metal', 'soldadura', 'plancha de madera']
print("MAteriales: " + str(almacen))
print("\n")
print("Liste materiales de la Carpintería a utilizar:")
material1 = input("\nMAterial 1:  ")
material2 = input("\nMaterial 2: ")

#Menú
print("\nSeleccione una opción: ")
print("\n")
print("a) Fabricar una ventana ")
print("b) Fabricar una puerta metálica")
print("c) Construir una puerta ")

ventana = ['clavos', 'madera']
puertametal = ['plancha de metal', 'soldadura']
puerta = ['madera', 'plancha de madera']

print("\n")
opcion = input("Digita a, b, O c y presiona enter:")
print("\n")
if material1 not in almacen:
    if material2 not in almacen:
        print("\nEl material especificado no se encuentra en el almacén, se solicita comprar mas materiales")
    
if opcion == "a":
    if material1 in ventana:
        if material2 in ventana:
            print("Es posible construir una ventana")
        else:
            print("No es posible construir una ventana")
else:
    if opcion == "b":
        if material1 in puertametal:
            if material2 in puertametal:
                print("Es posible construir una puerta metálica")
            else:
                print("No es posible construir una puerta metálica")
        else:
            if opcion == "c":
                if material1 in puerta:
                    if material2 in puerta:
                        print('Es posible construir una puerta')
                    else:
                        print("No es posible construir una puerta")
            else:
                print("\nSolo hay tres opciones: a, b, c.")
                print('Tu has tecleado "{}".'.format(opcion))
                        
 


print('\n')
#####EJERCICIO 6: Hacer un Programa de selección para jovenes postulantes a la Marina de Guerra del Perú, verificando el ingreso de los siguientes datos:
 #Deben ser Mujeres mayores de edad, con altura mínima de 1,60 metros, con peso entre 55 y 60 kilos y tenga en la prueba mayor a 65 puntos.
 #Deben ser Varones mayores de edad, con altura mínima de 1,65 metros, con peso entre 55 y 60 kilos y tenga en la prueba mayor a 65 puntos.
 #Si no cumplen debe salir un mensaje de "NO SELECCIONADO".

#DEFINIMOS LA FUNCION de "Seleccion" en funcion a las 5 variables que tenemos como condicion: Sexo, Edad, Altura, Peso y Puntaje obtenido

def seleccion(a,b,c,d,e):
    if a == "masculino" :
        if b >= 18 :
            if c >= 1.65 :
                if d >= 55 and d <= 60 :
                    if e > 65:
                        print(f'\nUsted ha sido SELECCIONADO')
                    else:
                        print(f'\nUsted NO ha sido SELECCIONADO')
                else:
                    print(f'\nUsted NO ha sido SELECCIONADO')
            else:
                print(f'\nUsted NO ha sido SELECCIONADO')
        else:
            print(f'\nUsted NO ha sido SELECCIONADO')
    elif a == "femenino" :
        if b >= 18 :
            if c >= 1.6 :
                if d >= 55 and d <= 60 :
                    if e > 65:
                        print(f'\nUsted ha sido SELECCIONADO')
                    else:
                        print(f'\nUsted NO ha sido SELECCIONADO')
                else:
                    print(f'\nUsted NO ha sido SELECCIONADO')
            else:
                print(f'\nUsted NO ha sido SELECCIONADO')
        else:
            print(f'\nUsted NO ha sido SELECCIONADO')

print("bienvenido al Programa de selección para jovenes postulantes a la Marina de Guerra del Perú".upper())
print("\nPara realizar la verificacion de su resultado, por favor ingrese los siguientes datos:")

#INGRESO DE DATOS
nombre = input('\nIngresa tus nombres completos: ')
sexo = input('Ingresa tu sexo (femenino o masculino): ')
edad = int(input('Ingresa tu edad: '))
altura = float(input('Ingresa tu altura (en m): '))
peso = float(input('Ingresa tu peso (en kg): '))
puntaje = float(input('Ingresa tu puntaje obtenido: '))

seleccion(sexo,edad,altura,peso,puntaje)
        



print('\n')
#####EJERCICIO 7: Hacer un Programa de verificación de datos para obtención Tarjeta Única de Circulación (TUC) electrónica:
 #Deben ser Mujeres/Hombres mayores de edad, aprobar examen médico, prueba de conocimiento mayor a 80 puntos, prueba de manejo mayor a 95 puntos, verificar pago de 10 soles, debe imprimir un mensaje de "APTO TUC".
 #Si no cumplen cualquiera de las opciones debe imprimir un mensaje de "NO APTO TUC".
 
 
print("              VERIFICACION DE DATOS PARA OBTENCION DE TUC")
print("\n\n  ----------------------------------------------------------")
exm = input("¿Aprobo examen medico? Responder si - no : ")
edad =int(input("INGRESE SU EDAD : "))
pnts = int(input("INGRESE SU PUNTAJE DE LA PRUEBA DE CONOCIMIENTOS : "))
pntsm = int(input("INGRESE SU PUNTAJE DE LA PRUEBA DE MANEJO : "))
pago = input("¿Realizo el pago? Responder si - no  : ")



if edad >= 18:
    if pnts > 80:
        if pntsm >95:
            if pago == 'si':
                
                if exm == 'si':
                    print("Cumple con todos los requisitos")
                    print("\n APTO PARA TUC")
                else:
                    print("No aprobo examen medico")
                    print("\n NO APTO TUC")
                    
            else:
                print("Falta realizar el pago")
                print("\n NO APTO TUC")
        else:
            print("No aprobo la prueba de manejo")
            print("\n NO APTO TUC")
    else:
        print("No aprobo la prueba de conocimiento")
        print("\n NO APTO TUC")
else:
    print("Usted es menor de edad")
    print("\n NO APTO TUC")
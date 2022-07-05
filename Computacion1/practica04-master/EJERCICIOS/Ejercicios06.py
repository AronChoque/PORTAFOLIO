#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################# * EJERCICIOS * #################################

##### EJERCICIO 1: Hacer un programa que imprima en pantalla un menu "Numeros Pares e Impares" con la siguientes opciones:
#Ingresar numeros de inicio y de fin del rango
#Imprimir los numeros pares del rango.
#Imprimir los numeros Impares del rango.
#Imprimir los numeros Primos del rango.
#Salir






####### EJERCICIO 2: Hacer un programa que imprima en pantalla menu "Tabla de Multiplicar" con la siguientes opciones:
#Ingresar rango de numeros.
#Imprimir Tabla de multiplicar solo numeros pares del rango.
#Imprimir Tabla de multiplicar solo numeros impares del rango.
#Ingrese numero para Imprimir su tabla de multiplicar.
#Salir

def menu():
    titulo = ("      'tabla de multiplicar'    ")
    print(titulo.center(50,'*'))
    print('\n\n')
    print("Selecciona una Opción")
    print("\t1 - Ingresar rango de numeros.")
    print("\t2 - Ingrese numero para Imprimir su tabla de multiplicar.")
    print("\t3 - Imprimir Tabla de multiplicar solo numeros pares del rango.")
    print("\t4 - Imprimir Tabla de multiplicar solo numeros impares del rango.")
    print("\t5 - salir")

def validar():
    while True:
        try:
            menu()
            opcionMenu = input("Seleccione una opción: => ")
            if opcionMenu == "1":
                print ("")
                print("Ingrese rango de numeros:")
                try:
                    m = int(input("desde: "))
                    n = int(input("hasta: "))
                    print("rango de numeros:")
                    for x in range(m-1,n):
                        print(x+1, "", end = "")
                    print("\n______________________________________________________________________________________________")
                    print("\n")
                except ValueError:
                    print('ERROR..Ingrese un numero entero')       
            
            elif opcionMenu == "2":
                print ("")
                try:
                    c = int(input ("Has pulsado la opción 2... \n ingresar el número:"))
                    final = n
                    contador = m
                    while contador <= final:
                        producto = (contador * c)
                        print("{} x {} = {}".format(c,contador,producto))
                        contador = contador + 1
                    print("\n_______________________________________________________________________________________________")
                    print("\n")
                except ValueError:
                    print('ERROR..Ingrese un numero entero') 
                
            
            elif opcionMenu == "3":
                print ("")
                print ("Has pulsado la opción 3... \n Impriendo números pares\n")
                final = n
                contador = m
                for i in range(m,n+1):
                    if i % 2 == 0:
                        print(c, "x", i, "=",i*c)
                print("\n_______________________________________________________________________________________________")
                print("\n")
<<<<<<< HEAD
            except ValueError:
                print('ERROR..Ingrese un numero entero')
            except UnboundLocalError: print("\n ERROR.. Debes ingresar los datos anteriores")
                
            
        elif opcionMenu == "3":
            try:
                print ("")
                print ("Has pulsado la opción 3... \n Impriendo números pares\n")
                final = n
                contador = m
                for i in range(m,n):
                    if i % 2 == 0:
                        print(c, "x", i, "=",i*c)
                print("\n_______________________________________________________________________________________________")
                print("\n")
            except UnboundLocalError: print("\n ERROR.. Debes ingresar los datos anteriores")
        
        elif opcionMenu == "4":
            try:
=======
        
            elif opcionMenu == "4":
>>>>>>> 9749745a778ddd1ee9e27e83a7f1ede0af9418c4
                print ("")
                print ("Has pulsado la opción 4... \n Impriendo números impares\n")
                final = n
                contador = m
                for i in range(m,n):
                    if (i + 1 )% 2:
                        print(c, "x", (i+1), "=",(i+1) * c)
                print("\n_______________________________________________________________________________________________")
                print("\n")
<<<<<<< HEAD
            except UnboundLocalError: print("\n ERROR.. Debes ingresar los datos anteriores")
=======
>>>>>>> 9749745a778ddd1ee9e27e83a7f1ede0af9418c4
            
            elif opcionMenu == "5":
                break
            else:
                print("")
                input("NO has pulsado ninguna opción correcta... \n pulsa una tecla para continuar")
        except UnboundLocalError:
            print("ERROR...primero debe ingresar un rango y el numero a multiplicar\n")
            print("\n__________________________________________________________________________________________")
    return opcionMenu

if __name__ == '__main__':
    validar()
    
    print('\t\t\t\t FIN DEL PROGRAMA \t\t\t\t')
        
        




####### EJERCICIO 3: Hacer un programa que imprima en pantalla menu "Números Capicua"con la siguientes opciones:
#Ingresar un rango de numeros de hasta 4 cifras.
#Imprimir numeros capicua de dos cifras del rango.
#Imprimir numeros capicua de tres cifras del rango.
#Salir








###### EJERCICIO 4: Hacer un programa que imprima en pantalla un menu de "Datos del Postulante" que solicite ingresar las siguientes opciones:
#Nombre (sin numeros o simbolos extraños)
#Apellido (sin numeros o simbolos extraños)
#DNI
#Celular 1
#Celular 2
#Altura
#Peso
#Imprimir los datos ingresados del postulante
#Salir
y = 0
a=""
b=""
c=""
d=""
e=""
f=""
g=""
def programa():       
    try:
        import time         
        def menu():
            print("\n\n                        ----  MENU  ---- \n\n ")
            print("1. Nombre")
            print("2. Apellido")
            print("3. DNI")
            print("4. Celular 1")
            print("5. Celular 2")
            print("6. Altura")
            print("7. Peso")
            print("8. Imprimir los datos ingresados por los postulantes")
            print("9. Salir")
            def nombre():
                global a
                a = input("\nIngresa tu nombre aqui : ")
                lista= ["1","2","3","4","5","6","7","8","9","0",'?','!','$','%','&','/','ª','º',",",".",'+',"-", "_","@"]
                for cf in a:
                    if cf in lista:
                        print("\n\n ---- >> Digite bien su nombre, no debe contener caracteres extraños, ni numeros")
                        time.sleep(3)
                        nombre()
                        break
                    else:
                        pass                                    
            def apellido():
                global b
                b = input("\nIngresa tu apellido aqui : ")
                lista= ["1","2","3","4","5","6","7","8","9","0",'?','!','$','%','&','/','ª','º', '+',"-", "_","@",".",","]
                for cf in b:
                    if cf in lista:
                        print("\n\n ---- >> Digite bien su apellido, no debe contener caracteres extraños, ni numeros")
                        time.sleep(3)
                        apellido()
                        break
                    else:
                        pass 
            def dni():        
                global c
                c = input("\nIngresa tu DNI aqui : ")
                if len(c) > 8 or len(c) < 8:
                    print("\n\n ---- >>  Son 8 digitos, vuelva a intentar")
                    time.sleep(3)
                    dni()
                else:
                    lista= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",'?','!','$','%','&','/','ª','º', '-',"+", "_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",",","."]
                    for cf in c:
                        if cf in lista:
                            print("\n\n ---- >> Solo debes ingresar numeros, vuelva a intentar")
                            time.sleep(3)
                            dni()
                            break
                        else:
                            pass      
            def celu_1():
                global d
                d = input("\nIngresa tu numero de celular aqui : ")
                if len(d) > 9 or len(d) < 9:
                    print("\n\n ---- >>  Son 9 digitos, vuelva a intentar")
                    time.sleep(3)
                    celu_1()
                else:
                    lista= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",'?','!','$','%','&','/','ª','º', '-',"+", "_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",".",","]
                    for cf in d:
                        if cf in lista:
                            print("\n\n ---- >> Solo debes ingresar numeros, vuelva a intentar")
                            time.sleep(3)
                            celu_1()
                            break
                        else:
                            pass
            def celu_2():
                global e
                e = input("\nIngresa tu segundo numero de celular aqui : ")
                if len(e) > 9 or len(e) < 9:
                    print("\n\n ---- >>  Son 9 digitos, vuelva a intentar")
                    time.sleep(3)
                    celu_2()
                else:
                    lista= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",'?','!','$','%','&','/','ª','º', '-',"+", "_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z",",","."]
                    for cf in e:
                        if cf in lista:
                            print("\n\n ---- >> Solo debes ingresar numeros, vuelva a intentar")
                            time.sleep(3)
                            celu_2()
                            break
                        else:
                            pass
            def altura():
                global f
                f = input("\nIngresa tu altura aqui (m): ")
                if len(f) > 4 or len(f) < 4:
                    print("\n\n ---- >>  Ingresa bien tu altura, usar dos decimales, intenta de nuevo")
                    time.sleep(3)
                    altura()
                else:
                    lista= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",'?','!','$','%','&','/','ª','º', '-',"+", "_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
                    for cf in f:
                        if cf in lista:
                            print("\n\n ---- >> Solo debes ingresar numeros, vuelva a intentar")
                            time.sleep(3)
                            altura()
                            break
                        else:
                            pass
            def peso():
                global g
                g = input("\nIngresa tu peso aqui (kg): ")
                if len(g) > 5 or len(g) < 5:
                    print("\n\n ---- >>  Ingresa bien tu peso, usar dos decimales, intenta de nuevo")
                    time.sleep(3)
                    peso()
                else:
                    lista= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",'?','!','$','%','&','/','ª','º', '-',"+", "_","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
                    for cf in g:
                        if cf in lista:
                            print("\n\n ---- >> Solo debes ingresar numeros, vuelva a intentar")
                            time.sleep(3)
                            peso()
                            break
                        else:
                            pass
            def mostrar():                            
                if a == "":
                    print("\n\n ** --  DEBES INGRESAR TODOS LOS DATOS  -- ** ")
                    time.sleep(4)
                elif b == "":
                    print("\n\n ** --  DEBES INGRESAR TODOS LOS DATOS  -- ** ")
                    time.sleep(4)
                elif c == "":
                    print("\n\n ** --  DEBES INGRESAR TODOS LOS DATOS  -- ** ")
                    time.sleep(4)
                elif d == "":
                    print("\n\n ** --  DEBES INGRESAR TODOS LOS DATOS  -- ** ")
                    time.sleep(4)
                elif e == "":
                    print("\n\n ** --  DEBES INGRESAR TODOS LOS DATOS  -- ** ")
                    time.sleep(4)
                elif f == "":
                    print("\n\n ** --  DEBES INGRESAR TODOS LOS DATOS  -- ** ")
                    time.sleep(4)
                elif g == "":
                    print("\n\n ** --  DEBES INGRESAR TODOS LOS DATOS  -- ** ")
                    time.sleep(4)
                else:
                    print("\n\n  --- DATOS DEL POSTULANTE --- \n\n Nombre : ",a,"\n Apellido : ",b,"\n DNI : ",c,"\n #Celular 1 : ",d,"\n #Celular 2 : ",e,"\n Altura : ",f,"m","\n Peso : ",g,"kg")
                    time.sleep(5)
            def fin_del_programa():
                global y
                y = 9
                print("\n\n --------------- ")

            x = int(input("\n\n Ingrese la opcion deseada  --- >  "))

            if x == 1:
                nombre()
            elif x == 2:
                apellido()
            elif x == 3:
                dni()
            elif x == 4:
                celu_1()
            elif x == 5:
                celu_2()
            elif x == 6:
                altura()
            elif x == 7:
                peso()
            elif x == 8:
                mostrar()
            elif x == 9:
                fin_del_programa()
            elif x > 9 or x < 1:
                print("\n\n --->  NO EXISTE ESA OPCION \n       Intenta de nuevo ")
                time.sleep(3)
            else:
                print(" --> Solo numeros <--")
        def iniciar():
            while True:
                global y
                if y == 9:
                    break
                else:
                    menu()
        iniciar()

    except (NameError, ValueError):
        print("\n\n --> DEBES INGRESAR NUMEROS !! \n\n")
if __name__ == '__main__': 
        programa()
        print(" -- Hasta luego--")







######## EJERCICIO 5: Hacer un programa que imprima en pantalla un menu de "Datos del Alumno" que solicite ingresar las siguientes opciones:
#Nombre (sin numeros o simbolos extraños)
#Apellido (sin numeros o simbolos extraños)
#Nota1
#Nota2
#Nota3
#Nota4
#Nota Proyecto Final
#Imprimir promedio del alumno
#Salir
#La impresión del promedio es:
##promedio = (nota1 + nota2 + nota3 + nota4 + nota proyecto final * 3) / 7
##Si las notas: nota1 , nota2 , nota3 , nota4 ; debe tener 5 puntos extras.
##Si promedio es mayor a 10.5, debe imprimir la palabra APROBADO, sino DESAPROBADO.
##Si promedio es mayor a 17.5, debe imprimar adicionalmente la palabra QUINTO SUPERIOR.
##Si promedio es mayor a 19.5, debe imprimar adicionalmente la palabra DECIMO SUPERIOR










######## EJERCICIO 6: Hacer un programa que imprima en pantalla menu "Numeros Capicua" con la siguientes opciones:
#Imprimir Numeros Capicua de 3 cifras
#Imprimir Numeros Capicua de 4 cifras
#Validar Numeros Capicua de 3 cifras
#Validar Numeros Capicua de 4 cifras
#Salir







####### EJERCICIO 7: Hacer un programa que imprima en pantalla menu "Datos del Paciente" que solicite ingresar la siguientes opciones:
#Nombre (sin numeros o simbolos extraños)
#Apellido (sin numeros o simbolos extraños)
#Edad
#Peso
#Sexo
#Imprimir Dieta
#Salir
#La impresión de la dieta dependera de:
##Para Mujeres:
###Si su peso es menor a 40Kilos no hay dieta
###Si su peso esta entre 40kilos y 50Kilos dieta rica en vegetales (detallar dieta)
###Si su peso esta entre 50kilos y 60Kilos dieta rica en vegetales y frutas (detallar dieta)
###Si su peso esta entre 60kilos y 80Kilos dieta rica en vegetales, frutas y semillas (detallar dieta)
###Si su peso es mayor a 80Kilos debe hacerse cirugía
##Para Varones:
###Si su peso es menor a 60Kilos no hay dieta
###Si su peso esta entre 60kilos y 75Kilos dieta rica en vegetales (detallar dieta)
###Si su peso esta entre 75kilos y 95Kilos dieta rica en vegetales y frutas (detallar dieta)
###Si su peso esta entre 95kilos y 120Kilos dieta rica en vegetales, frutas y semillas (detallar dieta)
###Si su peso es mayor a 120Kilos debe hacerse cirugía

print('\n')

nom = ""
ape = ""
y = 0
x = 0
diet = ""
sex = ""
elegir = 0
fin = 0
def menu():
    global elegir
    print('\n')
    print(" -- DATOS DEL PACIENTE --")
    print('\n')
    print("Por favor digite el número una sola vez, preferible en orden\n")
    print("1. Nombre")
    print("2. Apellido")
    print("3. Edad")
    print("4. Sexo")
    print("5. Peso")
    print("6. Imprimir Dieta")
    print("7. Salir")
    try:
    
        elegir = int(input("DIGITA TU OPCION : "))
        if elegir == 1:
            validar_nom()
        elif elegir == 2:
            validar_ape()
        elif elegir == 3:
            validar_num()
        elif elegir == 4:
            validar_sexo()
        elif elegir == 5:
            validar_peso()
        elif elegir == 6:
            if diet == "":
                print("DATOS INSUFICIENTES")
            else:
                print('\n')
                print(" Paciente ",nom, ape, "usted ",diet)
        elif elegir == 7:
            global fin
            fin = 7
        else:
            print("ESA OPCION NO EXISTE")
    except ValueError: print("DEBES INGRESAR SOLO NUMEROS") + menu()

def validar_nom(): 
    global nom
    nom = input("Ingresar nombre: ")
    while True:
        if nom.isalpha():
            break          
        else:
            print("\nNOMBRE NO VALIDO! \nEvite usar símbolos y números \nVuelva a ingresar su nombre:  ")
            nom = input("")
def validar_ape(): 
    global ape
    ape = input("Ingresar apellido: ")
    while True:
        if ape.isalpha():
            break          
        else:
            print("\nAPELLIDO NO VALIDO! \nEvite usar símbolos y números \nVuelva a ingresar su apellido: ")
            ape = input("")
def validar_num():
    global x
    while True:
        try:
            x = int(input("Ingresar edad: "))
            break
        except ValueError:
            print("\nEDAD NO VALIDA!   ...  \t\t Vuelva a ingresar su edad: ")


#Crear función para obtener respectiva dieta
def validar_sexo():
    global sex
    print("Ingrese una de estás opciones: \n\na) Femenino \nb) Masculino")
    sex = input("Igresar sexo:   ")
    if sex == "b" or "a":
        menu()
    else:
        print("INGRESA BIEN LA OPCION")
        validar_sexo()
def validar_peso():
    global sex,diet,y
    if sex == "a":
        while True:
            try:
                y = int(input("Ingresar su peso:  "))
                if y<=40:
                    diet = "\n\nNo necesita de una dieta..."
                elif 40<y<=50:
                    diet = "\n\nDeberá comer una dieta rica en vegetales como: tuberculos, brocoli, coliflor, apio, etc."
                elif 50<y<=60:
                    diet = "\n\nDeberá tener una dieta rica en vegetales y frutas, como: ensalada de distintas frutas o verduras"
                elif 60<y<=80:
                    diet = "\n\nDeberá tener una dieta rica en vegetales, frutas y semillas, obligatoriamente"
                elif y>80:
                    diet = "\n\nDeberá recurrir a una cirugía de pérdida de peso\n\n\n"
                break
            except ValueError:
                print("\nPESO NO VALIDO!   ...  \t\t Vuelva a ingresar su peso: ")

                
    elif sex == "b":
        while True:
            try:
                y = int(input("Ingresar su peso:  "))
                if y<=60:
                    diet = "\n\nNo necesita de una dieta..."
                elif 60<y<=75:
                    diet = "\n\nDeberá comer una dieta rica en vegetales como: tuberculos, brocoli, coliflor, apio, etc."
                elif 75<y<=95:
                    diet = "\n\nDeberá tener una dieta rica en vegetales y frutas, como: ensalada de distintas frutas o verduras"
                elif 95<y<=120:
                    diet = "\n\nDeberá tener una dieta rica en vegetales, frutas y semillas, obligatoriamente"
                elif y>120:
                    diet = "\n\nDeberá recurrir a una cirugía de pérdida de peso\n\n\n"
                break
            except ValueError:
                print("\nPESO NO VALIDO!   ...  \t\t Vuelva a ingresar")
    else:
        print("OPCIONES INVALIDAS!")




if __name__=='__main__':
    titulo = ('          DATOS DEL PACIENTE           ')
    print(titulo.center(50,'*'))
    while True:
        menu()
        if fin == 7:
            break



print('\n\n')
print('FINALIZÓ')    
print('\n\n*****          GRACIAS POR SU ELECCIÓN          *****')

print('\n')



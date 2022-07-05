#Práctica 03 
#PYTHON - Estructuras Condicionales
#@author: mkr-jakhu
"""
"Ejemplos"
"Listas"
"Operadores con variables:"
lista1 = [10, 20, 30]
lista2 = [40, 50, 60]
print(lista1 + lista2)


"Mejorando la impresión de varias listas:"
listaA = ["audi", "toyota", "mazda"]
puerta = [2, 4]

print("Mi auto es: " +listaA[-1].title())
print(f"Mi auto {listaA[-2].title()} tiene {puerta[-2]} puertas")


"Operadores matemáticos de una lista:"
lista3 = [100, 500, 200, 7000, -200]

print(sum(lista3))
print(max(lista3))
print(min(lista3))



lista1 = list(range(7))
lista2 = list(range(1,10))
lista3 = list(range(-10,2))
lista4 = list(range(200,100,-20))
lista5 = list(range(200,100,20))
print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)


"Condicionales"
"Hacer un programa que determine si un número ingresado por pantalla es positivo o negativo"
x = int(input("Ingrese un número entero, positivo o negativo: "))
if x > 0:
    y = "positivo"
else:
    if x < 0:
        y = "negativo"
    else:
        if x == 0:
            y = "cero"
print("\nEl número: {}".format(x))
print("Es número: {}".format(y))



def det(xx):
    if xx < 0:
        p = "negativo"
    elif xx > 0:
        p = "positivo"
    else:
        p = "cero"
        print(p)
    return p

num = int(input("Ingrese un número entero, positivo o negativo: "))
resp = det(num)

print("\nEl número: {}".format(num))
print("Es un número: {}".format(resp))


"Hacer un programa que pueda ingresar radio del círculo y calcule: Perímetro, Área y Diámetro"
#Método 1:
from math import pi
radio = float(input("Ingrese radio del círculo: "))
print("Seleccione una opcion: ")
print("a) Calcular el diametro: ")
print("b) Calcular el perimetro: ")
print("c) Calcular el area: ")
opcion = input("Digita a, b, o c y presiona enter: ")

if opcion == "a":
    diametro = 2*radio
    print("\nEl diametro del círculo es: {0}.".format(diametro))
else:
    if opcion == "b":
        perimetro = 2*pi*radio
        print("\nEl perimetro del círculo es: {0}.".format(perimetro))
    else:
        if opcion == "c":
                area = pi*radio**2
                print("\nEl area del círculo es: {0}.".format(area))
        else:
            print("\nSolo hay tres opciones: a, b, c.")
            print('Tu has tecleado "{0}".'.format(opcion))
            
            
#Método 2:
radio = float(input("Ingrese el radio del circulo: "))
print("Seleccione una opcion: ")
print("a) Calcular el diametro: ")
print("b) Calcular el perimetro: ")
print("c) Calcular el area: ")
opcion = input("Digita a, b, o c y presiona enter: ")

if opcion == "a":
    diametro = 2* radio
    print("El diametro del circulo es: {0}.".format(diametro))
elif opcion == "b":
    perimetro = 2*pi*radio
    print("El perimetro del circulo es: {0}.".format(perimetro))
elif opcion == "c":
    area = pi*radio**2
    print("El area del circulo es: {0}.".format(area))
else: 
    print("Solo hay tres opciones: a, b, c.")
    print('Tu has tecleado "{0}".'.format(opcion))


"Hacer un programa que verifique si se ha comprado carne en la lista de mercado para hacer parrillada"
alimento = ["arroz", "papas", "camotes", "leche", "carne", "cebolla", "tomate", "lechuga"]
if "carne" in alimento:
    print("Hoy comemos rica parrila!!!!!")
else:
    print("Hoy comemos verduras")
    
    
"Hacer un programa que verifique en una jugeria si tienen la fruta que deseas y te prepare un jugo"
def preparar(fruit):
    if fruit in fruta:
        print(f"\nSi tenemos {antojo.upper()} !!!, te preparamos un Jugo")
    else: 
        print(f"\nHoy no tenemos {antojo.upper()}, pero regresa mañana")
              
fruta = ["platano", "manzana", "pera", "naranja", "mandarina", "uva"]
antojo = input("Ingresa la fruta que deseas comer hoy: ")
preparar(antojo)
print("\nGracias por tu preferencia !!!, Vuelve pronto")


"Hacer un programa que verifique mayoria de edad"
def mayoria(nom,xx):
    if xx >= 18:
        print(f"\n{nom.upper()} es Mayor de edad con {xx} años de edad")
    else:
        print(f"\n{nom.upper()} es Menor de edad con {xx} años de edad")
        
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingrese su edad: "))

mayoria(nombre,edad)

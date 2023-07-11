print("-------------- RETO-1 --------------")
"""Construye una función “calculadora()” que reciba como
parámetros de entrada:
Tipo de operación y Operadores (siempre 2 operadores para
hacerlo más sencillo).
Las operaciones permitidas son: suma (“sum”), resta (“subs”),
multiplicación (“mult”) y división (“div”).
Dependiendo del identificador de la operación, y los parámetros de
entrada, la función debe decidir qué operación realizar y
devolvernos un resultado válido."""
def calculadora(operacion, num1, num2):
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    elif operacion == "multiplicacion":
        resultado = num1 * num2
    elif operacion == "division":
        resultado = num1 / num2
    else:
        print("Solo se puede: sumar, restar, mult. y dividir")

    return resultado
operacion = "suma"
num1 = 33
num2 = 20
resultado = calculadora(operacion, num1, num2)
print(resultado)

operacion = "resta"
num1 = 33
num2 = 20
resultado = calculadora(operacion, num1, num2)
print(resultado)

operacion = "multiplicacion"
num1 = 33
num2 = 20
resultado = calculadora(operacion, num1, num2)
print(resultado)

operacion = "division"
num1 = 220
num2 = 20
resultado = calculadora(operacion, num1, num2)
print(resultado)


print("-------------- RETO-2 --------------")
"""Crea un fichero llamado Vector.py con las siguientes funciones:
• Crear vector(n, m): Crea un vector de n números aleatorios que van desde
0 hasta m.
• Suma vector(v1, v2): Suma dos vectores v1 y v2 si y solo si tienen el mismo
numero de elementos.
• Producto numero vector(n, v1): Multiplica el vector v1 por el numero n.
• Resta vector(v1, v2): Resta dos vectores v1 y v2 si y solo si tienen el mismo
numero de elementos.
• Producto vector(v1, v2): Multiplica dos vectores v1 y v2 si y solo si tienen el
mismo número de elementos"""

import Vector

vector1 = Vector.crear_vector(3, 9)
print(vector1)

vector2 = Vector.crear_vector(3, 9)
print(vector2)

suma = Vector.suma_vector(vector1, vector2)
print(suma)

numero = 3
producto = Vector.producto_numero_vector(numero, vector1)
print(producto)

resta = Vector.resta_vector(vector1, vector2)
print(resta)

producto_vector = Vector.producto_vector(vector1, vector2)
print(producto_vector)

print("-------------- RETO-3 --------------")
"""• Use la función incorporada len() para encontrar la longitud de la
siguiente cadena de texto: "¡Hola, mundo!".
• Cree una función llamada doblar() que toma un número y
devuelve el doble de ese número. Luego use la función map()
para doblar todos los números en la siguiente lista: [1, 2, 3, 4, 5].
• Cree una función llamada multiplicar() que toma dos números y
devuelve su producto. Luego use la función reduce() para
multiplicar todos los números en la siguiente lista: [1, 2, 3, 4, 5]."""

from functools import reduce

texto = "¡Hola, mundo!"
longitud = len(texto)
print("La longitud del texto es:", longitud)

def doblar(numero):
    return numero * 2

numeros = [2,3,4,5]
resultado_map = list(map(doblar, numeros))
print("El resultado de doblar los elementos es:", resultado_map)

def multiplicar(a, b):
    return a * b

resultado_reduce = reduce(multiplicar, numeros)
print("Si multiplicamos todos los elentos, el resultado es:", resultado_reduce)
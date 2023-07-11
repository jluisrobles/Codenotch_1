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

import random
def crear_vector(n, m):
    vector = []
    for i in range(n):
        vector.append(random.randint(0, m))
    return vector
def suma_vector(v1, v2):
    if len(v1) != len(v2):
        return "Error"

    resultado = []
    for i in range(len(v1)):
        resultado.append(v1[i] + v2[i])
    return resultado
def producto_numero_vector(n, v1):
    resultado = []
    for i in range(len(v1)):
        resultado.append(n * v1[i])
    return resultado
def resta_vector(v1, v2):
    if len(v1) != len(v2):
        return None

    resultado = []
    for i in range(len(v1)):
        resultado.append(v1[i] - v2[i])
    return resultado
def producto_vector(v1, v2):
    if len(v1) != len(v2):
        return None

    resultado = []
    for i in range(len(v1)):
        resultado.append(v1[i] * v2[i])
    return resultado
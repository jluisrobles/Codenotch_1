print("-------------- RETO-1 --------------")
"""De la misma manera que en el ejemplo de esta unidad, crea la clase
“Persona” de la manera más completa que se te ocurra."""
class Persona:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero

persona1 = Persona("Luis", "Perez", 18, "Masculino")

print("Nombre:", persona1.nombre)
print("Apellido:", persona1.apellido)
print("Edad:", persona1.edad)
print("Género:", persona1.genero)


print("-------------- RETO-2 --------------")
"""Utilizando la clase “Persona” definida en el punto anterior, haz que se pueda
calcular el IMC (índice de mas corporal) de cualquier persona que se haya
creado como un objeto de la clase."""
class Persona:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero
    def calcular_imc(self, peso, altura):
        altura_metros = altura / 100
        imc = peso / (altura_metros ** 2)
        return imc
persona1 = Persona("Luis", "Perez", 18, "Masculino")

peso_persona1 = 70  # Peso en kg
altura_persona1 = 175  # Altura en cm

imc_persona1 = persona1.calcular_imc(peso_persona1, altura_persona1)

print("El IMC de", persona1.nombre, "es:", imc_persona1)


print("-------------- RETO-3 --------------")
"""Añadir el atributo anyoNacimiento a la clase ”Persona” e implementar el
método edad que tome como parámetro el año actual y calcule la edad de
la persona"""
class Persona:
    def __init__(self, nombre, apellido, edad, genero, anyoNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.anyoNacimiento = anyoNacimiento

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero
    def calcular_edad(self, anyo_actual):
        edad = anyo_actual - self.anyoNacimiento
        return edad
persona1 = Persona("Luis", "Perez", 18, "Masculino", 2005)

anyo_actual = 2023

edad_persona1 = persona1.calcular_edad(anyo_actual)

print("La edad de", persona1.nombre, "es:", edad_persona1)


print("-------------- RETO-4 --------------")
"""Añadir un método que se denomine mostrarTodos que muestre por
consola cada una de los atributos de la clase “Persona” seguido por “:”
y el valor del atributo."""
class Persona:
    def __init__(self, nombre, apellido, edad, genero, anyoNacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.anyoNacimiento = anyoNacimiento

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero

    def calcular_edad(self, anyo_actual):
        edad = anyo_actual - self.anyoNacimiento
        return edad
    def mostrarTodos(self):
        atributos = self.__dict__
        for atributo, valor in atributos.items():
            print(f"{atributo}: {valor}")
persona1 = Persona("Luis", "Perez", 18, "Masculino", 2005)

persona1.mostrarTodos()
print("-------------- RETO-5 --------------")
"""Añadir el atributo aficiones a la clase “Persona”, que es un array de strings, y
crear un método denominado mostrarAficiones, que muestre por consola las
aficiones de la persona."""
class Persona:
    def __init__(self, nombre, apellido, edad, genero, anyoNacimiento, aficiones):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
        self.anyoNacimiento = anyoNacimiento
        self.aficiones = aficiones

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero

    def calcular_edad(self, anyo_actual):
        edad = anyo_actual - self.anyoNacimiento
        return edad
    def mostrarAficiones(self):
        for aficion in self.aficiones:
            print(aficion)
persona1 = Persona("Luis", "Perez", 18, "Masculino", 2005, ["Viajar", "Caminar"])

persona1.mostrarAficiones()

print("-------------- RETO-6 --------------")
class Persona:
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero

    def obtener_nombre(self):
        return self.nombre

    def obtener_edad(self):
        return self.edad

    def obtener_genero(self):
        return self.genero
class Agenda:
    def __init__(self):
        self.lista_personas = []

    def agregar_persona(self, persona):
        self.lista_personas.append(persona)

    def printPersonas(self):
        for persona in self.lista_personas:
            atributos = vars(persona)
            for atributo, valor in atributos.items():
                print(f"{atributo}: {valor}")
            print()  # Salto de línea entre personas


persona1 = Persona("Luis", "Perez", 18, "Masculino")
persona2 = Persona("Ana", "García", 25, "Femenino")

agenda = Agenda()

agenda.agregar_persona(persona1)
agenda.agregar_persona(persona2)

agenda.printPersonas()
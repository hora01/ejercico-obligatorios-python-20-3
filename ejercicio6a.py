
# 6) Crea una clase llamada Persona:
# Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase: 
# 1) un constructor, donde los datos pueden estar vacíos. 
# 2) los setters y getters para cada uno de los atributos. Validar las entradas de datos. 
# 3) mostrar(): muestra los datos de la persona. 
# 4) es_mayor_de_edad(): devuelve un valor lógico indicando si es mayor de edad.

# El método '__init__' es el constructor de la clase y se utiliza para inicializar los atributos de la instancia.
# Los getters y setters se utilizan para acceder & modificar los atributos de la clase, respectivamente.
# En cada uno de los setters, se valida que el valor ingresado sea del tipo y formato adecuado, lanzando una excepción ValueError si no es así.
# El método 'mostrar' se utiliza para imprimir en pantalla los datos de la persona.
# El método 'es_mayor_de_edad' devuelve un valor lógico indicando si la persona es mayor de edad o no.

class Persona:
    def __init__(self, nombre='', edad=0, dni=''):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    # getters y setters para Nombre:
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    # getters y setters para Edad:
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self._edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo")

    # getters y setters para DNI:
    def get_dni(self):
        return self._dni

    def set_dni(self, dni):
        if isinstance(dni, str) and len(dni) == 9 and dni.isnumeric():
            self._dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de texto de 9 dígitos numéricos")

    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._dni}")

    def es_mayor_de_edad(self):
        return self._edad >= 18

p = Persona()
p.set_nombre('Horacio')
p.set_edad(16)
p.set_dni('123456789')
p.mostrar()
print(p.es_mayor_de_edad())
# Este código crea una instancia de la clase 'Persona', 
# establece sus atributos utilizando los setters, 
# muestra los datos de la persona 
# y determina si es mayor de edad o no.


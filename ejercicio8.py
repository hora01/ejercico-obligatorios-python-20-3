#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
#CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
#además del titular y la cantidad se debe guardar una bonificación que estará expresada en
#tanto por ciento. Crear los siguientes métodos para la clase:
#● Un constructor.
#● Los setters y getters para el nuevo atributo.
#● En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
#tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
#mayor de edad pero menor de 25 años y falso en caso contrario.
#● Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
#● El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta

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


class Cuenta:
    
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    def get_titular(self):
        return self.__titular
    
    def set_titular(self, titular):
        self.__titular = titular
        
    def get_cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print(f"Titular: {self.__titular.mostrar()}, Cantidad: {self.__cantidad}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
    
    def retirar(self, cantidad):
        self.__cantidad -= cantidad



class CuentaJoven(Cuenta):
    
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion
        
    def es_titular_valido(self):
        return self.get_titular().es_mayor_de_edad() and self.get_titular().get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Titular no válido para realizar la operación")
    
    def mostrar(self):
        print(f"Cuenta Joven. Bonificación: {self.__bonificacion}")

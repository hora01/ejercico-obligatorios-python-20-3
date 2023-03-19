#Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
#siguientes métodos para la clase:
#● Un constructor, donde los datos pueden estar vacíos.
#● Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
#datos.
#● mostrar(): Muestra los datos de la persona.
#● es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad


from datetime import date # Para obtener el año actual
 
# Definimos una clase Persona
class Persona:
    # Definimos los atributos de la clase
    nombre = ''
    apellidos = ''
    DNI = ''
    edad = 0
    
    # Definimos un "constructor" para la clase que recibirá el nombre de la persona
    def __init__(self, nombre):
        self.nombre = nombre
    
    #Definimos los "setters"
    def setNombre(self, nombre):
        self.nombre = nombre
 
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    
    def setDni(self, dni):
        self.dni = dni
 
    def setEdad(self, edad):
        self.edad = edad
 
 
    #Definimos los "getters"
    def getNombre(self):
        return self.nombre
 
    def getApellidos(self):
        return self.apellidos
    
    def getDni(self):
        return self.dni
     
    def getEdad(self):
        return self.edad
     
    # Ejemplo de método que devuelve el año de nacimiento en función de la edad
    def añoNacimiento (self):
        # Obtenemos la fecha actual
        fechaActual = date.today()
        # Obtenemos el año de la fecha actual
        año = fechaActual.year
        # Calculamos el año de nacimiento restando al año actual la edad de la persona
        añoNacimiento = año - self.edad
        return añoNacimiento
    
  
    #Definimos un método en la clase para mostrar todos los datos de la persona por pantalla
    def mostrarDatos(self):
        print('El nombre de la persona es: ' + self.nombre)
        print('La edad de la persona es: ' + str(self.edad))
        print('El DNI de la persona es: ' + self.dni)
        
    # Método para asignar el nombre completo a partir de los apellidos y el nombre    
    def generarNombreCompleto (self):
        global nombreCompleto
        nombreCompleto = self.apellidos + ', ' + self.nombre
        
 
#Fuera de la clase, definimos un objeto "ciudadano" de la clase Persona
#Le pasamos el nombre al constructor de la clase
ciudadano = Persona("horacio Fernando")
# Con los setters establecemos los datos del ciudadano
ciudadano.setApellidos('Perezz')
ciudadano.setEdad(47)
ciudadano.setDni('25470767')
 
# Usamos el método de la clase que muestra los datos de la persona por pantalla
ciudadano.mostrarDatos()
 
# Usamos los setters y algún método de la clase para mostrar 
# algunos datos del objeto ciudadano de la clase Persona
print('El ciudadano ' + ciudadano.getNombre() + ', nació en el año ' + str(ciudadano.añoNacimiento()))


# Llamamos al método que obtiene el nombre completo en la clase
ciudadano.generarNombreCompleto();
 
#Datos del objeto ciudadano
print('Datos del ciudadano:')
ciudadano.mostrarDatos()
print('El nombre completo en el Registro es: ' + nombreCompleto)
 

#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
#cada palabra que contiene y la cantidad de veces que aparece (frecuencia).


def creador_dict(cadena):
  '''Recibe una cadena de caracteres y regresa un diccionario con las palabras (keys) y conteo (value)'''
  lista_1= cadena.split()
  dict_1={}
  for i in lista_1:
    if i in dict_1:
      dict_1[i] +=1
    else:
      dict_1[i]= 1
  return dict_1

def contador_dict(dictionario):
  '''Recibe un diccionario y regresa una tupla: la palabra mas repetida y cuantas veces aparece'''
  palabra_frecuente= ''
  cantidad=0
  for keys,values in dictionario.items():
    if values > cantidad:
      cantidad= values
      palabra_frecuente= keys
  return palabra_frecuente,cantidad
entrada=input('Ingrese su cadena de caracteres: ')
print(creador_dict(entrada))
print(contador_dict(creador_dict(entrada)))

# ejemplo hola , hola , hola , mundo
#("hola" : 2 ,", : 2" mundo :1)
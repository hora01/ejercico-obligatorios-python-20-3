#Escribir una función que calcule el mínimo común múltiplo entre dos números

a=int(input("digite el primer valor"))
b=int(input("digite el segundo valor"))

#variable comienza en 2 y va incrementando

i=2

# ciclo 

while True:
    if i%a==0 and i%b==0:
        mcm =i
        break
    
    i+=1

print("el minimo comun multiple es:",mcm) 

# para reiniciar borrar la consola 



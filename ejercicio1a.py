# Escribir una función que calcule el máximo común divisor entre dos números

# MCD el numero mas grande que divide dos numeros 


def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def maximo_comun_divisor_recursivo(a, b):
    if b == 0:
        return a
    return maximo_comun_divisor_recursivo(b, a % b)


a = 80
b = 4
resultado = maximo_comun_divisor(a, b)
resultado_recursivo = maximo_comun_divisor_recursivo(a, b)
print(
    f"El Máximo común divisor de {a} y {b} es {resultado}. De manera recursiva, es {resultado_recursivo}")


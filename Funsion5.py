# *******************************************************
# ** PARCIAL 01 - PROGRAMACIÓN 05                      **
# ** ARCHIVO: FunsionG5.py                             **
# ** Enunciado: lista-máximo / lista-factorial         **
# ** **
# ** Desarrollado por: Ray Barreto                     **
# ** Desarrollado por: Andy Montañez                   **
# *******************************************************

# Inicia desarrollo de la función dada (Estudiante 1: Ray Barreto)
def obtener_valor_maximo(lista):
    # Recibe una lista y retorne el valor máximo
    return max(lista)

# Ejemplo de prueba Obligatorio
print(f"Ray Barreto - Resultado: {obtener_valor_maximo([5, 12, 9, 2])}")


# Inicia desarrollo de la función dada (Estudiante 2: Andy Montañez)
def calcular_factorial(numero):
    # Recibe un número y calcule su factorial
    if numero < 0:
        return "No definido para números negativos"
    fact = 1
    for i in range(1, numero + 1):
        fact *= i
    return fact

# Ejemplo de prueba Obligatorio
print(f"Andy Montañez - Resultado: {calcular_factorial(5)}")
# *******************************************************
# ** PARCIAL 01 - PROGRAMACIÓN 05                      **
# ** ARCHIVO: FunsionG2.py                             **
# ** Enunciado: Suma-lista / promedio-lista            **
# ** **
# ** Desarrollado por: Ruben Blades                    **
# ** Desarrollado por: Cheo Feliciano                  **
# *******************************************************

# Inicia desarrollo de la función dada (Estudiante 1: Ruben Blades)
def calcular_suma_lista(lista):
    # Recibe una lista de números y calcule la suma total
    return sum(lista)

# Ejemplo de prueba Obligatorio
print(f"Ruben Blades - Resultado: {calcular_suma_lista([1, 2, 3, 4, 5])}")


# Inicia desarrollo de la función dada (Estudiante 2: Cheo Feliciano)
def calcular_promedio_lista(lista):
    # Recibe una lista de números y calcule el promedio
    if not lista:
        return 0
    return sum(lista) / len(lista)

# Ejemplo de prueba Obligatorio
print(f"Cheo Feliciano - Resultado: {calcular_promedio_lista([10, 20, 30, 40])}")
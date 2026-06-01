# *******************************************************
# ** PARCIAL 01 - PROGRAMACIÓN 05                      **
# ** ARCHIVO: FunsionG1.py                             **
# ** Enunciado: Par-Impar / Mayor-numero               **
# ** **
# ** Desarrollado por: Héctor Lavoe                    **
# ** Desarrollado por: Ismael Rivera                   **
# *******************************************************

# Inicia desarrollo de la función dada (Estudiante 1: Héctor Lavoe)
def determinar_par_impar(numero):
    # Determina si un número entero es par o impar
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Ejemplo de prueba Obligatorio
print(f"Hector Lavoe - Resultado: {determinar_par_impar(7)}")


# Inicia desarrollo de la función dada (Estudiante 2: Ismael Rivera)
def retornar_mayor(n1, n2):
    # Recibe dos números y retorna el mayor de ellos
    return max(n1, n2)

# Ejemplo de prueba Obligatorio
print(f"Ismael Rivera - Resultado: {retornar_mayor(15, 28)}")
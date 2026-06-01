# *******************************************************
# ** PARCIAL 01 - PROGRAMACIÓN 05                      **
# ** ARCHIVO: FunsionG6.py                             **
# ** Enunciado: lista-negativo / lista-positivo        **
# ** **
# ** Desarrollado por: Roberto Roena                   **
# ** Desarrollado por: Bobby Valentin                  **
# *******************************************************

# Inicia desarrollo de la función dada (Estudiante 1: Roberto Roena)
def filtrar_negativos(lista):
    # Recibe una lista de números y retorne solo los números negativos
    return [x for x in lista if x < 0]

# Ejemplo de prueba Obligatorio
print(f"Roberto Roena - Resultado: {filtrar_negativos([1, -2, 3, -4, 5])}")


# Inicia desarrollo de la función dada (Estudiante 2: Bobby Valentin)
def filtrar_positivos(lista):
    # Recibe una lista de números y retorne solo los números positivos
    return [x for x in lista if x > 0]

# Ejemplo de prueba Obligatorio
print(f"Bobby Valentin - Resultado: {filtrar_positivos([1, -2, 3, -4, 5])}")
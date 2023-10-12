

from biblioteca_stark_00 import *
#Estuve repasando el STARK PARA PODER HACERLO DE MANERA MÁS OPTIMIZADA Y NO ME SALEN LOS EJERCICIOS CON MINIMO. ADEMÁS EL MENÚ PARA SELECCIONAR QUE EJERCICIO VISUALIZAR ME DA ERROR EN VARIOS. 
# I) Ordenar el código implementando una función para cada uno de los valores informados.
# Función principal que muestra el menú y llama a las funciones correspondientes
def main_app(lista_personajes: list[dict]):
    while True:

        opcion = mostrar_menu()

        match opcion:
            case "1":
                print_nombre_superheroe(lista_personajes)
            case "2":
                print_nombre_altura_superheroe(lista_personajes)
            case "3":
                encontrar_maxima_altura(lista_personajes)

            case "4":
                encontrar_altura_minima(lista_personajes)

            case "5":
                obtener_altura_promedio(lista_personajes)
            case "6":
                obtener_heroe_mas_pesado(lista_personajes)

            case "7":
                obtener_heroe_menos_pesado(lista_personajes)

            case "8":
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción válida.")


#Ejecutar el menú principal

#Mostrar todos los datos

# Desafío #00:

# A) Analizar detenidamente el set de datos
# B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
# D) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F) Recorrer la lista y determinar la altura promedio de los  superhéroes (PROMEDIO)
# G) Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
# H) Calcular e informar cual es el superhéroe más y menos pesado.
# I) Ordenar el código implementando una función para cada uno de los valores informados.
# J) Construir un menú que permita elegir qué dato obtener.
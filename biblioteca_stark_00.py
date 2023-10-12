#ALUMNO: ALAN JOEL CALVEYRA
#DIVISIÓN: E

# B) Recorrer la lista imprimiendo por consola el nombre de cada superhéroe.
def print_nombre_superheroe(lista_heroes: list):

    for nombre_superheroe in lista_heroes: 
        print(nombre_superheroe["nombre"])



# C) Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def print_nombre_altura_superheroe(lista_heroes: list[dict]):

    for superheroe in lista_heroes:
        
        nombre_superheroe = superheroe["nombre"]
        altura_superheroe = float(superheroe["altura"])
        print(f"C) {nombre_superheroe}, {altura_superheroe}")


# D) Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def encontrar_maxima_altura(lista_personajes):
    max_altura = 0
    heroe_max = None
    for heroe in lista_personajes :
        altura = float(heroe["altura"])
        
        if altura > max_altura:
            max_altura = altura
        if altura == max_altura:
            heroe_max = heroe["nombre"]
    print(heroe_max)

    
# E) Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)

def encontrar_altura_minima(lista_personajes):
    minima_altura = float("inf")
    heroe_altura_minima = None
    for heroe in lista_personajes:
        altura = float(heroe["altura"])

        if altura < minima_altura:
            minima_altura = altura
        if altura == minima_altura:
            heroe_altura_minima = heroe["nombre"]

    print(heroe_altura_minima) 

# F) Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def obtener_altura_promedio(lista_personajes):
    acumulador_altura = 0
    contador = 0
    for heroe_altura in lista_personajes:
        altura = float(heroe_altura["altura"])
        acumulador_altura += altura
        contador += 1
    promedio = acumulador_altura / contador
    print(promedio) 

# G) Informar cual es la identidad del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

def obtener_identidad_del_heroe(lista_personajes):
    max_altura = 0
    identidad_heroe_altura_maxima = ""
    minima_altura = 0
    identidad_heroe_altura_minima = ""
    for heroe in lista_personajes:
        altura = float(heroe["altura"])

        if altura > max_altura:
            max_altura = altura
            identidad_heroe_altura_maxima = heroe["identidad"]
        
        if altura < minima_altura:
            minima_altura = altura
            identidad_heroe_altura_minima = heroe["identidad"]
    
    print(identidad_heroe_altura_maxima, identidad_heroe_altura_minima)

# H) Calcular e informar cual es el superhéroe más y menos pesado.
def obtener_heroe_mas_pesado(lista_personajes):
    
    peso_maximo = 0
    heroe_mayor_peso = None
    
    for heroe_peso_maximo in lista_personajes:
        peso_heroe = float(heroe_peso_maximo["peso"])
        
        if peso_heroe > peso_maximo:
            peso_maximo = peso_heroe
            heroe_mayor_peso = heroe_peso_maximo["nombre"]
    print(heroe_mayor_peso)

def obtener_heroe_menos_pesado(lista_personajes):
    peso_minimo = float("inf")
    heroe_menor_peso = None
    for heroe_peso_minimo in lista_personajes:
        peso_heroe = float(heroe_peso_minimo["peso"])
        
        if peso_heroe < peso_minimo:
            peso_minimo = peso_heroe
        if peso_minimo == peso_heroe:
            heroe_menor_peso = heroe_peso_minimo["nombre"]
    
    print(heroe_menor_peso) 

def perdir_opcion_menu() -> str:
    opcion = input("Elegí una opción: ")
    return opcion

def mostrar_menu()-> str:
    Menu = \
    """
        "1. Imprimir nombres de superhéroes"
        "2. Imprimir nombres y alturas de superhéroes"
        "3. Encontrar superhéroe más alto"
        "4. Encontrar superhéroe más bajo"
        "5. Calcular altura promedio de superhéroes"
        "6. Encontrar superhéroe más pesado"
        "7. Encontrar superhéroe menos pesado"
        "8. Salir"
    """
    print(Menu)
    return perdir_opcion_menu()
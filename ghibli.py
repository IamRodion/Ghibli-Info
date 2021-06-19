# Importando librerías necesarias
import os, requests

# Creando una constante con la dirección de la API Ghibli
URL_FILMS = "https://ghibliapi.herokuapp.com/films/"

# Creando constantes de títulos e información
LOGO = """\t _______ _     _ _     _  _ 
\t(_______) |   (_) |   | |(_)
\t _   ___| |__  _| |__ | | _ 
\t| | (_  |  _ \| |  _ \| || |
\t| |___) | | | | | |_) ) || |
\t \_____/|_| |_|_|____/ \_)_|
"""

INFO = """[Info] Programa creado con Python3 y la API de Ghibli para ver información de películas de Estudio Ghibli
[Info] Creado por __Rodion__ (https://github.com/RodionButEncapsulated)\n"""

# Creando función para limpiar la pantalla
def cleanscreen():
    os.system("clear || cls")    

# Creando función para consultar la api, pasarla a formato "json" e imprimir los títulos junto a un indice.
# [importante] Esta función devuelve la consulta de la API convertida en formato "json".
def check_films():
    data_films = requests.get(URL_FILMS)
    data_films = data_films.json()
    for i in range(0, len(data_films)):
        print(i, data_films[i]["title"])
    return data_films

# Creando función para mostrar la información de la película elegida a través de un indice (choice)
def choice_film(choice):
    code = data_films[choice]["id"]
    url_choice = f"{URL_FILMS}/{code}"
    data_choice = requests.get(url_choice)
    data_choice = data_choice.json()

    print(LOGO)
    print("Titulo: ", data_choice["title"])
    print("Titulo Original: ", data_choice["original_title"])
    print("Titulo Original en alfabeto occidental: ", data_choice["original_title_romanised"])
    print("Director: ", data_choice["director"])
    print("Productor: ", data_choice["producer"])
    print("Fecha de realización: ", data_choice["release_date"])
    print("Duración: ", data_choice["running_time"], "min")
    print("Puntaje: ", data_choice["rt_score"])
    print("Descripción: ", data_choice["description"])

# Definiendo el orden de las funciones a ejecutar.
while True:
    cleanscreen()
    print(LOGO)
    print(INFO)
    data_films = check_films()
    choice = input("\n[?] Ingrese el indice que desea abrir: ")
    # Sí la entrada es "Exit" finaliza el script
    if choice == "exit":
        break
    # Si la entrada es numérica, convierte el valor a un número entero y continúa con el script.
    elif choice.isnumeric():
        choice = int(choice)
    # Sí la entrada es un carácter no numérico, muestra un error en pantalla y finaliza el script.
    else:
        print("[!] Error, ingrese solo números.")
        break
    
    cleanscreen()
    choice_film(choice)
    print()
    input('[!] Pulse "Enter" para volver al menú principal.')

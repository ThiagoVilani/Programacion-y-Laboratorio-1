import json

#1 - Listar los personajes ordenados por altura
#2 - Mostrar el personaje mas alto de cada genero
#3 - Ordenar los personajes por peso
#4 - Armar un buscador de personajes 
#5 - Exportar lista personajes a CSV
#6 - Salir

ruta = r"C:\Users\vilan\OneDrive\Escritorio\Programación & Laboratorio I\Programacion-y-Laboratorio-1\Parcial-Lambda\data.json"

def cargar_json(ruta:str):
    """
    Se encarga de cargar el archivo .json desde el exterior\n
    Como parametro espera recibir la ruta del archivo en formato string\n
    Retorna la lista contenida dentro del archivo
    """
    with open(ruta) as file:
        data = json.load(file)
    return data["results"]

lista_personajes = cargar_json(ruta).copy()

#:::::::::::::::::::ORDENAR LA LISTA POR ALTURA:::::::::::::::::::::
def ordenar_lista_altura(lista:list):
    def pasar_int(personaje):
        personaje["height"] = int(personaje["height"])
        return personaje
    lista_personajes_copia = list(map(pasar_int, lista))
    def pasar_altura(personaje):
        return personaje["height"]
    lista_personajes_copia.sort(key = pasar_altura)
    return lista_personajes_copia
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


#:::::::::::::::::PERSONAJES MAS ALTOS SEGUN GENERO::::::::::::::::::
lista_masculinos = list(filter(lambda personaje : personaje["gender"] == "male", lista_personajes))
lista_femeninos = list(filter(lambda personaje : personaje["gender"] == "female", lista_personajes))
lista_na = list(filter(lambda personaje : personaje["gender"] == "n/a", lista_personajes))

def pasar_altura(personaje):
    return personaje["height"]

mensaje_altos = "El hombre mas alto es {0}\nLa mujer mas alta es {1}\nEl nada mas alto es {2}".format(
    (max(lista_masculinos, key = pasar_altura)["name"]), 
    (max(lista_femeninos, key = pasar_altura)["name"]), 
    (max(lista_na, key = pasar_altura)["name"]))
print(mensaje_altos) 
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


#:::::::::::::::::::::::::ORDENAR POR PESO::::::::::::::::::::::::::

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
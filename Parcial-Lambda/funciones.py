import json

#1 - Listar los personajes ordenados por altura
#2 - Mostrar el personaje mas alto de cada genero
#3 - Ordenar los personajes por peso
#4 - Armar un buscador de personajes 
#5 - Exportar lista personajes a CSV
#6 - Salir

ruta = r"C:\Users\vilan\Desktop\Programación & Laboratorio I\Programacion-y-Laboratorio-1\Parcial-Lambda\data.json"

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
def pasar_int(personaje):
    personaje["height"] = int(personaje["height"])
    return personaje
lista_personajes_copia = list(map(pasar_int, lista_personajes))
def pasar_altura(personaje):
    return personaje["height"]
lista_personajes_copia.sort(key = pasar_altura)
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

#:::::::::::::
lista_masculinos = list(filter(lambda personaje : personaje["gender"] == "male", lista_personajes))
lista_femeninos = list(filter(lambda personaje : personaje["gender"] == "female", lista_personajes))
lista_na = list(filter(lambda personaje : personaje["gender"] == "n/a", lista_personajes))

def pasar_altura_masculino(personaje):
    return personaje["height"]
    
def pasar_altura_femenino(personaje):
    return personaje["height"]

def pasar_na(personaje):
    return personaje["height"]

lista_masculinos.sort(key = pasar_altura_masculino)
lista_femeninos.sort(key = pasar_altura_femenino)
lista_na.sort(key = pasar_na)
print("El hombre mas alto es {}".format(lista_masculinos[-1]))
print("La mujer mas alta es {}".format(lista_femeninos[-1]))
print("El nada mas alto es {}".format(lista_na[-1]))


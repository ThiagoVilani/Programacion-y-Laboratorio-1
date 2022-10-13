from data import lista_personajes

#------------------CORRIGIENDO TIPOS DE DATOS------------------
def Stark_normalizar_datos(lista:list):
    """
    Compruebo si los datos numericos estan en el tipo correcto
    
    lista: Espera un dato de tipo list y no debe esta vacia

    return: Se retornara un mensaje en caso de que la lista este vacia
            o que algun dato sea normalizado
    """
    if lista==[]:
        mensaje=print("Error, la lista esta vacia")
        return (mensaje)
    mensaje=False
    for personaje in lista_personajes:
        if lista_personajes[0]["altura"]!=type(1.0):
            personaje["altura"]=float(personaje["altura"])
            mensaje=True
        if lista_personajes[0]["peso"]!=type(1.0):
            personaje["peso"]=float(personaje["peso"])
            mensaje=True
        if lista_personajes[0]["fuerza"]!=type(1):
            personaje["fuerza"]=int(personaje["fuerza"])
            mensaje=True
    if mensaje==True:
        mensaje=print("Datos normalizados")
    return mensaje

#--------------------------------------------------------------

#-----------------NOMBRE-------------------------------------

def Obtener_nombre(diccionario:dict):
  """
  Espera el ingreso de un dato de tipo diccionario y 
  que no debe estar vacio

  Comprueba que los parametros se cumplan

  Retorna un mensaje de tipo string anunciando el nombre
  encontrado dentro del diccionario  
  """
  if diccionario == {}:
    return "Error, el diccionario esta vacio"
  mensaje = "Nombre: {0}".format(diccionario["nombre"])
  return mensaje


def Imprimir_dato(texto:str):
    """
    Recibe un dato de tipo string y lo imprime
    """
    print(texto)


def Stark_imprimir_nombres_heroes(lista:list):
    """
    Espera recibir un dato de tipo lista que no este vacia
    
    Recorre la lista e imprime el nombre de cada heroe
    """
    if lista == []:
        mensaje = print(-1)
        return mensaje
    for i in range(len(lista_personajes)):
        Imprimir_dato(lista_personajes[i]["nombre"])


def Obtener_nombre_y_dato(diccionario:dict, clave:str):

    mensaje = print("Nombre: {0} | {1}: algo".format(diccionario["nombre"], diccionario[clave]))



Stark_normalizar_datos(lista_personajes)
print(Obtener_nombre(lista_personajes[0]))
Stark_imprimir_nombres_heroes(lista_personajes)

Obtener_nombre_y_dato(lista_personajes[2], "fuerza")
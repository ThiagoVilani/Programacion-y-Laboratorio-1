import json
import re

def Leer_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        data = json.load(archivo)
    return data

data_stark_json = r"C:\Users\vilan\OneDrive\Escritorio\Programación & Laboratorio I\Clase 8\data_stark.json"

data_dic = Leer_archivo(data_stark_json)


opciones = """ 
"\n A - Nombres de los heroes masculinos\n"
" B - Nombres de las heroinas\n"
" C - Altura del masculino mas alto\n"
" D - Altura del femenino mas alto\n"
" E - Altura del masculino mas bajo\n"
" F - Altura del femenino mas bajo\n"
" G - Promedio de las alturas de los masculinos\n"
" H - Promedio de las altura de los femeninos\n"
" I - Asignacion de nombre a los puntos del 3 al 6\n"
" J - Cantidad de heroes por cada color de ojos\n"
" K - Cantidad de heroes por cada color de pelo\n"
" L - Cantidad de heroes por cada tipo de inteligencia\n"
" M - Agrupacion de heroes por color de ojos\n"
" N - Agrupacion de heroes por color de pelo\n"
" O - Agrupacion de heroes por tipo de inteligencia\n\n"
"""
#--------------SELECCIONO NOMBRES MASCULINOS--------------

def Calcular_nombre_masculinos():
  dic_personaje=data_dic[0]

  for personaje in data_dic:
    if personaje["genero"]=="M":
      dic_personaje=personaje
      print(dic_personaje["nombre"])

#----------------------------------------------------------

#--------------SELECCIONO NOMBRES FEMENINOS--------------
def Calcular_nombre_femeninos():
  dic_personaje=data_dic[0]

  for personaje in data_dic:
    if personaje["genero"]=="F":
      dic_personaje=personaje
      print(dic_personaje["nombre"])

#---------------------------------------------------------

#--------------CALCULO MASCULINO MAS ALTO--------------
def Calcular_masculino_mas_alto():
  flag_masculino_mas_alto=0

  for personaje in data_dic:
    if personaje["genero"]=="M":
      personaje["altura"]=float(personaje["altura"])
      if (flag_masculino_mas_alto==0):
        dic_personaje=personaje
        flag_masculino_mas_alto=1
      else:
        if personaje["altura"]>dic_personaje["altura"]:
          dic_personaje=personaje        
      
  print("Altura:{0}".format(dic_personaje["altura"]))
  return("Nombre:{0}\n".format(dic_personaje["nombre"]))

#-------------------------------------------------------

#--------------CALCULO FEMENINO MAS ALTO--------------

def Calcular_femenino_mas_alto():
  flag_femenino_mas_alto=0

  for personaje in data_dic["heroes"]:
    if personaje["genero"] == "F":
      personaje["altura"]=float(personaje["altura"])
      if (flag_femenino_mas_alto==0):
        dic_personaje=personaje
        flag_femenino_mas_alto=1
      else:
        if personaje["altura"]>dic_personaje["altura"]:
          dic_personaje=personaje        
      
  print("Altura:{0}".format(dic_personaje["altura"]))
  return("Nombre:{0}\n".format(dic_personaje["nombre"]))

#-----------------------------------------------------

#--------------CALCULO MASCULINO MAS BAJO--------------

def Calcular_masculino_mas_bajo():
  flag_masculino_mas_bajo=0

  for personaje in data_dic:
    if personaje["genero"]=="M":
      personaje["altura"]=float(personaje["altura"])
      if (flag_masculino_mas_bajo==0):
        dic_personaje=personaje
        flag_masculino_mas_bajo=1
      else:
        if personaje["altura"]<dic_personaje["altura"]:
          dic_personaje=personaje        
      
  print("Altura:{0}".format(dic_personaje["altura"]))
  return("Nombre:{0}\n".format(dic_personaje["nombre"]))

#------------------------------------------------------

#--------------CALCULO FEMENINO MAS BAJO--------------

def Calcular_femenino_mas_bajo():
  flag_femenino_mas_bajo=0

  for personaje in data_dic:
    if personaje["genero"]=="F":
      personaje["altura"]=float(personaje["altura"])
      if (flag_femenino_mas_bajo==0):
        dic_personaje=personaje
        flag_femenino_mas_bajo=1
      else:
        if personaje["altura"]<dic_personaje["altura"]:
          dic_personaje=personaje        
      
  print("Altura:{0}".format(dic_personaje["altura"]))
  return("Nombre:{0}\n".format(dic_personaje["nombre"]))
#--------------------------------------------------------


#----------CALCULAR PROMEDIO ALTURAS MASCULINOS----------

def Calcular_promedio_alturas_masculinos():
  suma_alturas_masculinos=0
  cantidad_masculinos=0

  for personaje in data_dic:
    if personaje["genero"]=="M":
      personaje["altura"]=float(personaje["altura"])
      suma_alturas_masculinos+=personaje["altura"]
      cantidad_masculinos+=1
  
  print(suma_alturas_masculinos/cantidad_masculinos)

#----------------------------------------------------------

#----------CALCULAR PROMEDIO ALTURAS FEMENINOS----------

def Calcular_promedio_alturas_femeninos():
  suma_alturas_femeninos=0
  cantidad_femeninos=0

  for personaje in data_dic:
    if personaje["genero"]=="F":
      personaje["altura"]=float(personaje["altura"])
      suma_alturas_femeninos+=personaje["altura"]
      cantidad_femeninos+=1
  
  print(suma_alturas_femeninos/cantidad_femeninos)

#----------------------------------------------------------

#--------ASIGNO LOS NOMBRES A LOS ANTERIORES PUNTOS--------
def Asignacion_nombres():

  print(Calcular_masculino_mas_alto())
  print(Calcular_femenino_mas_alto())
  print(Calcular_femenino_mas_bajo())
  print(Calcular_masculino_mas_bajo())

#------------CANTIDAD HEROES POR COLOR OJOS-----------------

def Cantidad_heroes_por_tipo_color_ojos():
  cant_heroes_por_color={}
  for personaje in data_dic:
    cant_heroes_por_color[personaje["color_ojos"]]=0

  for personaje in data_dic:
    cant_heroes_por_color[personaje["color_ojos"]]+=1
  
  print(cant_heroes_por_color)

#------------------------------------------------------------

#------------CANTIDAD HEROES POR COLOR PELO-----------------

def Cantidad_heroes_por_tipo_color_pelo():
  cant_heroes_por_color_pelo={}
  for personaje in data_dic:
    cant_heroes_por_color_pelo[personaje["color_pelo"]]=0

  for personaje in data_dic:
    cant_heroes_por_color_pelo[personaje["color_pelo"]]+=1
  
  print(cant_heroes_por_color_pelo)

#------------------------------------------------------------

#------------CANTIDAD HEROES POR TIPO INTELIGENCIA-----------------

def Cantidad_heroes_por_tipo_inteligencia():
  cant_heroes_por_inteligencia={}
  for personaje in data_dic:
    cant_heroes_por_inteligencia[personaje["inteligencia"]]=0
   # if personaje["inteligencia"]=="":
    #  cant_heroes_por_inteligencia["No tiene"]=cant_heroes_por_inteligencia["inteligencia"]

  for personaje in data_dic:
    try:
      cant_heroes_por_inteligencia[personaje["inteligencia"]]+=1
    except:
      pass
  
  print(cant_heroes_por_inteligencia)

#------------------------------------------------------------

#---------------AGRUPAR SUPERS EN CADA COLOR DE OJO----------

def Agrupar_heroes_color_ojos():
  colores_ojos=set()
  dic_ojos_heroes={}

  for personaje in data_dic:
    colores_ojos.add(personaje["color_ojos"])
  for color in colores_ojos:  
    list_heroe_color=[]
    for personaje in data_dic:
      if personaje["color_ojos"]==color:
        list_heroe_color.append(personaje["nombre"])
    dic_ojos_heroes[color]=list_heroe_color
      
  print(dic_ojos_heroes)

#------------------------------------------------------------

#---------------AGRUPAR SUPERS EN CADA COLOR DE PELO----------

def Agrupar_heroes_color_pelo():
  colores_pelo=set()
  dic_pelo_heroes={}

  for personaje in data_dic:
    colores_pelo.add(personaje["color_pelo"])
  for color in colores_pelo:  
    list_heroe_color=[]
    for personaje in data_dic:
      if personaje["color_pelo"]==color:
        list_heroe_color.append(personaje["nombre"])
    dic_pelo_heroes[color]=list_heroe_color
      
  print(dic_pelo_heroes)

#------------------------------------------------------------

#---------------AGRUPAR SUPERS EN CADA TIPO INTELIGENCIA----------

def Agrupar_heroes_tipo_inteligencia():
  tipos_inteligencia=set()
  dic_inteligencia_heroes={}

  for personaje in data_dic:
    tipos_inteligencia.add(personaje["inteligencia"])
  for tipo in tipos_inteligencia:  
    list_heroe_inteligencia=[]
    for personaje in data_dic:
      if personaje["inteligencia"]==tipo:
        list_heroe_inteligencia.append(personaje["nombre"])
    dic_inteligencia_heroes[tipo]=list_heroe_inteligencia
      
  print(dic_inteligencia_heroes)

#------------------------------------------------------------


#------------------------------------------------------------
def Imprimir_dato(texto:str):
    """
    Recibe un dato de tipo string y lo imprime
    """
    print(texto)
#------------------------------------------------------------


#------------------------------------------------------------
def Imprimir_menu_desafio_5(opciones):
    Imprimir_dato(opciones)
#------------------------------------------------------------


#------------------------------------------------------------
def Stark_menu_principal_desafio_5(lista:str):
    Imprimir_menu_desafio_5(lista)
    eleccion_usuario = input("Elija la letra de la opcion que desea saber")
    if re.search("[a-ozA-OZ]", eleccion_usuario) == None:
        return -1
    return eleccion_usuario
#------------------------------------------------------------


#------------------------------------------------------------
def Stark_marvel_app_5(lista:list):
    while True:
        eleccion_usuario = Stark_menu_principal_desafio_5(opciones).upper()
        
        if (eleccion_usuario=="A"):
            Calcular_nombre_masculinos()
        elif (eleccion_usuario=="B"):
            Calcular_nombre_femeninos()
        elif (eleccion_usuario=="C"):
            Calcular_masculino_mas_alto()
        elif (eleccion_usuario=="D"):
            Calcular_femenino_mas_alto()
        elif (eleccion_usuario=="E"):
            Calcular_masculino_mas_bajo()
        elif(eleccion_usuario=="F"):
            Calcular_femenino_mas_bajo()
        elif(eleccion_usuario=="G"):      
            Calcular_promedio_alturas_masculinos()
        elif(eleccion_usuario=="H"):
            Calcular_promedio_alturas_femeninos()        
        elif(eleccion_usuario=="I"):
            Asignacion_nombres()        
        elif(eleccion_usuario=="J"):
            Cantidad_heroes_por_tipo_color_ojos()        
        elif(eleccion_usuario=="K"):
            Cantidad_heroes_por_tipo_color_pelo()        
        elif(eleccion_usuario=="L"):
            Cantidad_heroes_por_tipo_inteligencia()
        elif(eleccion_usuario=="M"):
            Agrupar_heroes_color_ojos()
        elif(eleccion_usuario=="N"):
            Agrupar_heroes_color_pelo()
        elif(eleccion_usuario=="O"):
            Agrupar_heroes_tipo_inteligencia()



        eleccion_usuario=input("\nQuiere continuar\n"
                                " 1 - Continuar\n"
                                " 2 - Salir\n")
        if (eleccion_usuario=="1"):
            continue
        else:
            break
#------------------------------------------------------------


#------------------------------------------------------------
def leer_archivo(nombre_archivo:str):
    with open(nombre_archivo, "r") as archivo:
        dic_heroes = json.load(archivo)
        dic_heroes = dic_heroes["heroes"]
    return dic_heroes
#------------------------------------------------------------

#print(leer_archivo(data_stark_json))



lista = [1, 2,3 ,4,1, 5,6,2,87,3,98,2,53,612,8,2,87,3,98,2,53,612,8]
contador_vueltas = 0
posicion = 0
while contador_vueltas<13:
    contador_vueltas +=1
    for i in range(len(lista) - contador_vueltas):
        if lista[i] < lista[i+1]:#swap de posiciones
            lista[i], lista[i+1] = lista[i], lista[i+1] 
print(lista)
            
        
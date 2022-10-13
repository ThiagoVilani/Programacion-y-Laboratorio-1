from data import lista_personajes

#--------------SELECCIONO NOMBRES MASCULINOS--------------

def Calcular_nombre_masculinos():
  dic_personaje=lista_personajes[0]

  for personaje in lista_personajes:
    if personaje["genero"]=="M":
      dic_personaje=personaje
      print(dic_personaje["nombre"])

#----------------------------------------------------------

#--------------SELECCIONO NOMBRES FEMENINOS--------------
def Calcular_nombre_femeninos():
  dic_personaje=lista_personajes[0]

  for personaje in lista_personajes:
    if personaje["genero"]=="F":
      dic_personaje=personaje
      print(dic_personaje["nombre"])

#---------------------------------------------------------

#--------------CALCULO MASCULINO MAS ALTO--------------
def Calcular_masculino_mas_alto():
  flag_masculino_mas_alto=0

  for personaje in lista_personajes:
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

  for personaje in lista_personajes:
    if personaje["genero"]=="F":
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

  for personaje in lista_personajes:
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

  for personaje in lista_personajes:
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

  for personaje in lista_personajes:
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

  for personaje in lista_personajes:
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
  for personaje in lista_personajes:
    cant_heroes_por_color[personaje["color_ojos"]]=0

  for personaje in lista_personajes:
    cant_heroes_por_color[personaje["color_ojos"]]+=1
  
  print(cant_heroes_por_color)

#------------------------------------------------------------

#------------CANTIDAD HEROES POR COLOR PELO-----------------

def Cantidad_heroes_por_tipo_color_pelo():
  cant_heroes_por_color_pelo={}
  for personaje in lista_personajes:
    cant_heroes_por_color_pelo[personaje["color_pelo"]]=0

  for personaje in lista_personajes:
    cant_heroes_por_color_pelo[personaje["color_pelo"]]+=1
  
  print(cant_heroes_por_color_pelo)

#------------------------------------------------------------

#------------CANTIDAD HEROES POR TIPO INTELIGENCIA-----------------

def Cantidad_heroes_por_tipo_inteligencia():
  cant_heroes_por_inteligencia={}
  for personaje in lista_personajes:
    cant_heroes_por_inteligencia[personaje["inteligencia"]]=0
   # if personaje["inteligencia"]=="":
    #  cant_heroes_por_inteligencia["No tiene"]=cant_heroes_por_inteligencia["inteligencia"]

  for personaje in lista_personajes:
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

  for personaje in lista_personajes:
    colores_ojos.add(personaje["color_ojos"])
  for color in colores_ojos:  
    list_heroe_color=[]
    for personaje in lista_personajes:
      if personaje["color_ojos"]==color:
        list_heroe_color.append(personaje["nombre"])
    dic_ojos_heroes[color]=list_heroe_color
      
  print(dic_ojos_heroes)

#------------------------------------------------------------

#---------------AGRUPAR SUPERS EN CADA COLOR DE PELO----------

def Agrupar_heroes_color_pelo():
  colores_pelo=set()
  dic_pelo_heroes={}

  for personaje in lista_personajes:
    colores_pelo.add(personaje["color_pelo"])
  for color in colores_pelo:  
    list_heroe_color=[]
    for personaje in lista_personajes:
      if personaje["color_pelo"]==color:
        list_heroe_color.append(personaje["nombre"])
    dic_pelo_heroes[color]=list_heroe_color
      
  print(dic_pelo_heroes)

#------------------------------------------------------------

#---------------AGRUPAR SUPERS EN CADA TIPO INTELIGENCIA----------

def Agrupar_heroes_tipo_inteligencia():
  tipos_inteligencia=set()
  dic_inteligencia_heroes={}

  for personaje in lista_personajes:
    tipos_inteligencia.add(personaje["inteligencia"])
  for tipo in tipos_inteligencia:  
    list_heroe_inteligencia=[]
    for personaje in lista_personajes:
      if personaje["inteligencia"]==tipo:
        list_heroe_inteligencia.append(personaje["nombre"])
    dic_inteligencia_heroes[tipo]=list_heroe_inteligencia
      
  print(dic_inteligencia_heroes)

#------------------------------------------------------------

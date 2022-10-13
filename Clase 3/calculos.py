from data import lista_personajes

#Thiago Vilani

#--------------CALCULO PERSONAJE MAS ALTO--------------------
def calcular_personaje_mas_alto():
  dic_personaje=lista_personajes[0]

  for personaje in lista_personajes:
    personaje["altura"]=float(personaje["altura"])
    if personaje["altura"]>dic_personaje["altura"]:
      dic_personaje=personaje
      
  print(dic_personaje["nombre"], dic_personaje["altura"])
#-------------------------------------------------------------

#--------------CALCULO PERSONAJE MAS BAJO--------------------
def calcular_personaje_mas_bajo():
  dic_personaje=lista_personajes[0]

  for personaje in lista_personajes:
    personaje["altura"]=float(personaje["altura"])
    if personaje["altura"]<dic_personaje["altura"]:
      dic_personaje=personaje
      
  print(dic_personaje["nombre"], dic_personaje["altura"])
#-------------------------------------------------------------

#--------------CALCULO PROMEDIO DE ALTURA--------------------
def calcular_promedio_altura():
  dic_personaje=lista_personajes[0]
  suma_alturas=0

  for personaje in lista_personajes:
    personaje["altura"]=float(personaje["altura"])
    suma_alturas+=personaje["altura"]
    
  print(suma_alturas/len(lista_personajes))
#-------------------------------------------------------------

#--------------CALCULO PERSONAJE MAS PESADO--------------------
def calcular_personaje_mas_pesado():
  dic_personaje=lista_personajes[0]

  for personaje in lista_personajes:
    personaje["peso"]=float(personaje["peso"])
    if personaje["peso"]>dic_personaje["peso"]:
      dic_personaje=personaje
      
  print(dic_personaje["nombre"], dic_personaje["peso"])
#-------------------------------------------------------------

#--------------CALCULO PERSONAJE MENOS PESADO--------------------
def calcular_personaje_menos_pesado():
  dic_personaje=lista_personajes[0]

  for personaje in lista_personajes:
    personaje["peso"]=float(personaje["peso"])
    if personaje["peso"]<dic_personaje["peso"]:
      dic_personaje=personaje
      
  print(dic_personaje["nombre"], dic_personaje["peso"])
#-------------------------------------------------------------
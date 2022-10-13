import calculos
from data import lista_personajes

#Thiago Vilani

while True:
  eleccion_usuario=input("\n\nQue desea saber? Ingrese el numero de la opcion\n"
                          " 1 - Personaje mas alto\n"
                          " 2 - Personaje mas bajo\n"
                          " 3 - Promedio de altura de los superheroes\n"
                          " 4 - Personaje mas pesado\n"
                          " 5 - Personaje menos pesado\n\n"
                          "==>")

  if (eleccion_usuario=="1"):
      calculos.calcular_personaje_mas_alto()
  else:
    if (eleccion_usuario=="2"):
      calculos.calcular_personaje_mas_bajo()
    else:
      if (eleccion_usuario=="3"):
        calculos.calcular_promedio_altura()
      else:
        if (eleccion_usuario=="4"):
          calculos.calcular_personaje_mas_pesado()
        else:
          if (eleccion_usuario=="5"):
            calculos.calcular_personaje_menos_pesado()
          else:
            if(eleccion_usuario=="6"):
              break

  eleccion_usuario=input("\nQuiere continuar\n"
                          " 1 - Continuar\n"
                          " 2 - Salir\n")
  if (eleccion_usuario=="1"):
    continue
  else:
    break
    

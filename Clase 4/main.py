import calculos

while True:
  eleccion_usuario=input("\n\nQue desea saber? Ingrese el numero de la opcion\n"
                          " 1 - Nombres de los heroes masculinos\n"
                          " 2 - Nombres de las heroinas\n"
                          " 3 - Altura del masculino mas alto\n"
                          " 4 - Altura del femenino mas alto\n"
                          " 5 - Altura del masculino mas bajo\n"
                          " 6 - Altura del femenino mas bajo\n"
                          " 7 - Promedio de las alturas de los masculinos\n"
                          " 8 - Promedio de las altura de los femeninos\n"
                          " 9 - Asignacion de nombre a los puntos del 3 al 6\n"
                          " 10 - Cantidad de heroes por cada color de ojos\n"
                          " 11 - Cantidad de heroes por cada color de pelo\n"
                          " 12 - Cantidad de heroes por cada tipo de inteligencia\n"
                          " 13 - Agrupacion de heroes por color de ojos\n"
                          " 14 - Agrupacion de heroes por color de pelo\n"
                          " 15 - Agrupacion de heroes por tipo de inteligencia\n\n"
                          "==>")

  if (eleccion_usuario=="1"):
        calculos.Calcular_nombre_masculinos()
  elif (eleccion_usuario=="2"):
        calculos.Calcular_nombre_femeninos()
  elif (eleccion_usuario=="3"):
        calculos.Calcular_masculino_mas_alto()
  elif (eleccion_usuario=="4"):
        calculos.Calcular_femenino_mas_alto()
  elif (eleccion_usuario=="5"):
        calculos.Calcular_masculino_mas_bajo()
  elif(eleccion_usuario=="6"):
        calculos.Calcular_femenino_mas_bajo()
  elif(eleccion_usuario=="7"):      
        calculos.Calcular_promedio_alturas_masculinos()
  elif(eleccion_usuario=="8"):
        calculos.Calcular_promedio_alturas_femeninos()        
  elif(eleccion_usuario=="9"):
        calculos.Asignacion_nombres()        
  elif(eleccion_usuario=="10"):
        calculos.Cantidad_heroes_por_tipo_color_ojos()        
  elif(eleccion_usuario=="11"):
        calculos.Cantidad_heroes_por_tipo_color_pelo()        
  elif(eleccion_usuario=="12"):
        calculos.Cantidad_heroes_por_tipo_inteligencia()
  elif(eleccion_usuario=="13"):
        calculos.Agrupar_heroes_color_ojos()
  elif(eleccion_usuario=="14"):
        calculos.Agrupar_heroes_color_pelo()
  elif(eleccion_usuario=="15"):
        calculos.Agrupar_heroes_tipo_inteligencia()
                
              

  eleccion_usuario=input("\nQuiere continuar\n"
                          " 1 - Continuar\n"
                          " 2 - Salir\n")
  if (eleccion_usuario=="1"):
    continue
  else:
    break
from data import lista_personajes
import re


#------------------------------------------------------------
def Extraer_iniciales(nombre_heroe:str):
    if nombre_heroe == "":
        mensaje = print("N/A")
    nombre_heroe = nombre_heroe.replace("the", "")
    nombre_heroe = nombre_heroe.replace("-", "")
    lista_nombre = nombre_heroe.split(" ")
    i=0
    iniciales = ""
    for palabra in lista_nombre:
        if lista_nombre[i] == "":
            lista_nombre.pop(i)
        lista_nombre[i] = lista_nombre[i][:1]
        iniciales = iniciales + "{0}.".format(lista_nombre[i])
        i+=1
    mensaje = iniciales
    return mensaje
#------------------------------------------------------------


#------------------------------------------------------------
def Definir_iniciales_nombre(heroe:dict):
    if type(heroe) != type({}) or heroe.get("nombre") == None:
        return False
    heroe["iniciales"] = Extraer_iniciales(heroe["nombre"])
    return True
#------------------------------------------------------------


#--------------------------------------------------------------
def Agregar_iniciales_nombre(lista:list):
    if type(lista) != type([]) or len(lista)<1:
        return False
    for heroe in lista:
        try:
            Definir_iniciales_nombre(heroe)
        except:
            print("El origen de datos no contiene el formato correcto")
            return False
    return True
#--------------------------------------------------------------


#--------------------------------------------------------------
def Stark_imprimir_nombres_con_iniciales(lista:list):
    if type(lista) != type([]) or len(lista)<1:
        return False
    Agregar_iniciales_nombre(lista)
    for heroe in lista:
        impresion = "*{0} ({1})".format(heroe["nombre"], heroe["iniciales"])
        print(impresion)
#--------------------------------------------------------------

#|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

#--------------------------------------------------------------
def Generar_codigo_heroe(id_heroe:int, genero_heroe:str):
    genero_heroe.upper()
    if type(id_heroe) != type(2) and genero_heroe != "F" and genero_heroe != "M" and genero_heroe != "NB":
        return "N/A" 
    impresion = "{0}-{1}".format(genero_heroe, id_heroe)
    id_heroe = str(id_heroe)
    ceros = 9 - len(genero_heroe)
    impresion = "{0}-{1}".format(genero_heroe, id_heroe.zfill(ceros))
    return impresion
#--------------------------------------------------------------


#--------------------------------------------------------------
def Agregar_codigo_heroe(heroe:dict, id_heroe:int):
    codigo = Generar_codigo_heroe(id_heroe, heroe["genero"] ) 
    if len(heroe) == 0 or len(codigo) != 10:
        return False
    heroe["codigo_heroe"] = codigo 
    return True
#--------------------------------------------------------------


#--------------------------------------------------------------
def Stark_generar_codigos_heroes(lista:list, imprimir=True):
    numero = 0
    for heroe in lista:
        if len(heroe) == 0 or type(heroe) != type({}) or heroe.get("genero") == None:
            mensaje = print("El origen de datos no contiene el formato correcto")
            return mensaje
        numero += 1
        Agregar_codigo_heroe(heroe, numero)
    if imprimir == True:
        print("Se asignaron {0} codigos\n"
            "El codigo del primer heroe es: {1}\n"
            "El codigo del ultimo heroe es: {2}".format(numero, 
                                                    lista_personajes[0]["codigo_heroe"], 
                                                    lista_personajes[-1]["codigo_heroe"]))
#--------------------------------------------------------------

#|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

#--------------------------------------------------------------
def Sanitizar_entero(numero_str:str):
    numero_str = numero_str.replace(" ", "")
    try: 
        numero_str = int(numero_str)
        if numero_str < 1:
            return -2
        else:
            return numero_str
    except:
        numero_str = re.findall("[a-z]+", numero_str)
        if numero_str == []:
            return -3
        else:
            return -1
#--------------------------------------------------------------


#--------------------------------------------------------------
def Sanitizar_float(numero_str:str):
    numero_str = numero_str.replace(" ", "")
    try: 
        numero_str = float(numero_str)
        if numero_str < 1:
            return -2
        else:
            return numero_str
            
    except:
        numero_str = re.findall("[a-z]+", numero_str)
        if numero_str == []:
            return -3
        else:
            return -1
#--------------------------------------------------------------


#--------------------------------------------------------------
def Sanitizar_string(valor_str:str, valor_por_defecto:str):
    try: 
        re.findall("[a-zA-Z0-9]+")
    except:
        return valor_por_defecto
    string = re.split(" ", valor_str)
    string_terminada = ""
    for palabra in string:
        if re.findall("[0-9]+", palabra) != []:
            return "N/A"
        else:
            palabra = re.sub("[/]+", " ", palabra)
            string_terminada = "{0} {1}".format(string_terminada, palabra)
    string_terminada = re.sub(r'\s+', ' ', string_terminada)
    string_terminada = string_terminada.strip()
    string_terminada = string_terminada.lower()
    print(string_terminada)
    return string_terminada
#--------------------------------------------------------------


#--------------------------------------------------------------

#|||||||||||NO ENTIENDO QUE HAY QUE HACER EN ESTE PUNTO|||||||||||

def Sanitizar_dato(heroe:dict, clave:str, tipo_dato):
    tipo_dato = tipo_dato.lower()
    funcion_cadena = Sanitizar_string(tipo_dato, "-")
    if Sanitizar_entero(tipo_dato) < 0 or Sanitizar_float(tipo_dato) < 0 or funcion_cadena != "N/A" or funcion_cadena != "-":
        resultado = print("Tipo de dato no reconocido")
        return resultado
    if heroe.get(clave) == None:
        resultado = print("La clave especificada no existe en el heroe")
        return resultado
    if clave == heroe[clave] and tipo_dato == heroe[clave][tipo_dato]:
        print(heroe)
    return resultado    
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

#--------------------------------------------------------------


#--------------------------------------------------------------
def Stark_normalizar_datos():
    print("hay que terminar la de arriba") 
#--------------------------------------------------------------

#|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

#--------------------------------------------------------------
def Generar_indice_nombres(lista:list):
    mensaje = print("El origen de datos no contiene el formato correcto")
    if len(lista) < 1:
        return mensaje

    indice = []
    nombre_dividido = []
    for diccionario in lista:
        if type(diccionario) != type({}):
            return mensaje
        else:
            if diccionario.get("nombre") == None:
                return mensaje
        nombre_dividido = (re.split(" ", diccionario["nombre"]))
        for palabra in nombre_dividido:
            indice.append(palabra)
    return indice

#--------------------------------------------------------------


#--------------------------------------------------------------
def Stark_imprimir_indice_nombre(lista:list):
    lista_nombres = Generar_indice_nombres(lista)
    lista_imprimir = ""
    for palabra in lista_nombres:
        lista_imprimir = "{0}-{1}".format(lista_imprimir, palabra)
    lista_imprimir = lista_imprimir[1:]
    print(lista_imprimir)
#--------------------------------------------------------------

#|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|

#--------------------------------------------------------------
      
       #ACA TAMPOCO ENTIENDO MUY BIEN QUE HAY QUE HACER
       
#def Convertir_cm_a_mtrs(valor_cm):
#    valor_cm = Sanitizar_float(valor_cm)
#    if valor_cm == -1 or valor_cm == -2 or valor_cm == -3:
#        return -1
#    
#    if valor_cm > 100:
#        valor_cm = str(valor_cm)
#        valor_mts = re.split("", valor_cm)
#        print(valor_mts)
#--------------------------------------------------------------
#--------------------------------------------------------------
#def Convertir_cm_a_mtrs(valor_cm):
#    numeros = []
#    if type(valor_cm) == type(1.2) and valor_cm > 0:
#        if valor_cm > 99:
#            valor_cm = re.split("", valor_cm)
#            print(valor_cm)
#            valor_retorno = 1
#    else: 
#        valor_retorno = -1
#    return valor_retorno
#--------------------------------------------------------------


#--------------------------------------------------------------
def Generar_separador(patron:str, largo:int, imprimir=True):
    if len(patron) < 1 or len(patron) > 2:
        return "N/A"
    if largo < 1 or largo > 235:
        return "N/A"
    
    string_patron = ""
    for i in range(largo):
        string_patron = "{0}{1}".format(string_patron, patron)
    if imprimir == True:
        print(string_patron)
#--------------------------------------------------------------


#--------------------------------------------------------------
def Generar_encabezado(titulo:str):
    titulo = titulo.upper()
    titulo_estilizado = "{0}\n{1}\n{2}".format(("*")*60, titulo, ("*")*60)
    print(titulo_estilizado)
#--------------------------------------------------------------


#--------------------------------------------------------------
def Imprimir_ficha_heroe(heroe:dict):
    Agregar_iniciales_nombre(lista_personajes)
    Stark_generar_codigos_heroes(lista_personajes, False)
    ficha_principal = "\n{0}\nPRINCIPAL\n{0}\n".format(("*")*70) 
    ficha_nombre_heroe = "{0}NOMBRE DEL HÉROE:{1}{2} {3}\n\n".format((" ")*4, (" ")*(25-len("NOMBRE DEL HÉROE")), heroe["nombre"], heroe["iniciales"])
    ficha_identidad_secreta = "{0}IDENTIDAD SECRETA:{1}{2}\n\n".format((" ")*4, (" ")*(25-len("IDENTIDAD SECRETA")), heroe["identidad"])
    ficha_consultora = "{0}CONSULTORA:{1}{2}\n\n".format((" ")*4, (" ")*(25-len("CONSULTORA")), heroe["empresa"])
    ficha_codigo_heroe = "{0}CÓDIGO DE HÉROE: {1}{2}".format((" ")*4, (" ")*(25-len("CÓDIGO DE HÉROE")), heroe["codigo_heroe"])
    ficha_fisico = "\n{0}\nFISICO\n{1}\n".format((" ")*5, ("*")*70)
    ficha_altura = "\n{0}ALTURA:{1}{2} Mtrs.\n".format((" ")*5, (" ")*(25-len("ALTURA")), heroe["altura"])
    ficha_peso = "\n{0}PESO:{1}{2} Kg.\n".format((" ")*5, (" ")*(25-len("PESO")), heroe["peso"])
    ficha_fuerza = "\n{0}FUERZA:{1}{2} N.\n".format((" ")*5, (" ")*(25-len("FUERZA")), heroe["fuerza"])
    ficha_señas_particulares =  "\n{0}\nSEÑAS PARTICULARES\n{0}\n".format(("*")*70)
    ficha_color_ojos = "\n{0}COLOR DE OJOS:{1}{2}\n".format((" ")*5, (" ")*(25-len("COLOR DE OJOS")), heroe["color_ojos"])
    ficha_color_pelo = "\n{0}COLOR DE PELO:{1}{2}\n".format((" ")*5, (" ")*(25-len("COLOR DE PELO")), heroe["color_pelo"])
    print(ficha_principal, ficha_nombre_heroe, ficha_identidad_secreta, 
    ficha_consultora, ficha_codigo_heroe, ficha_fisico,
    ficha_altura, ficha_peso, ficha_fuerza, ficha_señas_particulares, ficha_color_ojos, ficha_color_pelo)
#--------------------------------------------------------------


#--------------------------------------------------------------
def Stark_navegar_fichas(lista:list):
    posicion_lista = 0
    Imprimir_ficha_heroe(lista[posicion_lista])
    while True:
        eleccion_usuario = input("""
                                    A donde desea dirigirse?\n
                        [1] Ir a la izquierda  [2] Ir a la derecha  [S] Salir\n
                                ----->
                                """)
        if re.search("[12sS]", eleccion_usuario) == None:
            False
        else:
            if eleccion_usuario.lower() == "s":
                return print("Esta opcion te tiene que devolver al menu principal")
            else:
                eleccion_usuario = int(eleccion_usuario)
                if eleccion_usuario == 1:
                    posicion_lista -=1
                    Imprimir_ficha_heroe(lista[posicion_lista])
                else:
                    if eleccion_usuario == 2:
                        posicion_lista +=1
                        Imprimir_ficha_heroe(lista[posicion_lista])
#--------------------------------------------------------------
                

#--------------------------------------------------------------
def Imprimir_menu():
    print("""
    1 - Imprimir la lista de nombres junto con sus iniciales
    2 - Generar códigos de héroes
    3 - Normalizar datos
    4 - Imprimir índice de nombres
    5 - Navegar fichas
    S - Salir
    ____________________________________________________________
    """)
#--------------------------------------------------------------


#--------------------------------------------------------------
def Stark_menu_principal():
    while True:
        Imprimir_menu()
        eleccion_usuario = input("""
        Elija una opcion
        --->
                                """)
        if eleccion_usuario == "1":
            Stark_imprimir_nombres_con_iniciales(lista_personajes)
        else:
            if eleccion_usuario == "2":
                Stark_generar_codigos_heroes(lista_personajes)
            else:
                if eleccion_usuario == "3":
                    pass
                else:
                    if eleccion_usuario == "4":
                        Stark_imprimir_indice_nombre(lista_personajes)
                    else:
                        if eleccion_usuario == "5":
                            Stark_navegar_fichas(lista_personajes)
                        else:
                            if eleccion_usuario.lower() == "s":
                                False
#--------------------------------------------------------------

Stark_menu_principal()
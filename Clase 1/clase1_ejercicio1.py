contador = 0
flag_barbijo_caro = 0
precio_barbijo_caro = 0
cant_barbijo_caro = 0
fabricante_barbijo_caro = 0
flag_barbijo_mas_uni = 0
flag_jabon_mas_uni = 0
flag_alcohol_mas_uni = 0
cant_uni_bar = 0
cant_uni_jabon = 0
cant_uni_alcohol = 0
fabricante_alcohol_mas_uni = 0
fabricante_jabon_mas_uni = 0
fabricante_barbijo_mas_uni = 0
cant_total_jabones = 0

while(contador < 5):

    while(True):
        tipo = input("Que tipo de producto es, barbijo, jabón o alcohol?")
        if (tipo != "barbijo" and tipo != "jabon" and tipo != "alcohol"): continue
        else: break

    while(True):
        precio = int(input("Ingrese el precio en pesos?"))
        if (precio < 100 and precio > 300): continue
        else: break

    while(True):
        cant_unidades = int(input("Cuantas unidades son?"))
        if (cant_unidades < 0 and cant_unidades > 1000): continue
        else: break

    marca = input("Que marca es?")
    fabricante = input("Que fabricante es?")

    if (flag_barbijo_caro == 0 and tipo == "barbijo"):
        precio_barbijo_caro = precio
        cant_barbijo_caro = cant_unidades
        fabricante_barbijo_caro = fabricante
        flag_barbijo_caro = 1
    else:
        if (precio_barbijo_caro < precio and tipo == "barbijo"):
            precio_barbijo_caro = precio
            cant_barbijo_caro = cant_unidades
            fabricante_barbijo_caro = fabricante

    if (flag_barbijo_mas_uni == 0 and tipo == "barbijo"):
        cant_uni_bar = cant_unidades
        fabricante_barbijo_mas_uni = fabricante
        flag_barbijo_mas_uni = 1
    else:
        if(cant_uni_bar < cant_unidades and tipo == "barbijo"):
            cant_uni_bar = cant_unidades
            fabricante_barbijo_mas_uni = fabricante
    
    if (flag_alcohol_mas_uni == 0 and tipo == "alcohol"):
        cant_uni_alcohol = cant_unidades
        fabricante_alcohol_mas_uni = fabricante
        flag_alcohol_mas_uni = 1
    else:
        if(cant_uni_alcohol < cant_unidades and tipo == "alcohol"):
            cant_uni_alcohol = cant_unidades
            fabricante_alcohol_mas_uni = fabricante
    
    if (flag_jabon_mas_uni == 0 and tipo == "jabon"):
        cant_uni_jabon = cant_unidades
        fabricante_jabon_mas_uni = fabricante
        flag_jabon_mas_uni = 1
    else:
        if (tipo == "jabon"):
            cant_total_jabones += cant_unidades
            if(cant_uni_jabon < cant_unidades):
                cant_uni_jabon = cant_unidades
                fabricante_jabon_mas_uni = fabricante

    contador += 1

if (cant_uni_jabon > cant_uni_alcohol and cant_uni_jabon > cant_uni_bar):
    mensaje = "El item con mas unidades es "+fabricante_jabon_mas_uni+" y es: "+cant_uni_jabon
else:
    if (cant_uni_alcohol > cant_uni_jabon and cant_uni_alcohol > cant_uni_bar):
        mensaje = "El item con mas unidades es "+fabricante_alcohol_mas_uni+" y es: "+cant_uni_alcohol
    else:
        if (cant_uni_bar > cant_uni_alcohol and cant_uni_bar > cant_uni_jabon):
            mensaje = "El item con mas unidades es "+fabricante_barbijo_mas_uni+" y es: "+cant_uni_bar

print("El mas caro de los barbijos tiene una cantidad de: "+cant_barbijo_caro+" y es fabricado por: "+fabricante_barbijo_caro+"/n"+
        mensaje+"/n"+
        "La cantidad de jabones es: "+cant_total_jabones)
"""Thiago Vilani""" 

pregunta=True
descuento=0
peso_total=0
precio_bruto=0
precio_descuento=0
flag_alimento_caro=0
tipo_alimento_caro=0
precio_alimento_caro=0


while(pregunta):
	
	while(True):
		peso=int(input("Que peso tiene? solo entre 10 y 100 kg"))	
		if (peso<10 or peso>100):
			continue
		else: 
			break

	while(True):
		precio=int(input("Que precio tiene?"))	
		if (precio<0 and precio.isnumeric()==False):
			continue
		else:
			break
	
	while(True):
		tipo=input("Que tipo es? (vegetal, animal, mezcla)")	
		if (tipo!="v" and tipo!="a" and tipo!="m"):
			continue
		else:
			break
	
	peso_total=peso+peso_total
	precio_bruto=precio+precio_bruto
	kilos_total=peso+kilos_total

	if(flag_alimento_caro==0):
		precio_alimento_caro=precio
		tipo_alimento_caro=tipo
		flag_alimento_caro=1
	else:
		if(precio_alimento_caro<precio):
			precio_alimento_caro=precio
			tipo_alimento_caro=tipo


	pregunta=input("Desea agregar otra compra?")

if (peso_total>100):
	precio_descuento=((precio_bruto*15)/100)-precio_bruto
	print("El precio total con descuento es de: "+precio_descuento+"/n")
else:
	if(peso_total>300):
		precio_descuento=((precio_bruto*25)/100)-precio_bruto
		print("El precio total con descuento es de: "+precio_descuento+"/n")

promedio_precio_kilo=precio_bruto/kilos_total

print("El importe total bruto a pagar es de: "+precio_bruto+"/n"+
		"El tipo de alimento mas caro es "+tipo_alimento_caro+"/n"+
		"El promedio de precio por kilo es de: "+promedio_precio_kilo)

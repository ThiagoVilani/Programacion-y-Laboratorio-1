lista_precios = {
    
    "banana" : {
        "precio" : 120.10,
        "unidad_medida": "kg",
        "stock": 50
    },
    
    "pera": {
        "precio": 240.50,
        "unidad_medida": "kg",
        "stock": 40        
    },
    
    "frutilla": {
        "precio": 300,
        "unidad_medida": "kg",
        "stock": 100        
    }, 
    
    "mango" : {
        "precio": 300,
        "unidad_medida": "unidad",
        "stock": 100  
    }

}

# Punto 1: solicitar al usuario un producto y verificiar si existe 
# en 'lista_precios' en caso de existir mostrar precio y el stock. En caso de no existir el 
# producto mostrar el mensaje 'el articulo no se encuentra en la lista'

# Punto 2: agregar al punto anterior que el usuario ingrese la cantidad y 
# retornar el precio total (precio * cantidad)

# Punto 3: solicitar al usuario que ingrese una nueva fruta junto con su precio, 
# unidad de medida y stock. Agregar la nueva fruta a la lista de precios

# Punto 4: imprimir el listado de frutas (solo su nombre)

# Punto 5: solicitarle al usuario el nombre de fruta y en caso de 
# exisitir eliminarla. En caso de que el producto no exista mostrar 
# el mensaje 'el articulo no se encuentra en la lista'

def imprimir_lista(lista):
    string_imprimir = ""
    for fruta in lista:
        string_imprimir += "{0}\n".format(fruta.capitalize())
    return(string_imprimir)

def modificando_diccionario(lista:list):
#PUNTO 1
    while True:
        input_producto = input("\nIngrese un producto de la lista\n{0}\n".format(imprimir_lista(lista)))
        if lista.get(input_producto) == None:
            print("\nEl articulo no se encuentra en la lista\n")
        else:
            break
    print("El precio es de ${0} y el stock {1}".format(lista[input_producto]["precio"], lista[input_producto]["stock"]))
#PUNTO 2
    while True:
        input_cantidad = input("Ingrese la cantidad que desea comprar")
        input_cantidad = int(input_cantidad)
        if input_cantidad > 0:
            break
    resultado = lambda cantidad, precio : cantidad * precio
    print("El precio total por la cantidad solicitada es de: {0}".format(resultado(input_cantidad, lista[input_producto]["precio"])))
#PUNTO 3
    input_nombre_fruta = input("Ingrese el nombre de una nueva fruta")
    input_precio_fruta = int(input("Ingrese el precio de la fruta"))
    input_medida_fruta = input("Ingrese la unidad de medida")
    input_stock_fruta = int(input("Ingrese la canitdad de stock que hay"))

    lista.update({input_nombre_fruta : {"precio" : input_precio_fruta, "unidad_medida" : input_medida_fruta, "stock" : input_stock_fruta}})
    print(lista)
#PUNTO 4
    nombres_frutas = list(lista.keys())
    print(nombres_frutas)
#PUNTO 5
    input_eliminar = input("Ingrese el nombre de la fruta que desea eliminar")
    articulo_eliminado = lista.pop(input_eliminar, "El articulo no se encuentra en la lista")
    print("{}\n{}".format(articulo_eliminado, lista))

modificando_diccionario(lista_precios)

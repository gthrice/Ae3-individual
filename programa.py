"""Trabajo individual Ae3 Felipe Burgos"""

import random 

# Elementos de la tienda
Productos = {
    1: ("Zapatilla nike", 110),
    2: ("Zapatilla adidas", 120),
    3: ("Zapatilla puma", 100),
    4: ("Camiseta nike", 50),
    5: ("Camiseta adidas", 60),
    6: ("Camiseta puma", 55),
    7: ("Pantalon nike", 80),
    8: ("Pantalon adidas", 90),
    9: ("Pantalon puma", 85),
    10: ("Gorra nike", 30),
    11: ("Gorra adidas", 40),
    12: ("Gorra puma", 35)
}
# Clientes frecuentes

clientes_frecuentes = {
    1: {"rut": "12345678-9", "nombre": "Juan Perez"},
    2: {"rut": "98765432-1", "nombre": "Maria Lopez"},
    3: {"rut": "11222333-4", "nombre": "Carlos Gomez"}
}

# Días de la semana
dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}
# bienvenida al programa
print("\n\nBienvenido a la tienda de ropa deportiva\n")

# Seleccionar un día aleatorio de la semana
random_dia = dias[random.randint(1, 7)] # random.randint(1, 7) genera un número aleatorio entre 1 y 7 inclusive y lo almacena en la variable random_dia

print("Hoy es:", random_dia)

if random_dia == "Lunes" or random_dia == "Martes":
    print("Hoy hay descuentos especiales, no te los pierdas!")
else:
    print("Hoy no hay descuentos especiales.")

# Pregutar si es cliente freuente o no para luego verirficar con la base de datos (lista)
boleano_cliente_frecuente = False # Variable para almacenar la respuesta del cliente frecuente

while True:
    variable_cliente_frecuente = input("¿Eres cliente frecuente? (si/no): ").strip().lower()
    if variable_cliente_frecuente == "si":
        ingreso_rut = input("Por favor, ingresa tu RUT: ").strip()
        #verificar si el rut ingresado está en la base de datos de clientes frecuentes 
        # clientes_frecuentes es un diccionario, por lo que se puede verificar si el rut está en los valores del diccionario
        if any(cliente["rut"] == ingreso_rut for cliente in clientes_frecuentes.values()): # any() devuelve True si al menos un elemento del iterable es True
            nombrecliente = next(cliente["nombre"] for cliente in clientes_frecuentes.values() if cliente["rut"] == ingreso_rut) # next() devuelve el primer elemento del iterable que cumple la condición 
            print(f"¡Bienvenido de nuevo {nombrecliente} !")
            boleano_cliente_frecuente = True
            break
        else:
            print("RUT no registrado como cliente frecuente. Intenta nuevamente o responde 'no'.")
    elif variable_cliente_frecuente == "no":
        print("\n¡Bienvenido a nuestra tienda!")
        break
    else:
        print("Respuesta no válida. Por favor, responde 'si' o 'no'.")

# Mostrar los productos disponibles
print ("\nProductos disponibles:\n")
for tlp, (nombre, precio) in Productos.items(): #tlp todos los productos #
    print(f"{tlp}. {nombre} - ${precio}")

# Solicitar al usuario que ingrese el ID del producto y la cantidad deseada
print ("\nPor favor, ingresa el ID del producto que deseas comprar y la cantidad deseada")
print("si quieres salir de la plataforma escribe 'adios'")

carrito = {}

while True: # Bucle principal para agregar productos al carrito
    input_id_str = input("ID del producto: ").strip().lower() 

    if input_id_str == "adios": # Verificar si el usuario quiere salir
        break
    if not input_id_str.isdigit(): # Verificar si la entrada es un número la funciuón isdigit() devuelve True si todos los caracteres de la cadena son dígitos
        print("Entrada no válida. Por favor, ingresa un número para el ID del producto.")
        continue
    id_producto = int(input_id_str) # Convertir a entero aquí
    if id_producto not in Productos:
        print("ID de producto no válido. Por favor, ingresa un ID de producto existente.")
        continue # volver a pedir el ID
    cantidad_str = input("Cantidad: ").strip()
    if not cantidad_str.isdigit(): 
        print("Entrada no válida. Por favor, ingresa un número para la cantidad.")
        continue
    cantidad = int(cantidad_str)
    if cantidad <= 0:
        print("La cantidad debe ser un número positivo.")
        continue 

    # Agregar producto al carrito
    carrito[id_producto] = carrito.get(id_producto, 0) + cantidad
    print(f"\n{cantidad} unidad(es) de '{Productos[id_producto][0]}' agregada(s) al carrito.")

    # Mostrar carrito actual 
    print('\nCarrito actual:')
    total_compra_bruto = 0 # Variable para almacenar el total de la compra antes de aplicar descuentos
    total_productos_en_carrito = 0 # Variable para almacenar el total de productos en el carrito
    for carrito_actual_id, cantidad_en_carrito in carrito.items(): # carrito_actual_id es el id del producto y cantidad_en_carrito es la cantidad de ese producto en el carrito
        nombre_producto = Productos[carrito_actual_id][0] # Obtener el nombre del producto usando el ID
        precio_producto = Productos[carrito_actual_id][1] # Obtener el precio del producto usando el ID
        subtotal_producto = cantidad_en_carrito * precio_producto # Calcular el subtotal del producto
        total_compra_bruto += subtotal_producto # Sumar el subtotal al total de la compra
        total_productos_en_carrito += cantidad_en_carrito # Sumar la cantidad de productos al total de productos en el carrito
        print(f"- {cantidad_en_carrito} unidad(es) de '{nombre_producto}' - ${precio_producto} c/u = ${subtotal_producto} en total")# Mostrar el subtotal del producto
    
    n_descuento = 0
    lista_descuentos = [] # Lista para almacenar los descuentos aplicados
    
    # aplicar descuento si es cliente frecuente
    if boleano_cliente_frecuente == True:
        n_descuento += 0.05 # 5% de descuento para clientes frecuentes y lo suma l descuento
        lista_descuentos.append("5% de descuento por ser cliente frecuente.")
    if total_productos_en_carrito > 10: # Si el total de productos en el carrito es mayor a 10
        n_descuento += 0.1
        lista_descuentos.append("10% de descuento por comprar más de 10 productos.")
    if sum(cantidad * Productos[id_producto][1] for id_producto, cantidad in carrito.items()) > 500: # Si el total de la compra es mayor a 500 dolares
        n_descuento += 0.07
        lista_descuentos.append("7% de descuento por comprar productos superiores a 500 dolares.")
    if random_dia == "Lunes" or random_dia == "Martes": # Si es lunes o martes
        n_descuento += 0.15 # 15% de descuento en dias de promociones
        lista_descuentos.append("15% de descuento por ser lunes.")
    boleano_descuento_maximo = False # Variable para indicar si se ha aplicado el descuento máximo
    if n_descuento > 0.3:
        boleano_descuento_maximo = True # Indicar que se ha aplicado el descuento máximo
        n_descuento = 0.3 # 30% de descuento máximo
        

    descuento_aplicado_monto = total_compra_bruto * n_descuento # Calcular el monto del descuento aplicado
    total_compra_final = total_compra_bruto - descuento_aplicado_monto # Calcular el total de la compra después del descuento
    
    #total sin descuento
    print(f"\n        Total bruto: ${total_compra_bruto}") # Mostrar el total de la compra antes de aplicar descuentos
    if descuento_aplicado_monto > 0: # Si se aplica algún descuento 
        print("        Descuentos por considerar:")
        for desc in lista_descuentos: # Iterar sobre la lista de descuentos y mostrarlos
            print(f"        - {desc}") # Mostrar los descuentos aplicados
        print(f"        Porcentaje de descuento final: {n_descuento * 100:.0f}%") #:.0f formatea el número a 0 decimales
        if boleano_descuento_maximo == True:
            print("        de acuerdo a las políticas de la tienda, el descuento máximo es del 30%")
        print(f"        Monto de descuento aplicado: -${descuento_aplicado_monto}")
    else:
        print("        No se aplicó descuento.")
    
    print(f"\n        Total a pagar: ${total_compra_final}")
    
    # Preguntar si desea agregar otro producto
    while True:
        respuesta = input("\n¿Deseas agregar otro producto? (si/no)\nPara ver los productos disponibles escribe 0 : ").strip().lower()
        if respuesta == 'si': # Si la respuesta es sí, volver al inicio del bucle while para agregar otro producto
            break # Salir del bucle while para agregar otro producto
        elif respuesta == 'no': # Si la respuesta es no, salir del bucle while 
            break 
        elif respuesta == '0': # Si la respuesta es 0, mostrar los productos disponibles
            print("\nProductos disponibles:\n")
            for tlp, (nombre, precio) in Productos.items():
                print(f"{tlp}. {nombre} - ${precio}")
        else:
            print("Respuesta no válida. Por favor, responde 'si' o 'no'.")
    
    if respuesta == 'no': # Si la respuesta es no, salir del bucle while principal
        print ('\nel resumen de tu compra es el siguiente:')
        for carrito_actual_id, cantidad_en_carrito in carrito.items():
            nombre_producto = Productos[carrito_actual_id][0]
            precio_producto = Productos[carrito_actual_id][1]
            subtotal_producto = cantidad_en_carrito * precio_producto
            print(f"   - {cantidad_en_carrito} unidad(es) de '{nombre_producto}' - ${precio_producto} c/u = ${subtotal_producto:}")
        print(f'\n                         Total bruto: ${total_compra_bruto}')
        if descuento_aplicado_monto > 0:
            print(f'    Porcentaje de descuento aplicado: {n_descuento * 100:.0f}%')
        print(f'                 Total final a pagar: ${total_compra_final}')
        print ('\n\nDirigiéndote a la pantalla de pago...')
        print ("\nProcesando tu compra...")
        print ("\nGracias por tu compra, por favor espera un momento mientras procesamos tu pedido.")
        print ("\nProcesando tu pedido...")
        print ("\nTu pedido ha sido procesado con éxito.")
        break


print("\n¡Gracias por venir! Vuelve pronto.\n")
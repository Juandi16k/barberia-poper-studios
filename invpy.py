import json
def guardar_objetos(datos):
    with open("Inventario.json" , "w") as archivo:
            json.dump(datos , archivo , indent=4)
    

try:
    with open("Inventario.json" , "r") as archivo:
        Inventario = json.load(archivo)
except (FileNotFoundError,  json.JSONDecodeError): #En caso que no exista o que este dañado creamos uno nuevo con las llaves preestablecidas
    Inventario = {}
    with open("Inventario.json" , "w") as archivo:
        json.dump(Inventario , archivo)
        print("Archivo Json creado e inicializado con exito...")
        
        

while True:
    print("\n"+"="*20) 
    print("Bienvenido a poperStudios Barberia\n")
    print("=====MENU=====\n")
    print("1.Registrar productos. \n")
    print("2. Ver resumen\n")
    print("3. Modificar o eliminar producto...\n")
    print("4. Salir...\n")
    print("="*20)
    opcion = input("Selecciona una de las opciones...\n") 
    
    if opcion =='1':
        try:
            numProductos = int(input("Hola chaval, ingresa el numero de productos que ingresaremos:"))
        except ValueError:
            print("Que parte de ingresa un NUMERO no entiendes...")
            continue
        
        if numProductos <= 0:
            print("Se enloquecio HP, tenes que poner un numero POSITIVO MKON...")
            continue
        
        for i in range(numProductos):
            producto = input(f"\nIngresa El nombre del producto #{i + 1}: ").lower().strip()

    
            while True:
                try:
                    stock = int(input(f"\nIngresa la cantidad de stock para {producto}: "))
                    
                    if stock <0:
                        print("\nSe enloquecio mi viejo, stock negativo como asi")
                        continue
                    break 
                except ValueError:
                    print("Socio que ingrese un NUMEROOOO")
                    
            Inventario[producto] = Inventario.get(producto , 0) + stock
            total = Inventario[producto]



            if total == 0:
                print ("SE AGOTÓ MI HERMANO")
            elif total <= 5:
                print (f"Ojo que estamos en los rines para {producto}")
            else:
                print(f"stock de {producto} al dia mi H...")
        
        guardar_objetos(Inventario)

        print("\n--- Registro finalizado ---")
        


    elif opcion == '2': 
        print("\n"+"="*20) 
        print("=====Resumen Actual=====")
        if not Inventario:
            print("No hay nada creado chaval...")
        else:
            for p , s in Inventario.items():   #No olvides el .items para que el programa sepa que p y s al tiempo se leen en Inventario
                if s ==  0:
                    estado = f"Noooo mano SE AGOTO EL {p}"
                elif s <= 5:
                    estado = f"Stock medio paila para {p}"
                elif s > 5:
                    estado = f"Vamos es una chimba mi sooo , pleno stock para {p}"
                
                print (f"\nProducto {p.capitalize:<15} | Stock {s:<5} | {estado}")    
        print ("\n=" *30)
        
    elif opcion == "3":
        print("===== MODIFICAR O ELIMINAR =====\n")
        producto_editar = input("Ingresa el producto que vamos a editar o eliminar: ").lower().strip()
        
        if producto_editar in Inventario:
            print(f"Encontrado papacho, Producto : {producto_editar.capitalize:<15} | Stock : {Inventario[producto_editar]:<3}\n")
            accion = input("Quieres (C)ambiar el stock o (E)liminarlo por completo? \n").lower()
            
            if accion == "c":
                while True:
                    try:
                        Inventario[producto_editar]= int(input("STOCK REAL: "))
                        break
                    except ValueError:
                        print("Socio que un numero, no ingrese mkdas si? ")

            
            elif accion == "e":
                del Inventario[producto_editar]
                print (f"{producto_editar} ha sido eliminado exitosamente.")
            
            guardar_objetos(Inventario)
                
        else :
            print("Este producto no existe en la base de datos actual")
    elif opcion == '4' :
        if  input("Seguro que quieres salir? s/n\n").lower() == "s":
            print("Ah listo socio suerte pues...")
            break
    else : 
        print("esa opcion no existe hermanito mio...")
input("\nPresiona enter pa irnos a la shit... ")




productoAlerta = []
bajoStock = 0
buenStock = 0
agotado = 0
while True:
    print("="*20)
    print("Bienvenido a poperStudios Barberia\n")
    print("=====MENU=====\n")
    print("1.Registrar productos. \n")
    print("2. Ver resumen\n")
    print("3. Salir...\n")
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
            producto = input(f"\nIngresa El nombre del producto #{i + 1}: ")
            stock = int(input(f"\nIngresa la cantidad de stock que hay para {producto} "))
                
          
    
            while stock <0:
                 print("\nSe enloquecio mi viejo, stock negativo como asi")
                 stock = int(input(f"\nIngresa la cantidad de stock que hay para {producto} "))
            with open("inventario.txt ", "a") as archivo:
                archivo.write(f"{producto} , {stock}\n")
        
            if stock <=5 and stock >0:
                 print(f"\nSocio te estas quedando sin stock para:  {producto} ojito ahi hermanazo. ")
                 productoAlerta.append(producto)
                 bajoStock += 1 
    
            elif stock >5:
              print("\nVas pleno de stock mi chamo.")
              buenStock += 1

            else:
              print("AGOTADO!!!")
              productoAlerta.append(producto)
              agotado +=1
        
        print("\n--- Registro finalizado ---")
        
             
    elif opcion == '2': 
        print("\n"+"="*20) 
        print("=====Resumen Actual=====")
        
        try:
            with open("inventario.txt" , "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    nombre = datos[0]
                    cantidad = int(datos[1])
                    
                    estado = "Stock mas bajo de lo recomendado" if cantidad < 5 else "Vamos es plenos de stock"
                    
                    print(f"Producto: {nombre:<15} | Stock: {cantidad:<3} | {estado}\n")
                    
        except FileNotFoundError:
            print("Error, chaval no hay nada registrado mano.")
                       
        print("="*20)
        
        
    elif opcion == '3' :
        salir = input("Seguro que quieres salir? s/n\n")
        if salir == "s" :
            print("Ah listo socio suerte pues...")
            break
    else : 
        print("esa opcion no existe hermanito mio...")
input("\nPresiona enter pa irnos a la shit... ")




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
        numProductos = int(input("Hola chaval, ingresa el numero de productos que ingresaremos:"))
        
        if numProductos <= 0:
          print("Se enloquecio HP, tenes que poner un numero POSITIVO MKON...")
        for i in range(numProductos):
          producto = input(f"\nIngresa El nombre del producto #{i + 1}: ")
          stock = int(input(f"\nIngresa la cantidad de stock que hay para {producto} "))
    
          while stock <0:
            print("\nSe enloquecio mi viejo, stock negativo como asi")
            stock = int(input(f"\nIngresa la cantidad de stock que hay para {producto} "))
        
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
        print(f"\nTienes un total de {bajoStock} productos con poco stock , compre pues.")
        print(f"\nTambien tienes lo que vienen siendo {buenStock} productos con buen stock por ahora")
        print(f"\nTambien tienes un total de {agotado} productos agotados.. ")
        print(f"\nLos productos que tendras que reponer lo antes posible serian: {productoAlerta} ")
    elif opcion == '2': 
        print("\n" "="*20) 
        print("=====Resumen Actual=====")
        print(f"Productos que queda poquito: {bajoStock} ")
        print(f"Buen stock: {buenStock}")
        print(f"Agotados: {agotado}")
        print(f"Lista de compras: {list(set(productoAlerta))}")
        print("="*20)
    elif opcion == '3' :
        salir = input("Seguro que quieres salir? s/n\n")
        if salir == "s" :
            print("Ah listo socio suerte pues...")
            break
    else : 
        print("esa opcion no existe hermanito mio...")
input("\nPresiona enter pa irnos a la shit... ")



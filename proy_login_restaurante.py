import datetime



CUENTA="empresarent123"
CONTRASENIA="128904y"
listaplatillos=["picante de pollo","sopa de mani","lomo saltado","aji de fideo","caldo de res","caldo de pollo"]
precio=[12,5,13,8,13,13]
cantidad=[5,7,10,13,15,14]
#modulo que validara la cuenta
def validarlacuenta(cuenta, contrasena):
    
    while((cuenta !=CUENTA) and (contrasena!=CONTRASENIA)):
        cuenta=input("ingrese la cuenta nuevamente-> ")
        contrasena=input("ingrese la contraseña nuevamente-> ")
    



#modulo para mostarr los paltillo
def mostrarplatillos(listaplatillos,precio,cantidad):
    print("Nro\t nombre \tprecio\t cantidad")
    print("--------------------------------------------")
    for i in range(len(listaplatillos)):
        print(i,"|",listaplatillos[i],"\t",precio[i],"\t ",cantidad[i])
      

 #modulo para añadir un nuevo platillo, precio, cantidad a la lista   
def anadirplatillo():
    platillo=input("ingrese el nombre del platillo->")
    return platillo
def anadirprecio():
    precio=int(input("ingrese el precio->"))
    return precio
def anadircntidad():
    cantidad=int(input("ingrese la cantidad->"))
    return cantidad

#modulo para ingresar  un platillo que desea comprar el cliente
def ingresonomplatillo():
    print("ingrese el platillo")
    platilloo=input("-> ")
   # platillotot=platillotot+" "+platillo
    return platilloo


#modulo para realizar el registro de platos que quiere el cliebnte
def nuevaventa(indice):
    
    
    PICP=0.1
    LOMSAL=0.2
    OTRO=0.05
    preciodes=0
    preciototal=0
    des=0
    print("ingrese la cantidad")
    cantid=int(input("-> "))

    if(listaplatillos[indice]=="picante de pollo"):
        preciodes=precio[indice]*PICP
        des=PICP
        cantidad[indice]=cantidad[indice]-cantid

    elif(listaplatillos[indice]=="lomo saltado"):
        preciodes=precio[indice]*LOMSAL
        des=LOMSAL
        cantidad[indice]=cantidad[indice]-cantid
    elif((listaplatillos[indice]!="lomo saltado")and(listaplatillos[indice]!="picante de pollo")):
        preciodes=precio[indice]*OTRO
        des=OTRO
        cantidad[indice]=cantidad[indice]-cantid

    preciototal=precio[indice]-preciodes
    print(f"su pago total es {preciototal} con un descuento del {des} %")
    facturacion(indice,preciototal,des)
    print("YA SE GENERO LA FACTURA, FAVOR DE REVISAR!!!!!\n")
    
  #modulo para realizar la facturacion  
def facturacion(indice,preciototal,des):
    
    print("Ingreso de datos para la factura----------")
    nombre=input("ingrese su nombre-> ")
    dni=input("ingrese su DNI->")
    print("********** F A C T U R A  ***************", file=open("D:\Archivo Registro de Ventas\Archivo_restaurant.txt","w"))
    print("NOMBRE: "+nombre+"\t DNI: "+dni+"\n",file=open("D:\Archivo Registro de Ventas\Archivo_restaurant.txt","a"))
    
    print("PLATOS CONSUMIDOS: "+listaplatillos[indice]+"\t TOTAL: ",preciototal,"\t DESCUENTO: ",des,"\n",file=open("D:\Archivo Registro de Ventas\Archivo_restaurant.txt","a"))
    print(f"\nFecha:  {datetime.datetime.now().date()}  ",file=open("D:\Archivo Registro de Ventas\Archivo_restaurant.txt","a"))
    print(f"Hora:  {datetime.datetime.now().time()}  ",file=open("D:\Archivo Registro de Ventas\Archivo_restaurant.txt","a"))

#modulo dnde se mostrara el menu

def mostrarmenu():
    print(" \n                     R E S T A U R A N T E                      ")
    # Melissa Zarate Cusi
    print( "»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»·««««««««««««««««««««««««««««««")
    print("Menu de seleccion:")
    print("1.- Mostrar el Menu de Platillos")
    print("2.- Añadir platillos al Menu")
    print("3.- eliminar platillos del Menu")
    print("4.- Añadir nueva venta")
    print("5.- salir\n")
    print( "»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»·««««««««««««««««««««««««««««««")
    resp=int(input("-> "))
    contraldeseleccion(resp)
#modulo donde se encontraran todos los modulos
def contraldeseleccion(resp):
    if(resp==1):
        mostrarplatillos(listaplatillos,precio,cantidad)
        mostrarmenu()
        print("─────────────────────────────────────────────────────────────\n")    
    elif (resp==2):
        #para añadir a la lista de platillo
        listaplatillos.insert(len(listaplatillos)+1,anadirplatillo())
        precio.insert(len(precio)+1,anadirprecio())
        cantidad.insert(len(cantidad)+1,anadircntidad())
        print("             Se Actualizo la Lista con Exito!!!                     \n ")
        mostrarplatillos(listaplatillos,precio,cantidad)
        mostrarmenu()
        print("─────────────────────────────────────────────────────────────\n")  

    elif (resp==3):
        #para eliminar de la lista de platillos
        mostrarplatillos(listaplatillos,precio,cantidad)
        listaplatillos.remove(anadirplatillo())
        precio.remove(anadirprecio())
        cantidad.remove(anadircntidad())
        print("             Se Actualizo la Lista con Exito!!!                    \n  ")
        mostrarplatillos(listaplatillos,precio,cantidad)
        mostrarmenu()
        print("─────────────────────────────────────────────────────────────\n")  

    elif (resp==4):
        #añadir venta
        mostrarplatillos(listaplatillos,precio,cantidad)
        indice=listaplatillos.index(anadirplatillo())
        nuevaventa(indice)
          #mostrarplatillos(listaplatillos,precio,cantidad)
        mostrarmenu()
        print("─────────────────────────────────────────────────────────────\n")  
    else:
        print("gracias")
        print("─────────────────────────────────────────────────────────────\n")  
        
    


        


#sera la parte principal conde se llamaran a todasd l funciones y por donde se podra ingrasar al sistema        




print("******** INGRESO  AL  SISTEMA  DEL \n \t R E S T A U R A N T E  *********")

print("─────────────────────────────────────────────────────────────")

cuenta1=input("ingrese la cuenta-> ")
contrasena1=input("ingrese la contraseña-> ")
validarlacuenta(cuenta1,contrasena1)
print("─────────────────────────────────────────────────────────────")
print("******** Datos Correctos->  *********\n")
mostrarmenu()









#menu para gestionar ordenes de los clientes
#añadir venta
#indice=listaplatillos.index(anadirplatillo())
#nuevaventa(indice)
#mostrarplatillos(listaplatillos,precio,cantidad)









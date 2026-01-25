#Realiza un menu itearctivo para el sistema inmobiliario 
# crea un diccionario de usuarios 
# Agregar usuarios
# realiza un login
# Cerrar session
# Crear producto 
# Listar Productos
# Detalle de un producto
# Editar producto
# Cambiar de estado 
# Registrar cliente
# evaluacion de clientes
# Listar Clientes
# Estados de cliente
# Crear transaccion de venta
# generar simulacion : Monto , TEA , Plazo
# cuota : Mxi/1-(1+i)-n
# Asociar cliente a producto
# Marcar producto como reservado o vendido
# buscador de producto
# filtro de producto
# Pagos de cliente
# documentos asociados a propiedad
# Reporte de ventas
# Reporte de ingresos 

# Analisis 
# Clases :Usuarios , Clientes
#  Fx : metodos de las clases
# caracteristicas o atributos : atributos
from usuarios.userservices import getUser
def getMenu():
    msg = """
        Bienvenido al sistema 
        1. Login
        2. Salir
    """
    print(msg)
    opcion = int(input("ingrese una opcion:"))
    return opcion

def evaluate(opcion:int):
    if opcion ==1:
        email="this is email"
        password ="password"
        data=getUser(email)
        if data['password'] == password:
            print("Login correct")
        else:
            print("Incorrecto")
            getMenu()
    elif opcion==2:
        print("Adios!")
        return False

if __name__ == "__main__":
    running = True
    while running:
        opcion = getMenu()
        eval = evaluate(opcion) 
        running = eval

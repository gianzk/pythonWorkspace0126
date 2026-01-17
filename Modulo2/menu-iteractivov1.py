#Realiza un menu itearctivo para el sistema inmobiliario 

msg = """
    Bienvenido a SISTEMA-DATUX-IN
    1.Login
    2.Salir
"""
usuarios =[
    {
        'id':1,
        'name':'Ana',
        'lastName':'Torres',
        'perfil':'Administrador',
        'email':'ana.torres@sistema.com',
        'password':'Admin123*',
        'status':True
    }
]
def MenuIteractivoUserLogeado():
    msgv2="""
        1.Crear Producto
        2.Listar Producto
        3.Evaluar Cliente
        4.Salir
    """
    logueado = True
    while logueado:
        print(msgv2)
        opcionV2 = int(input("ingrese una opcion: "))
        if opcionV2 == 1:
            pass
        elif opcionV2 ==2:
            pass
        elif opcionV2 == 3:
            pass
        elif opcionV2 == 4:
            logueado = False
        else:
            print("ingrese una opcion valida")


def buscarUsuario(email):
    for i in usuarios:
        if email == i['email']:
            return i
    return False


def login():
    # usuario y una password
    # comparar en una "base de datos"
    email = input("ingrese su email: ")
    usuario=buscarUsuario(email)
    if type(usuario) == dict:
            if usuario.get('status'):
                password = input("ingrese su password: ")
                if password == usuario["password"]:
                    print(f"LOGIN CORRECTO {usuario['name']}")
                    return usuario
                else:
                    print("error de password")
            else:
                print("usuario no activo")
    else:
        print("usuario no encotrado")
#manejar variable global para el usuario
# logica para que si el usuario no se loguea no entre a la proxima vista

n=1
while True:
    print(msg)
    opcion = int(input("ingrese una opcion: "))
    # match case o if 
    if opcion ==1:
       usuarioLogeado = login()
       MenuIteractivoUserLogeado()
    elif opcion == 2:
        pass
    else:
        print("ingrese una opcion valida")

# aplicando divide y venceras


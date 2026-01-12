propertys = ["casa nro1 ","casa nro 2","casa nro 3","casa nro 4"]
address_propertys = ("calle1","calle2","calle3","calle4")

countPropertys = len(propertys)

propertys_v2 = {
    "propiedades":[
        {
            "id":1,
            "nombre":"casa blanca",
            "direccion":("av siempre viva","lima"),
            "precio":341231,
            "moneda":"usd",
            "disponible":False,
            "personas":[]
        },
          {
            "id":2,
            "nombre":"casa rosada",
            "direccion":("av siempre felicad","lima"),
            "precio":341231,
            "moneda":"usd",
            "disponible":True,
            "personas":[]
        },
          {
            "id":3,
            "nombre":"casa amarilla",
            "direccion":("av blanca","lima"),
            "precio":234123,
            "moneda":"pen",
            "disponible":True,
            "personas":[]
        }
    ]
}

msg = """
    == Bienvenido a SISTEMA INDATUX ==
    1.Mostrar propiedades
    2.Ver cantidad de propiedades
    3.Ver primera y ultima propiedad
    4. agragar propiedad
    5. Salir
"""
while True:
    print(msg)

    opcion = int(input("ingrese la opcion a realizar: "))


    if opcion == 1:
        print(propertys_v2["propiedades"])
    elif opcion == 2:
        print(len(propertys_v2["propiedades"]))
    elif opcion == 3:
        primera = propertys[0]
        ultima = propertys[-1]
        print(primera,address_propertys[0],ultima,address_propertys[3])
    elif opcion == 4:
        #new_property = input("ingrese la nueva propiedad:")
        #propertys.append(new_property)   
        #print(propertys)
        id_new= len(propertys_v2["propiedades"]) + 1
        #new_property={}
        new_property_2={}
        #new_property["id"]= id_new
        #name = input("ingrese el nombre")
        #new_property["nombre"]=name
        #addres1= input("ingrese su direccion1:")
        #addres2= input("ingrese su direccion2:")
        #new_property["direccion"]=(addres1,addres2)
        #new_property["precio"]= float(input("ingrese el precio:"))
        #propertys_v2["propiedades"].append(new_property)
        #print(propertys_v2["propiedades"])
        #nuevo
        dict_base = propertys_v2["propiedades"][0].keys()
        direcciones =[]
        for i in dict_base:
           if i =="id":
               continue
           valor = input(f"ingrese el valor de {i}")
           if i == "direccion":
                for j in range(2):
                  direccion_tmp =input(f"ingrese el valor de su direccion nro{j}")
                  direcciones.append(direccion_tmp)
                direcciones_tuple=tuple(direcciones)
                new_property_2[i]=direcciones_tuple
    else:
        print("ingrese una opcion correcta")

# base de datos cl

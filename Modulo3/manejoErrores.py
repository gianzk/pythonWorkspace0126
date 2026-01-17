""" try:
    #opcion=int(input("ingresa una opcion"))
    opcion=10
    print(opcion)
except:
    print("este cogio fallo porque no pusiste un entero")
else:
    print("solo si las lineas 2 y 3 se ejecutan yo funcion")
finally:
    print("esto siempre se ejecuta") """
#forma generica
try:
    #print(0/0)
    #lista=[1,2,3]
    #lista[5]
    a=10
    b="hola"
    a+b
except Exception as e:
    print(e)

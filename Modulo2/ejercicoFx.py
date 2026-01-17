def saludar(name):
    print("hola soy dev:",name)
    print("hola soy dev:",name)
# defincion 
# implementacion
# call o llamada

saludar("gian")

#divide y venceras

def saludarv2(name):
    return f"hola soy dev {name}"


#saludo = saludarv2("gian2")

""" if len(saludo)>10:
    print("el mensaje no se puede enviar")
else:
    print("el mensaje se envio correctamente") """


def rangoSalarial(nivel):
    if nivel ==0:
        print("salario 100")
    elif nivel<10 :
        print("salario 200")
    elif nivel<20:
        print("salario 300")
    else:
        print("salario nivel x")

#nivel = int(input("nivel de salario"))
#rangoSalarial(nivel)

rango = 10
#rangoSalarial(rango)
#rangoSalarial(12)

print("-------------------------------")
resultado=10
def suma(a,b):
    global resultado
    resultado = a+b
    print(a,b,resultado)

suma(1,2)
print(resultado)
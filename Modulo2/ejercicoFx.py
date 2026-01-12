def saludar(name):
    print("hola soy dev:",name)
# defincion 
# implementacion
# call o llamada

saludar("gian")

#divide y venceras

def saludarv2(name):
    return f"hola soy dev {name}"


saludo = saludarv2("gian2")

if len(saludo)>10:
    print("el mensaje no se puede enviar")
else:
    print("el mensaje se envio correctamente")
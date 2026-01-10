#notas
dni=input("ingrese su dni: ")
fullname=input("ingrese su nombre completo: ")
nota1=float(input("ingrese su nota de practica nro1"))
nota2=float(input("ingrese su nota de practica nro2"))
nota3=float(input("ingrese su nota de practica nro3"))
nota4=float(input("ingrese su nota de practica nro4"))
#evoluciona en
listaNotas = [nota1,nota2,nota3] #variable

promedio = (nota1+nota2+nota3+nota4)/4

if promedio>11:
    print(f"aprobaste {fullname}")
else:
    print(":(")
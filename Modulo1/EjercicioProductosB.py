msg="""
    Hola Bienvenido a Datux Banca
    1.Para realizar un proceso de evaluacion ingrese los siguientes valores
    - DNI
    - edad 
    - nombre completo
    - Salario
"""

print(msg)
riskIndicator = 1.0

dni = input("ingrese el valor de su dni: ")
edad = int(input("ingrese el valor de su edad: "))
nombre_completo = input("ingrese el valor de su nombre_completo: ")
salario = float(input("ingrese el valor de su salario: "))
deudaTotal = float(input("ingrese el valor de su deuda: "))

riskCalcutor = deudaTotal*0.1/salario
lineaCredito = salario*5
if edad > 18:
    tarjetaDebit = input("usted tiene tarjeta de debito(S/N): ")
    if tarjetaDebit.upper() == 'n'.upper():
        print("Tienes una tarjeta que te espera")
    if riskCalcutor>=riskIndicator:
        print("No tiene tarjeta de credito aprobada")
    else:
        print(f"Si cuenta con una tarjeta de credito de linea {lineaCredito}")
else:
    print("No tiene ningun producto disponible por el momento")



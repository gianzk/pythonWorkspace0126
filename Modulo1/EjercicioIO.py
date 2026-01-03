# realice un programa que muestre si una persona tiene una linea de credito aprobada

msg="""
    Hola Bienvenido a Datux Banca
    1.Para realizar un proceso de evaluacion ingrese los siguientes valores
    - DNI
    - edad 
    - nombre completo
    - Salario
"""

print(msg)
dni = input("ingrese el valor de su dni: ")
edad = int(input("ingrese el valor de su edad: "))
nombre_completo = input("ingrese el valor de su nombre_completo: ")
salario = float(input("ingrese el valor de su salario: "))

aprobeCredit = edad>18 and salario >1500

print(f"Estimado {nombre_completo} con dni: {dni} su credito esta {aprobeCredit}")


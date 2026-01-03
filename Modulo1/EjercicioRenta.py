#variables sueldo (input) , renta (que se calcula) , tasa

sueldo = float(input("ingrese su salario: "))
tasa = 0.0
if sueldo<10000:
    tasa = 0.05
elif sueldo>=10000 and sueldo<20000:
    tasa = 0.15
elif sueldo>=20000 and sueldo<35000:
    tasa = 0.20
elif sueldo>=35000 and sueldo<60000:
    tasa = 0.30
else:
    tasa = 0.45
renta = tasa*sueldo
print(f"el valor de tu tasa es {tasa} con renta de : {renta}")
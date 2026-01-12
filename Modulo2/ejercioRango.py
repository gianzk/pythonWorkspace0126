
while False:
    cantidad= int(input("ingrese la cantidad de numeros a iterar :"))

    for i in range(1,cantidad+1):
        print(i)


d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d.keys():
    print('k =', k,d[k])

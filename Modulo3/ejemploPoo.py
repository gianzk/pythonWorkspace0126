

class PropiedadInmobiliaria:
    dimensionV2:float
    precioPropiedad:float
    def __init__(self,name,adress,dimensiones:str,withSize:float,heigthSize:float,precioUnit:float):
        #este es el constructor
        self.name=name
        self.adress=adress
        self.dimensiones=dimensiones #"7*4"
        self.withSize=withSize
        self.heigthSize = heigthSize
        self.precioUnitario = precioUnit
        self.enable = True
        self.calculateDimensionV2()
    def getWith(self):
        withPropiedad = self.dimensiones.split("*")[0]
        return withPropiedad
    def getHeigth(self):
        heightPropiedad = self.dimensiones.split("*")[1]
        return heightPropiedad
    def calculateDimensionV1(self):
        size = self.dimensiones.split("*")
        dimension = float(size[0])*float(size[1])
        return dimension
    def calculateDimensionV2(self):
         self.dimensionV2 = self.withSize*self.heigthSize
    def calculatePriceAprox(self):
        self.precioPropiedad=self.precioUnitario*self.dimensionV2
        return self.precioPropiedad
    def comprar(self):
        self.enable=False
    def __str__(self):
        disponibilidad:str
        if self.enable:
            disponibilidad="esta disponible"
        else:
            disponibilidad="no esta disponible"
        #operador ternario
        disponibilidadv2="esta disponible" if self.enable else "no esta disponible"
        return f"{self.name} con dimensiones {self.dimensiones} , un precio {self.calculatePriceAprox()} y {disponibilidadv2} "

pr1 = PropiedadInmobiliaria('pr-1','calle siempre viva','7.1*4.0',7.1,4.0,500)
pr2 = PropiedadInmobiliaria('pr-2','calle siempre felidica','6.8*4.0',6.8,4.0,400)
pr3 = PropiedadInmobiliaria('pr-3','calle siempre viva','7.1*4.0',7.1,4.0,550)
pr4 = PropiedadInmobiliaria('pr-4','calle siempre viva','7.1*4.0',7.1,4.0,520)
pr5 = PropiedadInmobiliaria('pr-5','calle siempre viva','7.1*4.0',5.1,8.0,530)
pr3.comprar()
listaProductos= [pr1,pr2,pr3,pr4,pr5]

class Inmobiliario:
    rutaReporte="./reporte.csv"
    headers = ["name","description","dimension","precio\n"]
    def __init__(self,listaPropiedades:list[PropiedadInmobiliaria]):
        self.listaProductos= listaPropiedades        

    def listarPropiedades(self):
        for item in self.listaProductos:
            print(item)
    def generarReporte(self):
        file = open(self.rutaReporte,mode="a")
        file.write(",".join(self.headers))
        for i in self.listaProductos:
            file.write(str(i)+"\n")
        

inmobiliario=Inmobiliario(listaPropiedades=listaProductos)

inmobiliario.listarPropiedades()
inmobiliario.generarReporte()


#C:\Users\User\Desktop\courseWorkspace\pythonWorkspace0126\Modulo4\src\dog_breeds.txt
#Modulo4\src\dog_breeds.txt

ruta="C://Users//User//Desktop//courseWorkspace//pythonWorkspace0126//Modulo4//src//dog_breeds.txt"
rutav2 ="./src/dog_breeds.txt"
with open(rutav2,mode='r') as file:
    data= file.read()
    print(data)
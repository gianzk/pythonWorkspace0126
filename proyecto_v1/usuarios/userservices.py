
from sqlite3 import Connection
# llama a la libreria y trae su objecto connection

def getUser(email:str,con:Connection):
    cursor = con.cursor()
    query = "select * from user where email = ?"
    result= cursor.execute(query,email)
    data= result.fetchone()
    return data

if __name__ == "__main__":
    print("soy el archivo main 2")
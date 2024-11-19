#Este archivo se usara cada vez que se quiera conectar con la BDD
import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    _instance = None

    #Creamos metodo para establecer una conexion 
    def __new__(cls):
        #Verificamos el estado de conexión. Si no existe conexión, creamos una nueva
        if cls._instance is None :
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = None 
        return cls._instance 
    
    #Metodo para conectarnos
    def connect(self):
        if self.connection is None:
            try:
                self.connection = mysql.connector.connect(
                    host = '192.168.56.101' ,
                    database = 'delivery' ,
                    user = 'pythonapp' ,
                    password = 'inacap.2024'

                )
                #En caso de conexión exitosa mostramos un mensaje 
                print("conexión efectuada correctamente")
            except Error as e:
                print(f"Se ha producido un error : {e}")  #e = error (se puede escribir "error")
                self.connection = None
        return self.connection
    #Metodo para cerrar conexion 
    def close(self):  
        #En caso de que exista una conexión y se encuentre activa 
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            self.connection = None
            print("Conexión cerrada")
    #Obtenemos una conexión existente 
    def get_connection(self):
        return self.connect()
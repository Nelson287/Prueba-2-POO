from modelos.repartidor import Repartidor
from mysql.connector import Error
#Archivo de operaciones de tipo producto
from operaciones.repartidor_operaciones import RepartidorOperaciones


# Función para actualizar datos
def actualizar(self, producto):
    conexion = self.db_conexion.get_connection()
    try:
        cursor = conexion.cursor()
        query = "UPDATE producto SET nombre = %s, descripcion = %s, precio = %s, tipo_producto = %s WHERE id = %s"
        valores = (producto.nombre, producto.descripcion, producto.precio, producto.tipo_producto, producto.id)
        cursor.execute(query, valores)
        conexion.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error al actualizar el registro: {e}")
    finally:
        if cursor:
            cursor.close()


# Función para eliminar datos
def eliminar(self, id):
    conexion = self.db_conexion.get_connection()
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM producto WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Error al eliminar el registro: {e}")
    finally:
        if cursor:
            cursor.close()



def main():
    operaciones = RepartidorOperaciones()

    while True:
        print("°°°Menu Principal°°°")
        print("1. Agregar repartidor")
        print("2. Listar repartidores")
        print("3. Actualizar repartidor")
        print("4. Eliminar repartidor")
        print("5. Salir")

        #Capturar la opcion seleccionada
        opcion = input("Selecciona una opcion: ")


        if opcion == "1":
            #Solicitamos los datos del nuevo producto
            nombre = input("Nombre del repartidor: ")
            telefono = input("telefono: ")
            estado = input("estado: ")
            #Creamos un objeto de la clase producto
            nuevo_repartidor = Repartidor(nombre=nombre, telefono=telefono, estado=estado) 

            resultado = operaciones.agregar(nuevo_repartidor)

            #En caso de que la operacion se ejecute correctamente
            if resultado:
                print(f"Repartidor ingresado correctamente con ID: {resultado.id}")
            else:
                print("Error al agregar el repartidor")


        if opcion == "2":
            repartidores = operaciones.listar()
            if repartidores:
                print("** Repartidores registrados **")
                for repartidor in repartidores:
                    print(f"id: {repartidor.id}")
                    print(f"nombre: {repartidor.nombre}")
                    print(f"telefono: {repartidor.telefono}")
                    print(f"estado: {repartidor.estado}")
            else:
                print("No hay registros del repartidor")


        if opcion == "3":
            id = input("Ingrese id del repartidor a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono= input("Nuevo telefono: ")
            nuevo_estado = input("Nuevo estado: ")
            repartidor_actualizado = Repartidor(id = int(id), nombre = nuevo_nombre, telefono=nuevo_telefono, estado=nuevo_estado)
            if operaciones.actualizar(repartidor_actualizado):
                print("Repartidor actualizado correctamente")
            else:
                print("No se actualizó ningún repartidor")


        if opcion == "4":
            id_repartidor = input("Ingrese id del repartidor a eliminar: ")
            if operaciones.eliminar(int(id_repartidor)):
                print("Registro eliminado correctamente")
            else:
                print("No fue posible eliminar")


        if opcion == "5":
            print("Programa finalizado")


if __name__ == "__main__":
    main()    
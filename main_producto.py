from modelos.producto import Producto
from mysql.connector import Error
# Archivo de operaciones de producto
from operaciones.producto_operaciones import ProductoOperaciones


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



# Menú principal
def main():
    # Creamos una instancia de operaciones
    operaciones = ProductoOperaciones()

    # Menú de opciones
    while True:
        print("°°°Menú Principal°°°")
        print("1. Agregar producto")
        print("2. Listar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        # Capturar la opción seleccionada
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Solicitar los datos del nuevo producto
            nombre = input("Nombre del producto: ")
            descripcion = input("Descripción: ")
            precio = float(input("Precio: "))
            tipo_producto = input("Tipo de producto: ")

            # Crear un objeto de la clase Producto
            nuevo_producto = Producto(
                nombre=nombre, 
                descripcion=descripcion, 
                precio=precio, 
                tipo_producto=tipo_producto
            )

            # Agregar el registro
            resultado = operaciones.agregar(nuevo_producto)

            # Confirmar operación
            if resultado:
                print(f"Producto ingresado correctamente con ID: {resultado.id}")

        if opcion == "2":
            productos = operaciones.listar()
            # Si existen productos, los mostramos; si no, mostramos un mensaje al usuario
            if productos:
                print("** Productos registrados **")
                for producto in productos:
                    print(f"ID: {producto.id}")
                    print(f"Nombre: {producto.nombre}")
                    print(f"Descripción: {producto.descripcion}")
                    print(f"Precio: {producto.precio}")
                    print(f"Tipo de producto: {producto.tipo_producto}")
            else:
                print("No hay registros de productos.")

        if opcion == "3":
            id = input("Ingrese ID del producto a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_descripcion = input("Nueva descripción: ")
            nuevo_precio = float(input("Nuevo precio: "))
            nuevo_tipo = input("Nuevo tipo de producto: ")

            # Crear un objeto de la clase Producto
            producto_actualizado = Producto(
                id=int(id), 
                nombre=nuevo_nombre, 
                descripcion=nueva_descripcion, 
                precio=nuevo_precio, 
                tipo_producto=nuevo_tipo
            )

            # Verificar si la operación devuelve True, lo cual indica que actualizó registros
            if operaciones.actualizar(producto_actualizado):
                print("Registro actualizado correctamente.")
            else:
                print("No se actualizó ningún registro.")

        if opcion == "4":
            id = input("Ingrese ID del producto a eliminar: ")
            if operaciones.eliminar(int(id)):
                print("Registro eliminado correctamente.")
            else:
                print("No fue posible eliminar el registro.")

        if opcion == "5":
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()

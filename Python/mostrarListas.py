import tkinter as tk
from tkinter import ttk, messagebox, BOTH
import psycopg2
from psycopg2 import sql
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
import email.mime.multipart
import email.mime.base
import email.encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase



# Función para conectar y obtener datos ordenados de productos desde PostgreSQL
def mostrar_productos_ordenados(opcion, ventana_padre=None):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Llamar a la función MostrarProductosOrdenados en PostgreSQL
        cursor.execute(f"SELECT * FROM MostrarProductosOrdenados({opcion})")
        rows = cursor.fetchall()

        def borrar_treeview():
            if hasattr(ventana_padre, 'tree_productos_ordenados'):
                ventana_padre.tree_productos_ordenados.destroy()
                del ventana_padre.tree_productos_ordenados
                scrollbar_x.destroy()
                scrollbar_y.destroy()

        # Si no se proporciona una ventana_padre, mostrar mensaje de error
        if not ventana_padre:
            messagebox.showerror("Error", "No se especificó una ventana padre para mostrar los productos ordenados.")
            return

        # Crear Treeview si no existe dentro de ventana_padre
        if not hasattr(ventana_padre, 'tree_productos_ordenados'):
            # Crear Treeview
            tree = ttk.Treeview(ventana_padre, columns=("ID Producto", "ID Categoría", "Código de Barras", "Nombre", "Precio de Compra", "Peso en Kg", "Unidades en Bodega", "Precio de Venta", "Cantidad en Stock"))
            
            # Configurar las columnas y encabezados
            tree.heading("#0", text="", anchor=tk.CENTER)  # Columna vacía para alinear
            tree.heading("ID Producto", text="ID Producto", anchor=tk.CENTER)
            tree.heading("ID Categoría", text="ID Categoría", anchor=tk.CENTER)
            tree.heading("Código de Barras", text="Código de Barras", anchor=tk.CENTER)
            tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)
            tree.heading("Precio de Compra", text="Precio de Compra", anchor=tk.CENTER)
            tree.heading("Peso en Kg", text="Peso en Kg", anchor=tk.CENTER)
            tree.heading("Unidades en Bodega", text="Unidades en Bodega", anchor=tk.CENTER)
            tree.heading("Precio de Venta", text="Precio de Venta", anchor=tk.CENTER)
            tree.heading("Cantidad en Stock", text="Cantidad min Stock", anchor=tk.CENTER)

            # Configurar alineación de datos en las columnas
            tree.column("#0", stretch=tk.NO, width=0)  # Ajustar ancho de la columna vacía
            for col in tree["columns"]:
                tree.column(col, anchor=tk.CENTER, width=130)  # Ajustar ancho de las columnas de datos

            # Guardar el Treeview como un atributo de la ventana_padre
            ventana_padre.tree_productos_ordenados = tree

        else:
            # Si ya existe el Treeview, borrar datos anteriores y actualizar con los nuevos datos
            tree = ventana_padre.tree_productos_ordenados
            tree.delete(*tree.get_children())  # Limpiar datos anteriores

        # Insertar nuevos datos en el Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        # Configurar scrollbars para el Treeview
        scrollbar_y = ttk.Scrollbar(ventana_padre, orient=tk.VERTICAL, command=tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x = ttk.Scrollbar(ventana_padre, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Vincular scrollbars al Treeview
        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Ajustar el tamaño del Treeview dentro de ventana_padre
        tree.pack(expand=True, fill=tk.BOTH, padx=40, pady=90)  # Ajusta el espacio alrededor del Treeview

        btn_borrar = ttk.Button(ventana_padre, text="Borrar tabla", command=borrar_treeview)
        btn_borrar.place(x=1100, y=60)

    except psycopg2.Error as e:
        print(f"Error al obtener productos ordenados desde PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al obtener productos ordenados")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def mostrar_productosDelPedido_ordenados(opcion, ventana_padre=None):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Llamar a la función MostrarProductosDelPedidoOrdenados en PostgreSQL
        cursor.execute(f"SELECT * FROM MostrarProductosDelPedidoOrdenados({opcion})")
        rows = cursor.fetchall()

        # Si no se proporciona una ventana_padre, mostrar mensaje de error
        if not ventana_padre:
            messagebox.showerror("Error", "No se especificó una ventana padre para mostrar los productos del pedido ordenados.")
            return
        
        def borrar_treeview():
            if hasattr(ventana_padre, 'tree_productos_pedido'):
                ventana_padre.tree_productos_pedido.destroy()
                del ventana_padre.tree_productos_pedido
                scrollbar_x.destroy()
                scrollbar_y.destroy()

        btn_borrar = ttk.Button(ventana_padre, text="Borrar tabla", command=borrar_treeview)
        btn_borrar.place(x=1100, y=60)
        # Crear Treeview si no existe dentro de ventana_padre
        if not hasattr(ventana_padre, 'tree_productos_pedido'):
            # Crear Treeview
            tree = ttk.Treeview(ventana_padre, columns=("ID Producto", "ID Pedido", "Cant. Requerida", "Cant. Despachada"))
            
            # Configurar las columnas y encabezados
            tree.heading("#0", text="", anchor=tk.CENTER)  # Columna vacía para alinear
            tree.heading("ID Producto", text="ID Producto", anchor=tk.CENTER)
            tree.heading("ID Pedido", text="ID Pedido", anchor=tk.CENTER)
            tree.heading("Cant. Requerida", text="Cant. Requerida", anchor=tk.CENTER)
            tree.heading("Cant. Despachada", text="Cant. Despachada", anchor=tk.CENTER)

            # Configurar alineación de datos en las columnas
            tree.column("#0", stretch=tk.NO, width=0)  # Ajustar ancho de la columna vacía
            for col in tree["columns"]:
                tree.column(col, anchor=tk.CENTER, width=150)  # Ajustar ancho de las columnas de datos

            # Guardar el Treeview como un atributo de la ventana_padre
            ventana_padre.tree_productos_pedido = tree

        else:
            # Si ya existe el Treeview, borrar datos anteriores y actualizar con los nuevos datos
            tree = ventana_padre.tree_productos_pedido
            tree.delete(*tree.get_children())  # Limpiar datos anteriores

        # Insertar nuevos datos en el Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        # Configurar scrollbars para el Treeview
        scrollbar_y = ttk.Scrollbar(ventana_padre, orient=tk.VERTICAL, command=tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x = ttk.Scrollbar(ventana_padre, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Vincular scrollbars al Treeview
        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Ajustar el tamaño del Treeview dentro de ventana_padre
        tree.pack(expand=True, fill=tk.BOTH, padx=40, pady=90)  # Ajusta el espacio alrededor del Treeview

    except psycopg2.Error as e:
        print(f"Error al obtener productos del pedido ordenados desde PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al obtener productos del pedido ordenados")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def mostrar_Pedidos_ordenados(opcion, ventana_padre=None):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Llamar a la función MostrarPedidosOrdenados en PostgreSQL con la opción proporcionada
        cursor.execute(f"SELECT * FROM MostrarPedidosOrdenados({opcion})")
        rows = cursor.fetchall()
       
        def borrar_treeview():
            if hasattr(ventana_padre, 'tree_pedidos'):
                ventana_padre.tree_pedidos.destroy()
                del ventana_padre.tree_pedidos
                scrollbar_x.destroy()
                scrollbar_y.destroy()

        btn_borrar = ttk.Button(ventana_padre, text="Borrar tabla", command=borrar_treeview)
        btn_borrar.place(x=1100, y=60)
        # Si no se proporciona una ventana_padre, mostrar mensaje de error
        if not ventana_padre:
            messagebox.showerror("Error", "No se especificó una ventana padre para mostrar los pedidos ordenados.")
            return
 
        # Crear Treeview si no existe dentro de ventana_padre
        if not hasattr(ventana_padre, 'tree_pedidos'):
            # Crear Treeview
            tree = ttk.Treeview(ventana_padre, columns=("ID Pedido", "ID Cliente", "Fecha Registro", "Hora Registro", "Apellido Recibe", "Nombre Recibe", "Dirección Destino"))
            
            # Configurar las columnas y encabezados
            tree.heading("#0", text="", anchor=tk.CENTER)  # Columna vacía para alinear
            tree.heading("ID Pedido", text="ID Pedido", anchor=tk.CENTER)
            tree.heading("ID Cliente", text="ID Cliente", anchor=tk.CENTER)
            tree.heading("Fecha Registro", text="Direccion destino", anchor=tk.CENTER)
            tree.heading("Hora Registro", text="Hora Registro", anchor=tk.CENTER)
            tree.heading("Apellido Recibe", text="Apellido Recibe", anchor=tk.CENTER)
            tree.heading("Nombre Recibe", text="Nombre Recibe", anchor=tk.CENTER)
            tree.heading("Dirección Destino", text="Fech de registro", anchor=tk.CENTER)

            # Configurar alineación de datos en las columnas
            tree.column("#0", stretch=tk.NO, width=0)  # Ajustar ancho de la columna vacía
            for col in tree["columns"]:
                tree.column(col, anchor=tk.CENTER, width=150)  # Ajustar ancho de las columnas de datos

            # Guardar el Treeview como un atributo de la ventana_padre
            ventana_padre.tree_pedidos = tree

        else:
            # Si ya existe el Treeview, borrar datos anteriores y actualizar con los nuevos datos
            tree = ventana_padre.tree_pedidos
            tree.delete(*tree.get_children())  # Limpiar datos anteriores

        # Insertar nuevos datos en el Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        # Configurar scrollbars para el Treeview
        scrollbar_y = ttk.Scrollbar(ventana_padre, orient=tk.VERTICAL, command=tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x = ttk.Scrollbar(ventana_padre, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Vincular scrollbars al Treeview
        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Ajustar el tamaño del Treeview dentro de ventana_padre
        tree.pack(expand=True, fill=tk.BOTH, padx=40, pady=90)  # Ajusta el espacio alrededor del Treeview

    except psycopg2.Error as e:
        print(f"Error al obtener pedidos ordenados desde PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al obtener pedidos ordenados")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def mostrar_clientes_ordenados(opcion, ventana_padre=None):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Llamar a la función MostrarClientesOrdenados en PostgreSQL con la opción proporcionada
        cursor.execute(f"SELECT * FROM MostrarClientesOrdenados({opcion})")
        rows = cursor.fetchall()
        
        def borrar_treeview():
            if hasattr(ventana_padre, 'tree_clientes'):
                ventana_padre.tree_clientes.destroy()
                del ventana_padre.tree_clientes
                scrollbar_x.destroy()
                scrollbar_y.destroy()

        btn_borrar = ttk.Button(ventana_padre, text="Borrar tabla", command=borrar_treeview)
        btn_borrar.place(x=1100, y=60)

        # Si no se proporciona una ventana_padre, mostrar mensaje de error
        if not ventana_padre:
            messagebox.showerror("Error", "No se especificó una ventana padre para mostrar los clientes ordenados.")
            return

        # Crear Treeview si no existe dentro de ventana_padre
        if not hasattr(ventana_padre, 'tree_clientes'):
            # Crear Treeview
            tree = ttk.Treeview(ventana_padre, columns=("ID Cliente", "Nombre", "Apellido", "Dirección"))
            
            # Configurar las columnas y encabezados
            tree.heading("#0", text="", anchor=tk.CENTER)  # Columna vacía para alinear
            tree.heading("ID Cliente", text="ID Cliente", anchor=tk.CENTER)
            tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)
            tree.heading("Apellido", text="Apellido", anchor=tk.CENTER)
            tree.heading("Dirección", text="Dirección", anchor=tk.CENTER)

            # Configurar alineación de datos en las columnas
            tree.column("#0", stretch=tk.NO, width=0)  # Ajustar ancho de la columna vacía
            for col in tree["columns"]:
                tree.column(col, anchor=tk.CENTER, width=150)  # Ajustar ancho de las columnas de datos

            # Guardar el Treeview como un atributo de la ventana_padre
            ventana_padre.tree_clientes = tree

        else:
            # Si ya existe el Treeview, borrar datos anteriores y actualizar con los nuevos datos
            tree = ventana_padre.tree_clientes
            tree.delete(*tree.get_children())  # Limpiar datos anteriores

        # Insertar nuevos datos en el Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        # Configurar scrollbars para el Treeview
        scrollbar_y = ttk.Scrollbar(ventana_padre, orient=tk.VERTICAL, command=tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x = ttk.Scrollbar(ventana_padre, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Vincular scrollbars al Treeview
        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Ajustar el tamaño del Treeview dentro de ventana_padre
        tree.pack(expand=True, fill=tk.BOTH, padx=40, pady=90)  # Ajusta el espacio alrededor del Treeview

    except psycopg2.Error as e:
        print(f"Error al obtener clientes ordenados desde PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al obtener clientes ordenados")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

# Ejemplo de llamada para mostrar productos ordenados por unidades en bodega (opción 3)
def mostrar_Ganancias_Por_Fecha(diaInicio, diaFinal, ventana_padre=None):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Llamar a la función calcularGananciasPorFecha en PostgreSQL con las fechas proporcionadas
        cursor.execute("SELECT * FROM calcularGananciasPorFecha(%s, %s)", (diaInicio, diaFinal))
        rows = cursor.fetchall()
       
        def borrar_treeview():
            if hasattr(ventana_padre, 'tree_ganancias'):
                ventana_padre.tree_ganancias.destroy()
                del ventana_padre.tree_ganancias
                scrollbar_x.destroy()
                scrollbar_y.destroy()

        btn_borrar = ttk.Button(ventana_padre, text="Borrar tabla", command=borrar_treeview)
        btn_borrar.place(x=1100, y=60)
        # Si no se proporciona una ventana_padre, mostrar mensaje de error
        if not ventana_padre:
            messagebox.showerror("Error", "No se especificó una ventana padre para mostrar las ganancias por fecha.")
            return
 
        # Crear Treeview si no existe dentro de ventana_padre
        if not hasattr(ventana_padre, 'tree_ganancias'):
            # Crear Treeview
            tree = ttk.Treeview(ventana_padre, columns=("Nombre Producto", "Ventas", "Gastos", "Ganancias"))
            
            # Configurar las columnas y encabezados
            tree.heading("#0", text="", anchor=tk.CENTER)  # Columna vacía para alinear
            tree.heading("Nombre Producto", text="Nombre Producto", anchor=tk.CENTER)
            tree.heading("Ventas", text="Ventas", anchor=tk.CENTER)
            tree.heading("Gastos", text="Gastos", anchor=tk.CENTER)
            tree.heading("Ganancias", text="Ganancias", anchor=tk.CENTER)

            # Configurar alineación de datos en las columnas
            tree.column("#0", stretch=tk.NO, width=0)  # Ajustar ancho de la columna vacía
            for col in tree["columns"]:
                tree.column(col, anchor=tk.CENTER, width=150)  # Ajustar ancho de las columnas de datos

            # Guardar el Treeview como un atributo de la ventana_padre
            ventana_padre.tree_ganancias = tree

        else:
            # Si ya existe el Treeview, borrar datos anteriores y actualizar con los nuevos datos
            tree = ventana_padre.tree_ganancias
            tree.delete(*tree.get_children())  # Limpiar datos anteriores

        # Insertar nuevos datos en el Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        # Configurar scrollbars para el Treeview
        scrollbar_y = ttk.Scrollbar(ventana_padre, orient=tk.VERTICAL, command=tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x = ttk.Scrollbar(ventana_padre, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Vincular scrollbars al Treeview
        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Ajustar el tamaño del Treeview dentro de ventana_padre
        tree.pack(expand=True, fill=tk.BOTH, padx=40, pady=90)  # Ajusta el espacio alrededor del Treeview

    except psycopg2.Error as e:
        print(f"Error al obtener ganancias por fecha desde PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al obtener ganancias por fecha")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def mostrar_busqueda(tabla, criterioBusqueda, ventana_padre=None):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Llamar a la función buscarDato en PostgreSQL con los parámetros proporcionados
        cursor.execute(f"SELECT * FROM buscarDato({tabla}, '{criterioBusqueda}')")
        rows = cursor.fetchall()

        def borrar_treeview():
            if hasattr(ventana_padre, 'tree_busqueda'):
                ventana_padre.tree_busqueda.destroy()
                del ventana_padre.tree_busqueda
                scrollbar_x.destroy()
                scrollbar_y.destroy()

        btn_borrar = ttk.Button(ventana_padre, text="Borrar tabla", command=borrar_treeview)
        btn_borrar.place(x=1100, y=60)

        # Si no se proporciona una ventana_padre, mostrar mensaje de error
        if not ventana_padre:
            messagebox.showerror("Error", "No se especificó una ventana padre para mostrar los resultados de la búsqueda.")
            return

        # Crear o actualizar Treeview
        if hasattr(ventana_padre, 'tree_busqueda'):
            tree = ventana_padre.tree_busqueda
            tree.delete(*tree.get_children())  # Limpiar datos anteriores
        else:
            # Crear Treeview si no existe dentro de ventana_padre
            tree = ttk.Treeview(ventana_padre, columns=("ID", "Nombre", "Descripción", "Precio", "Cantidad"))
            tree.heading("#0", text="", anchor=tk.CENTER)  # Columna vacía para alinear
            tree.heading("ID", text="ID", anchor=tk.CENTER)
            tree.heading("Nombre", text="Nombre", anchor=tk.CENTER)
            tree.heading("Descripción", text="Descripción", anchor=tk.CENTER)
            tree.heading("Precio", text="Precio", anchor=tk.CENTER)
            tree.heading("Cantidad", text="Cantidad", anchor=tk.CENTER)

            # Configurar alineación de datos en las columnas
            tree.column("#0", stretch=tk.NO, width=0)  # Ajustar ancho de la columna vacía
            for col in tree["columns"]:
                tree.column(col, anchor=tk.CENTER, width=150)  # Ajustar ancho de las columnas de datos

            # Guardar el Treeview como un atributo de la ventana_padre
            ventana_padre.tree_busqueda = tree

        # Insertar nuevos datos en el Treeview
        for row in rows:
            tree.insert("", tk.END, values=row)

        # Configurar scrollbars para el Treeview
        scrollbar_y = ttk.Scrollbar(ventana_padre, orient=tk.VERTICAL, command=tree.yview)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
        scrollbar_x = ttk.Scrollbar(ventana_padre, orient=tk.HORIZONTAL, command=tree.xview)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Vincular scrollbars al Treeview
        tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Ajustar el tamaño del Treeview dentro de ventana_padre
        tree.pack(expand=True, fill=tk.BOTH, padx=40, pady=90)  # Ajusta el espacio alrededor del Treeview

    except psycopg2.Error as e:
        print(f"Error al obtener datos desde PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al obtener datos")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()
            
def insertar_producto(idCategoria, codigoDeBarras, nombre, precioUnitarioDeCompra, pesoEnKg, unidadesEnBodega, precioUnitarioVenta, cantidadMinStock):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Verificar y convertir campos opcionales a None si están vacíos
        if codigoDeBarras == "":
            codigoDeBarras = None
        if pesoEnKg == "":
            pesoEnKg = None
        if unidadesEnBodega == "":
            unidadesEnBodega = None
     

        # Llamar a la función insertarProducto en PostgreSQL con los parámetros proporcionados
        cursor.execute("""
            SELECT insertarProducto(
                %s, %s, %s, %s, %s, %s, %s, %s
            )
        """, (
            idCategoria,
            codigoDeBarras,
            nombre,
            precioUnitarioDeCompra,
            pesoEnKg,
            unidadesEnBodega,
            precioUnitarioVenta,
            cantidadMinStock
        ))

        # Confirmar la ejecución de la transacción
        connection.commit()

        # Mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Producto insertado correctamente.")

    except psycopg2.Error as e:
        print(f"Error al insertar producto en PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al insertar el producto.")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def borrar_producto_(id_usuario):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Verificar si el usuario existe
        cursor.execute('''
            SELECT * FROM productos WHERE idproducto = %s
        ''', (id_usuario,))
        usuario = cursor.fetchone()

        if usuario:
            # Si el usuario existe, borrarlo de la base de datos
            cursor.execute('''
                DELETE FROM productos WHERE idproducto = %s
            ''', (id_usuario,))
            connection.commit()
            messagebox.showinfo("Éxito", f"Producto con ID {id_usuario} ha sido borrado correctamente")
        else:
            messagebox.showerror("Error", f"No se encontró ningún producto con ID {id_usuario}")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al borrar producto: {e}")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def actualizar_ProductO(columna, nuevo_valor, id_producto):

    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Llamar a la función actualizar_producto en PostgreSQL
        cursor.callproc('actualizar_producto', [columna, nuevo_valor, id_producto])
        connection.commit()

        print(f"Producto actualizado correctamente. Columna: {columna}, Nuevo valor: {nuevo_valor}, ID Producto: {id_producto}")

    except psycopg2.Error as e:
        print(f"Error al actualizar el producto en PostgreSQL: {e}")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def avanzar_pantalla(scroll_valor, apellido_cliente, nombre_cliente, direccion_cliente):
    # Validación básica de campos
    
    if not apellido_cliente or not nombre_cliente or not direccion_cliente:
        messagebox.showerror("Error", "Todos los campos de cliente son obligatorios.")
        print(scroll_valor, apellido_cliente, nombre_cliente, direccion_cliente)
        return
    
    idpedido=llamar_insertar_pedido_con_cliente(scroll_valor, apellido_cliente, nombre_cliente, direccion_cliente)
    # Aquí puedes realizar la lógica para avanzar a la siguiente pantalla o procesar los datos
    crear_interfaz_principal(idpedido)
# Función principal para crear la interfaz de la primera pantalla


 
def verificar_existencias(id_producto, cantidad_requerida, cantidad_despachada, id_pedido):
    def mostrar_errorpeso():
    # Crear una ventana emergente
     ventana_exito = tk.Toplevel()
     ventana_exito.title("Éxito")
     ventana_exito.geometry("300x100+500+300")  # Dimensiones y posición de la ventana
     label_exito = tk.Label(ventana_exito, text="No hay suficientes kg disponibles.", padx=20, pady=20)
     label_exito.pack()
     ventana_exito.after(7000, ventana_exito.destroy)

    def mostrar_errorNumerico():
    # Crear una ventana emergente
     ventana_error = tk.Toplevel()
     ventana_error.title("Error!")
     ventana_error.geometry("300x100+500+300")  # Dimensiones y posición de la ventana
     label_error = tk.Label(ventana_error, text="No hay suficientes unidades disponibles", padx=20, pady=20)
     label_error.pack()
     
     
    # Cerrar la ventana después de 3 segundos (3000 milisegundos)
     ventana_error.after(7000, ventana_error.destroy)
    try:
        # Conectar a la base de datos PostgreSQL
         connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
         cursor = connection.cursor()

        # Verificar existencias y almacenar producto del pedido
         cursor.execute(f"SELECT unidadesEnBodega, pesoEnKg FROM productos WHERE idProducto = {id_producto}")
         producto = cursor.fetchone()

         if not producto:
            messagebox.showerror("Error", f"El producto con ID {id_producto} no existe.")
            return
        
         unidades_disponibles = producto[0]
         peso_en_kg = producto[1]
        
         if unidades_disponibles is not None:
            if cantidad_requerida > unidades_disponibles:
                mostrar_errorNumerico()
                return
         else:
            if cantidad_requerida > peso_en_kg:
                mostrar_errorpeso()
                return
        
        # Insertar producto del pedido
         insertar_producto_pedido(id_pedido, id_producto, cantidad_requerida, cantidad_despachada)

        # Mostrar mensaje de éxito
        

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al conectar con la base de datos: {e}")

    finally:
        if connection:
            connection.close()

def llamar_insertar_pedido_con_cliente(p_inserta_cliente, p_apellido, p_nombre, p_direccion):
    id_pedido = None
    try:
        # Parámetros de conexión
        params = {
            'host': 'localhost',
            'user': 'postgres',
            'password': '1234',
            'database': 'ferreteria'
        }
        
        # Conectar a la base de datos
        connection = psycopg2.connect(**params)
        print("Conexión exitosa")
        
        # Crear un cursor
        cursor = connection.cursor()
        
        # Llamar a la función insertarPedidoConCliente y obtener el ID del pedido insertado
        query = sql.SQL("SELECT insertarPedidoConCliente(%s, %s, %s, %s) AS id_pedido;")
        cursor.execute(query, (p_inserta_cliente, p_apellido, p_nombre, p_direccion))
        
        # Obtener el ID del pedido insertado
        id_pedido = cursor.fetchone()[0]
        
        # Confirmar cambios
        connection.commit()
        
        print("Función ejecutada correctamente")
        
    except Exception as ex:
        print("Error:", ex)
        
    finally:
        # Cerrar conexión
        if connection:
            connection.close()
            print("Conexión terminada")
    
    return id_pedido


def insertar_producto_pedido(id_pedido, id_producto, unidades_requeridas, unidades_despachadas):
    
    def mostrar_exito():
    # Crear una ventana emergente
     ventana_exito = tk.Toplevel()
     ventana_exito.title("Éxito")
     ventana_exito.geometry("300x100+500+300")  # Dimensiones y posición de la ventana
     label_exito = tk.Label(ventana_exito, text="Producto del pedido ingresado correctamente.", padx=20, pady=20)
     label_exito.pack()
     ventana_exito.after(7000, ventana_exito.destroy)

    def mostrar_errorNumerico():
    # Crear una ventana emergente
     ventana_error = tk.Toplevel()
     ventana_error.title("Error!")
     ventana_error.geometry("1000x1000")  # Dimensiones y posición de la ventana
     label_error = tk.Label(ventana_error, text="Error, Ingrese valores numéricos para el ID del Pedido, ID del Producto, unidades requeridas y unidades despachadas.", padx=20, pady=20)
     label_error.pack()

    # Cerrar la ventana después de 3 segundos (3000 milisegundos)
     ventana_error.after(7000, ventana_error.destroy)

    try:
        id_pedido = int(id_pedido)
        
        id_producto = int(id_producto)
        unidades_requeridas = int(unidades_requeridas)
        unidades_despachadas = int(unidades_despachadas)
        
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        cursor.execute("""
            SELECT insertarProductoDelPedido(
                %s, %s, %s, %s
            )
        """, (id_pedido, id_producto, unidades_requeridas, unidades_despachadas))

        connection.commit()
        mostrar_exito()

    except ValueError:
        mostrar_errorNumerico()

    except psycopg2.Error as e:
        print(f"Error al insertar producto del pedido en PostgreSQL: {e}")
        messagebox.showerror("Error", "Ocurrió un error al insertar producto del pedido.")

    finally:
        if connection:
            connection.close()

def crear_interfaz_principal(idpedido):
    root = tk.Tk()
    root.title("Sistema de Pedidos")
    root.geometry("1200x800")
    lista_tuplas = []
    frame_busqueda = ttk.Frame(root)
    frame_busqueda.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    label_busqueda = ttk.Label(frame_busqueda, text="Buscar Producto:")
    label_busqueda.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    entry_busqueda = ttk.Entry(frame_busqueda, width=30)
    entry_busqueda.grid(row=0, column=1, padx=10, pady=5)
    entry_busqueda.bind("<KeyRelease>", lambda event: actualizar_busqueda(entry_busqueda, listbox_resultados))

    listbox_resultados = tk.Listbox(frame_busqueda, selectmode=tk.SINGLE, width=100)
    listbox_resultados.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)
    
    scrollbar_resultados = ttk.Scrollbar(frame_busqueda, orient=tk.VERTICAL, command=listbox_resultados.yview)
    scrollbar_resultados.grid(row=1, column=2, sticky=tk.NS)
    listbox_resultados.config(yscrollcommand=scrollbar_resultados.set)
    
    label_cantidad_unidades_requeridas = ttk.Label(frame_busqueda, text="Cantidad de Unidades Requeridas:")
    label_cantidad_unidades_requeridas.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
    cantidad_unidades_requeridas = tk.IntVar()
    entry_cantidad_requerida = ttk.Entry(frame_busqueda, textvariable=cantidad_unidades_requeridas, width=30)
    entry_cantidad_requerida.grid(row=5, column=1, padx=10, pady=5)

    label_cantidad_unidades_despachadas = ttk.Label(frame_busqueda, text="Cantidad de Unidades Despachadas:")
    label_cantidad_unidades_despachadas.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
    cantidad_unidades_despachadas = tk.IntVar()
    entry_cantidad_despachada = ttk.Entry(frame_busqueda, textvariable=cantidad_unidades_despachadas, width=30)
    entry_cantidad_despachada.grid(row=6, column=1, padx=10, pady=5)
    
 
    
    def actualizar_busqueda(entry_busqueda, listbox_resultados):
        criterio_busqueda = entry_busqueda.get()
        listbox_resultados.delete(0, tk.END)

        # Accedemos a la variable de la closure

        if criterio_busqueda:
            try:
                connection = psycopg2.connect(
                    host='localhost',
                    user='postgres',
                    password='1234',
                    database='ferreteria'
                )
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM buscar_producto_por_nombre('{criterio_busqueda}')")
                rows = cursor.fetchall()
                for index, row in enumerate(rows):
                    # Formato para mostrar: ID - Nombre - Precio Venta - Cantidad Disponible - Peso
                    listbox_resultados.insert(tk.END, f"{row[0]} - {row[3]} - Precio: {row[7]} - Disponibles: {row[6]} - Peso: {row[5]} kg")
                    
                    tupla = (index, row[0])  # Supongamos que almacenamos más datos del row según sea necesario
                    lista_tuplas.append(tupla)
                connection.close()

                # Función para seleccionar el producto y almacenar el idproducto
              


            except psycopg2.Error as e:
                print(f"Error al buscar productos: {e}")
                messagebox.showerror("Error", "Ocurrió un error al buscar productos en la base de datos.")
    
    def imprimir_primer_indice_():
     def noSeleccion():
    # Crear una ventana emergente
      ventana_exito = tk.Toplevel()
      ventana_exito.title("Éxito")
      ventana_exito.geometry("300x100+500+300")  # Dimensiones y posición de la ventana
      label_exito = tk.Label(ventana_exito, text="No ha seleccionado un producto", padx=20, pady=20)
      label_exito.pack()
      ventana_exito.after(7000, ventana_exito.destroy)

     def mostrar_errorNumerico():
    # Crear una ventana emergente
      ventana_error = tk.Toplevel()
      ventana_error.title("Error!")
      ventana_error.geometry("800x100+500+300")  # Dimensiones y posición de la ventana
      label_error = tk.Label(ventana_error, text="Error, Ingrese valores numéricos para el ID del Pedido, ID del Producto, unidades requeridas y unidades despachadas.", padx=20, pady=20)
      label_error.pack()
      
    # Cerrar la ventana después de 3 segundos (3000 milisegundos)
      ventana_error.after(7000, ventana_error.destroy)
     indices = listbox_resultados.curselection()
     
     if indices:
        primer_indice = indices[0]
        segundo_indice = lista_tuplas[primer_indice][1]
        try:
            unidades_requeridas = int(entry_cantidad_requerida.get())
            unidades_despachadas = int(entry_cantidad_despachada.get())
            
            verificar_existencias(segundo_indice, unidades_requeridas, unidades_despachadas, idpedido)
            
            
        except ValueError:
            mostrar_errorNumerico()
     else:
        noSeleccion()


    btn_guardar_producto = ttk.Button(frame_busqueda, text="Generar factura", command=lambda:  generar_pdf(idpedido))
    btn_guardar_producto.grid(row=8, column=0, columnspan=2, pady=12)

    btn_guardar_producto = ttk.Button(frame_busqueda, text="Cerrar pedido", command=lambda: root.destroy())
    btn_guardar_producto.place(x=260, y=400)
 
    btn_guardar_pedido = ttk.Button(frame_busqueda, text="Guardar producto", command=lambda:imprimir_primer_indice_())
    btn_guardar_pedido.grid(row=7, column=0, columnspan=2, pady=10)
    
    root.mainloop()


def guardar_pedido(listbox_resultados, apellido_cliente, nombre_cliente, direccion_cliente,
                   cantidad_unidades_requeridas, cantidad_unidades_despachadas):
    producto_seleccionado = listbox_resultados.get(tk.ACTIVE)
    if not producto_seleccionado:
        messagebox.showerror("Error", "Seleccione un producto para guardar el pedido.")
        return

    id_producto = producto_seleccionado.split(" - ")[0]

    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        cursor.execute(f"SELECT unidadesEnBodega FROM productos WHERE idProducto = {id_producto}")
        unidades_disponibles = cursor.fetchone()[0]

        if unidades_disponibles is not None:
            if cantidad_unidades_requeridas > unidades_disponibles:
                messagebox.showwarning("Advertencia", "No hay suficientes existencias disponibles.")
                return
        else:
            cursor.execute(f"SELECT pesoEnKg FROM productos WHERE idProducto = {id_producto}")
            peso_producto = cursor.fetchone()[0]
            if peso_producto is not None and peso_producto >= cantidad_unidades_requeridas:
                messagebox.showinfo("Información", "Suficientes existencias disponibles.")
            else:
                messagebox.showwarning("Advertencia", "No hay suficientes existencias disponibles.")
                return

        # Aquí deberías implementar la lógica para guardar el pedido y los datos del cliente en la base de datos PostgreSQL
        
        messagebox.showinfo("Éxito", "Pedido guardado correctamente.")
        connection.commit()

    except psycopg2.Error as e:
        print(f"Error al guardar pedido: {e}")
        messagebox.showerror("Error", "Ocurrió un error al guardar el pedido.")

    finally:
        if connection:
            connection.close()


def crear_interfaz_validacion(idpedido):
    
    idproducto_PPP = 0
    # Configuración de la ventana principal
    ventana = tk.Tk()
    ventana.title("Validación de Existencias e Inserción de Productos")
    ventana.geometry("800x400")
    
    # Frame principal
    frame = ttk.Frame(ventana, padding="20")
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    ttk.Label(frame, text="Validación de Existencias e Inserción de Productos", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
    
    # Mostrar Productos
    # Aquí debes implementar la lógica para mostrar los productos utilizando la función buscarDato
    #def __init__(self, root):
        #self.root = root
        #self.root.title("Búsqueda de Productos")
        #self.root.geometry("800x600")

        #self.frame = ttk.Frame(self.root)
        #self.frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Cuadro de texto para búsqueda
    entry_busqueda = ttk.Entry(frame, width=50)
    entry_busqueda.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        # Botón para realizar la búsqueda


        # Scrollbar para la lista de resultados
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.grid(row=1, column=1, sticky=tk.NS)

        # Listbox para mostrar resultados
    listbox_resultados = tk.Listbox(frame, width=80, yscrollcommand=scrollbar.set)
    listbox_resultados.grid(row=1, column=0, padx=10, pady=10, sticky=tk.NSEW)
    scrollbar.config(command=listbox_resultados.yview)

        # Función para obtener y mostrar resultados según la búsqueda
    def buscar_productos():
            # Limpiar la lista de resultados previos
        listbox_resultados.delete(0, tk.END)
            
            # Obtener el texto de búsqueda
        texto_busqueda = entry_busqueda.get()

            # Conectar a la base de datos PostgreSQL
        try:
            connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='1234',
                database='ferreteria'
            )
            cursor = connection.cursor()

                # Ejecutar la función buscar_producto_por_nombre en PostgreSQL
            cursor.execute("SELECT * FROM buscar_producto_por_nombre(%s)", (texto_busqueda,))
            rows = cursor.fetchall()
            if rows:
             idproducto_PPP = rows[0][0]
            else:
             idproducto_PPP = 0  # Asignar un valor por defecto si no se encontraron resultados

                # Mostrar los resultados en el Listbox
            for row in rows:
                listbox_resultados.insert(tk.END, f"ID: {row[0]}, Nombre: {row[3]}, Peso en kg: {row[5]}, Unidades disponibles {row[6]}, Precio: {row[7]}")  # Ajusta según tus columnas
                
                # Confirmar cambios en la base de datos
                connection.commit()

        except psycopg2.Error as e:
                print(f"Error al buscar productos: {e}")
                messagebox.showerror("Error", "Ocurrió un error al buscar productos.")

        finally:
                # Cerrar la conexión con la base de datos PostgreSQL
                if connection:
                    connection.close()

        # Asociar la función buscar_productos al evento del botón Buscar
    btn_buscar = ttk.Button(frame, text="Buscar", command=buscar_productos)
    btn_buscar.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
    btn_buscar.config(command=buscar_productos)
    # Cantidad de Unidades
    ttk.Label(frame, text="Cantidad de Unidades Requeridas:").grid(row=2, column=0, padx=10, pady=5)
    cantidad_requerida_entry = ttk.Entry(frame, width=30)
    cantidad_requerida_entry.grid(row=2, column=1, padx=10, pady=5)
    
    ttk.Label(frame, text="Cantidad de Unidades Despachadas:").grid(row=3, column=0, padx=10, pady=5)
    cantidad_despachada_entry = ttk.Entry(frame, width=30)
    cantidad_despachada_entry.grid(row=3, column=1, padx=10, pady=5)
    
    # Botón Comprobar Existencias
    btn_comprobar = ttk.Button(frame, text="Comprobar Existencias", 
                               command=lambda: verificar_existencias(idproducto_PPP, 
                                                                    int(cantidad_requerida_entry.get()),
                                                                    int(cantidad_despachada_entry.get()),
                                                                    idpedido))
    btn_comprobar.grid(row=4, column=1, padx=10, pady=10)
    
    # Botón Finalizar Inserción de Productos
    btn_finalizar = ttk.Button(frame, text="Finalizar Inserción de Productos", command=lambda: ventana.destroy())
    btn_finalizar.grid(row=5, column=1, padx=10, pady=10)
    
    ventana.mainloop()

import psycopg2
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

def enviar_correo(destinatario, asunto, cuerpo, archivo_adjunto):
    remitente = "tu_correo@gmail.com"
    password = "tu_contraseña"

    # Crear el objeto del mensaje
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Adjuntar el cuerpo del mensaje
    msg.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar el archivo PDF
    with open(archivo_adjunto, "rb") as attachment:
        part = MIMEApplication(attachment.read(), _subtype="pdf")
        part.add_header('Content-Disposition', 'attachment', filename=archivo_adjunto)
        msg.attach(part)

    # Configurar el servidor SMTP
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, password)
        text = msg.as_string()
        server.sendmail(remitente, destinatario, text)
        server.quit()
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")




def generar_pdf(idPedidoInput):
    try:
        # Establecer la conexión a la base de datos
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        print("Conexion exitosa")

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Consultar los datos del pedido
        cursor.execute("SELECT * FROM sacandoPedidoPDF(%s)", (idPedidoInput,))
        rows = cursor.fetchall()

        # Separar los datos del cliente y del pedido
        datos_cliente = rows[0][6:11]  # Suponiendo que los primeros 5 elementos son datos del cliente
        detalles_pedido = rows  # Todos los datos son detalles del pedido

        # Inicializar el objeto PDF
        pdf = FPDF()
        pdf.add_page()

        # Configurar fuente y tamaño
        pdf.set_font("Arial", size=12)

        # Encabezado en un recuadro
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, "Ferreteria Huerto de Riego", 1, 1, 'C')
        pdf.ln(10)  # Espacio después del encabezado
        
        # Tabla con los datos del cliente
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Datos del Pedido", 0, 1, 'C')
        pdf.ln(5)
        
        pdf.set_font("Arial", size=10)
        pdf.cell(40, 10, "Nombre Recibe", 1)
        pdf.cell(40, 10, "Apellido Recibe", 1)
        pdf.cell(40, 10, "Direccion Destino", 1)
        pdf.cell(40, 10, "Hora Registro", 1)
        pdf.cell(40, 10, "Fecha Registro", 1)
        pdf.ln()

        # Imprimir datos del cliente solo una vez
        pdf.cell(40, 10, str(datos_cliente[0]), 1)
        pdf.cell(40, 10, str(datos_cliente[1]), 1)
        pdf.cell(40, 10, str(datos_cliente[2]), 1)
        pdf.cell(40, 10, str(datos_cliente[3]), 1)
        pdf.cell(40, 10, str(datos_cliente[4]), 1)
        pdf.ln()

        pdf.ln(10)  # Espacio después de la tabla

        # Tabla con detalles del pedido
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Detalle del Pedido", 0, 1, 'C')
        pdf.ln(5)

        pdf.set_font("Arial", size=10)
        pdf.cell(30, 10, "ID Pedido", 1)
        pdf.cell(30, 10, "ID Cliente", 1)
        pdf.cell(30, 10, "Nombre Producto", 1)
        pdf.cell(30, 10, "Precio Unidad", 1)
        pdf.cell(39, 10, "Cantidad Despachada", 1)
        pdf.cell(35, 10, "Monto Total Producto", 1)
        pdf.ln()

        # Imprimir detalles del pedido
        for row in detalles_pedido:
            pdf.cell(30, 10, str(row[0]), 1)
            pdf.cell(30, 10, str(row[1]), 1)
            pdf.cell(30, 10, str(row[2]), 1)
            pdf.cell(30, 10, str(row[3]), 1)
            pdf.cell(39, 10, str(row[4]), 1)
            pdf.cell(35, 10, str(row[5]), 1)
            pdf.ln()

        pdf.ln(10)  # Espacio después de la tabla

        # Calcular el total a pagar
        total = sum(row[5] for row in detalles_pedido)

        # Mostrar el total a pagar
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "Total a Pagar", 1, 1, 'C')
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"${total:.2f}", 1, 1, 'C')

        # Guardar el PDF en la ruta especificada
        pdf_output = f"C:\\Users\\Daniel\\Documents\\recibos\\{idPedidoInput}.pdf"
        pdf.output(pdf_output)

        print(f"PDF generado: {pdf_output}")

        # Enviar el PDF por correo electrónico
        destinatario = "eltanquegavi@gmail.com"
        asunto = f"Pedido {idPedidoInput}"
        cuerpo = "Adjunto encontraras el PDF del pedido."
        #enviar_correo(destinatario, asunto, cuerpo, pdf_output)

    except Exception as ex:
        print(f"Error: {ex}")

    finally:
        # Cerrar la conexión a la base de datos
        if connection:
            connection.close()
            print("Conexion terminada")

def enviar_correo(destinatario, asunto, cuerpo, ruta_archivo):
    remitente = ""
    password = ""

    # Crear la conexión SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remitente, password)

    # Crear el mensaje del correo electrónico
    mensaje = email.mime.multipart.MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = asunto

    # Añadir el cuerpo del mensaje
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Añadir el archivo PDF como adjunto
    with open(ruta_archivo, 'rb') as archivo:
        adjunto = MIMEBase('application', 'octet-stream')
        adjunto.set_payload(archivo.read())
        email.encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', f"attachment; filename={ruta_archivo.split('/')[-1]}")
        mensaje.attach(adjunto)

    # Convertir el mensaje a texto plano
    texto = mensaje.as_string()

    # Enviar el correo electrónico
    try:
        server.sendmail(remitente, destinatario, texto)
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        # Cerrar la conexión SMTP
        server.quit()

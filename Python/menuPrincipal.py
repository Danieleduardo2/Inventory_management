from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from usuarios import *
from usuarios import borrar_usuario_
import os
from mostrarListas import *



def ingresar_usuario():
    def guardar():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        guardar_usuario(nombre, apellido)
        nueva_ventana.destroy()
    
    nueva_ventana = Toplevel()
    nueva_ventana.title("Ingresar usuario")
    nueva_ventana.geometry("200x200")

    label_nombre = Label(nueva_ventana, text="Nombre:")
    label_nombre.pack()
    entry_nombre = Entry(nueva_ventana)
    entry_nombre.pack()

    label_apellido = Label(nueva_ventana, text="Contraseña:")
    label_apellido.pack()
    entry_apellido = Entry(nueva_ventana)
    entry_apellido.pack()

    btn_guardar = Button(nueva_ventana, text="Guardar", command=guardar)
    btn_guardar.pack()

    nueva_ventana.mainloop()

def borrar_usuario():
    def borrar():
        # Obtener el ID del usuario a borrar
        id_usuario = entry_id.get()

        # Validar que se ingresó un ID válido
        if id_usuario == '':
            resultad.config(text="ID de usuario vacío", fg="red")
            resultad.pack(pady=10)
            messagebox.showerror("Error", "Por favor ingrese un ID de usuario")
            return

        # Llamar a la función para borrar el usuario en la base de datos
        borrar_usuario_(id_usuario)

        # Limpiar el campo de entrada después de borrar
        entry_id.delete(0, END)

    nueva_ventana = Toplevel()
    nueva_ventana.title("Borrar usuario")
    nueva_ventana.geometry("400x300")

    label_id = Label(nueva_ventana, text="ID de usuario:")
    label_id.pack(pady=10)

    entry_id = Entry(nueva_ventana, width=30)
    entry_id.pack()
    
    resultad = Label(nueva_ventana, text="", font=("Arial", 12), fg="red")

    btn_borrar = Button(nueva_ventana, text="Borrar", command=borrar)
    btn_borrar.pack(pady=20)

    nueva_ventana.mainloop()

def hacerPedido_():
    nueva_ventana = Toplevel()
    nueva_ventana.title("Calcular ganancias")
    nueva_ventana.geometry("400x300")
    
    # Aquí puedes configurar la ventana para cerrar sesión
    
    nueva_ventana.mainloop()



def seleccionar_opcion(opcion):
    if opcion == "Ingresar usuario":
        ingresar_usuario()
    elif opcion == "Borrar usuario":
        borrar_usuario()
def screen2():

    new_root = Tk()
    new_root.title("Menu principal")
    new_root.geometry("1300x700")

    # Creando boton usuario_________________________________________________________________
    opciones = ["Ingresar usuario", "Borrar usuario", "Cerrar sesión"]
    menu_desplegable = Menubutton(new_root, text="Usuarios", font=('Times new roman', 12), indicatoron=True, borderwidth=2, relief="raised", bg="White")
    menu1 = Menu(menu_desplegable, tearoff=False)
    menu_desplegable.config(menu=menu1)
    
    for opcion in opciones:
        if opcion == "Cerrar sesión":
            menu1.add_command(label=opcion, command=lambda: [new_root.destroy(), os.system('python interfazInit.py')])
        else:
            menu1.add_command(label=opcion, command=lambda op=opcion: seleccionar_opcion(op))
    
    
    menu_desplegable.place(x=10, y=10)
    # Creando boton Mostrar_________________________________________________________________
    def seleccionar_opcionMostrarLista(opcion):
        if opcion == "Mostrar productos ordenados":
           
        # Función para mostrar la ventana de productos ordenados
           def accion_btn1():
            mostrar_productos_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_productos_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_productos_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_productos_ordenados(4, new_root)
            nueva_ventana.destroy()

        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Productos ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. Nombre", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=200, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. Precio unitario de compra", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=200, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Cantidad de unidades disponibles", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=200, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Precio unitario de venta", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=200, height=30)
           
           nueva_ventana.mainloop()

        elif opcion == "Mostrar productos del pedido ordenados":
           # Función para mostrar la ventana de productos ordenados
           def accion_btn1():
            mostrar_productosDelPedido_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_productosDelPedido_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_productosDelPedido_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_productosDelPedido_ordenados(4, new_root)
            nueva_ventana.destroy()
            
        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Productos del pedido ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. id Pedido", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=100, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. id Producto", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=100, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Cantidad de unidades requeridas", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=220, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Cantidad de unidades despachadas", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=230, height=30)
           
           nueva_ventana.mainloop()

        elif opcion == "Mostrar pedidos ordenados":
           
           def accion_btn1():
            mostrar_Pedidos_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_Pedidos_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_Pedidos_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_Pedidos_ordenados(4, new_root)
            nueva_ventana.destroy()
           def accion_btn5():
            mostrar_Pedidos_ordenados(5, new_root)
            nueva_ventana.destroy()
            
        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Pedidos ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. Id pedido", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=100, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. Id cliente", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=100, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Fecha de realizacion", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=220, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Nombre persona que recibe", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=230, height=30)

           btn5 = Button(nueva_ventana, text="5. Direccion destino", command=accion_btn5, bg="white", borderwidth=5, relief="raised")
           btn5.place(x=50, y=250, width=230, height=30)
           
           nueva_ventana.mainloop()

        elif opcion == "Mostrar clientes ordenados":
           
           def accion_btn1():
            mostrar_clientes_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_clientes_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_clientes_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_clientes_ordenados(4, new_root)
            nueva_ventana.destroy()
            
        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Clientes ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. Id cliente", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=100, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. Nombre", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=100, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Apellido", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=220, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Direccion", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=230, height=30)
           
           nueva_ventana.mainloop()
        else:
           print("Opción no reconocida")
    
    def calcularFecha():
     nueva_ventana = Toplevel()
     nueva_ventana.title("Seleccionar Fechas")
     nueva_ventana.geometry("600x400")
    
     fecha_inicio = None
     fecha_fin = None
    
     def obtener_fecha_inicio():
        nonlocal fecha_inicio
        fecha_inicio = cal.get_date()
    
     def obtener_fecha_fin():
        nonlocal fecha_fin
        fecha_fin = cal.get_date()
        nueva_ventana.destroy()
        mostrar_Ganancias_Por_Fecha(fecha_inicio, fecha_fin, new_root)
        
         
        
     cal = Calendar(nueva_ventana, selectmode='day', date_pattern='dd/mm/yyyy')
     cal.pack(pady=20)
    
     btn_obtener_fecha_inicio = Button(nueva_ventana, text="Seleccionar Fecha de Inicio", command=obtener_fecha_inicio)
     btn_obtener_fecha_inicio.pack(pady=10)
    
     btn_obtener_fecha_fin = Button(nueva_ventana, text="Seleccionar Fecha de Fin", command=obtener_fecha_fin)
     btn_obtener_fecha_fin.pack(pady=10)
    
     nueva_ventana.mainloop()

    def buscarT(op):
       def on_buscar_click():
        texto_busqueda = entry_busqueda.get()
        nueva_ventana.destroy()
        # Mapeo de opciones a números
        opciones = {
            "Categorias": 1,
            "Productos": 2,
            "Clientes": 3,
            "Productos del pedido": 4,
            "Usuarios": 5
        }
        # Obtener el número correspondiente a la opción seleccionada
        opcion_seleccionada = opciones[op]
        # Llamar a mostrar_busqueda con el número y el criterio de búsqueda
        mostrar_busqueda(opcion_seleccionada, texto_busqueda, new_root)

       nueva_ventana = tk.Toplevel()
       nueva_ventana.title("Buscar")
       nueva_ventana.geometry("300x200")

       # Frame para organizar widgets
       frame = ttk.Frame(nueva_ventana)
       frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Entrada para el texto de búsqueda
       entry_busqueda = ttk.Entry(frame)
       entry_busqueda.pack(pady=10, padx=20, fill=tk.X)

    # Botón para realizar la búsqueda
       btn_buscar = ttk.Button(frame, text="Buscar", command=on_buscar_click)
       btn_buscar.pack(pady=10)

    # Ejecutar el bucle principal de tkinter
       nueva_ventana.mainloop()

    def seleccionar_Modificacion(opcion):
     if opcion == "Ingresar producto":
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Ingresar Producto")
        nueva_ventana.geometry("500x500")
        
        frame = ttk.Frame(nueva_ventana)
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        try:
            # Conectar a la base de datos PostgreSQL para obtener las categorías
            connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='1234',
                database='ferreteria'
            )
            cursor = connection.cursor()

            # Obtener nombres de categorías desde la base de datos
            cursor.execute("SELECT idCategoria, nombre FROM categorias")
            categorias = cursor.fetchall()

            # Lista de nombres de categorías para el Listbox
            nombres_categorias = [categoria[1] for categoria in categorias]

            # Crear Listbox para seleccionar la categoría
            label_categoria = ttk.Label(frame, text="(obligatorio) Seleccione Categoría:")
            label_categoria.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

            listbox_categorias = tk.Listbox(frame, selectmode=tk.SINGLE, width=30)
            for nombre in nombres_categorias:
                listbox_categorias.insert(tk.END, nombre)
            listbox_categorias.grid(row=0, column=1, padx=10, pady=5)

            # Labels y Entradas para los datos del producto
            ttk.Label(frame, text="Código de Barras:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
            entry_codigo_barras = ttk.Entry(frame, width=30)
            entry_codigo_barras.grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio) Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
            entry_nombre = ttk.Entry(frame, width=30)
            entry_nombre.grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio) Precio Unitario de Compra:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
            entry_precio_compra = ttk.Entry(frame, width=30)
            entry_precio_compra.grid(row=3, column=1, padx=10, pady=5)

            ttk.Label(frame, text="Peso en Kg:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
            entry_peso = ttk.Entry(frame, width=30)
            entry_peso.grid(row=4, column=1, padx=10, pady=5)

            ttk.Label(frame, text="Unidades en Bodega:").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
            entry_unidades_bodega = ttk.Entry(frame, width=30)
            entry_unidades_bodega.grid(row=5, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio)Precio Unitario de Venta:").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
            entry_precio_venta = ttk.Entry(frame, width=30)
            entry_precio_venta.grid(row=6, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio) Cantidad Mínima en Stock:").grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
            entry_cantidad_min_stock = ttk.Entry(frame, width=30)
            entry_cantidad_min_stock.grid(row=7, column=1, padx=10, pady=5)

            # Función para obtener el idCategoria seleccionado
            def obtener_id_categoria():
                indice_seleccionado = listbox_categorias.curselection()
                if indice_seleccionado:
                    id_categoria = categorias[indice_seleccionado[0]][0]  # Obtener idCategoria según el nombre seleccionado
                    return id_categoria
                else:
                    return None

            # Botón para ingresar el producto
            btn_ingresar_producto = ttk.Button(frame, text="Ingresar Producto", command=lambda: on_ingresar_producto())
            btn_ingresar_producto.grid(row=8, column=0, columnspan=2, pady=10)

            # Función para manejar el ingreso del producto
            def on_ingresar_producto():
                idCategoria = obtener_id_categoria()
                if idCategoria:
                    insertar_producto(
                        idCategoria, entry_codigo_barras.get(), entry_nombre.get(), entry_precio_compra.get(),
                        entry_peso.get(), entry_unidades_bodega.get(), entry_precio_venta.get(), entry_cantidad_min_stock.get()
                    )
                    nueva_ventana.destroy()

        except psycopg2.Error as e:
            print(f"Error al obtener categorías desde PostgreSQL: {e}")
            messagebox.showerror("Error", "Ocurrió un error al obtener las categorías.")

        finally:
            # Cerrar la conexión con la base de datos PostgreSQL
            if connection:
                connection.close()

        nueva_ventana.mainloop() 
         
     elif opcion == "Borrar producto":
        def borrar():
        # Obtener el ID del usuario a borrar
         id_producto = entry_id.get()

        # Validar que se ingresó un ID válido
         if id_producto == '':
            resultad.config(text="ID de producto vacío", fg="red")
            resultad.pack(pady=10)
            messagebox.showerror("Error", "Por favor ingrese un ID de producto")
            return

         borrar_producto_(id_producto)

        # Limpiar el campo de entrada después de borrar
         entry_id.delete(0, END)

        nueva_ventana = Toplevel()
        nueva_ventana.title("Borrar producto")
        nueva_ventana.geometry("400x300")

        label_id = Label(nueva_ventana, text="ID de producto:")
        label_id.pack(pady=10)

        entry_id = Entry(nueva_ventana, width=30)
        entry_id.pack()
    
        resultad = Label(nueva_ventana, text="", font=("Arial", 12), fg="red")

        btn_borrar = Button(nueva_ventana, text="Borrar", command=borrar)
        btn_borrar.pack(pady=20)

        nueva_ventana.mainloop() 

     elif opcion == "Actualizar producto":
      def actualizar_producto_():

        try:
          indice_seleccionado = lista_opciones.curselection()[0]
          columna = opciones[indice_seleccionado]
        except IndexError:
           messagebox.showerror("Error", "Debes seleccionar una columna para actualizar.")
           return
         
        id_producto = entrada_id_producto.get()
        nuevo_valor = entrada_nuevo_valor.get()

        if not id_producto.isdigit():
            messagebox.showerror("Error", "El ID del producto debe ser un número.")
            return

        if columna in ["idCategoria", "codigoDeBarras", "nombre", "precioUnitarioDeCompra", 
         "pesoEnKg", "unidadesEnBodega", "precioUnitarioVenta", "CantidadMinStock"]:
            

        # Aquí puedes agregar la lógica para actualizar el producto en tu base de datos
          actualizar_ProductO(columna, nuevo_valor, id_producto)
          messagebox.showinfo("Éxito", f"Producto {id_producto} actualizado con éxito en la columna {columna} con el valor {nuevo_valor}")

      ventana = tk.Tk()
      ventana.title("Actualizar Producto")
      ventana.geometry("400x300")
    # Crear y ubicar el Label y el Scrollbar para las opciones de columna
      label_opciones = tk.Label(ventana, text="Selecciona la columna \n que desea actualizar:")
      label_opciones.grid(row=0, column=0, padx=10, pady=10)

      scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL)
      scrollbar.grid(row=0, column=2, padx=10, pady=10, sticky='ns')

      opciones = [
        "idCategoria", "codigoDeBarras", "nombre", "precioUnitarioDeCompra", 
        "pesoEnKg", "unidadesEnBodega", "precioUnitarioVenta", "CantidadMinStock"
      ]
      lista_opciones = tk.Listbox(ventana, yscrollcommand=scrollbar.set, height=8)
      for opcion in opciones:
       lista_opciones.insert(tk.END, opcion)
      
      lista_opciones.grid(row=0, column=1, padx=10, pady=10)
      scrollbar.config(command=lista_opciones.yview)


    # Crear y ubicar el Label y Entry para el ID del producto
      label_id_producto = tk.Label(ventana, text="ID del Producto:")
      label_id_producto.grid(row=1, column=0, padx=10, pady=10)
      entrada_id_producto = tk.Entry(ventana)
      entrada_id_producto.grid(row=1, column=1, padx=10, pady=10)

    # Crear y ubicar el Label y Entry para el nuevo valor
      label_nuevo_valor = tk.Label(ventana, text="Nuevo Valor:")
      label_nuevo_valor.grid(row=2, column=0, padx=10, pady=10)
      entrada_nuevo_valor = tk.Entry(ventana)
      entrada_nuevo_valor.grid(row=2, column=1, padx=10, pady=10)

    # Botón para actualizar el producto
      boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_producto_)
      boton_actualizar.place(x=120, y=250)

    # Ejecutar la ventana
      ventana.mainloop()


    opcionesMostrar = ["Mostrar productos ordenados", "Mostrar productos del pedido ordenados", "Mostrar pedidos ordenados", "Mostrar clientes ordenados"]
    menu_desplegableMostrar = Menubutton(new_root, text="Mostrar Lista", font=('Times new roman', 12), indicatoron=True, borderwidth=2, relief="raised", bg="White")
    menuMostrar = Menu(menu_desplegableMostrar, tearoff=False)
    menu_desplegableMostrar.config(menu=menuMostrar)
    
    for opcion in opcionesMostrar:
        menuMostrar.add_command(label=opcion, command=lambda op=opcion: seleccionar_opcionMostrarLista(op))
    
    menu_desplegableMostrar.place(x=120, y=10)
#__Creando calcular ganancias__________________________________________________________________________________ 
    btn_calcularGanancias = Button(new_root, text="Calcular ganancias", font=('Times new roman', 12), borderwidth=2, relief="raised", bg="White",
                                   command= calcularFecha)
    btn_calcularGanancias.place(x=260, y=8)
    

#Creando Buscar producto_____________________________________________________________________________________
    opcionesBuscar = ["Categorias", "Productos", "Clientes", "Productos del pedido", "Usuarios"]
    menu_desplegableBuscar = Menubutton(new_root, text="Buscar", font=('Times new roman', 13), indicatoron=True, borderwidth=2, relief="raised", bg="White")
    menuBuscar = Menu(menu_desplegableBuscar, tearoff=False)
    menu_desplegableBuscar.config(menu=menuBuscar)
    
    for opcion in opcionesBuscar:
        menuBuscar.add_command(label=opcion, command=lambda op=opcion: buscarT(op))
    
    menu_desplegableBuscar.place(x=400, y=9)
#Modificando productos________________________________________________

    opcionesCproducto = ["Ingresar producto", "Borrar producto", "Actualizar producto"]
    menu_desplegableProducto = Menubutton(new_root, text="Productos", font=('Times new roman', 13), indicatoron=True, borderwidth=2, relief="raised", bg="White")
    menuProducto = Menu(menu_desplegableProducto, tearoff=False)
    menu_desplegableProducto.config(menu=menuProducto)
    
    for opcion in opcionesCproducto:
        menuProducto.add_command(label=opcion, command=lambda op=opcion: seleccionar_Modificacion(op))
    
    menu_desplegableProducto.place(x=500, y=9)
#Hacer pedido________________________________
    def crear_interfaz_pedido():
     
     def on_avanzar_click():
        avanzar_pantalla(scroll_valor.get(), apellido_entry.get(), nombre_entry.get(), direccion_entry.get())
        

    # Configuración de la ventana principal
     ventana = tk.Tk()
     ventana.title("Ingreso de Datos del Pedido")
     ventana.geometry("400x350")
    
    # Frame principal
     frame = ttk.Frame(ventana, padding="20")
     frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
     ttk.Label(frame, text="Ingreso de Datos del Pedido", font=("Arial", 16)).place(x= 40, y=10)
    
    # Scroll (combo box para guardar cliente o no)
     scroll_valor = tk.IntVar()
     simulate = tk.StringVar()

     scroll = ttk.Combobox(frame, width=27, textvariable=simulate)
     scroll['values'] = ('No guardar cliente', 'Guardar cliente')
     scroll.current(0)
     scroll.place(x=90, y =60)

     scroll_valor.set(1) if simulate == 'Guardar cliente' else scroll_valor.set(0)

    # Campos de Cliente
     ttk.Label(frame, text="Apellido del Cliente:").place(x=20, y=110)
     apellido_entry = ttk.Entry(frame, width=30)
     apellido_entry.place(x=130, y=110)
    
     ttk.Label(frame, text="Nombre del Cliente:").place(x=20, y=140)
     nombre_entry = ttk.Entry(frame, width=30)
     nombre_entry.place(x=130, y=140)
    
     ttk.Label(frame, text="Dirección del Cliente:").place(x=13, y=170)
     direccion_entry = ttk.Entry(frame, width=30)
     direccion_entry.place(x=130, y=170)
     

    # Botón Avanzar
     btn_avanzar = ttk.Button(frame, text="Avanzar", command=lambda: on_avanzar_click())
     btn_avanzar.place(x=130, y=210)
    
 
     ventana.mainloop()
    
    
    
    def registroC():
         crear_interfaz_pedido()
      
      
         
    hacerPedido = Button(new_root, text="Registrar compra", font=('Times new roman', 12), borderwidth=2, relief="raised", bg="White",
                                   command=registroC)
    hacerPedido.place(x=620, y=7)

    

    frame = Frame(new_root,  width=1260, height=570, bg="lightyellow", bd=4, relief="solid")
    frame.place(x=5, y=50)
    
    new_root.mainloop()

def screen3():

    new_root = Tk()
    new_root.title("Menu principal")
    new_root.geometry("1300x700")

    # Creando boton usuario_________________________________________________________________
    opciones = ["Cerrar sesión"]
    menu_desplegable = Menubutton(new_root, text="Usuarios", font=('Times new roman', 12), indicatoron=True, borderwidth=2, relief="raised", bg="White")
    menu1 = Menu(menu_desplegable, tearoff=False)
    menu_desplegable.config(menu=menu1)
    
    for opcion in opciones:
        if opcion == "Cerrar sesión":
            menu1.add_command(label=opcion, command=lambda: [new_root.destroy(), os.system('python interfazInit.py')])
        else:
            menu1.add_command(label=opcion, command=lambda op=opcion: seleccionar_opcion(op))
    
    
    menu_desplegable.place(x=10, y=10)
    # Creando boton Mostrar_________________________________________________________________
    def seleccionar_opcionMostrarLista(opcion):
        if opcion == "Mostrar productos ordenados":
           
        # Función para mostrar la ventana de productos ordenados
           def accion_btn1():
            mostrar_productos_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_productos_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_productos_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_productos_ordenados(4, new_root)
            nueva_ventana.destroy()

        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Productos ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. Nombre", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=200, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. Precio unitario de compra", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=200, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Cantidad de unidades disponibles", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=200, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Precio unitario de venta", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=200, height=30)
           
           nueva_ventana.mainloop()

        elif opcion == "Mostrar productos del pedido ordenados":
           # Función para mostrar la ventana de productos ordenados
           def accion_btn1():
            mostrar_productosDelPedido_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_productosDelPedido_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_productosDelPedido_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_productosDelPedido_ordenados(4, new_root)
            nueva_ventana.destroy()
            
        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Productos del pedido ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. id Pedido", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=100, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. id Producto", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=100, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Cantidad de unidades requeridas", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=220, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Cantidad de unidades despachadas", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=230, height=30)
           
           nueva_ventana.mainloop()

        elif opcion == "Mostrar pedidos ordenados":
           
           def accion_btn1():
            mostrar_Pedidos_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_Pedidos_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_Pedidos_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_Pedidos_ordenados(4, new_root)
            nueva_ventana.destroy()
           def accion_btn5():
            mostrar_Pedidos_ordenados(5, new_root)
            nueva_ventana.destroy()
            
        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Pedidos ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. Id pedido", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=100, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. Id cliente", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=100, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Fecha de realizacion", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=220, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Nombre persona que recibe", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=230, height=30)

           btn5 = Button(nueva_ventana, text="5. Direccion destino", command=accion_btn5, bg="white", borderwidth=5, relief="raised")
           btn5.place(x=50, y=250, width=230, height=30)
           
           nueva_ventana.mainloop()

        elif opcion == "Mostrar clientes ordenados":
           
           def accion_btn1():
            mostrar_clientes_ordenados(1, new_root)
            nueva_ventana.destroy()
           def accion_btn2():
            mostrar_clientes_ordenados(2, new_root)
            nueva_ventana.destroy()
           def accion_btn3():
            mostrar_clientes_ordenados(3, new_root)
            nueva_ventana.destroy()
           def accion_btn4():
            mostrar_clientes_ordenados(4, new_root)
            nueva_ventana.destroy()
            
        # Crear nueva ventana
           nueva_ventana = Toplevel()
           nueva_ventana.geometry('400x300')

           label_im = Label(nueva_ventana, text="Clientes ordenados por:")
           label_im.place(x=20, y=15)

        # Configurar botón 1
           btn1 = Button(nueva_ventana, text="1. Id cliente", command=accion_btn1, bg="white", borderwidth=5, relief="raised")
           btn1.place(x=50, y=50, width=100, height=30)

        # Configurar botón 2
           btn2 = Button(nueva_ventana, text="2. Nombre", command=accion_btn2, bg="white", borderwidth=5, relief="raised")
           btn2.place(x=50, y=100, width=100, height=30)

        # Configurar botón 3
           btn3 = Button(nueva_ventana, text="3. Apellido", command=accion_btn3, bg="white", borderwidth=5, relief="raised")
           btn3.place(x=50, y=150, width=220, height=30)

        # Configurar botón 4
           btn4 = Button(nueva_ventana, text="4. Direccion", command=accion_btn4, bg="white", borderwidth=5, relief="raised")
           btn4.place(x=50, y=200, width=230, height=30)
           
           nueva_ventana.mainloop()
        else:
           print("Opción no reconocida")
    
    def calcularFecha():
     nueva_ventana = Toplevel()
     nueva_ventana.title("Seleccionar Fechas")
     nueva_ventana.geometry("600x400")
    
     fecha_inicio = None
     fecha_fin = None
    
     def obtener_fecha_inicio():
        nonlocal fecha_inicio
        fecha_inicio = cal.get_date()
    
     def obtener_fecha_fin():
        nonlocal fecha_fin
        fecha_fin = cal.get_date()
        nueva_ventana.destroy()
        mostrar_Ganancias_Por_Fecha(fecha_inicio, fecha_fin, new_root)
        
         
        
     cal = Calendar(nueva_ventana, selectmode='day', date_pattern='dd/mm/yyyy')
     cal.pack(pady=20)
    
     btn_obtener_fecha_inicio = Button(nueva_ventana, text="Seleccionar Fecha de Inicio", command=obtener_fecha_inicio)
     btn_obtener_fecha_inicio.pack(pady=10)
    
     btn_obtener_fecha_fin = Button(nueva_ventana, text="Seleccionar Fecha de Fin", command=obtener_fecha_fin)
     btn_obtener_fecha_fin.pack(pady=10)
    
     nueva_ventana.mainloop()

    def buscarT(op):
       def on_buscar_click():
        texto_busqueda = entry_busqueda.get()
        nueva_ventana.destroy()
        # Mapeo de opciones a números
        opciones = {
            "Categorias": 1,
            "Productos": 2,
            "Clientes": 3,
            "Productos del pedido": 4,
            "Usuarios": 5
        }
        # Obtener el número correspondiente a la opción seleccionada
        opcion_seleccionada = opciones[op]
        # Llamar a mostrar_busqueda con el número y el criterio de búsqueda
        mostrar_busqueda(opcion_seleccionada, texto_busqueda, new_root)

       nueva_ventana = tk.Toplevel()
       nueva_ventana.title("Buscar")
       nueva_ventana.geometry("300x200")

       # Frame para organizar widgets
       frame = ttk.Frame(nueva_ventana)
       frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

    # Entrada para el texto de búsqueda
       entry_busqueda = ttk.Entry(frame)
       entry_busqueda.pack(pady=10, padx=20, fill=tk.X)

    # Botón para realizar la búsqueda
       btn_buscar = ttk.Button(frame, text="Buscar", command=on_buscar_click)
       btn_buscar.pack(pady=10)

    # Ejecutar el bucle principal de tkinter
       nueva_ventana.mainloop()

    def seleccionar_Modificacion(opcion):
     if opcion == "Ingresar producto":
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Ingresar Producto")
        nueva_ventana.geometry("500x500")

        frame = ttk.Frame(nueva_ventana)
        frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        try:
            # Conectar a la base de datos PostgreSQL para obtener las categorías
            connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='1234',
                database='ferreteria'
            )
            cursor = connection.cursor()

            # Obtener nombres de categorías desde la base de datos
            cursor.execute("SELECT idCategoria, nombre FROM categorias")
            categorias = cursor.fetchall()

            # Lista de nombres de categorías para el Listbox
            nombres_categorias = [categoria[1] for categoria in categorias]

            # Crear Listbox para seleccionar la categoría
            label_categoria = ttk.Label(frame, text="(obligatorio) Seleccione Categoría:")
            label_categoria.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

            listbox_categorias = tk.Listbox(frame, selectmode=tk.SINGLE, width=30)
            for nombre in nombres_categorias:
                listbox_categorias.insert(tk.END, nombre)
            listbox_categorias.grid(row=0, column=1, padx=10, pady=5)

            # Labels y Entradas para los datos del producto
            ttk.Label(frame, text="Código de Barras:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
            entry_codigo_barras = ttk.Entry(frame, width=30)
            entry_codigo_barras.grid(row=1, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio) Nombre:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
            entry_nombre = ttk.Entry(frame, width=30)
            entry_nombre.grid(row=2, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio) Precio Unitario de Compra:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
            entry_precio_compra = ttk.Entry(frame, width=30)
            entry_precio_compra.grid(row=3, column=1, padx=10, pady=5)

            ttk.Label(frame, text="Peso en Kg:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
            entry_peso = ttk.Entry(frame, width=30)
            entry_peso.grid(row=4, column=1, padx=10, pady=5)

            ttk.Label(frame, text="Unidades en Bodega:").grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
            entry_unidades_bodega = ttk.Entry(frame, width=30)
            entry_unidades_bodega.grid(row=5, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio)Precio Unitario de Venta:").grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
            entry_precio_venta = ttk.Entry(frame, width=30)
            entry_precio_venta.grid(row=6, column=1, padx=10, pady=5)

            ttk.Label(frame, text="(obligatorio) Cantidad Mínima en Stock:").grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
            entry_cantidad_min_stock = ttk.Entry(frame, width=30)
            entry_cantidad_min_stock.grid(row=7, column=1, padx=10, pady=5)

            # Función para obtener el idCategoria seleccionado
            def obtener_id_categoria():
                indice_seleccionado = listbox_categorias.curselection()
                if indice_seleccionado:
                    id_categoria = categorias[indice_seleccionado[0]][0]  # Obtener idCategoria según el nombre seleccionado
                    return id_categoria
                else:
                    return None

            # Botón para ingresar el producto
            btn_ingresar_producto = ttk.Button(frame, text="Ingresar Producto", command=lambda: on_ingresar_producto())
            btn_ingresar_producto.grid(row=8, column=0, columnspan=2, pady=10)

            # Función para manejar el ingreso del producto
            def on_ingresar_producto():
                idCategoria = obtener_id_categoria()
                if idCategoria:
                    insertar_producto(
                        idCategoria, entry_codigo_barras.get(), entry_nombre.get(), entry_precio_compra.get(),
                        entry_peso.get(), entry_unidades_bodega.get(), entry_precio_venta.get(), entry_cantidad_min_stock.get()
                    )
                    nueva_ventana.destroy()

        except psycopg2.Error as e:
            print(f"Error al obtener categorías desde PostgreSQL: {e}")
            messagebox.showerror("Error", "Ocurrió un error al obtener las categorías.")

        finally:
            # Cerrar la conexión con la base de datos PostgreSQL
            if connection:
                connection.close()

        nueva_ventana.mainloop() 
         
     elif opcion == "Borrar producto":
        def borrar():
        # Obtener el ID del usuario a borrar
         id_producto = entry_id.get()

        # Validar que se ingresó un ID válido
         if id_producto == '':
            resultad.config(text="ID de producto vacío", fg="red")
            resultad.pack(pady=10)
            messagebox.showerror("Error", "Por favor ingrese un ID de producto")
            return

         borrar_producto_(id_producto)

        # Limpiar el campo de entrada después de borrar
         entry_id.delete(0, END)

        nueva_ventana = Toplevel()
        nueva_ventana.title("Borrar producto")
        nueva_ventana.geometry("400x300")

        label_id = Label(nueva_ventana, text="ID de producto:")
        label_id.pack(pady=10)

        entry_id = Entry(nueva_ventana, width=30)
        entry_id.pack()
    
        resultad = Label(nueva_ventana, text="", font=("Arial", 12), fg="red")

        btn_borrar = Button(nueva_ventana, text="Borrar", command=borrar)
        btn_borrar.pack(pady=20)

        nueva_ventana.mainloop() 

     elif opcion == "Actualizar producto":
      def actualizar_producto_():

        try:
          indice_seleccionado = lista_opciones.curselection()[0]
          columna = opciones[indice_seleccionado]
        except IndexError:
           messagebox.showerror("Error", "Debes seleccionar una columna para actualizar.")
           return
         
        id_producto = entrada_id_producto.get()
        nuevo_valor = entrada_nuevo_valor.get()

        if not id_producto.isdigit():
            messagebox.showerror("Error", "El ID del producto debe ser un número.")
            return

        if columna in ["idCategoria", "codigoDeBarras", "nombre", "precioUnitarioDeCompra", 
         "pesoEnKg", "unidadesEnBodega", "precioUnitarioVenta", "CantidadMinStock"]:
            

        # Aquí puedes agregar la lógica para actualizar el producto en tu base de datos
          actualizar_ProductO(columna, nuevo_valor, id_producto)
          messagebox.showinfo("Éxito", f"Producto {id_producto} actualizado con éxito en la columna {columna} con el valor {nuevo_valor}")

      ventana = tk.Tk()
      ventana.title("Actualizar Producto")
      ventana.geometry("400x300")
    # Crear y ubicar el Label y el Scrollbar para las opciones de columna
      label_opciones = tk.Label(ventana, text="Selecciona la columna \n que desea actualizar:")
      label_opciones.grid(row=0, column=0, padx=10, pady=10)

      scrollbar = tk.Scrollbar(ventana, orient=tk.VERTICAL)
      scrollbar.grid(row=0, column=2, padx=10, pady=10, sticky='ns')

      opciones = [
        "idCategoria", "codigoDeBarras", "nombre", "precioUnitarioDeCompra", 
        "pesoEnKg", "unidadesEnBodega", "precioUnitarioVenta", "CantidadMinStock"
      ]
      lista_opciones = tk.Listbox(ventana, yscrollcommand=scrollbar.set, height=8)
      for opcion in opciones:
       lista_opciones.insert(tk.END, opcion)
      
      lista_opciones.grid(row=0, column=1, padx=10, pady=10)
      scrollbar.config(command=lista_opciones.yview)


    # Crear y ubicar el Label y Entry para el ID del producto
      label_id_producto = tk.Label(ventana, text="ID del Producto:")
      label_id_producto.grid(row=1, column=0, padx=10, pady=10)
      entrada_id_producto = tk.Entry(ventana)
      entrada_id_producto.grid(row=1, column=1, padx=10, pady=10)

    # Crear y ubicar el Label y Entry para el nuevo valor
      label_nuevo_valor = tk.Label(ventana, text="Nuevo Valor:")
      label_nuevo_valor.grid(row=2, column=0, padx=10, pady=10)
      entrada_nuevo_valor = tk.Entry(ventana)
      entrada_nuevo_valor.grid(row=2, column=1, padx=10, pady=10)

    # Botón para actualizar el producto
      boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_producto_)
      boton_actualizar.place(x=120, y=250)

    # Ejecutar la ventana
      ventana.mainloop()


    opcionesMostrar = ["Mostrar productos ordenados", "Mostrar productos del pedido ordenados", "Mostrar pedidos ordenados", "Mostrar clientes ordenados"]
    menu_desplegableMostrar = Menubutton(new_root, text="Mostrar Lista", font=('Times new roman', 12), indicatoron=True, borderwidth=2, relief="raised", bg="White")
    menuMostrar = Menu(menu_desplegableMostrar, tearoff=False)
    menu_desplegableMostrar.config(menu=menuMostrar)
    
    for opcion in opcionesMostrar:
        menuMostrar.add_command(label=opcion, command=lambda op=opcion: seleccionar_opcionMostrarLista(op))
    
    menu_desplegableMostrar.place(x=120, y=10)
#__Creando calcular ganancias__________________________________________________________________________________ 
  
    

#Creando Buscar producto_____________________________________________________________________________________
    opcionesBuscar = ["Categorias", "Productos", "Clientes", "Productos del pedido", "Usuarios"]
    menu_desplegableBuscar = Menubutton(new_root, text="Buscar", font=('Times new roman', 13), indicatoron=True, borderwidth=2, relief="raised", bg="White")
    menuBuscar = Menu(menu_desplegableBuscar, tearoff=False)
    menu_desplegableBuscar.config(menu=menuBuscar)
    
    for opcion in opcionesBuscar:
        menuBuscar.add_command(label=opcion, command=lambda op=opcion: buscarT(op))
    
    menu_desplegableBuscar.place(x=400, y=9)
#Modificando productos________________________________________________

 
#Hacer pedido________________________________
    def crear_interfaz_pedido():
     
     def on_avanzar_click():
        avanzar_pantalla(scroll_valor.get(), apellido_entry.get(), nombre_entry.get(), direccion_entry.get())
        

    # Configuración de la ventana principal
     ventana = tk.Tk()
     ventana.title("Ingreso de Datos del Pedido")
     ventana.geometry("400x350")
    
    # Frame principal
     frame = ttk.Frame(ventana, padding="20")
     frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
     ttk.Label(frame, text="Ingreso de Datos del Pedido", font=("Arial", 16)).place(x= 40, y=10)
    
    # Scroll (combo box para guardar cliente o no)
     scroll_valor = tk.IntVar()
     simulate = tk.StringVar()

     scroll = ttk.Combobox(frame, width=27, textvariable=simulate)
     scroll['values'] = ('No guardar cliente', 'Guardar cliente')
     scroll.current(0)
     scroll.place(x=90, y =60)

     scroll_valor.set(1) if simulate == 'Guardar cliente' else scroll_valor.set(0)

    # Campos de Cliente
     ttk.Label(frame, text="Apellido del Cliente:").place(x=20, y=110)
     apellido_entry = ttk.Entry(frame, width=30)
     apellido_entry.place(x=130, y=110)
    
     ttk.Label(frame, text="Nombre del Cliente:").place(x=20, y=140)
     nombre_entry = ttk.Entry(frame, width=30)
     nombre_entry.place(x=130, y=140)
    
     ttk.Label(frame, text="Dirección del Cliente:").place(x=13, y=170)
     direccion_entry = ttk.Entry(frame, width=30)
     direccion_entry.place(x=130, y=170)
     

    # Botón Avanzar
     btn_avanzar = ttk.Button(frame, text="Avanzar", command=lambda: on_avanzar_click())
     btn_avanzar.place(x=130, y=210)
    
 
     ventana.mainloop()
    
    
    
    def registroC():
         crear_interfaz_pedido()
      
      
         
    hacerPedido = Button(new_root, text="Registrar compra", font=('Times new roman', 12), borderwidth=2, relief="raised", bg="White",
                                   command=registroC)
    hacerPedido.place(x=620, y=7)

    

    frame = Frame(new_root,  width=1260, height=570, bg="lightyellow", bd=4, relief="solid")
    frame.place(x=5, y=50)
    
    new_root.mainloop()

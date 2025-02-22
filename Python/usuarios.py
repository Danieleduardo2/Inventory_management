import psycopg2
from tkinter import messagebox
fuente = ('Arial', 10, 'bold') 
# Función para guardar un usuario en la base de datos PostgreSQL
def guardar_usuario(nombre, contraseña):
    try:
        # Conectar a la base de datos PostgreSQL
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='1234',
            database='ferreteria'
        )
        cursor = connection.cursor()

        # Insertar el usuario en la tabla usuarios
        cursor.execute('''
            INSERT INTO usuarios (nombre, contraseña)
            VALUES (%s, %s)
        ''', (nombre, contraseña))

        # Confirmar la transacción
        connection.commit()
        print(f"Usuario guardado en la base de datos: {nombre} {contraseña}")
        messagebox.showinfo("Guardado exitoso", f"EL usuario ha sido guardado con exito")

    except psycopg2.Error as e:
        print(f"Error al insertar usuario en la base de datos PostgreSQL: {e}")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()

def borrar_usuario_(id_usuario):


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
            SELECT * FROM usuarios WHERE idUsuario = %s
        ''', (id_usuario,))
        usuario = cursor.fetchone()

        if usuario:
            # Si el usuario existe, borrarlo de la base de datos
            cursor.execute('''
                DELETE FROM usuarios WHERE idUsuario = %s
            ''', (id_usuario,))
            connection.commit()
            messagebox.showinfo("Éxito", f"Usuario con ID {id_usuario} ha sido borrado correctamente")
        else:
            messagebox.showerror("Error", f"No se encontró ningún usuario con ID {id_usuario}")

    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Error al borrar usuario: {e}")

    finally:
        # Cerrar la conexión con la base de datos PostgreSQL
        if connection:
            connection.close()


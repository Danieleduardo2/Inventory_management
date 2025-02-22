import psycopg2

class Funcionalidades:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host='localhost',
                user='postgres',
                password='1234',
                database='ferreteria'
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa")
        except Exception as ex:
            print(f"Error al conectar a la base de datos: {ex}")

    def iniciar_sesion(self, usuario, contraseña):
        try:
            query = "SELECT 1 FROM usuarios WHERE nombre = %s AND contraseña = %s"
            self.cursor.execute(query, (usuario, contraseña))
            result = self.cursor.fetchone()
            if result:
                return True
            else:
                return False
        except Exception as ex:
            print(f"Error al verificar credenciales: {ex}")
            return False

    def __del__(self):
        try:
            self.cursor.close()
            self.connection.close()
            print("Conexión terminada")
        except Exception as ex:
            print(f"Error al cerrar la conexión: {ex}")

# Ejemplo de uso


import psycopg2
from psycopg2 import sql


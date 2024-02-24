"""Sistema de Gestión de Biblioteca
Contexto: Desarrolla una aplicación de terminal para gestionar una biblioteca, 
que permita a los usuarios buscar, reservar y prestar libros. 
El sistema debe manejar información de libros, usuarios y préstamos.

"""


import pickle

def guardar_datos(biblioteca, usuarios):
    with open('datos_biblioteca.pkl', 'wb') as f:
        pickle.dump((biblioteca, usuarios), f)

def cargar_datos():
    try:
        with open('datos_biblioteca.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return [], []


class Libro:
    def __init__(self, titulo, autor, cantidad=1):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

biblioteca = []
usuarios = []

def agregar_libro(biblioteca, titulo, autor):
    for libro in biblioteca:
        if libro.titulo == titulo and libro.autor == autor:
            libro.cantidad += 1
            return
    biblioteca.append(Libro(titulo, autor))

def mostrar_libros(biblioteca):
    for libro in biblioteca:
        print(f"Titulo: {libro.titulo}, Autor: {libro.autor}, Cantidad: {libro.cantidad}, Disponible: {libro.disponible}")

def prestar_libro(biblioteca, titulo, nombre_usuario):
    for libro in biblioteca:
        if libro.titulo == titulo and libro.disponible:
            libro.disponible = False
            libro.cantidad -= 1
            for usuario in usuarios:
                if usuario.nombre == nombre_usuario:
                    usuario.libros_prestados.append(libro)
                    return
    print("Libro no disponible o usuario no registrado.")

def registrar_usuario(usuarios, nombre):
    usuarios.append(Usuario(nombre))

def guardar_datos(biblioteca, usuarios):
    with open('datos_biblioteca.pkl', 'wb') as f:
        pickle.dump((biblioteca, usuarios), f)

def cargar_datos():
    try:
        with open('datos_biblioteca.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return [], []

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(usuario.nombre)

def listar_libros_usuario(usuarios, nombre_usuario):
    for usuario in usuarios:
        if usuario.nombre == nombre_usuario:
            for libro in usuario.libros_prestados:
                print(libro.titulo)

def devolver_libro(biblioteca, usuarios, titulo, nombre_usuario):
    for usuario in usuarios:
        if usuario.nombre == nombre_usuario:
            for libro in usuario.libros_prestados:
                if libro.titulo == titulo:
                    libro.disponible = True
                    libro.cantidad += 1
                    usuario.libros_prestados.remove(libro)
                    return
    print("Libro no encontrado o usuario no registrado.")

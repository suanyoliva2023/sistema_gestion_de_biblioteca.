from biblioteca import *
def menu():
    print("Bienvenido al sistema de Gestion de Biblioteca")
    print("1.Agregar libro")
    print("2.Mostrar libro")
    print("3.prestar libro")
    print("4.Registrar usuario")
    print("5.listar Usuario")
    print("6.listar libros de usuarios")
    print("7. Devolver libro")
    print("8.salir")
    
    
    
def main():
    biblioteca, usuarios = cargar_datos()
    while True:
        menu()
        opcion = input("Elige una opcion: ")
        if opcion == '1':
            titulo = input("Introduce el título del libro: ")
            autor = input("Introduce el autor del libro: ")
            agregar_libro(biblioteca, titulo, autor)
        elif opcion == '2':
            mostrar_libros(biblioteca)
        elif opcion == '3':
            titulo = input("Introduce el título del libro: ")
            nombre_usuario = input("Introduce el nombre del usuario: ")
            prestar_libro(biblioteca, titulo, nombre_usuario)
        elif opcion == '4':
            nombre = input("Introduce el nombre del usuario: ")
            registrar_usuario(usuarios, nombre)
        elif opcion == '5':
            listar_usuarios(usuarios)
        elif opcion == '6':
            nombre_usuario = input("Introduce el nombre del usuario: ")
            listar_libros_usuario(usuarios, nombre_usuario)
        elif opcion == '7':
            titulo = input("Introduce el título del libro: ")
            nombre_usuario = input("Introduce el nombre del usuario: ")
            devolver_libro(biblioteca, usuarios, titulo, nombre_usuario)
        elif opcion == '8':
            guardar_datos(biblioteca, usuarios)
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

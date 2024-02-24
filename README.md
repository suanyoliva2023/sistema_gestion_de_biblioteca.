# sistema_gestion_de_biblioteca.
Diseño y Creación de una Aplicación de Terminal Interactiva con Python
Sistema de Gestión de Biblioteca
Contexto: Desarrolla una aplicación de terminal para gestionar una biblioteca, que permita a los usuarios buscar, reservar y prestar libros. El sistema debe manejar información de libros, usuarios y préstamos.

Las funciones a implementar son:

Agregar Libro: Esta función recibe los datos del libro (título, autor). Si el libro ya existe en la biblioteca, aumenta su cantidad en uno. Si el libro no existe, lo agrega con una cantidad inicial de 1.

Mostrar Libros: Esta función muestra la lista de libros en la biblioteca junto con su autor, cantidad y disponibilidad (disponible o no disponible) en la consola.

Prestar Libro: Esta función permite prestar un libro a un usuario dado su título y nombre de usuario. Verifica si el libro está disponible y si el usuario está registrado. Si ambos criterios se cumplen, presta el libro al usuario y actualiza la disponibilidad del libro y la cantidad en la biblioteca.

Registrar Usuario: Agrega un usuario a la biblioteca.

Guardar Datos: Guarda los datos actuales de la biblioteca (libros y usuarios) en un archivo llamado datos_biblioteca.pkl utilizando el módulo pickle.

Cargar Datos: Intenta cargar los datos previos de la biblioteca desde el archivo 'datos_biblioteca.pkl' utilizando pickle. Si el archivo no existe inicializar la biblioteca como vacía.

Listar Usuarios: Muestra una lista de los usuarios registrados en la biblioteca en la consola.

Listar Libros de Usuarios: Muestra una lista de libros prestados a un usuario específico.

Devolver Libro: Permite a un usuario devolver un libro prestado. Si el usuario tiene el libro y lo devuelve correctamente, actualiza la disponibilidad y la cantidad del libro en la biblioteca.

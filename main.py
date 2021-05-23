# Import modulos
import pedido as mod_pedido
import ingredientes as mod_ingredientes

# VARIABLES GLOBALES
sandwiches_tamano: dict = {
	"t": {
		"tipo": "Triple",
		"precio": 580
	},
	"d": {
		"tipo": "Doble",
		"precio": 430
	},
	"i": {
		"tipo": "Individual",
		"precio": 280
	}
}
ingredientes_adicionales: dict = {
	"ja": {
		"nombre": "Jamón",
		"precio": 40
	},
	"ch": {
		"nombre": "Champiñones",
		"precio": 35
	},
	"pi": {
		"nombre": "Pimentón",
		"precio": 30
	},
	"dq": {
		"nombre": "Doble queso",
		"precio": 40
	},
	"ac": {
		"nombre": "Aceitunas",
		"precio": 57.5
	},
	"pe": {
		"nombre": "Pepperoni",
		"precio": 38.5
	},
	"sa": {
		"nombre": "Salchichón",
		"precio": 62.5
	}
}
historico_pedidos: list = []

CANTIDAD_DE_RELLENO = 100


# FUNCIONES
def menu_principal():
	# definición de __doc__
	"""
	Punto de partida para el proyecto, se muestra un menu con las diferentes opciones disponibles
	1- Realizar pedido
	2- Gestión de ingredientes
	3- Estadísticas de ventas
	"""
	opcion_menu = "s"
	while True:
		print("*" * CANTIDAD_DE_RELLENO)
		print("¡Bienvenido a Sanguchito+!")
		print()
		print("\t 1- Realizar pedido")
		print("\t 2- Gestionar ingredientes")
		print("\t 3- Ver estadísticas de ventas")
		print("\t s- Salir")
		print()

		if opcion_menu not in ("1", "2", "3", "s"):
			print("Opción inválida, por favor ingrese una opción válida!")

		opcion_menu = input("Ingrese número de opción: ")
		if opcion_menu == "s":
			# Salir
			break

		elif opcion_menu == "1":
			# Invocador de pedidos
			pedido_temporal : list = mod_pedido.realizar_pedido(sandwiches_tamano, ingredientes_adicionales)
			# Agregamos pedido al historico
			historico_pedidos.extend(pedido_temporal)

			# Impresion de factura

		elif opcion_menu == "2":
			# Invocador de gestion de ingredientes
			submenu_gestion_ingredientes()

		elif opcion_menu == "3":
			# Invocador de estadisticas
			pass


def submenu_gestion_ingredientes():
	# definición de __doc__
	"""
		Punto de partida para la gestion de ingredientes, se invocan funciones del modulo
		A- Agregar ingredientes
		E- Eliminar ingredientes
	"""
	global ingredientes_adicionales
	opcion_submenu = "s"
	while True:
		print()
		print("\t\t A- Agregar ingredientes")
		print("\t\t E- Eliminar ingredientes")
		print("\t\t s- Volver a menú principal")
		print()

		if opcion_submenu not in ("A", "a", "E", "e", "s"):
			print("Opción inválida, por favor ingrese una opción válida!")
		opcion_submenu = input("Ingrese la opción que desee: ")

		if opcion_submenu in ("A", "a"):
			# Agregar ing
			ingredientes_adicionales = mod_ingredientes.agregar_ingredientes(ingredientes_adicionales)

		elif opcion_submenu in ("E", "e"):
			# Eliminar ing
			ingredientes_adicionales = mod_ingredientes.eliminar_ingredientes(ingredientes_adicionales)

		elif opcion_submenu == "s":
			break


# Punto de entrada del proyecto
if __name__ == "__main__":
	print("Ejecutando desde consola")
	menu_principal()

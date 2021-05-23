# Import módulos
import pedido as mod_pedido
import ingredientes as mod_ingredientes
import impresora_fiscal as mod_impresora

# Cantidad de "*" a rellenar en consola
CANTIDAD_DE_RELLENO = 100


def menu_principal() -> None:
	# definición de __doc__
	"""
	Punto de partida para el proyecto, se muestra un menu con las diferentes opciones disponibles
		1- Realizar pedido
		2- Gestión de ingredientes
		3- Estadísticas de ventas
	"""
	
	# Estructuras de datos utilizadas
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

	# Menu con sus opciones
	opcion_menu: str = "s"
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

		# se solicita la opción
		opcion_menu = input("Ingrese número de opción: ")

		# salir
		if opcion_menu == "s":
			break

		# realizar pedido
		elif opcion_menu == "1":
			# Invocador de gestion de pedidos
			submenu_pedidos(sandwiches_tamano, ingredientes_adicionales, historico_pedidos)
			pass

		# gestionar ingredientes (agregar o eliminar)
		elif opcion_menu == "2":
			# Invocador de gestión de ingredientes
			ingredientes_adicionales = submenu_gestion_ingredientes(ingredientes_adicionales)

		elif opcion_menu == "3":
			# Invocador de estadísticas
			pass


def submenu_pedidos(sandwiches_tamano: dict, ingredientes_adicionales: dict, historico_pedidos: list):
	# definición de __doc__
	"""
		Punto de partida para realizar un pedido
		Se invoca la gestión de pedido
		Luego la impresión de la factura
	"""
	# Invocador de gestion de pedidos
	pedido_temporal: list = mod_pedido.realizar_pedido(sandwiches_tamano, ingredientes_adicionales)

	# Agregamos pedido al histórico
	historico_pedidos.extend(pedido_temporal)
	
	# Impresión de factura
	mod_impresora.imprimir_factura(pedido_temporal)


def submenu_gestion_ingredientes(ingredientes_adicionales: dict) -> dict:
	# definición de __doc__
	"""
		Punto de partida para la gestión de ingredientes, se invocan funciones del modulo
		A- Agregar ingredientes
		E- Eliminar ingredientes
	"""

	# submenu de gestión de ingredientes
	opcion_submenu: str = "s"
	while True:
		print()
		print("\t\t A- Agregar ingredientes")
		print("\t\t E- Eliminar ingredientes")
		print("\t\t s- Volver a menú principal")
		print()
		
		# opción invalida
		if opcion_submenu not in ("A", "a", "E", "e", "s"):
			print("Opción inválida, por favor ingrese una opción válida!")

		# input de opción
		opcion_submenu = input("Ingrese la opción que desee: ")

		# si la opción es agregar
		if opcion_submenu in ("A", "a"):
			# Agregar ingredientes
			ingredientes_adicionales = mod_ingredientes.agregar_ingredientes(ingredientes_adicionales)

		# si la opción es eliminar
		elif opcion_submenu in ("E", "e"):
			# Eliminar ingredientes
			ingredientes_adicionales = mod_ingredientes.eliminar_ingredientes(ingredientes_adicionales)

		# si desea salir
		elif opcion_submenu == "s":
			break
	
	return ingredientes_adicionales


# Punto de entrada del proyecto
if __name__ == "__main__":
	menu_principal()


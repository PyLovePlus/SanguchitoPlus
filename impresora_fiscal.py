# cantidad de '*' o '-' a colocar en consola
CANTIDAD_DE_RELLENO: int = 100
DATOS_EMPRESA = ("Sanguchito+ S.A.",
                 "Caracas, Venezuela",
                 "(0212) 123-4567")


#METODOS
def imprimir_factura (pedido_realizado: list):
	# definición de __doc__
	"""
		Punto de partida para imprimir factura
		Argumento:
			Estructura de pedido realizado a imprimir
	"""
	total_pagar = 0.0
	print("*" * CANTIDAD_DE_RELLENO)
	print()

	# Encabezado factura
	print(("=" * (CANTIDAD_DE_RELLENO // 2)).center(CANTIDAD_DE_RELLENO))
	print(DATOS_EMPRESA[0].center(CANTIDAD_DE_RELLENO))
	print(DATOS_EMPRESA[1].center(CANTIDAD_DE_RELLENO))
	print(DATOS_EMPRESA[2].center(CANTIDAD_DE_RELLENO))
	print(("=" * (CANTIDAD_DE_RELLENO // 2)).center(CANTIDAD_DE_RELLENO))

	print()
	print(("\t ITEM".ljust(CANTIDAD_DE_RELLENO // 4) + "PRECIO \t".rjust(CANTIDAD_DE_RELLENO // 4))
		.center(CANTIDAD_DE_RELLENO))

	# Sección de detalle
	for sandwich in pedido_realizado:
		total_pagar += __detalle_sandwich(sandwich)

	# Totalizar
	print(f"Total a pagar: {total_pagar}".rjust(50).center(CANTIDAD_DE_RELLENO))

	# Input para espera
	input()


def __detalle_sandwich (pedido_sandwich: dict) -> float:
	# definición de __doc__
	"""
		Encargado de imprimir detalle de cada sandwich en un pedido
		Argumento
			Un sandwich con su ingredientes
	"""
	subtotal_sandwhich: float = 0.0


	# Linea detalle Sandwich
	linea_sandwich = (
			f"\t Sandwich {pedido_sandwich['tipo']}".ljust(CANTIDAD_DE_RELLENO // 4) + f"{float(pedido_sandwich['precio'])}    \t".format("%10.2f").rjust(CANTIDAD_DE_RELLENO // 4))\
		.center(CANTIDAD_DE_RELLENO)
	print(linea_sandwich)

	subtotal_sandwhich += pedido_sandwich['precio']

	# Detalle por ingrediente
	for ing in pedido_sandwich["ingredientes"]:
		subtotal_sandwhich += ing['precio']
		linea_ing = (
			f"\t  {ing['nombre']}".ljust(CANTIDAD_DE_RELLENO//4) + f"{float(ing['precio'])}    \t".format("%10.2f").rjust(CANTIDAD_DE_RELLENO // 4)
		).center(CANTIDAD_DE_RELLENO)
		print(linea_ing)

	# Imprimir subtotal
	print(f" {subtotal_sandwhich}".format("%10.2f").rjust(50, "-").center(CANTIDAD_DE_RELLENO))
	print()

	return subtotal_sandwhich

#Estadísticas de ventas - Cant de sandwich por tipo vendido y cant total

from pprint import *

def tipo_vendidos (hist_pedidos: list):
	i = j = ind = dob = tri = total = 0

	for i in range(0, len(hist_pedidos)):
		if hist_pedidos[i]['alias'] == 'i':
			ind += 1
		elif hist_pedidos[i]['alias'] == 'd':
			dob += 1
		else:
			tri += 1

	total = ind + dob + tri
	print("\tLa cantidad total de 'sanguchitos' vendidos son: ", total)
	print("\tLa cantidad de 'sanguchitos' de tipo individual vendidos son: ", ind)
	print("\tLa cantidad de 'sanguchitos' de tipo doble vendidos son: ", dob)
	print("\tLa cantidad de 'sanguchitos' de tipo triple vendidos son: ", tri)


def imprimir_ingredientes_vendidos (ing_vendidos: dict):
	# definición de __doc__
	"""
		Función que imprime en pantalla los ingredientes mas vendidos de manera ordenada
		Argumento:
			ing_vendidos: Diccionario de ingredientes vendidos que contiene nombre y cantidad
	"""
	# ordenar diccionario
	ing_vendidos = sorted(ing_vendidos.values(), key=lambda ing: ing["cantidad"], reverse=True)

	if len(ing_vendidos) > 0:
		for ingrediente in ing_vendidos:
			print("\t{}: {}".format(ingrediente["nombre"], ingrediente["cantidad"]))
	else:
		print("¡No se ha realizado ventas!")

def ing_vendidos (hist_pedidos: list):
	# definición de __doc__
	"""
		Función que genera un diccionario con los ingredientes vendidos y luego
		los imprime en pantalla ordenados.
		Argumento:
			hist_pedidos: lista de pedidos del sistema
	"""
	ing_vendidos: dict = {}
	for pedido in hist_pedidos:
		for ingrediente in pedido["ingredientes"]:
			if not ing_vendidos.get(ingrediente["alias"]):
				ing_vendidos[ingrediente["alias"]] = {
					"nombre": ingrediente["nombre"],
					"cantidad": 1
				}
			else:
				ing_vendidos[ingrediente["alias"]]["cantidad"] += 1
				
	imprimir_ingredientes_vendidos(ing_vendidos)
	




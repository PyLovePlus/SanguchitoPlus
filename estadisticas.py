#Estadísticas de ventas - Cant de sandwich por tipo vendido y cant total

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
	print("La cantidad total de 'sanguchitos' vendidos son: ", total)
	print("La cantidad de 'sanguchitos' de tipo individual vendidos son: ", ind)
	print("La cantidad de 'sanguchitos' de tipo doble vendidos son: ", dob)
	print("La cantidad de 'sanguchitos' de tipo triple vendidos son: ", tri)


#Estadísticas de ventas - Ventas por ingredientes ordenados de mayor a menor
def ing_mas_vendidos (hist_pedidos: list):
	i = j = k = jam = cha = pim = dqs = ace = ppe = sal = 0

	for i in range(0, len(hist_pedidos)):
		for j in range(0, len(hist_pedidos[i]['ingredientes'])):

			if hist_pedidos[i]['ingredientes'][j]['alias'] == 'ja':
				jam += 1
			elif hist_pedidos[i]['ingredientes'][j]['alias'] == 'ch':
				cha += 1
			elif hist_pedidos[i]['ingredientes'][j]['alias'] == 'pi':
				pim += 1
			elif hist_pedidos[i]['ingredientes'][j]['alias'] == 'dq':
				dqs += 1
			elif hist_pedidos[i]['ingredientes'][j]['alias'] == 'ac':
				ace += 1
			elif hist_pedidos[i]['ingredientes'][j]['alias'] == 'pp':
				ppe += 1
			else:
				sal += 1

	#Ordenar los contadores de ingredientes
	list_aux = []

	list_aux.extend([[jam, "Jamón"], [cha, "Champiñones"], [pim, "Pimentón"], [dqs, "Doble Queso"], [ace, "Aceituna"], [ppe, "Pepperoni"], [sal, "Salchichón"]])
	list_aux = sorted(list_aux, key = __ordernar_ingredientes, reverse=True)
	print()
	print("Los 3 ingredientes más vendidos fueron los siguientes:")
	for i in range(0, 3):
		print(i + 1, "-. ", list_aux[i][1], ": ", list_aux[i][0], " unidades")


def __ordernar_ingredientes (ingrediente : list) -> int:
	# definición de __doc__
	"""
		Encargado de devolver cantidad de ingredientes utilizados como clave de ordernamiento
		Argumentos
			Elemento ingrediente
	"""
	return ingrediente[0]

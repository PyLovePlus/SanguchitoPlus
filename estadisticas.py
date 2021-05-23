#Estadísticas de ventas - Cant de sandwich por tipo vendido y cant total

"""def tipo_vendidos (hist_pedidos: list):
	i, j = 0

	for i in range(0, len(hist_pedidos)):"""

#Estadisticas de ventas - Ventas por ingredientes ordenados de mayor a menor

def ing_mas_vendidos (hist_pedidos: list):
	i, j, k, jam, cha, pim, dqs, ace, ppe, sal = 0

	for i in range(0, len(hist_pedidos)):
		for j in range(0, len(hist_pedidos[i])):
			for k in range(0, len(hist_pedidos[i][j])):
				if hist_pedidos[i][j][k] == 'ja':
					jam += 1
				elif hist_pedidos[i][j][k] == 'ch':
					cha += 1
				elif hist_pedidos[i][j][k] == 'pi':
					pim += 1
				elif hist_pedidos[i][j][k] == 'dq':
					dqs += 1
				elif hist_pedidos[i][j][k] == 'ac':
					ace += 1
				elif hist_pedidos[i][j][k] == 'pp':
					ppe += 1
				else:
					sal += 1

	#Ordenar los contadores de ingredientes
	list_aux = []
	#list_aux.append(jam, cha, pim, dqs, ace, ppe, sal)
	list_aux.append([jam, "Jamón"], [cha, "Champiñones"], [pim, "Pimentón"], [dqs, "Doble Queso"], [ace, "Aceituna"], [ppe, "Pepperoni"], [sal, "Salchichón"])
	list_aux.sort()
	print("Los 3 ingredientes más vendidos fueron los siguientes:")
	for i in range(0, 2):
			print(i, "-. ", list_aux[i][i+1])
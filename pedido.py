# cantidad de '*' o '-' a colocar en consola
# ingrediente por defecto en caso de falta de ingredientes adicionales
CANTIDAD_DE_RELLENO = 100
INGREDIENTE_POR_DEFECTO = "Queso"


def realizar_pedido(sandwiches: dict, ingredientes: dict) -> list:
    # definición de __doc__
    """
      Punto de partida para el pedido de un usuario, construyendo los diferentes sandwiches que este desee.
      Argumentos:
        sandwiches: Diccionario que posee todos los sandwiches disponibles para realizar un pedido
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables
      Retorna: Lista de sandwiches solicitados con sus ingredientes adicionales solicitados
    """
    # lista de sandwiches a ser pedidos
    pedido: list = []

    # Ciclo para agregar sandwiches al pedido
    while True:
        print("*" * CANTIDAD_DE_RELLENO)
        print("Sandwich número {}\n".format(len(pedido) + 1))

        # construimos el sandwich a partir de las opciones disponibles y lo agregamos al pedido
        pedido.append(__construir_sandwich(sandwiches, ingredientes))

        # condición para completar el pedido
        continuar: str = ""
        while not continuar in ["n", "s"]:
            continuar = input("¿Desea realizar otro pedido? (s/n) --> ")
            if continuar == "n":
                return pedido
            elif continuar != "s":
                print("Error: ¡Las opciones validas son s/n!")
            else:
                break


def __imprimir_sandwich(sandwich: dict) -> None:
    # definición de __doc__
    """
      Imprime los datos de un sandwich y su precio
      Argumento:
        sandwich: Diccionario con los datos del sandwich y la lista de ingredientes adicionales
    """
    # impresión de tipo e ingredientes adicionales (INGREDIENTE_POR_DEFECTO en caso de que no haya ninguno)
    print("-" * 100)
    print(f'Usted ha seleccionado un sandwich {sandwich["tipo"]} con ', end="")
    if not sandwich["ingredientes"]:
        print(INGREDIENTE_POR_DEFECTO)
    else:
        nombres = [ing["nombre"] for ing in sandwich["ingredientes"]]
        print(", ".join(nombres))
    # impresión del precio del sandwich
    precios_ingredientes = [ing["precio"] for ing in sandwich["ingredientes"]]
    print("Subtotal a pagar por un sandwich {}: {}".format(sandwich["tipo"], sum(precios_ingredientes) + sandwich["precio"]))


def __construir_sandwich(sandwiches: dict, ingredientes: dict) -> dict:
    # definición de __doc__
    """
      Construye un sandwich a partir de una lista de opciones definida en sus argumentos.
      Argumentos:
        sandwiches: Diccionario que posee todos los sandwiches
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables
      Retorna: Diccionario con los datos del sandwich y los ingredientes adicionales
    """

    # Datos que debe contener un sandwich
    sandwich: dict = {
        "alias": "",
        "tipo": "",
        "precio": 0,
        "ingredientes": []
    }

    # Ciclo que solicita el sandwich a construir, si este no existe (alias) se repite
    while sandwich["alias"] not in sandwiches.keys():
        # solicitud del tipo de sandwich
        print("Tipo: ", end="")
        for sandw in sandwiches:
            print("{} ( {} )".format(sandwiches[sandw]["tipo"], sandw), end=" ")
        sandwich["alias"] = input("--> ")

        # en caso de tipo invalido
        if sandwich["alias"] not in sandwiches.keys():
            print("Error: ¡Debe seleccionar un tipo valido!")
            continue

        # si el tipo es valido
        sandwich = {
            "alias": sandwich["alias"],
            "tipo": sandwiches.get(sandwich["alias"])["tipo"],
            "precio": sandwiches.get(sandwich["alias"])["precio"],
            # solicitamos ingredientes adicionales y los guardamos
            "ingredientes": __agregar_ingredientes(ingredientes)
        }
        # imprimimos los datos del sandwich construido
        __imprimir_sandwich(sandwich)

    return sandwich


def __agregar_ingredientes(ingredientes: dict) -> list:
    # definición de __doc__
    """
      Construye una lista con todos los ingredientes adicionales que el usuario desee.
      Argumento:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables
      Retorna: Lista con ingredientes solicitados para agregar al sandwich
    """
    # Lista de ingredientes solicitados
    solicitados: list = []

    # imprimimos ingredientes disponibles
    print("\nIngredientes:")
    for i in ingredientes:
        print(f'({i}) {ingredientes[i]["nombre"]}')

    # mientras el usuario siga agregando ingredientes
    alias: str
    while True:
        alias = input("Indique un ingrediente (enter para terminar) --> ")

        # si no hay ingrediente seleccionado (enter)
        if not alias:
            break
        # si el ingrediente no existe
        elif not alias in ingredientes.keys():
            print("Error: ¡Este ingrediente no existe!")
            continue
        # si el ingrediente ya fue agregado
        elif alias in [ing["alias"] for ing in solicitados]:
            print("Error: ¡Este ingrediente ya fue agregado!")
            continue

        # si no hay errores, agregamos el ingrediente
        solicitados.append({
            "alias": alias,
            "nombre": ingredientes[alias]["nombre"],
            "precio": ingredientes[alias]["precio"]
        })

    return solicitados

# sandwiches = {
#   "t": {
#     "tipo": "Triple",
#     "precio": 580
#   },
#   "d": {
#     "tipo": "Doble",
#     "precio": 430
#   },
#   "i": {
#     "tipo": "Individual",
#     "precio": 280
#   }
# }

# ingredientes  = {
#   "ja": {
#     "nombre": "Jamón",
#     "precio": 40
#   },
#   "ch": {
#     "nombre": "Champiñones",
#     "precio": 35
#   },
#   "pi": {
#     "nombre": "Pimentón",
#     "precio": 30
#   },
#   "dq": {
#     "nombre": "Doble queso",
#     "precio": 40
#   },
#   "ac": {
#     "nombre": "Aceitunas",
#     "precio": 57.5
#   },
#   "pe": {
#     "nombre": "Pepperoni",
#     "precio": 38.5
#   },
#   "sa": {
#     "nombre": "Salchichón",
#     "precio": 62.5
#   }
# }

# pedido = realizar_pedido(sandwiches, ingredientes)

# print(pedido)

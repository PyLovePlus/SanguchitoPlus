# cantidad de '*' o '-' a colocar en consola
CANTIDAD_DE_RELLENO = 100


def agregar_ingredientes(ingredientes: dict) -> dict:
    # definición de __doc__
    """
      Punto de partida para agregar ingredientes, validando los atributos del mismo y agregándolo
      al diccionario de ingredientes cuando todos los atributos sean válidos.
      Argumentos:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables
      Retorna: Diccionario de ingredientes con los ingredientes agregados
    """

    salir: str = "n"
    nombre_ingrediente: str = ""
    precio: float = 0
    alias: str = ""

    print("*" * CANTIDAD_DE_RELLENO)
    print(format("Agregar Ingrediente(s)", ">60s"))

    while (salir != "s"):
        print("*" * CANTIDAD_DE_RELLENO)

        # se validan que los atributos del ingrediente a crear sean validos
        # el alias(key) no debe existir en el diccionario de ingredientes
        # el nombre del ingrediente no debe existir en el diccionario de ingredientes
        # el precio debe ser mayor a 0.00
        alias = __validar_alias(ingredientes)
        nombre_ingrediente = __validar_nombre_ingrediente(ingredientes)
        precio = __validar_precio()

        # se agrega el ingrediente al diccionario de ingredientes luego de validar todos los atributos
        ingredientes[alias] = {"precio": precio, "nombre": nombre_ingrediente}

        # se imprime la información del ingrediente agregado
        __imprimir_ingrediente_agregado(alias, nombre_ingrediente, precio)

        # se le pregunta al usuario si desea terminar de agregar ingredientes
        salir = __terminar_operacion()

    print("*" * CANTIDAD_DE_RELLENO)

    # se retorna el diccionario de ingredientes con el/los ingrediente(s) agregados
    return ingredientes


def eliminar_ingredientes(ingredientes: dict) -> dict:
    # definición de __doc__
    """
      Punto de partida para eliminar ingredientes, validando que exista y eliminándolo
      del diccionario de ingredientes.
      Argumentos:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables
      Retorna: Diccionario de ingredientes con los ingredientes eliminados
    """

    alias: str = ""
    salir: str = "n"

    print("*" * CANTIDAD_DE_RELLENO)
    print(format("Eliminar Ingrediente(s)", ">60s"))

    while (salir != "s"):
        print("*" * CANTIDAD_DE_RELLENO)
        alias = input("Ingrese alias del ingrediente a eliminar: ")

        # se elimina el ingrediente del diccionario de ingredientes en caso de que exista
        ingredientes = __ingrediente_eliminado(ingredientes, alias)

        # se le pregunta al usuario si desea terminar de eliminar ingredientes
        salir = __terminar_operacion()

    print("*" * CANTIDAD_DE_RELLENO)

    # se retorna el diccionario de ingredientes con el/los ingrediente(s) eliminados
    return ingredientes


def __existe_nombre_ingrediente(ingredientes: dict, nombre_ingrediente: str) -> bool:
    # definición de __doc__
    """
      Función encargada de validar si existe el nombre del ingrediente, retorna True en caso de que
      exista y False en caso de que no exista.
      Argumentos:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables,
        nombre_ingrediente: String que posee el nombre que se va a validar
      Retorna: True si el nombre del ingrediente ya existe o False si el nombre del ingrediente no existe
    """

    # Ciclo que revisa el nombre de cada ingrediente comparándolo con nombre_ingrediente
    for ingrediente in ingredientes.keys():
        # Si nombre_ingrediente ya existe se retorna True
        if (ingredientes[ingrediente]["nombre"] == nombre_ingrediente):
            return True

    # Si nombre_ingrediente no existe se retorna False
    return False


def __existe_alias(ingredientes: dict, alias: str) -> bool:
    # definición de __doc__
    """
      Función encargada de validar si existe el alias del ingrediente, retorna True en caso de que
      exista y False en caso de que no exista.
      Argumentos:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables,
        alias: String que posee el alias que se va a validar
      Retorna: True si el alias del ingrediente ya existe o False si el alias del ingrediente no existe
    """
    return alias in ingredientes.keys()


def __validar_alias(ingredientes: dict) -> str:
    # definición de __doc__
    """
      Función encargada de validar que el usuario introduzca un alias que no exista en el
      diccionario de ingredientes utilizando un ciclo while.
      Argumentos:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables,
      Retorna: el alias validado, es decir, un alias que no exista en el diccionario de ingredientes
    """

    # se le pide un alias al usuario
    alias: str = input("Ingrese alias para el ingrediente: ")

    # Ciclo para validar que el usuario ingrese un alias válido (que no existe en el diccionario de
    # ingredientes y que no sea vacío)
    while (True):
        # se valida que el alias no exista en el diccionario de ingredientes
        if (__existe_alias(ingredientes, alias)):
            alias = input("El alias ya se encuentra registrado, por favor ingrese otro: ")
        # se valida que el alias no esté vacío
        elif (len(alias) == 0):
            alias = input("El alias no puede estar vacío, por favor ingrese un alias válido: ")
        else:
            break

    print()

    # se retorna el alias validado
    return alias


def __validar_nombre_ingrediente(ingredientes: dict) -> str:
    # definición de __doc__
    """
      Función encargada de validar que el usuario introduzca un nombre de ingrediente que no exista en el
      diccionario de ingredientes utilizando un ciclo while.
      Argumentos:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables,
      Retorna: el nombre del ingrediente validado,
      es decir, un nombre de ingrediente que no exista en el diccionario de ingredientes
    """

    # se le pide un nombre de ingrediente al usuario
    nombre_ingrediente: str = input("Ingrese nombre para el ingrediente: ")

    # mientras el nombre del ingrediente exista en el diccionario de ingredientes
    # se le pide otro nombre para el ingrediente al usuario
    while (True):
        # se valida que el nombre del ingrediente no exista en el diccionario de ingredientes
        if (__existe_nombre_ingrediente(ingredientes, nombre_ingrediente)):
            nombre_ingrediente = input("El nombre ya se encuentra registrado, por favor ingrese otro: ")
        # se valida que el nombre del ingrediente no esté vacío
        elif (len(nombre_ingrediente) == 0):
            nombre_ingrediente = input("El nombre no puede estar vacío, por favor ingrese un nombre válido: ")
        else:
            break

    print()

    # se retorna el nombre del ingrediente validado
    return nombre_ingrediente


def __validar_precio() -> float:
    # definición de __doc__
    """
      Función encargada de validar que el precio del ingrediente sea válido, es decir,
      el precio del ingrediente debe ser mayor a 0.00.
      Retorna: el precio del ingrediente validado
    """
    # se le pide un precio para el ingrediente al usuario, validando que sea un float
    precio: float = 0
    while (precio == 0):
        try:
            precio: float = float(input(("Ingresa un precio para el ingrediente: ")))
        except:
            print("Error: El precio debe ser un número.")
            precio = 0

    # mientras el precio del ingrediente no sea válido, es decir, no sea mayor a 0.00
    # se le pide al usuario otro precio válido
    while (precio <= 0):
        print("El precio debe ser mayor a 0.00")
        precio: float = float(input(("Ingresa un precio para el ingrediente: ")))

    # se redondea el precio a dos decimales
    precio = round(precio, 2)

    print()

    # se retorna un precio válido
    return precio


def __terminar_operacion() -> str:
    # definición de __doc__
    """
      Función encarga de validar que el usuario introduzca una opción valida (s/n) para salir
      del menú de agregar o eliminar ingredientes.
      Retorna: una opción válida (s/n)
    """

    # se pide la opción al usuario
    salir: str = input('¿Desea salir? (s/n): ')

    # mientras el usuario no ingrese una opción válida (s/n) se le pide otra vez la opción
    while (salir not in ("s", "n")):
        salir = input("Opción inválida, por favor ingrese una opción válida (s/n): ")

    # se retorna la opción válida (s/n)
    return salir


def __ingrediente_eliminado(ingredientes: dict, alias: str) -> bool:
    # definición de __doc__
    """
      Función encargada de eliminar el ingrediente si existe el alias del ingrediente,
      retorna el diccionario de ingredientes sin el ingrediente eliminado (en caso de que exista)
      si no existe el ingrediente a eliminar se retorna el diccionario de ingredientes sin modificar.
      Argumentos:
        ingredientes: Diccionario que posee todos los ingredientes adicionales agregables,
        alias: String que posee el alias del ingrediente que se va a eliminar
      Retorna: el diccionario de ingredientes sin el ingrediente eliminado (en caso de que exista),
      si no existe el ingrediente a eliminar se retorna el diccionario de ingredientes sin modificar
    """
    # si el alias del ingrediente no existe en el diccionario de ingredientes se le indica
    # al usuario que el ingrediente con esa alias no existe mediante un mensaje en consola
    if (not (__existe_alias(ingredientes, alias))):
        print(f"El ingrediente con alias \"{alias}\" no existe")
    # si el alias del ingrediente si existe en el diccionario de ingredientes se elimina
    # el ingrediente del diccionario de ingredientes y se le indica al usuario que el ingrediente
    # fue eliminado exitosamente mediante un mensaje en consola
    else:
        # se elimina el ingrediente con el alias respectivo
        ingredientes.pop(alias)

        # se imprime que se ha eliminado el ingrediente exitosamente
        __imprimir_ingrediente_eliminado()

    print()

    # se retorna el diccionario de ingredientes modificado
    return ingredientes


def __imprimir_ingrediente_agregado(alias: str, nombre_ingrediente: str, precio: float) -> None:
    # definición de __doc__
    """
      Función encargada de imprimir la información del ingrediente agregado al diccionario de
      ingredientes.
      Argumentos:
        alias: alias del nuevo ingrediente
        nombre_ingrediente: nombre del nuevo ingrediente,
        precio: precio del nuevo ingrediente
    """

    # Se imprime la información (alias, nombre_ingrediente y precio) del nuevo ingrediente agregado
    print("-" * CANTIDAD_DE_RELLENO)
    print("Ingrediente agregado exitosamente: ")
    print(f"Alias --> {alias}")
    print(f"Nombre --> {nombre_ingrediente}")
    print(f"Precio --> {precio}")
    print("-" * CANTIDAD_DE_RELLENO)


def __imprimir_ingrediente_eliminado() -> None:
    # definición de __doc__
    """
      Función encargada de imprimir que se ha eliminado el ingrediente exitosamente.
    """

    # Se imprime que se ha eliminado el ingrediente exitosamente
    print("-" * CANTIDAD_DE_RELLENO)
    print("Ingrediente eliminado exitosamente")
    print("-" * CANTIDAD_DE_RELLENO)

# ingredientes = {
#   "t": {
#     "precio" : 20,
#     "nombre" : "tomate"
#   }
# }

# ingredientes = agregar_ingredientes(ingredientes)
# print(ingredientes)
# ingredientes = eliminar_ingredientes(ingredientes)
# print(ingredientes)

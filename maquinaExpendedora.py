nombresProductos = ["Agua 💧", "Refresco 🥤", "Zumo 🍹"]
preciosProductos = [0.50, 0.75, 0.95]
reservaMonedas = [20, 20, 20, 20, 20, 20]
valoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]

def imprimirMenu(nombres, precios):
    textoMenu = "\nMenú de Productos:\n"
    for i in range(len(nombres)):
        textoMenu += f"{i+1} - {nombres[i]} : {precios[i]}€\n"
    textoMenu += f"{len(nombres)+1} - SALIR"
    print(textoMenu)

    print(f"La reserva de monedas es: {reservaMonedas}")
    eleccion = 0
    while eleccion < 1 or eleccion > len(nombres) + 1:
        eleccion_str = input("Introduce el artículo para comprar (1, 2, 3 o 4 para salir): ")
        try:
            eleccion = int(eleccion_str)
            if eleccion < 1 or eleccion > len(nombres) + 1:
                print("Introduce un número válido.")
                eleccion = 0
        except ValueError:
            print("Introduce un número válido.")
            eleccion = 0

    return eleccion

def entregarProducto(producto):
    print("Aquí tiene su " + producto + ".")

def ingresarMoneda():
    valoresValidos = [str(valor) for valor in valoresMonedas]
    moneda = input("Introduzca monedas de 2€, 1€, 0.50€, 0.20€, 0.10€, 0.05€: ")

    while moneda not in valoresValidos:
        moneda = input("Introduzca una moneda válida: ")

    return round(float(moneda), 2)


def ingresarImporte(opcion):
    opcion = opcion - 1
    if opcion >= len(preciosProductos):
        print("Saliendo...")
        return

    precio = preciosProductos[opcion]
    importeUsuario = 0
    monedasIntroducidas = []

    while importeUsuario < precio:
        print("Le queda " + str((precio - importeUsuario)) + "€ por ingresar.")
        moneda = ingresarMoneda()
        importeUsuario += moneda
        monedasIntroducidas.append(moneda)
        sumarMoneda(moneda)

    if importeUsuario > precio:
        resto = (importeUsuario - precio)
        darCambio(resto)

    entregarProducto(nombresProductos[opcion])

def sumarMoneda(moneda):
    for i in range(len(valoresMonedas)):
        if valoresMonedas[i] == moneda:
            reservaMonedas[i] += 1


def darCambio(resto):
    monedasDevueltas = []
    restoActual = resto

    for i in range(len(valoresMonedas)):
        valor = valoresMonedas[i]
        while restoActual >= valor and reservaMonedas[i] > 0:
            monedasDevueltas.append(valor)
            reservaMonedas[i] -= 1
            restoActual = round(restoActual - valor, 2)

    if restoActual > 0:
        print("Devolviendo dinero. No hay cambio")
        devolverMonedas(monedasDevueltas)
    else:
        totalCambio = sum(monedasDevueltas)
        print(f"Tu cambio es: {totalCambio}€")

def devolverMonedas(monedasDevueltas):
    for moneda in monedasDevueltas:
        sumarMoneda(moneda)

opcion = 0
while opcion != len(nombresProductos) + 1:
    opcion = imprimirMenu(nombresProductos, preciosProductos)
    if opcion != len(nombresProductos) + 1:
        ingresarImporte(opcion)

print("Gracias por su visita.")

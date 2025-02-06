nombresProductos = ["Agua", "Refrescos", "ZumÇ"]
preciosProductos = [0.50, 0.75, 0.95]
reservaMonedas = [20, 20, 20, 20, 20, 20]
valoresMonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]


def imprimirMenu(nombres, precios):
    cont = 0
    textoMenu = ""
    for nombre in nombres:
        textoMenu += f"{cont + 1} - {nombre} : {precios[cont]} \n"
        cont += 1
    textoMenu += f"{cont + 1} - SALIR\n"
    print(textoMenu)

    eleccion = int(input("Introduce el artículo para comprar (1, 2, 3, o 4 para salir): "))
    return eleccion


def entregarProducto():
    print("Aquí tiene su producto.")


def ingresarImporte(opcion):
    if opcion < 1 or opcion > len(preciosProductos):
        print("Opción no válida.")
        return False

    precio = preciosProductos[opcion - 1]
    importeUsuario = 0
    while importeUsuario < precio:
        print(f"Te quedan por ingresar {precio - importeUsuario:.2f} euros")
        importeUsuario += ingresarMoneda()

    if importeUsuario >= precio:
        print("Gracias por tu compra.")
        entregarProducto()
        return True
    return False

def darCambio(resto):
    vueltas = 0
    monedasDevueltas = []
    while vueltas < resto:
        monedasDevueltas.append(valor)
        if valor == resto:
            devolverMoneda

def ingresarMoneda():
    moneda = float(input("Introduce una moneda de 2, 1, 0.50cts, 0,20cts, 0,10cts o 0,05cts: "))
    while moneda not in valoresMonedas:
        print("Moneda no válida. Por favor, introduce una moneda válida.")
        moneda = float(input("Introduce una moneda de 2, 1, 0.50cts, 0,20cts, 0,10cts o 0,05cts: "))

    indiceMoneda = valoresMonedas.index(moneda)
    reservaMonedas[indiceMoneda] -= 1
    return moneda


continuar = True
while continuar:
    opcion = imprimirMenu(nombresProductos, preciosProductos)
    if opcion == len(nombresProductos) + 1:
        print("Vuelve pronto")
        continuar = False
    else:
        continuar = ingresarImporte(opcion)

def ordenamiento_shellsort(lista):
    """
    Ordena una lista de menor a mayor utilizando el algoritmo ShellSort,
    reduciendo gradualmente la brecha (gap) de comparación entre elementos.
    """
    datos = lista.copy()
    n = len(datos)
    brecha = n // 2
    pasada = 1

    print(f"\nLista inicial: {datos}")

    while brecha > 0:
        for i in range(brecha, n):
            temp = datos[i]
            j = i
            while j >= brecha and datos[j - brecha] > temp:
                datos[j] = datos[j - brecha]
                j -= brecha
            datos[j] = temp

        print(f"Pasada {pasada} (brecha = {brecha}): {datos}")
        brecha //= 2
        pasada += 1

    return datos


def ordenamiento_quicksort(lista):
    """
    Ordena una lista de menor a mayor utilizando el algoritmo Quicksort
    mediante particiones recursivas alrededor de un elemento pivote.
    """
    datos = lista.copy()
    print(f"\nLista inicial: {datos}")

    def _quicksort_recursivo(arr, inicio, fin, nivel=1):
        if inicio < fin:
            indice_pivote = _particionar(arr, inicio, fin)
            print(f"Partición (nivel {nivel}, pivote = {arr[indice_pivote]}): {arr}")
            _quicksort_recursivo(arr, inicio, indice_pivote - 1, nivel + 1)
            _quicksort_recursivo(arr, indice_pivote + 1, fin, nivel + 1)

    def _particionar(arr, inicio, fin):
        pivote = arr[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if arr[j] <= pivote:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
        return i + 1

    _quicksort_recursivo(datos, 0, len(datos) - 1)
    return datos


def ordenamiento_heapsort(lista):
    """
    Ordena una lista de menor a mayor utilizando Heapsort,
    construyendo un montículo máximo (Max-Heap) y extrayendo la raíz.
    """
    datos = lista.copy()
    n = len(datos)
    print(f"\nLista inicial: {datos}")

    def _ajustar_monticulo(arr, tamano, raiz):
        mayor = raiz
        izquierda = 2 * raiz + 1
        derecha = 2 * raiz + 2

        if izquierda < tamano and arr[izquierda] > arr[mayor]:
            mayor = izquierda
        if derecha < tamano and arr[derecha] > arr[mayor]:
            mayor = derecha

        if mayor != raiz:
            arr[raiz], arr[mayor] = arr[mayor], arr[raiz]
            _ajustar_monticulo(arr, tamano, mayor)

    # Construcción del Max-Heap inicial
    for i in range(n // 2 - 1, -1, -1):
        _ajustar_monticulo(datos, n, i)
    print(f"Montículo máximo construido: {datos}")

    # Extracción sucesiva del elemento mayor hacia el final
    pasada = 1
    for i in range(n - 1, 0, -1):
        datos[0], datos[i] = datos[i], datos[0]
        _ajustar_monticulo(datos, i, 0)
        print(f"Extracción {pasada} (elemento fijo = {datos[i]}): {datos}")
        pasada += 1

    return datos


def ordenamiento_radix(lista):
    """
    Ordena una lista de enteros no negativos de menor a mayor mediante
    Radix Sort (LSD), procesando dígito por dígito de derecha a izquierda.
    """
    datos = lista.copy()
    print(f"\nLista inicial: {datos}")

    maximo = max(datos)
    if maximo == 0:
        print("Todos los valores son 0; la lista ya se encuentra ordenada.")
        return datos

    def _conteo_por_digito(arr, exponente):
        n = len(arr)
        salida = [0] * n
        conteo = [0] * 10

        for numero in arr:
            digito = (numero // exponente) % 10
            conteo[digito] += 1

        for i in range(1, 10):
            conteo[i] += conteo[i - 1]

        for i in range(n - 1, -1, -1):
            digito = (arr[i] // exponente) % 10
            salida[conteo[digito] - 1] = arr[i]
            conteo[digito] -= 1

        for i in range(n):
            arr[i] = salida[i]

    exponente = 1
    pasada = 1
    while maximo // exponente > 0:
        _conteo_por_digito(datos, exponente)
        print(f"Pasada {pasada} (posición decimal {exponente}): {datos}")
        exponente *= 10
        pasada += 1

    return datos


def solicitar_cantidad():
    """Solicita y valida la cantidad de números a ordenar (mínimo 2)."""
    while True:
        entrada = input("\nIngresa la cantidad de números que deseas ordenar (mínimo 2): ").strip()
        try:
            cantidad = int(entrada)
            if cantidad >= 2:
                return cantidad
            print("Error: Debes ingresar un número entero mayor o igual a 2.")
        except ValueError:
            print("Error: Entrada no válida. Escribe únicamente un número entero.")


def capturar_datos(tipo_validacion):
    """
    Solicita los números al usuario aplicando las reglas específicas
    de cada ejercicio:
    - 'positivos': enteros o decimales mayores a 0.
    - 'reales': cualquier número entero o decimal (positivos, negativos o cero).
    - 'enteros_no_negativos': únicamente enteros >= 0 (requerido por Radix Sort).
    """
    cantidad = solicitar_cantidad()
    numeros = []

    for i in range(cantidad):
        while True:
            entrada = input(f"Ingresa el número #{i + 1}: ").strip()

            if tipo_validacion == "enteros_no_negativos":
                if "." in entrada or "," in entrada:
                    print("Error: Este método NO acepta decimales. Ingresa solo números enteros.")
                    continue
                try:
                    valor = int(entrada)
                    if valor >= 0:
                        numeros.append(valor)
                        break
                    print("Error: Este método NO acepta números negativos. Ingresa un entero mayor o igual a 0.")
                except ValueError:
                    print("Error: Entrada no válida. Ingresa únicamente dígitos enteros.")

            elif tipo_validacion == "positivos":
                try:
                    valor = float(entrada)
                    if valor > 0:
                        numeros.append(int(valor) if valor.is_integer() else valor)
                        break
                    print("Error: El valor debe ser mayor a 0 (no se aceptan negativos ni cero).")
                except ValueError:
                    print("Error: Entrada no válida. Ingresa un valor numérico.")

            elif tipo_validacion == "reales":
                try:
                    valor = float(entrada)
                    numeros.append(int(valor) if valor.is_integer() else valor)
                    break
                except ValueError:
                    print("Error: Entrada no válida. Ingresa un número entero o decimal.")

    return numeros


def mostrar_instrucciones(titulo, descripcion, permitidos, no_permitidos):
    """Imprime la ficha informativa y las reglas de captura antes de pedir datos."""
    print("\n" + "=" * 65)
    print(f" {titulo}")
    print("=" * 65)
    print(f"Contexto: {descripcion}")
    print("\nINSTRUCCIONES DE CAPTURA DE DATOS:")
    print(f"  [+] SÍ puedes ingresar: {permitidos}")
    print(f"  [-] NO puedes ingresar: {no_permitidos}")
    print("-" * 65)


def menu_principal():
    """Controla el menú interactivo hasta que el usuario elija salir."""
    while True:
        print("\n" + "#" * 65)
        print("   SISTEMA INTERACTIVO DE MÉTODOS DE ORDENAMIENTO AVANZADOS")
        print("#" * 65)
        print("1. Ejercicio 1 - ShellSort (Tiempos de carga de una aplicación)")
        print("2. Ejercicio 2 - Quicksort (Balances financieros diarios)")
        print("3. Ejercicio 3 - Heapsort  (Niveles de prioridad de paquetes)")
        print("4. Ejercicio 4 - Radix Sort (Folios o códigos numéricos de pedido)")
        print("5. Salir del programa")
        print("#" * 65)

        opcion = input("Selecciona el ejercicio que deseas ejecutar (1-5): ").strip()

        if opcion == "1":
            mostrar_instrucciones(
                titulo="EJERCICIO 1: SHELLSORT - TIEMPOS DE CARGA (ms)",
                descripcion="Ordena de menor a mayor los tiempos de respuesta medidos en milisegundos.",
                permitidos="Números enteros o decimales positivos mayores a 0 (ej. 45, 12.5, 120).",
                no_permitidos="Números negativos, el número 0, letras o símbolos."
            )
            datos = capturar_datos("positivos")
            resultado = ordenamiento_shellsort(datos)
            print(f"\n>>> Resultado final ordenado (ShellSort): {resultado}")

        elif opcion == "2":
            mostrar_instrucciones(
                titulo="EJERCICIO 2: QUICKSORT - BALANCES FINANCIEROS",
                descripcion="Ordena de menor a mayor ganancias y pérdidas registradas en un periodo.",
                permitidos="Cualquier número entero o decimal: positivos, negativos o cero (ej. -250.5, 0, 1400).",
                no_permitidos="Texto, letras, espacios vacíos o caracteres especiales."
            )
            datos = capturar_datos("reales")
            resultado = ordenamiento_quicksort(datos)
            print(f"\n>>> Resultado final ordenado (Quicksort): {resultado}")

        elif opcion == "3":
            mostrar_instrucciones(
                titulo="EJERCICIO 3: HEAPSORT - PRIORIDAD DE PAQUETES DE RED",
                descripcion="Ordena de menor a mayor los puntajes de prioridad asignados a paquetes.",
                permitidos="Números enteros o decimales (positivos, negativos o cero).",
                no_permitidos="Letras, palabras o valores vacíos."
            )
            datos = capturar_datos("reales")
            resultado = ordenamiento_heapsort(datos)
            print(f"\n>>> Resultado final ordenado (Heapsort): {resultado}")

        elif opcion == "4":
            mostrar_instrucciones(
                titulo="EJERCICIO 4: RADIX SORT - FOLIOS NUMÉRICOS DE PEDIDO",
                descripcion="Ordena de menor a mayor identificadores numéricos procesando dígito por dígito.",
                permitidos="Únicamente números enteros positivos o cero (ej. 0, 42, 105, 9830).",
                no_permitidos="Números negativos (-5), números con decimales (14.8), letras o símbolos."
            )
            datos = capturar_datos("enteros_no_negativos")
            resultado = ordenamiento_radix(datos)
            print(f"\n>>> Resultado final ordenado (Radix Sort): {resultado}")

        elif opcion == "5":
            print("\nPrograma finalizado por el usuario. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, elige un número del 1 al 5.")


if __name__ == "__main__":
    menu_principal()
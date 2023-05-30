def printListValues(list, start, end):
    for i in range(start, end+1):
        # Si es el ultimo valor, no imprimir coma y agregar <ENTER>
        if i == end:
            print(list[i])
        else: 
            print(list[i], end=", ")

# Regresa una lista con el numero de valores indicado e imprime detalles de la lista: cola, periodo, ciclo
def getRandomNumbersAndDisplayDetails(seed, mult, corr, mod, n):
    foundCiclo = False
    newNumber = seed
    result = [newNumber]

    period_ends_at = None
    cola_ends_at = None
    while len(result) < n or not foundCiclo:
        newNumber = ((newNumber*mult) + corr) % mod
        if not foundCiclo and newNumber in result:
            foundCiclo = True
            cola_ends_at = result.index(newNumber) - 1
            period_ends_at = len(result) - 1
        result.append(newNumber)

    # Imprimir valores de la cola
    print('cola')
    printListValues(result, 0, cola_ends_at)
    # Imprimir valores del periodo
    print('period')
    printListValues(result, 0, period_ends_at)
    # Imprimir valores del ciclo
    print('ciclo')
    printListValues(result, cola_ends_at+1, period_ends_at)
    # Imprimir longitudes
    print(cola_ends_at+1)
    print(period_ends_at+1)
    print(period_ends_at - cola_ends_at)
    return result[:n] # Regresar el arreglo con el numero de valores especificado
    
def getMedia(numbers):
    total = 0
    for n in numbers:
        total += n
    print(total / len(numbers))

# getRandomNumbers(9876, 48271, 0, 9999, 10)
numbers = getRandomNumbersAndDisplayDetails(5, 5, 1, 16, 17)

# TODO: sacar media, mediana, moda, dev est, varianza, subintervalos con arreglo numbers
getMedia(numbers)


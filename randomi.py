import math

def printListValues(list):
    if len(list) == 0:
        print('\n', end='')
    for i in range(len(list)):
        # Si es el ultimo valor, no imprimir coma y agregar <ENTER>
        if i == len(list) - 1:
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
    printListValues(result[:cola_ends_at+1])
    # Imprimir valores del periodo
    print('period')
    printListValues(result[:period_ends_at+1])
    # Imprimir valores del ciclo
    print('ciclo')
    printListValues(result[cola_ends_at+1:period_ends_at+1])
    # Imprimir longitudes
    print(cola_ends_at+1)
    print(period_ends_at+1)
    print(period_ends_at - cola_ends_at)
    return result[:n] # Regresar el arreglo con el numero de valores especificado
    
def getMedia(numbers):
    total = 0
    for n in numbers:
        total += n
    media = total/len(numbers)
    print(media)
    return media

# Calcula mediana, el arreglo debe estar ordenado
def getMediana(numbers):
    # El numero de valores es par
    if len(numbers)%2 == 0:
        print((numbers[len(numbers)//2] + numbers[(len(numbers)//2)-1])/2)
    else:
        print(numbers[len(numbers)//2])

# Calcula moda, el arreglo debe estar ordenado
def getModa(numbers):
    modas = []
    highest = 0
    currentNumber = None
    currentScore = 0
    i = 0
    while i < len(numbers):
        # Cambio de numero, checar si el anterior numero es una moda
        if currentNumber != numbers[i]:
            # Nueva moda definitiva
            if currentScore > highest:
                modas = [currentNumber]
                highest = currentScore
            # Nueva moda igual a la anterior
            elif currentScore == highest:
                modas.append(currentNumber)
            # Actualizar valores
            currentNumber = numbers[i]
            currentScore = 1
        else:
            currentScore += 1
        i += 1

    # Revisar si el ultimo valor es moda
    if currentScore > highest:
        modas = [currentNumber]
        highest = currentScore
    elif currentScore == highest:
        modas.append(currentNumber)
    
    # Si la moda no tiene repeticion, entonces no es realmente moda
    if highest == 1:
        printListValues([])
    else:        
        printListValues(modas)


def getDesviacionYVarianza(numbers, media):
    suma = 0
    for n in numbers:
        suma += (n - media) ** 2
    varianza = suma / (len(numbers)-1)
    desviacion = math.sqrt(varianza)
    print(desviacion)
    print(varianza)

# Calcula 10 intervalos, el arreglo debe estar ordenado
def getIntervalos(numbers):
    highest = numbers[-1]
    rangos = []
    # Definir los rangos de los intervalos
    for i in range(1,11):
        rangos.append(highest*(i/10))

    rangoIndex = 0
    rangoActual = rangos[rangoIndex]
    countRango = 0
    i = 0
    # Calcular porcentaje de numeros que entran a ese intervalo
    while i < len(numbers):
        if numbers[i] <= rangoActual:
            countRango += 1
            i += 1
        # Se termino un rango
        else:
            porcentaje = (countRango/len(numbers)) * 100 if countRango != 0 else 0
            print(porcentaje)
            rangoIndex += 1
            rangoActual = rangos[rangoIndex]
            countRango = 0
    porcentaje = (countRango/len(numbers)) * 100 if countRango != 0 else 0
    print(porcentaje)


# getRandomNumbers(9876, 48271, 0, 9999, 10)
x0 = int(input())
a = int(input())
c = int(input())
m = int(input())
cuantos = int(input())
numbers = getRandomNumbersAndDisplayDetails(x0, a, c, m, cuantos)
sortedNumbers = sorted(numbers)

# TODO: sacar media, mediana, moda, dev est, varianza, subintervalos con arreglo numbers
print('mmm')
media = getMedia(numbers)
getMediana(sortedNumbers)
getModa(sortedNumbers)
print('desv, var')
getDesviacionYVarianza(numbers, media)
print('intervalos')
getIntervalos(sortedNumbers)


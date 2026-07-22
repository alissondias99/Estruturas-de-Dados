def quicksort(array):
    if len(array) < 2:
        return array
    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]
    return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([54, 46, 100, 154, 6]))
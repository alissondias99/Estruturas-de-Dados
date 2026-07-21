# 4.1 Escreva o código para a função soma dos elementos de um listaay onde, receba uma lista, se a lista estiver vazia, retorne zero, se não a soma total será o primeiro elemento + a soma do restante dos elementos, e listaay deve ficar menor a cada recursão.

def soma_recursia(lista):
    if lista == []:
        return 0
    
    # primeiro = lista[0]
    # lista.pop(0)
    # return primeiro + soma_recursia(lista)

# resolução do livro
    return lista[0] + soma_recursia(lista[1:])

print(soma_recursia([2, 4, 6]))

# 4.2 Escreva uma função recursiva que conte o número de itens em uma lista.

def conta_recursia(lista):
    if lista == []:
        return 0
    
    # lista.pop(0)
    # return 1 + conta_recursia(lista)

# resolução do livro
    return 1 + conta_recursia(lista[1:])

print(conta_recursia([2, 4, 6]))

# 4.3 Encontre o valor mais alto em uma lista.

# resolução do livro
def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(maximo([1, 2, 3, 50 ,3, -5, 99, 888]))
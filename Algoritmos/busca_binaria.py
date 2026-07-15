# exemplo de busca binária
# O(log n)

def busca_binaria(lista_nuns, eu_quero):
    inicio_lista = 0 # ponteiro do começo da lista
    fim_lista = len(lista_nuns) - 1 # ponteiro do fim da lista

    while inicio_lista <= fim_lista: # laço infinito, um while True funcionaria da mesma forma
        chute = (inicio_lista + fim_lista) // 2 # pega o meio da lista
        print(chute)

        if lista_nuns[chute] < eu_quero: # compara pelo indice da lista se o chute é MENOR que o número procurado
            inicio_lista = chute + 1  # e se for altera o ponteiro do começo da lista que passa a apontar para o índice a DIREITA do chute

        elif lista_nuns[chute] > eu_quero: # compara pelo indice da lista se o chute é MAIOR que o número procurado
            fim_lista = chute - 1 # e se for altera o ponteiro do FIM da lista que passa a apontar para o índice a ESQUERDA do chute

        else:
            print('acertou')
            return chute # finaliza

    return None

lista_nuns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # uma lista ordenada simples
eu_quero = 10 # número dejesado

busca_binaria(lista_nuns, eu_quero)
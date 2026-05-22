#Ordenação por inserção

lista_a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

n = len(lista_a)
ord = 1
# ^ cria um lista, uma variável com o tamanho da lista e um outra variável para representar quantas ordenações foram feitas

#Os comentários abaixo são da 1º ordenação

for i in range(1, n): # uma laço que ira percorrer a lista começando do índice 1 (poderia começar pelo 0, mas isso faria com que tivesse uma ordenação a mais e desnecessária)
    
    elem = lista_a[i] # uma variável com valor igual o valor do índice atual da lista, começa como 8, pois 8 é o índice 1
    
    j= i - 1 # uma variável que recebe o valor de i -1, começa valenda 0 (porque i começa valendo 1)
    
    while j>= 0 and lista_a[j]> elem: # enquanto j (que começa valendo 0) for >=0 e o indice j na lista_a for maior que o elemento (lista_a[j] = 9 e elemento =8) 
        
        lista_a[j+1] = lista_a[j]
        '''
        atribui ao indice j+1 na lista_a o valor de j na lista_a
        j+1 passa a valer 1, ou seja o valor de inidce 1 será alterado agora, o valor que será atribuido é o índice 0, pois j ainda vale 0, o valor do índice 0 é 9
        logo o nove que está no índice 0 passará para o índice 1
        '''
        
        j = j - 1 # j que ainda está valendo 0 passa a valer -1, isso ocorre para que o loop sejá interrompido e uma nova ordenação possa começar
    lista_a[j + 1] = elem # atribui ao elemento 0 (j que começou a valer -1 volta a ser 0) o valor contido em elem, que é 8
    print(f"{ord}º ordenação: {lista_a}")
    ord +=1
Umas das estruturas de dados mais básicas da computação.

Uma simples coleção de elementos onde cada elemento têm um índice (sempre começa pelo 0) que representa sua posição na lista.

```
array = ["apples", "bananas", "cucumbers"]
			0			1			2	
```

## Reading (Leitura)

Em um array, a operação de read retorna o valor contido em uma índice especifico.
Como o computador consegue "pular" direto para o índice procurado, read só realiza um passo, ou seja é 0(1). 

Mas como o computador é capaz de olhar direto no índice procurado?

A memória de um computador é como um grande conjunto de células, onde algumas contém dados, e outras não

|      | 9   |     | "a" |
| ---- | --- | --- | --- |
|      | #   | c   |     |
| true |     |     |     |
|      |     | 1   |     |

Quando um programa declara um array, ele pega um conjunto de células para atribuir valores do arrays.

Por exemplo, um array de tamanho 3 resulta em:

|      | 9        |          | "a"      |
| ---- | -------- | -------- | -------- |
|      | #        | c        |          |
| true | array[0] | array[1] | array[2] |
|      |          | 1        |          |

Cada célula da memória possui um número que representa seu endereço, cada endereço é sempre maior que o anterior.

| 1000 | 1001 | 1002 |
| ---- | ---- | ---- |
| 1003 | 1004 | 1005 |
| 1006 | 1007 | 1008 |

```
array = ["apples", "bananas", "cucumbers"]
end. memó  1003      1004        1005
index	    0		  1		       2	
```

Então quando um programa pede ao computador para procurar um item pelo índice 2 por exemplo, ele faz o seguinte.
1. Identifica que o índice 0 do array está no endereço 1003.
2. O elemento de índice 2 fica duas casas a frente do índice 0.
3. Então o computador faz 1003 + 2 = 1005.
4. E encontra o elemento cucumbers.
## Searching (Busca)

O computador precisa testar todos os elementos, para tentar encontrar o elemento procurado, sempre começando pelo índice 0.

Se um item estivar localizado no índice 0, o computador só ira fazer um passo, se estiver no item 50, fará 50 passos, se não estiver na lista, o computador irá percorrer a lista toda por nada, esse é o pior caso. 
Como a quantidade de passos cresce de acordo com a entrada, essa operação é O(n).

## Insertion (Inserção)

Adicionar um novo elemento no array

A eficiência do operação de inserir depende de onde o novo elemento vai ser colocado.

Inserir um elemento no fim do array só precisa um passo (mesma lógica de read).

Mas inserir no meio ou no começo é bem diferente, nesses casos vai ser preciso "empurrar" o elementos para frente/esquerda.

```               
                  ↓ inserir "figs"
array = ["apples", "bananas", "cucumbers"]
			0			1			2	
```

Para inserir figs naquela posição 1, é preciso mover os itens de posição 1 ou maiores para as casas a frente, então cucumbers vai passar de 2 para 3, e bananas de 1 para 2, assim liberando espaço para colar figs onde queremos.

```
array = ["apples", "figs", "bananas", "cucumbers"]
			0		  1		   2	       3	
```

Nesse exemplo, a operação levou 3 passos, 2 de troca de posição e 1 de inserção. 

Então como a inserção sempre leva N (numero de elementos trocados de lugar) + 1 (inserção do novo elemento), a inserção é O (n+1)

O pior caso na inserção é ter que inserir no começo, pois ai todos os itens vão ter que ser "empurrados" para frente.

## Deletion (Remover)

Parecido com a inserção, mas ao contrário, invés de "empurrar" os itens, na remoção, vamos "puxar" eles.

```
				removeu figs
array = ["apples",        "bananas", "cucumbers"]
			0		  1		   2	       3	
```

Todos os outros que estavam na frente, voltam uma casa

```
array = ["apples","bananas", "cucumbers"]
			0		  1		      2	       	
```

Também é O(n+1), onde n é todos os elementos que voltaram um casa e 1 é o elemento removido.

Aqui o pior caso também é remover o 1º item do array.


Exemplos : [[array.py]]
## Ordenação por inserção
Os valos são ordenados na ordem que estão apresentados.

Exemplo: 9, 8, 7, 6, 5, 4, 3, 2, 1

Seria ordenado do 9 até o 1, onde o números maiores são continuamente "empurrados" para a direita, enquanto os menos são "puxados" para a esquerda.

Ou seja, uma verificação é feita entre os valores, o 1º valor é 9, o 2º é 8, como 9>8 então nove assume a posição de 8, e vice versa, e assim é feito até que todos estejam na ordem correta

### Estrutura do algoritmo

O laço for conta com uma asserção lógica chamado de invariante de laço, essa asserção deve ser  verdadeira antes do começo e no fim de cada iteração, a invariante é útil para entender o porque o algoritmo é útil.

Toda a invariante deve ter 3 características.

- Inicialização: A invariante de laço é verdadeira antes do laço começar a iterar

- Manutenção: Se for verdadeira antes da iteração, deve ser manter assim até o fim da iteração atual e antes do começo a próxima iteração comece

- Término: Quando o laço terminar a invariante retornará uma propriedade que mostra que o algoritmo é correto




Exemplo do algoritmo: [[Ordenação.py]]
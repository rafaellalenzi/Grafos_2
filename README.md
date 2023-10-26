## Grafos 👩🏽‍💻👨🏻‍💻
### Segunda parte do Trabalho da disciplina Teoria dos Grafos:
- Atualização do primeiro trabalho a partir da implementação de uma série de novas funções em nossa biblioteca para manipulação de grafos. Feito por Pedro Glaser de Senna e Rafaella Lenzi Romano
##
### 🧠 Objetivos a serem cumpridos:
#### Implementação do algoritmo de Dijkstra, com a utilização de vetor ou heap.
- Ambas as funções foram criadas com o papel de retornarem as distâncias em relação aos pais do vértice escolhido. Para o Dijkstra com vetor, criamos uma matriz com distâncias iniciais infinitas, já na utilização do Heap, criamos uma lista com as distâncias, também infinitas. Nos dois casos criamos a lista "pais", com todos os vértices inicializados como -1 (não encontrados ainda), exceto o de partida. Vale ressaltar que para o Dijkstra com Heap, utilizamos a biblioteca 'Heapdict'.
  
#### Cálculo da distância e do caminho mínimo entre vértices.
- Para obter a distância e o caminho mínimo entre um par de vértices, utilizamos o Dijkstra com heap, por ser mais eficiente. Para o caminho, os vértices foram sendo armazenados em uma lista durante a execução do código, para organizá-los em ordem. Para a distância, simplesmente iniciamos a função com os vértices de partida e o de chegada para poder rodar o Dijkstra com Heap e escolher um índice na lista de distâncias

#### Obtenção do tempo médio necessário para calcular a distância entre vértices, utilizando Dijkstra com vetor ou heap.
- Durante a execução, é criado um arquivo txt que armazena os tempos de execução de cada uma das 100 implementações do algoritmo. Depois das 100 iterações o tempo total é dividido por 100 e o tempo médio é encontrado.

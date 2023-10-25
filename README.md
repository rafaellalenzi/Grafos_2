## Grafos 👩🏽‍💻👨🏻‍💻
### Segunda parte do Trabalho da disciplina Teoria dos Grafos:
- Atualização do primeiro trabalho a partir da implementação de uma série de novas funções em nossa biblioteca para manipulação de grafos. Feito por Pedro Glaser de Senna e Rafaella Lenzi Romano
##
### 🧠 Objetivos a serem cumpridos:
#### Implementação do algoritmo de Dijkstra, com a utilização de vetor ou heap.
- Utilizamos duas funções que executam o algoritmo de maneiras diferentes para cada versão do Dijkstra, entretanto, ambas retornam uma lista de distâncias aos pais do vértice escolhido.
  
#### Cálculo da distância e do caminho mínimo entre vértices.
- Para obter a distância e o caminho mínimo entre um par de vértices, utilizamos o Dijkstra com heap, por ser mais eficiente. Para o caminho, os vértices foram sendo armazenados em uma lista, para organizar os vértices em ordem.

#### Obtenção do tempo médio necessário para calcular a distância entre vértices, utilizando Dijkstra com vetor ou heap.
- Durante a execução, é criado um arquivo txt que armazena os tempos de execução de cada uma das 100 implementações do algoritmo. Depois das 100 iterações o tempo total é dividido por 100 e o tempo médio é encontrado.

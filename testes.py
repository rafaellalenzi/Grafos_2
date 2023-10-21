# Imports
from grafos import Grafo
import time
import random

 
#Grafo a ser analisado: 
grafo_atual = 'grafo_W_2' 

grafo = Grafo(tipo_grafo="lista", peso=True, txt=f'{grafo_atual}.txt').grafo

#Questão 1

#Distância
print('Distância10 :\n')
print(f'20: {grafo.distanciaHeap(10, 20)}')
print(f'30: {grafo.distanciaHeap(10, 30)}')
print(f'40: {grafo.distanciaHeap(10, 40)}')
print(f'50: {grafo.distanciaHeap(10, 50)}')
print(f'60: {grafo.distanciaHeap(10, 60)}\n')

#Caminho mínimo
print('\nCaminho_minimo10 :\n')
print(f'20: {grafo.caminho_minimo(10, 20)}')
print(f'30: {grafo.caminho_minimo(10, 30)}')
print(f'40: {grafo.caminho_minimo(10, 40)}')
print(f'50: {grafo.caminho_minimo(10, 50)}')
print(f'60: {grafo.caminho_minimo(10, 60)}\n')

#Questão 2

arquivo = open(f'tempo{grafo_atual}.txt','w')
arquivo.writelines('passo,vertice,Heap,Vetor\n')
tempo_heap = 0
tempo_vetor = 0
for k in range(100):
    vertice = random.randint(1,grafo._vertices)
  
    inicio_heap = time.time()
    grafo.DijkstraHeap(vertice)
    fim_heap = time.time()

    inicio_vetor = time.time()
    grafo.DijkstraVetor(vertice)
    fim_vetor = time.time()

    tempo_heap += fim_heap - inicio_heap
    tempo_vetor += fim_vetor - inicio_vetor

    arquivo.writelines(
        f'{k},{vertice},{fim_heap - inicio_heap},{fim_vetor - inicio_vetor}\n'
        )
    print({k})


print(f'Tempo médio de Heap = {tempo_heap/100} segundos')
print(f'Tempo médio de Vetor = {tempo_vetor/100} segundos')
arquivo.close()

#QUESTAO 3

#Distância de Dijkstra
print('Dijkstra-Turing :\n')
print(f'{grafo.distanciaHeap(2722, 11365)}')
print('Dijkstra-Kruskal :\n')
print(f'{grafo.distanciaHeap(2722, 471365)}')
print('Dijkstra-Kleinberg :\n')
print(f'{grafo.distanciaHeap(2722, 5709)}')
print('Dijkstra-Tardos :\n')
print(f'{grafo.distanciaHeap(2722, 11386)}')
print('Dijkstra-Ratton :\n')
print(f'{grafo.distanciaHeap(2722, 343930)}')

#Caminho mínimo de Dijkstra
print('Dijkstra-Turing :\n')
print(f'{grafo.caminho_minimo(2722, 11365)}')
print('Dijkstra-Kruskal :\n')
print(f'{grafo.caminho_minimo(2722, 471365)}')
print('Dijkstra-Kleinberg :\n')
print(f'{grafo.caminho_minimo(2722, 5709)}')
print('Dijkstra-Tardos :\n')
print(f'{grafo.caminho_minimo(2722, 11386)}')
print('Dijkstra-Ratton :\n')
print(f'{grafo.caminho_minimo(2722, 343930)}')

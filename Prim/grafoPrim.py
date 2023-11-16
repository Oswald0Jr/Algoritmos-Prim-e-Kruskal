import heapq

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for _ in range(vertices)]

    def adicionar_aresta(self, u, v, peso):
        # Adiciona uma aresta bidirecional ao grafo
        self.grafo[u].append((v, peso))
        self.grafo[v].append((u, peso))

    def prim(self):
        # Inicializa a fila de prioridade (heap) e o conjunto de vértices visitados
        heap = [(0, 0)]  # (peso, vértice)
        visitados = set()
        resultado = []

        while heap:
            peso, vertice_atual = heapq.heappop(heap)

            # Se o vértice já foi visitado, continue para o próximo
            if vertice_atual in visitados:
                continue

            # Adiciona o vértice atual ao conjunto de visitados
            visitados.add(vertice_atual)

            # Adiciona a aresta à Árvore Geradora Mínima
            if peso > 0:
                resultado.append((vertice_atual, peso))

            # Adiciona os vértices adjacentes não visitados à fila de prioridade
            for vizinho, peso_vizinho in self.grafo[vertice_atual]:
                if vizinho not in visitados:
                    heapq.heappush(heap, (peso_vizinho, vizinho))

        return resultado

# Exemplo de uso
grafo = Grafo(5)
grafo.adicionar_aresta(0, 1, 2)
grafo.adicionar_aresta(0, 3, 3)
grafo.adicionar_aresta(1, 2, 4)
grafo.adicionar_aresta(1, 4, 1)
grafo.adicionar_aresta(3, 4, 5)

resultado_prim = grafo.prim()
print("Árvore Geradora Mínima (Prim):", resultado_prim)

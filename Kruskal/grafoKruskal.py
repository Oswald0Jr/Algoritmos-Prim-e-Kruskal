class Grafo:
    #construtor da classe incializa o grafo com o numero de vertices especificado e uma lista de arestas vazia
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []
        
    #adiciona um aresta ao grafo com vertices de origem, destino e peso
    def adicionar_aresta(self, origem, destino, peso):
        self.arestas.append((origem, destino, peso))

    #funcao para encontrar o pai de um vertice
    def encontrar(self, pai, i):
        if pai[i] == i:
            return i
        return self.encontrar(pai, pai[i])

    #funcao para unir dois vertices em uma mesma arvore (uniao-busca)
    def unir(self, pai, rank, x, y):
        
        #raiz_x e raiz_y sao as raizes dos conjuntos aos quais os vertices x e y pertencem
        raiz_x = self.encontrar(pai, x)
        raiz_y = self.encontrar(pai, y)
        
        #se o peso da raiz de x for menor que o peso da raiz de y, isso significa que a árvore enraizada em x é menor que a árvore enraizada em y. portanto a anexa a arvore menor à maior
        if rank[raiz_x] < rank[raiz_y]:
            
        #se a árvore enraizada em x é menor que a árvore enraizada em y, atualizamos o pai da raiz de x para ser a raiz de y.
            pai[raiz_x] = raiz_y
            
        #se o rank de x for maior que o rank de y, a lógica é invertida, e a árvore menor é anexada à raiz da árvore maior.    
        elif rank[raiz_x] > rank[raiz_y]:
        
        #se a árvore enraizada em y é menor, atualizamos o pai da raiz de y para ser a raiz de x.
            pai[raiz_y] = raiz_x
            
        #se os pesos forem iguais, podemos escolher qualquer arvore para anexar a outra, mas nesse caso incerementamos o peso da arvore escolhida (rank[raiz_y] += 1)
        else:
            pai[raiz_x] = raiz_y
            
        #Se os ranks são iguais, escolhemos uma árvore e atualizamos o pai dessa raiz para ser a outra raiz, e incrementamos o rank da raiz escolhida.
            rank[raiz_y] += 1

    #funcao que implementa o algoritmo de kruskal
    #resultado eh uma lista de arestas que compoem a arvore geradora minima
    #i eh um contador para percorrer a lista de arestas ordenadas por peso
    #e eh um contador para percorrer a lista de arestas da arvore geradora minima
    def kruskal(self):
        resultado = []
        i, e = 0, 0

        # Ordena as arestas por peso
        self.arestas = sorted(self.arestas, key=lambda item: item[2])

        #pai armazena a raiz de cada conjunto 
        #rank armazena a altura de cada conjuntoq
        pai = []
        rank = []


        for node in range(self.vertices):
            pai.append(node)
            rank.append(0)

        #isso garante que a arvore gereadora minima tenha -1 arestas do que vertices, ou seja se um grafo tiver 6 vertices ele tera 5 arestas
        while e < self.vertices - 1:
            origem, destino, peso = self.arestas[i]
            i += 1
            
            #x e y são as raízes dos conjuntos aos quais os vértices de origem e destino pertencem.
            #se x e y são diferentes, a aresta não forma um ciclo, então ela é adicionada à Árvore Geradora Mínima, e os conjuntos são unidos.
            x = self.encontrar(pai, origem)
            y = self.encontrar(pai, destino)

            if x != y:
                e += 1
                resultado.append((origem, destino, peso))
                self.unir(pai, rank, x, y)

        return resultado

# Exemplo de uso
grafo = Grafo(5)
grafo.adicionar_aresta(0, 1, 2)
grafo.adicionar_aresta(0, 3, 3)
grafo.adicionar_aresta(1, 2, 4)
grafo.adicionar_aresta(1, 4, 1)
grafo.adicionar_aresta(3, 4, 5)

resultado_kruskal = grafo.kruskal()
print("Árvore Geradora Mínima (Kruskal):", resultado_kruskal)
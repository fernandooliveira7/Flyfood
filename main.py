class BruteForce:
    def get_distances(self, file):
        """
        Metodo que calcula a distancia entre os pontos do grafo.
        Calcula a distancia entre os pontos como se fossem um plano cartesiano,
        subtraindo as coordenadas x e y dos pontos e somando sua diferenca.
        Dependendo da posicao dos termos o resultado pode sair negativo,
        basta pegar o valor absoluto para resolver isso
        > |px - px2| + |py - py2|
        Recebe:
            o conteudo do arquivo, onde está o grafo
        Retorna:
            Um dicionario contendo a distancia de um ponto para todos os outros, exemplo de item
            'D': {'A': 4, 'C': 2, 'R': 7, 'B': 5}
        """
        dictDistance = {}
        matrix = []
        m, n = map(int, file.readline().split())
        for i in range(m):
            x = list(file.readline().split())

            for j in range(n):
                if x[j] != '0':
                    matrix.append((x[j], i, j))

        for touple in matrix:
            p, px, py = touple
            dictDistance[p] = {}

            for near in matrix:
                if touple == near:
                    continue

                p2, px2, py2 = near
                # |px - px2| + |py - py2|
                dictDistance[p][p2] = abs(px - px2) + abs(py - py2) 

        return dictDistance

    def all_paths(self, vertices):
        """
        Metodo recursivo que retorna todas as permutacoes de uma .
        Segue a tecnica de dividir e conquistar, divindo a lista em listas menores
        e removendo um termo por vez, retornando recursivamente quando a quantidade 
        de termos é <= 1, constrindo todas as permutacoes
        Recebe:
            Uma lista contendo os vertices do grafo
        Retorna:
            Uma lista com sublistas, onde cada sublista é uma permutacao, exemplo:
            ['a', 'b', 'c'] resulta:
            [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['c', 'b', 'a']]
        """
        if len(vertices) <= 1:
            return [vertices]

        path = []
        for i in range(len(vertices)):
            a = vertices[i]
            remain_vertices = vertices[:i] + vertices[i+1:]

            for poss in self.all_paths(remain_vertices):
                path.append([a] + poss)

        return path


    def shortest_path(self, distance_matrix):
        """
        Metodo principal da classe, calcula o menor caminho do grafo, indo de R a R.
        Cria a lista de permutacoes com o metodo all_paths sem o ponto R, esse ponto 
        pode ser atribuido no final, reduzindo a pilha de recursao. Depois, calcula o
        custo de cada caminho e salva o menor custo e seu caminho.
        Recebe:
            Um dicionario, gerado pelo metodo get_distance
        Retorna:
            O menor caminho do grafo e seu custo
        """
        vertices = list(distance_matrix.keys())
        vertices.remove("R")
        sh_path = []
        sh_cost = float('inf')

        all_paths = self.all_paths(vertices)
        for path in all_paths:
            temp = 0

            for i in range(1, len(path)):
                temp += distance_matrix[path[i-1]][path[i]]
            temp += distance_matrix['R'][path[0]] + distance_matrix['R'][path[len(path)-1]]

            if temp < sh_cost:
                sh_cost = temp
                sh_path = path
        sh_path = ['R'] + sh_path + ['R']

        return sh_path, sh_cost
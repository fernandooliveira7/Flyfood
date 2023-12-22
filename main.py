import itertools

# Função para ler a matriz de um arquivo
def read_matrix(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        matrix = [list(line.strip().split()) for line in lines]
    return matrix

# Define o arquivo de entrada
input_file = "matriz.txt"

# Lê a matriz do arquivo de entrada
matrix = read_matrix(input_file)

# Encontra os pontos de entrega (exceto R)
points = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] not in ['0', 'R']:
            points.append(matrix[i][j])

# Calcula todas as permutações dos pontos de entrega
permutations = list(itertools.permutations(points))

# Calcula o custo de cada permutação e encontra a menor
min_cost = float('inf')
best_permutation = None
for permutation in permutations:
    permutation = ['R'] + list(permutation) + ['R']
    cost = 0
    for i in range(len(permutation) - 1):
        x1, y1 = [index for index, row in enumerate(matrix) if permutation[i] in row][0], [row.index(permutation[i]) for row in matrix if permutation[i] in row][0]
        x2, y2 = [index for index, row in enumerate(matrix) if permutation[i+1] in row][0], [row.index(permutation[i+1]) for row in matrix if permutation[i+1] in row][0]
        cost += abs(x1 - x2) + abs(y1 - y2)
    if cost < min_cost:
        min_cost = cost
        best_permutation = permutation[1:-1]

# Imprime a ordem de entrega com o menor custo
print(' '.join(best_permutation))

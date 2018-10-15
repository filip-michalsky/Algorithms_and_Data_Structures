
def matrix_to_list(matrix):
    graph = {}
    for i, node in enumerate(matrix):
        adj = []
        for j, connected in enumerate(node):
            if connected=='X':
                adj.append(j)
        graph[i] = adj
    return graph


matrix = [['X','X','X','X'],
['X', 'O', 'O' ,'X'],
['X', 'X', 'O', 'X'],
['X', 'O', 'X', 'X']]

print(matrix_to_list(matrix))
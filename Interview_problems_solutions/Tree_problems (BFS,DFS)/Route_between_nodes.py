graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
        #print(path[-1])
        path.append(parent[path[-1]])
    path.reverse()
    return path


def bfs(graph, start, end):
    '''
    This BFS algorithm only works on DAGs represented
    as ADJACENCY LIST!

    Complexity:
    
    ADJACENCY LIST:
    Space: O (V + E)
    Time: O (V + E)

    ADJACENCY MATRIX:
    Space: O(V^2)
    Time: O(V^2)
    '''
    parent = {}
    queue = []
    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node == end:
            return backtrace(parent, start, end)
        for adjacent in graph.get(node, []):
            if node not in queue :
                parent[adjacent] = node # <<<<< record its parent 
                queue.append(adjacent)


print(bfs(graph, '2', '10'))
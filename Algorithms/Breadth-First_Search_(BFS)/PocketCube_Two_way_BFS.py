# Gill's Pocket Cube Code
# -----------------------
# A Pocket Cube configuration is represented by a string of 24 color indices.
# Here is a string that represents the solved configuration:
SOLVED = '000011223344112233445555'

# Color locations correspond to a Latin Cross unfolding of a cube.
# print_config(SOLVED) returns:
#   00
#   00
# 11223344
# 11223344
#   55
#   55

"""
Implementation of two-way Breadth-First-Search to find the shortest way between
all possible states to solve 2x2 Pocket Cube.

@author: filip-michalsky 

"""
def print_config(c):
    'Prints a configuration using a Latin Cross unfolding.'
    print('\n'.join(['  ' + c[:2], '  ' + c[2:4], \
        c[4:12], c[12:20], '  ' + c[20:22], '  ' + c[22:]]))

def spin_cw(config, side, turns):
    'Spins side #{side} of configuration {config} clockwise by #{turns} turns.'
    c = list(config)
    if side == 0:
        shift(c, [0,1,3,2], turns)
        shift(c, [11,10,9,8,7,6,5,4], 2 * turns)
    elif side == 1:
        shift(c, [4,5,13,12], turns)
        shift(c, [0,2,6,14,20,22,19,11], 2 * turns)
    elif side == 2:
        shift(c, [6,7,15,14], turns)
        shift(c, [2,3,8,16,21,20,13,5], 2 * turns)
    return ''.join(c)

def shift(A, ps, d):
    'Circularly shifts values in {A} at indices from {ps} by {d} positions'
    values = [A[p] for p in ps]
    for i, p in enumerate(ps):
        A[p] = values[(i - d) % len(ps)]

def neighbors(config):
    'Returns a generator of the neighbors of configuration {config}'
    for side in range(3):
        for turns in range(1, 4):
            c = spin_cw(config, side, turns)
            yield (side, turns, c)

def relate(c1, c2):
    'Returns the side and turns needed to transform {c1} into {c2} with one move'
    for (side, turns, c) in neighbors(c1): 
        if c == c2: 
            return (side, turns)
    return None

def explore_frontier(frontier, parent): 
    'Explores {frontier}, adding new configs to {parent} and {new_frontier}'
    new_frontier = []
    for f in frontier:
        for (side, turns, c) in neighbors(f):
            if c not in parent:
                parent[c] = f
                new_frontier.append(c)
    return new_frontier

def path_to_config_from_parent_map(config, parent):
    'Returns a path of configurations from root of {parent} to {config}'
    path = [config]
    while path[-1] is not None:
        path.append(parent[path[-1]])
    path.pop()
    path.reverse()
    return path

def moves_from_path(path):
    'Given {path} of adjacent configurations, returns list of moves relating them'
    moves = []
    for i in range(len(path) - 1):
        moves.append(relate(path[i], path[i + 1]))
    return moves

def solve_BFS(config):
    'Solves {config} using BFS, with verbose output'
    print('Attempting to solve from configuration: ' + config)
    parent = {config: None}
    frontier = [config]
    while len(frontier) != 0:
        print('Exploring frontier containing # configs: ' + str(len(frontier)))
        frontier = explore_frontier(frontier, parent)
    print('Explored a total of ' + str(len(parent)) + ' configurations!')
    if SOLVED in parent:
        print('Path to solved state found!')
        path = path_to_config_from_parent_map(SOLVED, parent)
        return moves_from_path(path)
    else:
        print('Path to solved state not found... :(')
        return None

def solve_faster(config):
    'Solve {config} faster!'
    #use explore_frontier and path_to_config_from_parent_map
    
    'Solves {config} using BFS, with verbose output'
    print('Attempting to solve from configuration: ' + config)
    
    parent1 = {config: None}
    parent2 = {SOLVED: None}
    
    frontier1 = [config]
    frontier2 = [SOLVED]
    
    while len(frontier1) != 0:
        #print('Exploring frontier from start containing # configs: ' + str(len(frontier1)))
        #print('Exploring frontier from end containing # configs: ' + str(len(frontier2)))
        frontier1 = explore_frontier(frontier1, parent1)
        frontier2 = explore_frontier(frontier2, parent2)
        
        intersection_nodes = set(frontier1).intersection(set(frontier2))
        
        if intersection_nodes != set():
            break
        
    print('Explored a total of ' + str(len(parent1)) + ' configurations!')
    
    if intersection_nodes != set():
        connecting_node = intersection_nodes.pop()
        
        #from start to middle
        path1 = path_to_config_from_parent_map(connecting_node,parent1)
        
        print("path1",path1)
        #from end to middle
        path2 = path_to_config_from_parent_map(connecting_node,parent2)
        
        
        path2 = path2[::-1]
        print("path2",path2)
        path = path1[:-1]+path2
        
        return moves_from_path(path)
    
#    elif SOLVED in parent1:
#        print('Path to solved state found!')
#        path = path_to_config_from_parent_map(SOLVED, parent)
#        
#        return moves_from_path(path)
    else:
        print('Path to solved state not found... :(')
        return None
    return None

def check_moves(config, moves):
    'Prints a sequence of configurations, applying {moves} to {config}'
    print('Making ' + str(len(moves)) + ' moves from starting configuration:')
    print_config(config)
    for (side, turns) in moves:
        print('Rotating side ' + str(side) + ' clockwise ' + str(turns) + ' turns:')
        config = spin_cw(config, side, turns)
        print_config(config)
    if config == SOLVED:
        print('Move sequence terminated at solved state!')
    else:
        print('Move sequence did not terminate at solved state... :(')

def scramble(config, n):
    'Returns new configuration, applying {n} random moves to {config}'
    from random import randrange 
    c = config
    for i in range(n):
        c = list(neighbors(c))[randrange(9)][2]
    return c

if __name__ == '__main__':
    config = scramble(SOLVED, 100)
    moves = solve_faster(config)
    check_moves(config, moves)

def catwidth(n, s1, s2, connections):
    """
    Modified Dijkstra's Algorithm to return the maximal minimum weight on a path between two nodes.
    
    @author: Filip Michalsky
    
    Given a list containing triples (i, j, w) representing the bandwidth w 
    between servers i and j, return the catwidth between them.
    Input: 
        'n' is the number of servers
        'connections' is a list of triples (i, j, w) 
        i, j, 's1', 's2' are server IDs, while w are bandwidth values
        Servers IDs are unique numbers in range [0,n-1]
    Output: 
        'cw' is the catwidth between servers i and j
    """
    cw = 0 #this will be the final "maximal minimal edge weight on the path
    
    #build the graph
    graph = {}
    for i in connections:
        #one direction edges (because our graph is undirected)
        try:
            graph[i[0]].append((i[1],i[2]))
        except:
            graph[i[0]] = [(i[1],i[2])]
        
        #the other direction edges (because our graph is undirected)
        try:
            graph[i[1]].append((i[0],i[2]))
        except:
            graph[i[1]] = [(i[0],i[2])]
            
    #parent = {} #parent dictionary - not used here
    catwidth = {} # dictionary of min bandwidths
    
    #initialize catwidths for all vertices in the graph
    for vertex in graph:
        catwidth[vertex]= 0
    
    catwidth[s1] = 100000000 #initialize cadwidth of itself (+inf)
    
    #initialize priority queue
    PQ = {}
    for vertex in graph:
        PQ[vertex] = catwidth[vertex]
        
    #print(graph)
    #print("catwidth",catwidth)
    #print(PQ)
    
    #print(min(catwidth, key=catwidth.get))
    
    while PQ:
        
        u = min(PQ)
        #delete minimum from the priority queue
        del PQ[u]
        #loop through adjacency list of u
        for v in graph[u]:
            #triangle inequality
            #if current catwidth is lower than the minimum
            #of the path leading to the node from which there is the edge
            #and the weight of the edge from u,v, update it as the minimum
            if catwidth[v[0]]< min(catwidth[u],v[1]):
                #print(True)
                catwidth[v[0]] = min(catwidth[u],v[1])
                PQ[v[0]] = catwidth[v[0]]
                #parent[v[0]]=u
            #print(v)
    
    cw = catwidth[s2]
    
    return cw

##################
# Test your code #
##################
def test_on_case(case):
    with open('cases/' + str(case) + '.in', 'r') as f:
        s = f.read()
    lines = s.split('\n')
    parameters = [[int(i) for i in line.split(' ')] for line in lines]
    n, s1, s2 = parameters[0]
    #print(n,s1,s2)
    connections = parameters[1:]
    cw = catwidth(n, s1, s2, connections)
    with open('cases/' + str(case) + '.out', 'r') as f:
        golden = int(f.read())
    print(golden)
    print(cw)
    if cw == golden:
        print('Passed test case ' + str(case) + '!')
    else:
        print('Failed test case ' + str(case) + '... :(')

if __name__ == '__main__':
    for case in [1,2,3]:
        test_on_case(case)

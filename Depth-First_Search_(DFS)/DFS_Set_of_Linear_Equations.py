def solve_special(C):
    """
    Implementation of DFS to solve a set of linear equations.
    @author: Filip Michalsky
    
    Given a set of linear equations C, returns a solving assignment to variables
    if the set of equations is delegated and special, and None otherwise
    Input: 
        C is a list of n lists, each with length n + 1
        C_i = [d_i, c_i1, c_i2, ... c_in]
        C_i represents equation:  0 = d_i + \sum_j c_ij * x_j
    Output: 
        x = [x_1, ... x_n]
        solving assignment of variables
    """
    d_i= []
    counter=None
    
    #create the adjacency dictionary
    adj_dict ={}
    
    for index,row in enumerate(C):
        d_i.append(row[0])
        current_adj=[]
        counter=0
        for col_item in row[1:]:
            if col_item == 0 or col_item == -1:
                counter += 1
            else:
                current_adj.append("x_"+str(counter))
                counter += 1
        adj_dict["x_"+str(index)]=current_adj
    
    print("\n","Adjacency list implemented as dictionary:")
    print(adj_dict)
    
    #now dfs
    def dfs(u):

        visited[u]=0 #MARKED NODE TO BE PROCESSING
        temp = []

        for v in adj_dict[u]:

            if visited[v]==-1:
                temp = dfs(v)
            elif visited[v]== 0:
                #print("got to node currently in process")
                #temp+= [False]
                return [False]
        temp += [u]
        
        visited[u]=1 #DONE WITH THIS NODE
        return temp
    
    ##set up DFS
    visited={}
    my_dfs_tree = []
    
    #initialize all visited to -1
    for u in adj_dict.keys():
        visited[u]=-1
        
    #loop through adjacency list
    for u in adj_dict.keys():
        if visited[u] == -1:
            
            my_dfs_tree += dfs(u)
            
    if all(my_dfs_tree)!= False:
        
        print("My DFS tree",my_dfs_tree)

        my_order = []
        for i in my_dfs_tree:
            my_order.append(int(i.split("_")[-1]))
        
        #print("order of solving",my_order)
        
        
        #initialize x
        x = []
        for i in range(len(C)):
            x.append(0)
        #print(x)
        
        for k in my_order:
            this_x_coeff = 0
            x_temp = d_i[k]
            for i,j in zip(C[k][1:],x):
                if i != -1:
                    #print("this",i,j)
                    x_temp+=i*j
                else:
                    this_x_coeff=i
                    #print(i)
            
            x[k]=int((-1/this_x_coeff)*x_temp)
            
            #print(x)
        #print("first result",x)
        return x
    
    else:
        print("This graph has cycles!")
        return None
    
    

##################
# Test your code #
##################

def test_on_case(case):
    with open('cases/' + str(case) + '.in', 'r') as f:
        s = f.read()
        C = s.split('\n')
        n = len(C)
        for i in range(n):
            C[i] = C[i].split(' ')
            for j in range(n + 1):
                C[i][j] = int(C[i][j])
        x = solve_special(C)
    with open('cases/' + str(case) + '.out', 'r') as f:
        golden = f.read()
        if golden == 'None':
            golden = None 
        else:
            golden = [int(i) for i in golden.split(' ')]
        print(golden)
        print(x)
        if x == golden:
            print('Passed test case ' + str(case) + '!')
        else:
            print('Failed test case ' + str(case) + '... :(')

if __name__ == '__main__':
    for case in [1,2]:
        test_on_case(case)

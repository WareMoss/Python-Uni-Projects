import sys                                                      #needed for maxsize
'''
Graph class
'''
class Graph(): 
  
    def __init__(self, vertices):                               #implements graph as adjacency matrix
        self.V = vertices                                       #number of vertices
        self.graph = [[0 for column in range(vertices)]         #adjacency matrix with no edges (all connections set to zero)
                    for row in range(vertices)]                 # same as adj matrix, a list of lists all containing 5 0's is made
    '''
    printMST
    Input: Takes parent as an argument
    '''
    def printMST(self, parent): 
        print ("Edge \t Weight")
        for i in range(1, self.V): 
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])
                                                                #from reached nodes find the unreached node with the minimum cost
  
    def minKey(self, key, mstSet): 
        min = sys.maxsize                                       #set min to infinity (use maxsize which is next best thing!) #sys.maxsize represents the maximum size of a datastructure 
        for v in range(self.V):                                 #count through number of vertices
            if key[v] < min and mstSet[v] == False:             #if vertex is less than min and unreached, false representing unreached and true meaning reached #key list represents the weight of the adj matrix edges
                min = key[v]                                    #assign to min 
                min_index = v                                   #min_index is position of min in key
        return min_index                                        #return min_index
  
                                                                #find MST 
    def primMST(self): 
        key = [sys.maxsize] * self.V                            #initialise key to list of values all set to infinity; same length as self.V
                                                                # creates another list of lists to instead of being 5 0's, 5 entries of the max size possible             
        parent = [None] * self.V                                #list for constructed MST 
                                                                # create another list of lists, with none being the only value for all 5 entries
        key[0] = 0                                              #set first element of key to zero (this is where we start)                                                                                   
        mstSet = [False] * self.V                               #mstSet is list of booleans set to False #creates a new list with as many values as self.v all set to false to indicate no nodes have been visited
                                                                # create another list of lists, with the entry being false for alll 5 lists
        parent[0] = -1                                          #first element of parent list set to -1 # as shows first vertex doesnt have a parent, this list shows the node values so 1, 2, 3, 4                      
  
        for vertex in range(self.V):                            #go through all vertices
            u = self.minKey(key, mstSet)                        #call minKey; minKey returns u (index of unreached node) 
            mstSet[u] = True                                    #mstSet at index of node is set to True # indicating the node has been reached, first run returns 0 showing first node is reached                                                                                               
            for v in range(self.V):                             #go through all vertices # mstSet represents the list of if the vertex has been visited or not
                if self.graph[u][v] > 0:                        # check there isnt a shorter path
                    if mstSet[v] == False:                      # check it hasnt been visited
                        if key[v] > self.graph[u][v]:           # Check if there is an edge from u to v, v is not in the MST yet, and the weight of the edge from u to v is smaller than the current value of key[v]
                                                                # the and key[v] > self.graph[u][v] checks if it has been visited and if it has, is this the shortest path, primms algorithm  assumes that edges can be traversed in both directions
                                                                # to ensure the wrong path is not chosen, the key[v] is set to max size as PRIM relys on going to every node, shortest path 
                            key[v] = self.graph[u][v]           # gets the value from the weight of the edge between nodes u and v, then stores that weight at value key[v]
                                                                # u being the column and v being the row
                            parent[v] = u                       #parent[v] is index of node; so list of parents (nodes) is the MST
  
        self.printMST(parent)                                   #print the list of parents, i.e. the MST                                
  
g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
g.primMST(); 

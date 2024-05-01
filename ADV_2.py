from collections import defaultdict
import sys
"""
A class representing the individual graph
"""
class Graph():
    '''
    __init__
    input: Size of the graph to be created and self which is the instance of the graph
    output: no output but initialises the graphs creation
    '''
    def __init__(self, size):
        self.edges = defaultdict(list)                              #dictionary of all connected nodes e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights = {}                                           #dictionary of edges and weights e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        self.size = size                                            # sets size of graph
        self.dist = []                                              # keeps track of the shortest distance from starting node to all the other nodes on the graph
        for i in range(size):
            self.dist.append(sys.maxsize)                           # adds the max distance possible as a start to represent infinity
        self.previous = []                                          # keeps track of all nodes leading to the shortest node on the path
        for i in range(size):
            self.previous.append(None)                              # sets them as none
        
    '''
    add_edge
    input: from node and to node which are used to assign the weight of the connection between the nodes, and self as a instance of the graph class is called
    output: no output but this function initialises the weights of the nodes as well
    '''
    def add_edge(self, from_node, to_node, weight):                 #bidirectional
        self.edges[from_node].append(to_node)                       # keeps track of all the edges and their node to and from
        self.edges[to_node].append(from_node)                       # storing it in a dictionary with the current node being the key and the adjacent nodes being the values aassociated with the key 
        self.weights[(from_node, to_node)] = weight                 # stores the value for traversing between nodes
        self.weights[(to_node, from_node)] = weight
    '''
    findSmallestNode
    input: self is called as it uses an instance of the graph class
    output: returns the result which is the index of the node at the top of the stack
    '''
    def findSmallestNode(self): 
        smallest = self.dist[self.getIndex(self.Q[0])]              # returns index of current node and sets smallest so far
        result = self.getIndex(self.Q[0])                           # index of this node is assigned to result
        for i in range(len(self.dist)):                             # loops through distance, to find if there are smaller paths
            if self.dist[i] < smallest:
                node = self.unpoppedQ[i]
                if node in self.Q:
                    smallest = self.dist[i]
                    result = self.getIndex(node)
        return result
            
    '''
    getIndex
    input: the adjacent nodes to the current node
    output: returns index of the adj node
    '''
    def getIndex(self, neighbour):                                  # gets the index of the node in the graph
        for i in range(len(self.unpoppedQ)):                        # iterates through the unpopped list, until it finds the node passed in
            if neighbour == self.unpoppedQ[i]:                      # if node is the same as the unpoppedlist node
                return i                                            # return its index

    '''
    getPopPosition
    input: the current node
    output: returns index of the current node
    '''
    def getPopPosition(self, uNode):                                # didnt need to use this
        result = 0
        for i in range(len(self.Q)):
            if self.Q[i] == uNode:
                return i
        return result

    '''
    getUnvisitedNodes
    input: the current node and self as an instance of the graph class is being called
    output: returns a list of adj nodes to uNode
    '''
    def getUnvisitedNodes(self, uNode):                             # passes in current node being looked at 
        resultList = []                                             # a list of adj nodes
        allNeighbours = self.edges[uNode]                           # using uNode as the key, return all the nodes adj to uNode as allNeighbours which is a list
        for neighbour in allNeighbours:                             # for adj nodes in allNeighbours
            if neighbour in self.Q:                                 # if adj node is in self.Q
                resultList.append(neighbour)                        # store adj node in resultslist, append adds the neighbour node to the end of the list
        return resultList          

    '''
    dijsktra
    input: the node to start searching at, the node to finish the node that the shortest path should be found to and self as an instance of the graph class is called
    output: returns the shortest path and the weight of the total traversal
    '''
    def dijsktra(self, start, end):                                 
        self.Q = []                                                 # represents a list of nodes
        for key in self.edges:                                      # loop through dictionary keys
            self.Q.append(key)                                      # adds all nodes to Q
        for i in range(len(self.Q)):
            if self.Q[i] == start:                                  # if the current node is the start node then
                self.dist[i] = 0                                    # sets which node is the starting node to 0 as if you start at O the shortest path to O is 0
        self.unpoppedQ = self.Q[0:]                                 # creates a copy of Q

        while self.Q:                                               # while values are left                                                     
            u = self.findSmallestNode()                             # finds smallest node in the graph                                     
            if self.dist[u] == sys.maxsize:                         # stops as no more connections
                break                                           
            if self.unpoppedQ[u] == end:                            # if its T break as no more nodes
                break

            uNode = self.unpoppedQ[u]                               # assigns current node being looked at as uNode
                                                                    # this iterates getUnvisitedNodes to return a list of adj nodes for the new node being looked at 
            for adjnodes in self.getUnvisitedNodes(uNode):          # for number of nodes in results list which is the return of get unvisited nodes
                                                                    # returns a list of adj nodes, which adjnodes iterates through 
                totaldist = self.dist[u] + self.weights[(uNode, adjnodes)]# adj is self.dist of the starting node(being O) + the weight of traveling to the next node 
                if totaldist < self.dist[self.getIndex(adjnodes)]:  # if adj is less then the value in dist for that node
                    self.dist[self.getIndex(adjnodes)] = totaldist  # assigns the new smallest distance from starting node to each node
                    self.previous[self.getIndex(adjnodes)] = uNode  # stores the previous nodes according to the shortest path
                print(adjnodes)
                print(uNode)
            self.Q.remove(uNode)  
            print(self.Q)                                # removed the current node from the stack therefore the next node is now at 0
        shortest_path = []                                          # list for shortest path
        finaldist = 0                                               # final value for the total shortest path distance
        shortest_path.insert(0, end)                                # inserts at index 0, the last value, this is potentially a First in last out stack
        u = self.getIndex(end)                                      # gets the index of the last node to be visited                                                  
        while self.previous[u] != None:                             # u is the index of the previous node, and while there is a previous nodes 
            shortest_path.insert(0, self.previous[u])               # inserts previous node at index 0 in the list, potentially a first in last out stack                          
            u = self.getIndex(self.previous[u])                     # returns the index of the previous node according to the shortest path
        for i in range(len(shortest_path) - 1):                     # -1 to ensure it doesnt reach out of index range
            from_node = shortest_path[i]                            # gets node going from
            to_node = shortest_path[i + 1]                          # gets the node its going to
            edge_weight = self.weights[(from_node, to_node)]        # gets weights of the edges between those two nodes
            finaldist = edge_weight + finaldist                     # totals the weight of the journey
        return shortest_path, finaldist


graph = Graph(8)                                                    # sets number of nodes


edges = [
    ('O', 'A', 2),
    ('O', 'B', 5),
    ('O', 'C', 4),
    ('A', 'B', 2),
    ('A', 'D', 7),
    ('A', 'F', 12),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('B', 'E', 3),
    ('C', 'E', 4),
    ('D', 'E', 1),
    ('D', 'T', 5),
    ('E', 'T', 7),
    ('F', 'T', 3),
]
    

for edge in edges:
    graph.add_edge(*edge)                                           # unpacks the edge containing all data


print(graph.dijsktra('O', 'T'))                                     # passes in start and end nodes

'''
Graph class
'''
class Graph(object):
    '''
    function to initialise the adj matrix
    Input: size of the adj matrix and self as it is a instance of graph
    Output: while nothing is output, it populates the graph to the size passed in
    '''
    def __init__(self, size):
        self.adjMatrix = []                                     # initialises an empty adj matrix, a list of lists
        self.adjMatrix.append([i for i in range(size+1)])       # creates the row values for the adj matrix
        for i in range(size):
            row = [i+1] + [0] * size                            # Initialize the row with i at the first position and 0s for the rest
            self.adjMatrix.append(row)                          # creates the column values for the matrix
        self.size = size                                        # sets the size of the matrix
    '''
    function to add a edge to the graph once it is made
    Input: takes self as its adjusting the adj matrix which is a instance of the graph class
    Output: while it does't output anything, it adds a edge to and from 2 vertex's in the matrix
    '''
    def addedge(self):                                          # adds an edge between 2 vertexes
        vertex1 = input("Enter What edge connects to")          # takes vertex 1 as user input
        vertex2 = input("Enter what edge is being connected to")# takes vertex 2 as user input
        vertex1 = int(vertex1)                                  # converts the user input which is a string to an integer
        vertex2 = int(vertex2)
        self.adjMatrix[vertex1][vertex2] = 1                    # replaces the 0 in the adj matrix with a 1 if 2 points connect
        self.adjMatrix[vertex2][vertex1] = 1
    '''
    function to add a vertex to the adj matrix after its formed 
    Input: takes self as its adjusting the adj matrix which is a instance of the graph class
    Output: While it doesn't output anything, it adds a vertex to the adj matrix 
    '''
    def addvertex(self):                                                            # function to add vertex
        self.size = self.size + 1                                                   # Increment size by 1
        self.adjMatrix[0].append(self.size)                                         # updates and adds to the matrix rows
        for row in self.adjMatrix[1:]:                                              # updates and adds to the matrix columns excludes the first element as thats the values for the rows
            row.append(0)                                                           # populates new row with 0
        new_row = [0] * (self.size + 1)                                             # Add a new row for the new vertex, the * operator is used to create a new list full of as many 0's as is needed, this is indicated by self.size+1
        new_row[0] = self.size                                                      # sets the row number
        self.adjMatrix.append(new_row)                                              # appends the adjmatrix
    '''
    function to print adj matrix
    Input: takes self as its printing the adj matrix which is a instance of the graph class
    Output: Nothing returned but prints adj matrix to terminal
    '''
    def print_adjmatrix(self):                                                      # function to print matrix 
        for row in self.adjMatrix:                                                  # for each row in the matrix
            print(" ".join(map(str, row)))                                          # Join each element of the row into a single string separated by a space, 
                                                                                    # using the map function which applies a function to all elements of an iterable,
                                                                                    # in this case makes all the rows a string
    '''
    function to remove vertex from the adj matrix
    Input: takes self as its adjusting the adj matrix which is a instance of the graph class
    Output: If the vertex is't found, none is returned else nothing is returned as but the adj matrix is changed
    '''
    def remove_vertex(self):                                                        # function to remove a vertex
        removevertex = input("Enter vertex you want removed")                       # get user input for removed vertex
        removevertex = int(removevertex)                                            # converts string to an integer
        if removevertex < 0 or removevertex >= self.size:                           # error catch for if the vertex doesn't exist
            print("Invalid vertex index.")
            return None
        del self.adjMatrix[removevertex]                                            # Remove the row corresponding to the vertex
        for i in self.adjMatrix:                                                    # Remove the column corresponding to the vertex
            del i[removevertex]
        self.size -= 1                                                              # Update the size of the adj matrix
    '''
    function to remove edge from the adj matrix
    Input: takes self as its adjusting the adj matrix which is a instance of the graph class
    Output: If the edge isn't found, none is returned else the edges removed are printed
    '''
    def remove_edge(self):                                                          # function to remove an edge in the adj matrix
        vertex1 = input("Enter What vertex the edge connects to")                   # get user input for removed vertex
        vertex2 = input("Enter what vertex is being connected to")
        vertex1 = int(vertex1)                                                      # converts string to an integer
        vertex2 = int(vertex2)
        if vertex1 < 1 or vertex1 > self.size or vertex2 < 1 or vertex2 > self.size:# error catch for if the vertex is invalid
            print("Invalid vertex indices.")
            return None 
        if self.adjMatrix[vertex1][vertex2] == 0:                                   # error catch for if vertex exists but no edges
            print(f"No edge between vertices {vertex1} and {vertex2}.")             # f string to improve formatting 
        else:
            self.adjMatrix[vertex1][vertex2] = 0                                    # sets the vertex edge values to 0, removing the edges
            self.adjMatrix[vertex2][vertex1] = 0
            print(f"Edge between vertices {vertex1} and {vertex2} removed.")
'''
main function
Input: N/A
Output: Returns fin if the user decides to stop the loop by entering 6
'''
def main():                                                                          # main function
        g = Graph(6)                                                                 # creates a new instance of the graph class with a size of 6
        fin = False                                                                  # flag for iterative loop to loop until the user decides to stop
        while fin == False:
            choice = input("display graph(1), add vertex(2), add edge(3), remove vertex(4), remove edge(5), to end(6)")
            choice = int(choice)
            if choice == 1:
                g.print_adjmatrix()
            elif choice == 2:
                g.addvertex()
            elif choice == 3:
                g.addedge()
            elif choice == 4:
                g.remove_vertex()
            elif choice ==5:
                g.remove_edge()
            elif choice == 6:
                return fin == True
if __name__ == '__main__':                                                            # to call main function
   main()
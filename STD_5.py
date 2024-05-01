'''
Node class
'''
class Node:                                                                                                                        # defines node class for representing the nodes in the linked list
    def __init__(self, dataval = None):
        self.dataval = dataval                                                                                                     # sets value for the node
        self.nextval = None                                                                                                        # sets value for the next pointer of the node
'''
SLinkedList class
'''
class SLinkedList:                                                                                                                 # defines the class for the linked list
    def __init__(self):
        self.headval = None                                                                                                        # sets the head of the linked list
    '''
    listprint
    Input: takes no input other then self as it refers to an instance of the linked list and node class
    Output: Nothing is returned but this function prints the linked list to the terminal to display to the user
    '''
    def listprint(self):                                                                                                           # function to print the nodes in the linked list
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval                                                                                            # move to next node according to links
                                                                                                                                   # This funciton is never called originally so I incorporated it into the solution  
    '''
    AtBeginning
    Input: Takes newdata as a argument which is the value for the headval, first element in the linked list 
    as well as self as it references a instance of Node
    Output: While nothing is returned, the goal of this function is to set the headval of the linked list / replace it if there is already a value present
    '''       
    def AtBeginning(self, newdata):                                                                                                # inserts new node at the start of the list
        NewNode = Node(newdata)                                                                                                    # creates new node at start with specified data
        if self.headval is None:                                                                                                   # if there isn't a value for self.headval yet, set one
            self.headval = NewNode
            return
        else:
            answer = input(self.headval.dataval + " Is already stored as the first value, Would You Like To Overwrite this? Y / N")# a else to handle if there is already a value for self.headval
            if answer.capitalize() == "Y":                                                                                         # to ensure the user input is correct 
                self.headval = None                                                                                                # sets old value to none
                self.AtBeginning(newdata)                                                                                          # recursively calls subroutine with new value as newdata
            else: 
                return
    '''
    AtEnd
    Input: Takes newdata as a arguement which is the value for the last item in the list, and self as it references 
    an instance of node
    Output: while nothing is returned if a exception occurs such as headval being none, the goal of this function is to insert the last value 
    into the linked list
    '''
    def AtEnd(self, newdata):                                                                                                      # inserts new node at the end of the list
        NewNode = Node(newdata)                                                                                                    # creates new node
        if self.headval is None:                                                                                                   # if the list is empty, make the new node
            self.headval = NewNode                                                                                                 # sets pointer for headval
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode                                                                                                     # set the ext pointer of the last node to the new node
    '''
    Insert
    Input: This function takes val_before and newdata as arguments, these representing the location of the node before the new data and the 
    value being stored there, as well as self as a instance of the Node class is referenced
    Output: Nothing is returned if a exception is caught such as no node is entered or the input from the user is invalid, but the goal
    of this function is to insert a new node where the user specifies
    '''
    def Insert(self, val_before,newdata):                                                                                          # inserts new node after a val_before
        if val_before is None:                                                                                                     # if there is no value entered for the before
            print("No node to insert after")
            return
        else:
            cur_node = self.headval                                                                                                # start searching through the linked list, starting with the headval
            while cur_node.dataval != val_before:                                                                                  # if the val_before isnt found
                cur_node = cur_node.nextval                                                                                        # set the current node being looked at as the next node
                if cur_node is None:                                                                                               # If loop searches entire linked list and still no result, display invalid input
                    print("Invalid Input")
                    return
            newNode = Node(newdata)                                                                                                # creates a new node for the inserted value
            newNode.nextval = cur_node.nextval                                                                                     # stores the next value for the new node 
            cur_node.nextval = newNode                                                                                             # changes the next value for the previous node
list = SLinkedList()                                                                                                               # creates linked list
list.headval = Node("Fri")                                                                                                         # sets head node for the list
list.AtBeginning("Mon")                                                                                                            # calls at beginning function
e2 = Node("Tue")                                                                                                                   # creates nodes for the list
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2                                                                                                          #links the nodes together
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
list.AtEnd("Sun")                                                                                                                  # adding new node at the end 
list.listprint()                                                                                                                   # prints list
val_before = input("Enter date before the input data")                                                                             # alows user to correct the list if they want to
val_before = val_before.capitalize()                                                                                               # used to ensure the input conforms to the node syntax
newdata = input("Enter input data")
newdata = newdata.capitalize()
list.Insert(val_before, newdata)                                                                                                   # inserts data into the linked list
list.listprint()

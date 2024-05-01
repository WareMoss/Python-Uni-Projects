""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 5. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 5 (available in Week 5).

    There will be some ***introductory challenges*** in Week 4, with solutions released in Week 5.
    It is STRONGLY RECOMMENDED you attempt these!

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the Week 5 lab sheet guidance). 
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    '''
find_i
Input: target value in the tree and self which is a instance of the binary tree class
Output: if the value is found then it returns the node if not, return false
Iterative approach to search through the binary tree, starting from the root node and compares the value of each node to the target value
'''
    def find_i(self, target): 
        cur_node = self.root                         # sets the root of the tree to be the current node
        while cur_node is not None:                  # while the current node has a value:
            # print(cur_node.data)                   # this was helpful for debugging and checking the correct node was found
            if cur_node.data == target:              # check if the current node is the desired value
                return cur_node                      # if found then return the node value
            elif cur_node.data > target:             # checks if the current node is greater then target
                cur_node = cur_node.left             # if so move left
            else:
                cur_node = cur_node.right            # else the value must be bigger then the current node so move right 
        return False                                 # if the value isn't found, return false indicating the value isnt in the tree
    '''
find_r
Input: target value in the tree and self which is a instance of the binary tree class
Output: if the value is found then it returns true otherwise return false if its not found and return nothing if there is no root node
the function which calls the recursive function to search the binary tree
'''
    def find_r(self, target):                        # recursive method for searching the tree
        if self.root:                                # check if current node is the root, making sure the algorithm starts at the root node of the tree
            if self._find_r(target, self.root):      # call recursive function for searching the tree
                return True                          # if the target value is found return true
            return False                             # if target value is not found then return false
        else:
            return None                              # otherwise tree has no root so return nothing
    '''
_find_r
Input: target value in the tree, self which is a instance of the binary tree class and the current node being searched
Output: as this is a recursive funciton, it returns itself or true or if the node doesnt exist the function finishes
recursive function to search the binary tree, the function is called by find_r and depending on how the target value compares to the current node, if the target isnt found the function 
is called with the left or right child being set as the current node, if the target value is found then true is returned, otherwise the function ends
'''
    def _find_r(self, target, cur_node):               # recursive search function
        # print(cur_node.data)                         # this was helpful for debugging so I could see each node being searched and make sure it was correct
        if target > cur_node.data and cur_node.right:  # if the value being searched for is greater then the current node and it has a right child
            return self._find_r(target, cur_node.right)# recursivly call _find_r with the right child being set to the current node
        elif target < cur_node.data and cur_node.left: # if the value being searched for is less then the current node and the node has a left child
            return self._find_r(target, cur_node.left) # recursivly call _find_r with the left child being set to the current node
        if target == cur_node.data:                    # if target value is found 
            return True                                # return true
    '''
    REMOVE
    Input: target node to be removed from the tree and self which is a instancce of the binary tree class
    Output: Returns either false, True or calls IF_LEFT_AND_RIGHT function to deal with if the target node has left and right children
    '''
    def REMOVE(self, target):
        if self.root is None:                                       # exception handling for if the tree is empty, return false immediately 
            return False
        elif self.root.data == target:                              # if the root node is the target value
            if self.root.left is None and self.root.right is None:  # Checks if the target node has no children
                self.root = None                                    # if so, simply remove the node
            elif self.root.left and self.root.right is None:        # if the target node has a left child
                self.root = self.root.left                          # set the left child to be the new root node
            elif self.root.left is None and self.root.right:        # if the target node has a right child
                self.root = self.root.right                         # set the right child to be the new root node
            elif self.root.left and self.root.right:                # if the node to be removed is a root node and has both left and right children,
                self.IF_LEFT_AND_RIGHT(self.root)                   # call function to deal with this
            return True                                             # return true as the node has been removed
        else:                                                       # case for if the root node is not the target value
            parent = None                                           # used to keep track of the parent node 
            node = self.root                                        # used to keep track of the root node

            while node and node.data != target:                     # while loop for if the node being checked isnt the target value
                parent = node                                       # keep track of parent node
                if target < node.data:                              # if the target node is less than the current node, move to left child
                    node = node.left                                # move to the left child of current node
                elif target > node.data:                            # if the target node is greater than the current node, move to the right child
                    node = node.right                               # move on to the right child of current node
            if node is None or node.data != target:                 # if the current node is empty or the current node is not equal to target after the tree has been searched
                return False                                        # return false indicating not found
            elif node.left is None or node.right is None:           # if the target node has either no left or no right child or no children at all
                if target < parent.data:                            # if the target node is less then its parents value
                    parent.left = None                              # set the left child of current nodes parent to none, deleting the current node 
                else:
                    parent.right = None                             # set the right child of current nodes parent to none, deleting the current node 
                    return True                                     # return true as node has been removed
            elif node.left and node.right is None:                  # if target node has no left and right children
                if target < parent.data:                            # if less then target nodes parent
                    parent.left = node.left                         # sets left child of the target node to be the left child of the parent, deleting and replacing the target node
                else:
                    parent.right = node.left                        # sets left child of the target node to be the right child of the parent node
                return True                                         # true returned so node has been deleted
            elif node.left is None and node.right:                  # if there is no left child but there is a right child
                if target > parent.data:                            # if the target node is greater then the parent node
                    parent.right = node.right                       # the target nodes right child becomes the parents right child, deleting and replcing the target node
                else:
                    parent.left = node.right                        # the target nodes right child becomes the parents left child, replacing the target node
                return True
            else:
                self.IF_LEFT_AND_RIGHT(node)                        # call IF_LEFT_AND_RIGHT if the target node has both left and right children
    '''
    IF_LEFT_AND_RIGHT
    Input: Node is the node which is going to be removed so it takes that as a input and also self which is a instance of the binary tree class
    Output: While nothing is returned, this function removes the node while also sorting the children of the node into their appropriate places according to binary tree rules
    '''
    def IF_LEFT_AND_RIGHT(self, node):                              # this is called when the target node has been found and has both left and right children
        delNodeParent = node                                        # creates a new variable called delNodeParent and assigns it the value of the target node
        delNode = node.right                                        # creates a new variable called delNode and assigns it the value of the right child of the target node

        while delNode.left:                                         # while loop which terminates when there is no more left children
            delNodeParent = delNode                                 # sets delNodeParent as delNode
            delNode = delNode.left                                  # sets delNode as its left child
        node.data = delNode.data                                    # replace value of the target node with the value from delNode

        if delNode.right:                                           # if delNode has a right child
            if delNodeParent.data > delNode.data:                   # check if delNodeParent is greater then delNode
                delNodeParent.left = delNode.right                  # if true, set delNodeParents left child to delNodes right child 
            else:
                delNodeParent.right = delNode.right                 # set delNodeParents right child to delNodes right child
        else:
            if delNode.data < delNodeParent.data:                   # if delNode is less then delNodeParent
                delNodeParent.left = None                           # set delNodeParents left child to none 
            else:
                delNodeParent.right = None                          # set delNodeParents right child to none
            
#references: used: https://youtu.be/yYALsys-P_w?si=NwVO58ecXYYrYv3Z
                                                                    #example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
bst.insert(10)
bst.insert(11)
bst.insert(12)
bst.insert(13)
bst.insert(14)
bst.insert(15)
bst.insert(100)
bst.insert(200)

bst.REMOVE(6)
bst.find_i(200)
bst.find_r(200)
bst.display(bst.root)
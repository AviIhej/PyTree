class Node:
    #This vertex class has helper functions for the tree class invisible to the user/tester

    # Constructor initializing left and right children to none
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None
                

    def insert (self, data):
        #Check to see if the node that calls this info already has data that we want to assert. If so we return false
        if self.value == data: 
            return False
            
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data) #If there is a left child, we will insert the date into that left child
            else:
                self.leftChild = Node(data) #if no left child, we create a new node using that data, add it as the left child to the current node, and return true
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data) #if the data we are trying to insert is greater than the value of the current node, we insert it into the right child.
            else:
                self.rightChild = Node(data)#if the right child already exists we call the insert function on that right child using this data - if not, we create a new node and assign it as the new right child for that node
                return True

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)

class BinarySearchTree:
    # Define constructor which defines a root node into the tree
    def __init__ (self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    

def fill_tree(tBinarySearchTree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

bst = BinarySearchTree()
print(bst.insert(10))

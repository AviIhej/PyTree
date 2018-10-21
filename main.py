class node:
    def __init__(self, value=None):
        self.value=value
        self.left_child=None
        self.right_child=None

class binary_search_tree:
    def __init__(self):
        self.root=None
    
    # Allows you to add elements to a binary search tree
    def insert(self, value):
        if self.root==None:
            self.root=node(value)
        else:
            self._insert(value, self.root) #Private insert is going to be recursive

    def _insert(self, value, cur_node): #this is a privat function
        if value<cur_node.value: #Check to see if the past value is less than the value at the cuttent node
            if cur_node.left_child==None:#first case: the current node does not have a left child, in which case we create a new node and insert the value in to that node then set the current node's left child into that node
                cur_node.left_child==node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child = node(value)
            else:
                self.insert(value, cur_node.right_child)
        else:
            print "Value already in Tree!"
    
    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
    def _print_tree(self, cur_node): #Private Version
        if cur_node!=None:
            self._print_tree(cur_node.left_child)
            print str(cur_node.value)
            self._print_tree(cur_node.right_child)


def fill_tree(tree, num_elems=100, max_int=1000):
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree = fill_tree(tree)

tree.print_tree()

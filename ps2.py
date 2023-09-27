class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: int
    # item: int
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Part a #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)  # Corrected line
        return None

    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self.key is None:  # Corrected line
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    '''
    Inserts a key into the tree
    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        # Here, we shall only update the size of the current node based on its children. Count the current node and then add the size of its left and right subtrees
        self.size = 1 + (self.left.size if self.left else 0) + (self.right.size if self.right else 0)
        return self
    
    ####### Part b #######

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)
    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on
    Returns: the root of the tree/subtree
    Example:
    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10
    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if child_side == "R":
            target_node = self.right
        elif child_side == "L":
            target_node = self.left  
        elif child_side == "R":
            target_node = self.right  
        else:
            return self  # In case the child_slide will be invalid
        
        if not target_node:
            return self  
        
        if direction == "R":
            nu_target = target_node.left  
            if nu_target:
                target_node.left = nu_target.right
                nu_target.right = target_node
                # Update the sizes
                target_node.size = 1 + (target_node.left.size if target_node.left else 0) + \
                                (target_node.right.size if target_node.right else 0)
                nu_target.size = 1 + (nu_target.left.size if nu_target.left else 0) + \
                                (nu_target.right.size if nu_target.right else 0)
                if child_side == "L":
                    self.left = nu_target
                else:
                    self.right = nu_target
                    
        elif direction == "L":
            nu_target = target_node.right  
            if nu_target:
                target_node.right = nu_target.left
                nu_target.left = target_node
                # Update sizes
                target_node.size = 1 + (target_node.left.size if target_node.left else 0) + \
                                (target_node.right.size if target_node.right else 0)
                nu_target.size = 1 + (nu_target.left.size if nu_target.left else 0) + \
                                (nu_target.right.size if nu_target.right else 0)
                if child_side == "L":
                    self.left = nu_target
                else:
                    self.right = nu_target
        
        else:
            return self  # in case of an invalid direction parameter
        
        # Update the size of the current node
        self.size = 1 + self.size + (self.left.size if self.left else 0) + (self.right.size if self.right else 0)
        
        return self 


    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self
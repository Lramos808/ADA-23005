class Node:

    def __init__(self, value, index):
        self.value = value
        self.left = None
        self.right = None
        self.index = index
        self.path_length = None
        
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
    def get_left(self):
        return self.left
    
    def set_left(self, left):
        self.left = left
        
    def get_right(self):
        return self.right
    
    def set_right(self, right):
        self.right = right
    
    def get_index(self):
        return self.index
        

        
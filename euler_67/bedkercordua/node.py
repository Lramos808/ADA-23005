class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.sum_value = value
        
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
    
    def get_sum_value(self):
        return self.sum_value
    
    def add_sum_value(self, sum_value):
        self.sum_value += sum_value
    
        

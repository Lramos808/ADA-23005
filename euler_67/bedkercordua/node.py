class Node:

    def __init__(self, value, marker = False):
        self.value = value
        self.left = None
        self.right = None
        self.sum_value = value
        self.marker = marker
        
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
        
    
    def get_marker(self):
        return self.marker
    
    
    def set_marker(self, marker):
        self.marker = marker
    
        
    def determine_greater(self):
        if self.left.get_sum_value() > self.right.get_sum_value():
            self.left.set_marker(True)
            self.sum_value += self.left.get_sum_value()
            
        else: 
            self.right.set_marker(True)
            self.sum_value += self.right.get_sum_value()

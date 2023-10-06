class Node:

    def __init__(self, value, index):
        self.value = value
        self.left = index[0] + 1, index[1]
        self.right = index[0] + 1, index[1] + 1
        self.index = index
        self.no_go = False
        self.highest_sum = 0
        
    def get_no_go(self):
        return self.no_go
    
    def set_no_go(self, val):
        self.no_go = val
        
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
    
    def get_highest_sum(self):
        return self.highest_sum
    
    def set_highest_sum(self, high_sum):
        self.highest_sum = high_sum
    
        

        
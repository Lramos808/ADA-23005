class Beer:
    """ 
    This class creates a beer object with the __init__ function needing(brewery_id, name, style, abv) 
    """
    
    def __init__(self, brewery_id, name, style, abv, beer_id):
        self.brewery_id = brewery_id
        self.name = name
        self.style = style
        self.abv = abv
        self.id = beer_id
        self.brewery = None
        
    
    def get_brewery(self):
        print(self.brewery)
        return self.brewery
        
    
    def __str__(self):
        return self.name
    
    
    if __name__ == '__main__':
        print("Running for debug")
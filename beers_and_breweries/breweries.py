class Breweries:
    def __init__(self, data):
        self.b_id = data[0]
        self.name = name[1]
        self.city = data[2]
        self.state = state[3]
        self.beers = []
        
    
    def add_beer(self, beer):
        self.beers.append(beer)
        
    
    def list_beers(self):
        return self.beers
    
    
    def __str__(self):
        return self.name
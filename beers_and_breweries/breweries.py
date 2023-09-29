class Breweries:
    def __init__(self, b_id, name, state, city):
        self.b_id = b_id
        self.name = name
        self.state = state
        self.beers = []
        self.city = city
        
    
    def add_beer(self, beer):
        self.beers.append(beer)
        
    
    def list_beers(self):
        return self.beers
    
    
    def __str__(self):
        return self.name
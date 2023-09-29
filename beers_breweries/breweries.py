class Breweries:
    def __init__(self, brewery_id, name, city, state):
        self.brewery_id = brewery_id
        self.name = name
        self.city = city
        self.state = state
        self.beers = []
        
    
    def add_beer(self, beer):
        self.beers.append(beer)
        
        beer.brewery = self
        
    
    def list_beers(self):
        return self.beers
    
    
    def __str__(self):
        return self.name
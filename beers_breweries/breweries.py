from dataclasses import dataclass

@dataclass
class Breweries:
    def __init__(self, brewery_id, name, city, state):
        self.brewery_id = brewery_id
        self.name = name
        self.city = city
        self.state = state
        self.beers = []


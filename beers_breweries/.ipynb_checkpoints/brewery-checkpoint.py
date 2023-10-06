from dataclasses import dataclass, field

@dataclass (order=True)

class Brewery:
  """ 
  This dataclass takes a list with 3 freatures; name, city and state. The brewery object instanciated will also have an empty beer_list
  The dataclass also contains one method, add_beer_obj(self, beer) there it takes a beer object and appends to list
  """
    brewery_id: int
    name: str
    city: str
    state: str
    beer_list: list = field(default_factory=list)
    
    def add_beer_obj(self, beer):
        self.beer_list.append(beer)
        beer.brewery = self
    
    def __str__(self):
        return f"{self.name} {self.city} {self.state}"

""" The following code imports the breweries.csv and creates a list of brewery objects called brewery_obj"""

if __name__ == "__main__":
    brewery_obj = []
    with open("breweries.csv", "r") as f:
        for line in f:
            line = line.replace("\n", "")
            line = line.split(",")
            brewery_obj.append(Brewery(*line))
            
    brewery_obj.pop(0)

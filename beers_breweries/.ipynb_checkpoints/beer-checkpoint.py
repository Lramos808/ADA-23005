from dataclasses import dataclass, field

@dataclass(order=True)
class Beer():
    """ 
    This class creates a beer object with the __init__ function needing(brewery_id, beer_id, name, style, abv) 
    Methods include 
    get_brewery_id()
    get_beer_id()
    get_beer_info()
    """
    beer_index: int
    abv: str
    ibu: str
    beer_id: int
    name: str
    style: str
    brewery_id: int
    ounces: float
    brewery: object = field(default=None)
    
    
    def check_empty(self, thing):
        if thing == '':
            return None
        else:
            return float(thing)
        
    
    def __str__(self):
        return f'{self.name}: {self.style} from {self.brewery}'

    
if __name__ == '__main__':
    print("Running for debug")

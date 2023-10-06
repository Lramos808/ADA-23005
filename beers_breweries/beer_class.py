from dataclasses import dataclass

@dataclass
class Beer():
    """ 
    This class creates a beer object with the __init__ function needing(brewery_id, beer_id, name, style, abv) 
    Methods include 
    get_brewery_id()
    get_beer_id()
    get_beer_info()
    """
    def __init__(self, brewery_id, beer_id, name, style, abv):
        self.brewery_id = brewery_id
        self.beer_id = beer_id
        self.name = name
        self.style = style
        self.abv = abv
    
    if __name__ == '__main__':
        print("Running for debug")

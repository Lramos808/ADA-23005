class Lookup:
    def __init__(self):
        """
        Initializes the lookup object to manage listing of Car objects
        
        Attributes:
        listing of cars - dict - key: year make model, value: car object
        
        Methods:
        add_car - Parameters: car - obj
        
        remove_car - Parameters: car - obj
        
        search_for_car
        - return makes
        - return models
        - return years
        - return car
        
        """
        self.listing_of_cars = {}

    
    def add_car(self, car):
        self.listing_of_cars.update({f"{car.year} {car.make} {car.model}" : car})
    
    
    def remove_car(self, car):
        del self.listing_of_cars[f"{car.year} {car.make} {car.model}"]
        
    
    def display_car(self, car):
        return car.__str__()
    
    
    def search_for_car(self):
        self.return_makes()

        make = input('What is the make of the car you\'re looking for?')
        
        self.return_models(make)
                
        model = input('What is the model of the car you\'re looking for?')
        
        self.return_years(make, model)

        year = input('Which year are you looking for?')
        
        return self.return_car(make, model, year)


    def return_makes(self):
        makes = set()
        for car in self.listing_of_cars.values():
            makes.add(car.make)
        
        print(makes) 
    
    
    def return_models(self, make):
        models = set()
        for car in self.listing_of_cars.values():
            if car.make == make:
                models.add(car.model)
            
        print(models)
    
    
    def return_years(self, make, model):
        years = set()
        for car in self.listing_of_cars.values():
            if car.make == make and car.model == model:
                years.add(car.year)
        
        print(years)
    
    def return_car(self, make, model, year):
        cars = set()
        for car in self.listing_of_cars.values():
            if car.make == make and car.model == model and car.year == year:
                cars.add(car)
                
        return cars.pop()

    
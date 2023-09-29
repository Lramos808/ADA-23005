class Car:
    def __init__(self, data):
        self.make = data[0]
        self.model = data[1]
        self.year = data[2]
        self.fuel = data[3]
        self.hp = data[4]
        self.cyl = data[5]
        self.transmission = data[6]
        self.wheel_drive = data[7]
        self.doors = data[8]
        self.market_cat = data[9]
        self.size = data[10]
        self.style = data[11]
        self.hwympg = data[12]
        self.citympg = data[13]
        self.popularity = data[14]
        self.msrp = data[15]
        
    def __str__(self):
        return f"{self.make}, {self.model}, {self.year}, {self.fuel}, {self.hp}, {self.cyl}, {self.transmission}, {self.wheel_drive}, {self.doors}, {self.market_cat}, {self.size}, {self.style}, {self.hwympg}, {self.citympg}, {self.popularity}, {self.msrp}"
    
    # def __gt__(self, other):
    #     return 
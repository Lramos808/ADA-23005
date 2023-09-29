from car import Car 
from lookup import Lookup 

f = open("./data/car_data.csv", "r")
file_csv = f.read()
f.close()

lines = file_csv.split("\n")
lines.pop(0) # this is header info, we don't need
lines.pop() # looks like \n is here which will break our object init

database = list()
for x in lines:
    database.append(Car(x.split(",")))
    

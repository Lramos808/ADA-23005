from beer_class import Beer
f = open("beers.csv", "r")
file_csv = f.read()
f.close()

lines = file_csv.split("\n")
lines.pop(0) # this is header info, we don't need
lines.pop() # looks like \n is here which will break our object init

database = list()
for x in lines:
    y = []
    x = x.split(",")
    y.append(x[6])
    y.append(x[3])
    y.append(x[4])
    y.append(x[5])
    y.append(x[1])
    database.append(Beer(*y))
    

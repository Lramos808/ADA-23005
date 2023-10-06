from beer import Beer
import csv


beers = []
with open("beers.csv", "r") as f:
    for line in f.readlines()[1:]:
        temp = line.replace('\n', '').split(',')
        
        # two lines have been identified as being broken
        # (line 103 and 382). These have commas in the 
        # beer name. This will repair this error, assuming
        # a single comma exists in the name. This is NOT
        # a perfect solution... Temporary at best...
        if len(temp) > 8:
            temp.insert(4, temp.pop(4) + temp.pop(4))
            
        # replace empty string with None
        temp = [elm if elm else None for elm in temp]
        
        beers.append(temp)
        
        
beer_list = []
for idx, beer in enumerate(beers):
    new_beer = Beer(beer_index=int(beer[0]),
                    abv=beer[1],
                    ibu=beer[2],
                    beer_id=int(beer[3]),
                    name=beer[4],
                    style=beer[5],
                    brewery_id=int(beer[6]),
                    ounces=float(beer[7]))
    
    beer_list.append(new_beer)

    
print(beer_list[0])
print(beer_list[103])
print(beer_list[382])


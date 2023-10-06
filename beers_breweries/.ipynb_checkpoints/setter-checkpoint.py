def setter(beer, brewery_list):
    '''
    place beer object in brewery object
    
    look through brewery beer list and add the brewery to the beer's brewery list
    '''
    
        
    brewery_list[beer.brewery_id].beer_list.append(beer)

    beer.brewery = brewery_list[beer.brewery_id]

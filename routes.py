from os import close
from distance import get_distance
from prepare_data import package_map


'''
This file is where the routes ompitizing function is located. 
The function is used as part of the truck route preperation. 
The function uses neared neighbour.
'''
#Gets package address Id(1)
def get_package_address(package_id):
    return package_map.get(package_id).get_address_id()

#Recursive function to find the most optimal route using nearest neighbour O(n^2)
def optimize_route(on_truck,  delivered, start=0):
    #Keep track delivered
    route = delivered 
    #check truck not empty
    if(len(on_truck)>0):
        shortest = None
        index = None
        #loop get nearest neighbour and add to route
        for id in range(0,len(on_truck)):   
            a = 0
            if(start != 0):
                a = start
            b = get_package_address(on_truck[id])
            if(shortest == None or float(shortest) > get_distance(a,b)):
                    shortest = get_distance(a,b)
                    index = id   
        # shortest           
        closest_location = on_truck.pop(index)
        route.append(closest_location)
        #if not empty repeat
        return optimize_route(on_truck, route, get_package_address(closest_location))
    else:
        return route
        

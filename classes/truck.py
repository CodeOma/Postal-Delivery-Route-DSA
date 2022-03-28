from classes.hash_table import HashMap

class Truck:
    def __init__(self, capacity=16):
        self.truck = []
        pass
    
    # function used to get the full list of entries at start of day
    # Space-time complexity is O(1)
    def get_map(self):
        return self.truck

    # function to check the packages that are loaded into the truck
    # Space-time complexity is O(1)
    def check(self):
        return self.truck

    #
    def add(self, item):
        self.truck.append(item)
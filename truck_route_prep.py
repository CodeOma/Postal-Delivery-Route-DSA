from prepare_data import package_map
from distance import get_total_route_miles
from routes import optimize_route

'''
This file is where the packages are loaded onto the trucks given their requirements. 
The routes are then optimized using the optimize_route function from routes.py and then are ready for delivery.
'''

truck1 = []
truck2 = []
truck3 = []

# Assigns each package to a truck 1,2 or 3 based on rules.
# O(N)        
def load_trucks():
    packages = package_map.get_all()
    for package in packages:
        
        if 'Wrong address' in package.get_note():
            package.set_truck(3)
            truck3.append(package.get_id())
            package.set_address('410 S State St')
            package.set_zip('84111')
        elif 'on truck 2' in package.get_note():
            package.set_truck(2)
            truck2.append(package.get_id())
        elif 'Delayed' in package.get_note():
            package.set_truck(2)
            truck2.append(package.get_id())
        elif (package.get_deadline() != 'EOD' and package.get_id() not in truck2):
            package.set_truck(1)
            truck1.append(package.get_id()) 
        elif ('Must be' in package.get_note() or int(package.get_id()) in [13,15,19,20,14]):
            package.set_truck(2)
            truck2.append(package.get_id()) 



# Load the rest of the packages O(n)
def load_rest():
    packages = package_map.get_all()
    not_on_truck = []
    #get no on truck
    for package in packages:
        if(int(package.get_id()) not in truck1):
            if(int(package.get_id()) not in truck2):
                if(int(package.get_id()) not in truck3):
                    not_on_truck.append(package.get_id())

    # optimize route for not on truck
    route = optimize_route(not_on_truck, [])
# int(package_map.get(truck1[-1]).get_address_id())s
    for id in route:
        # print(package_map.get(package))
        if (package_map.get(id).get_truck() == 'None'):
            if(len(truck2) <=15):
                package_map.get(id).set_truck(1)
                truck2.append(package_map.get(id).get_id())
            elif(len(truck1) <=15):
                package.set_truck(2)
                truck1.append(package_map.get(id).get_id())               
            else:
                package.set_truck(3)
                truck3.append(package_map.get(id).get_id())

        # Assigns each package to a truck 1,2 or 3 based on rules.
        # O(N)
        
load_trucks()
load_rest()

#Get package delviery status O(n)
def get_package_delivery_status():
    id = int(input('Enter a package ID: '))
    if id in range(1, package_map.get_size()):
        package_map.get(id)
    elif id not in range(1, max):
        print('Invalid Entry')


truck1_route = optimize_route(truck1, [])
truck2_route = optimize_route(truck2, [])
truck3_route = optimize_route(truck3, [])

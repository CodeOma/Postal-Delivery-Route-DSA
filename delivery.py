import datetime
from distance import get_distance
from prepare_data import package_map
from routes import get_package_address
from truck_route_prep import truck1_route, truck2_route, truck3_route

'''
This file is where the delivery takes place. 
The package statuses are updated throughout the delivery process. The time and the miles are tallied throughout the process.
The delivery functions take the optimized routes from truck_route_prep.py
'''

size = package_map.get_size()

#Time complexity O(1)
def string_to_time(string):
    try:
        (h, m, s) = string.split(':')
        return datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    except:
        raise ValueError('Incorrect format')


#Time complexity O(n)
def out_for_delivery_update(truck):
    for i in range(0,len(truck)-1):
        package_map.get(truck[i]).set_delivery_status("Out for Delivery")
        package_map.get(truck[i]).set_time_delivered("Out for Delivery")

#Time complexity O(n)
def check_truck_status(truck):
    for pkg in truck:
        package_map.get(pkg).get_status()

#Time complexity O(n)
def deliver_miles(truck):
    total = get_distance(0,get_package_address(truck[0]))
    for i in range(0,len(truck)-1):
        total += get_distance(get_package_address(truck[i]),get_package_address(truck[i+1]))
    return total

#Time complexity O(n)
def deliver_time(truck,start, end='24:00:00'):
    start_time = string_to_time(start)
    end_time = string_to_time(end)
    
    out_for_delivery_update(truck)
    # total = get_distance(0,get_package_address(truck[0]))
    hours = start_time + datetime.timedelta(hours=get_distance(0,get_package_address(truck[0])) / 18)
    package_map.get(truck[0]).set_time_delivered(hours)
    package_map.get(truck[0]).set_delivery_status("Delivered")
    
    for i in range(0,len(truck)-1):
        miles = get_distance(get_package_address(truck[i]),get_package_address(truck[i+1]))
        if(hours + datetime.timedelta(hours=(miles/18)) <= end_time ):
            miles = get_distance(get_package_address(truck[i]),get_package_address(truck[i+1]))
            hours += datetime.timedelta(hours=(miles/18))
            package_map.get(truck[i+1]).set_time_delivered(hours)
            package_map.get(truck[i+1]).set_delivery_status("Delivered")
        else:
            break
    return hours

# O(1)
def to_hub_miles(truck):
    return get_distance(get_package_address(truck[-1]),0)


# O(1)
def to_hub_time(truck):
    miles = get_distance(get_package_address(truck[-1]),0)
    time = datetime.timedelta(hours=(miles / 18))
    return time



def print_delivered(time='24:00:00'):
    truck1_time = deliver_time(truck1_route, '08:00:00', time)
    truck2_time = deliver_time(truck2_route, '9:05:00', time)
    truck1_to_hub_time = to_hub_time(truck1_route)
    truck3_start_time = truck1_time + truck1_to_hub_time
    truck3_time = deliver_time(truck3_route, str(truck3_start_time), time)
    for pkg in package_map.get_all():
        print(pkg)




def print_delivered_individual(id,time='24:00:00'):
    truck1_time = deliver_time(truck1_route, '08:00:00', time)
    truck2_time = deliver_time(truck2_route, '09:05:00', time)
    truck1_to_hub_time = to_hub_time(truck1_route)
    truck3_start_time = truck1_time + truck1_to_hub_time
    truck3_time = deliver_time(truck3_route, str(truck3_start_time), time)
    pkg = package_map.get(id)
    print(pkg) 


truck1_total_miles = deliver_miles(truck1_route)
truck2_total_miles = deliver_miles(truck2_route)
truck1_time_to_miles = to_hub_miles(truck1_route)
truck3_total_miles = deliver_miles(truck3_route)

truck1_time = deliver_time(truck1_route, '08:00:00')

total_miles = truck2_total_miles + truck2_total_miles + truck2_total_miles + truck1_time_to_miles

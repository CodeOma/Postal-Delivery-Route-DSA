import datetime
from prepare_data import adjacency_matrix


'''
This file is where the total time and total miles per truck. 
'''

#Time complexity O(1)
def get_distance(a, b):
    distance = adjacency_matrix.get(a,b)    
    return float(distance)


#recursive function to get the total miles per truck O(n)
def get_total_route_miles(truck, total=0):
    truck_local = truck
    if(len(truck) == 1):
        return total
    distance = adjacency_matrix.get(truck[0],truck[1])
    truck.pop(0)
    total += distance
    return get_total_route_miles(truck_local, total)



# Calculate total time for a given truck (Time Complexity O(n))
def get_time(distance, truck_list):
    time = distance / 18
    distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
        *divmod(time * 60, 60))
    final_time = distance_in_minutes + ':00'
    truck_list.append(final_time)
    total = datetime.timedelta()
    for i in truck_list:
        (hrs, mins, secs) = i.split(':')
        total += datetime.timedelta(hours=int(hrs),
                                    minutes=int(mins), seconds=int(secs))
    return total




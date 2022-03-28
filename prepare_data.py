import csv
from classes.hash_table import HashTable
from classes.graph import Graph
from classes.package import Package


'''
This file is to prepare the address and distance data structures.
The addresses are stored in a hash table to quickly look up the ID and name using 
the addresses.

A adjacency matrix is created for the distances to allow quick looks up's using the
location IDs.
'''

#Importing CSV files
with open('data/address_data.csv', mode='r', encoding='utf-8-sig') as address_csv:
    address_data = list(csv.reader(address_csv, delimiter=',', skipinitialspace=True))

with open('data/distance_data.csv', mode='r', encoding='utf-8-sig') as distance_csv:
    distance_data = list(csv.reader(distance_csv, delimiter=',', skipinitialspace=True))

with open('./data/package_data.csv') as package_csv:
    package_data = list(csv.reader(package_csv, delimiter=','))
    
#Distances
adjacency_matrix = Graph(27)
#adding an edge for each location in adjacency matrix
#For quick distance look up we can use the location id and get distance
#matrix.get(0,2) = 3.8
#[0.0, 7.2, 3.8,...]
#[7.2, 0.0, 7.1,...]
#[3.8, 7.1, 0.0,...]

# O(N^2)???s
# Adjacency Matrix
def prep_distances(data):
    i = 0
    j = 0
    for row in data: 
        for edges in row:
            if(edges == ''):
                j = 0
                break
            adjacency_matrix.add_edge(i, j, float(edges))
            j += 1
        i += 1
    
prep_distances(distance_data)


#packages
package_map = HashTable(50) #create a instance of hash table to store...
   
#importing the data from csv and creating packages and putting them into hash map O(n^2)
def prep_packages(data):
    for row in data:
        package = Package(row)
        address = package.get_address()
        location_id = None
        for adrs in address_data:
            if(adrs[2]==address):
                location_id = int(adrs[0])
        package.set_address_id(location_id)
        package_map.insert(int(package.id), package)
        


prep_packages(package_data)
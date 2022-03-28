# Graph to create Adjacency Matrix 
class Graph():

    # Initialize the matrix O(n)
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    #print matrix O(n^2)
    def print(self):
        for i in range(0, len(self.adjMatrix)):
            for j in range(0, len(self.adjMatrix[i])):
                print(self.adjMatrix[i][j])

    # Add edges O(1)
    def add_edge(self, v1, v2, e):
        self.adjMatrix[v1][v2] = e
        self.adjMatrix[v2][v1] = e

    #Get edge O(1)
    def get(self, v1, v2):
        return self.adjMatrix[v1][v2]
    

    
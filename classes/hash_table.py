class HashTable:
    #Constructor of HashMap Class (Time Complexity O(n))
    def __init__(self, capacity=10):
        self.map = []
        self.size = 0
        for i in range(capacity):
            self.map.append([])

    # Create hash key Time Complexity O(1)
    def hash(self, key):
        return int(key) % len(self.map)

    # Insert package Time Complexity O(1)
    def insert(self, key, value):
        bucket = self.hash(key)
        entry = [key, value]
        self.map[bucket].append(entry)
        self.size += 1
        return True

    # Update package Time Complexity O(n)
    def update(self, key, value):
        bucket = self.hash(key)
        if self.map[bucket] != None:
            for entry in self.map[bucket]:
                if entry[0] == key:
                    entry[1] = value
                    print(entry[1])
                    return True
        else:
            print('There was no item with key: ' + key)

    # Get a value with key (Time Complexity O(n))
    def get(self, key):
        bucket = self.hash(key)
        if self.map[bucket] != None:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Delete a value (Time Complexity O(n))
    def delete(self, key):
        bucket = self.hash(key)
        if self.map[bucket] == None:
            return False
        for i in range(0, self.size):
            if self.map[bucket][i][0] == key:
                self.map[bucket].pop(i)
                self.size -= 1
                return True
        return False

    # Time Complexity: O(n^2)
    def get_all(self):
        package_list = []
        # Time Complexity: O(n)
        for bucket in self.map:
            # Time Complexity: O(n)
            for item in bucket:
                package_list.append(item[1])
        return package_list

    # Time Complexity: O(1)
    def get_size(self):
        return self.size

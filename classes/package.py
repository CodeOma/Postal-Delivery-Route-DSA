class Package(object):
    # Time Complexity = O(1)
    def __init__(self, package):
        self.id = int(package[0]) 
        self.address_id = '' 
        self.address = package[1] 
        self.city = package[2] 
        self.state = package[3]
        self.zip = package[4] 
        self.truck = 'None'
        self.deadline = package[5] 
        self.weight = package[6] 
        self.note = package[7] 
        self.delivery_start = ''
        self.delivery_status = 'at hub'
        self.time_delivered = 'at hub'
        



    
    # Time Complexity = O(1)
    def get_truck(self):
        return self.truck

    # Time Complexity = O(1)
    def set_truck(self, truck):
        self.truck  = truck

    # Time Complexity = O(1)
    def set_address(self, address):
        self.address  = address

    # Time Complexity = O(1)
    def get_id(self):
        return self.id

    # Time Complexity = O(1)
    def get_address(self):
        return self.address

    # Time Complexity = O(1)
    def get_address_id(self):
        return self.address_id


    # Time Complexity = O(1)
    def set_address_id(self, address_id):
        self.address_id = address_id


    #  Time Complexity = O(1)
    def get_zip(self):
        return self.zip

    # Time Complexity = O(1)
    def set_zip(self, zip):
        self.zip  = zip

    # Time Complexity = O(1)
    def get_status(self):
        return self.status

    # Time Complexity = O(1)
    def set_status(self, status):
        self.delivery_status  = status

    # Time Complexity = O(1)
    def set_time_delivered(self, time):
        self.time_delivered  = time

    # Time Complexity = O(1)
    def get_time_delivered(self):
        return self.time_delivered
    
    # Time Complexity = O(1)
    def get_delivery_status(self):
        return self.delivery_status


    # Time Complexity = O(1)
    def set_delivery_status(self, delivery_status):
        self.delivery_status = delivery_status

    # Time Complexity = O(1)
    def get_note(self):
        return self.note

    # Time Complexity = O(1)
    def get_deadline(self):
        return self.deadline

    # Time Complexity = O(1)
    def __str__(self):
        package_info  = f"ID:{self.id}\tAddress:{self.address}, {self.city}, {self.zip}\tWeight:{self.weight}\tDeadline:{self.deadline} \tStatus:{self.delivery_status}\t\
                           Delivered at:{str(self.time_delivered)}"
        return package_info
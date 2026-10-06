# Stores information about one farmer
class Farmer:
    def __init__(self, name, farmer_id, age, gender, location):
        self.name = name
        self.farmer_id = farmer_id
        self.age = age
        self.gender = gender
        self.location = location

    def display_info(self):
        print("\n*** Farmer Information ***")
        print(f"ID: {self.farmer_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Location: {self.location}")


# Stores and displays a list of farmers
class FarmerManager:
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.farmers = []

    def add_farmer(self, farmer):
        self.farmers.append(farmer)
        print("Farmer added successfully")

    def display_farmers(self):
        print("\n***** All Farmers *****")
        print(f"Farm: {self.farm_name}")

        if len(self.farmers) == 0:
            print("No farmer records found.")
        else:
            for farmer in self.farmers:
                farmer.display_info()


# Create three farmer objects
farmer1 = Farmer("Joseph", 101, 19, "Male", "Leicester Peak")
farmer2 = Farmer("Mary", 102, 25, "Female", "Green Valley")
farmer3 = Farmer("John", 103, 30, "Male", "Sunny Farm")

# Create a manager and add the farmers
farm1 = FarmerManager("Green Valley")
farm1.add_farmer(farmer1)
farm1.add_farmer(farmer2)
farm1.add_farmer(farmer3)

# Display all farmer records
farm1.display_farmers()
class Building:
    def __init__(self,numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
house_1 = Building(5, 'mini_house')
house_2 = Building(5, 'big_house')
print(house_1 == house_2)
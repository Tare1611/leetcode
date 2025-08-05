# Last updated: 8/5/2025, 4:48:42 PM
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigSize = big
        self.medSize = medium
        self.smlSize = small



    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.bigSize -= 1
            return self.bigSize >= 0
        elif carType == 2:
            self.medSize -= 1
            return self.medSize >= 0
        else:
            self.smlSize -= 1
            return self.smlSize >= 0
        
# Approach keep simple variable for the car sizes, as cars come subtract 1 from the size.
# Return the bool checking if value is greater than or equal to 0
# TC - O(1)
# SC - O(1)

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
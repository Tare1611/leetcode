# Last updated: 8/5/2025, 4:42:33 PM
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
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.counter_big = 0
        self.counter_medium = 0
        self.counter_small = 0

    def addCar(self, carType: int) -> bool:
        # if counter is smaller than size, can park
        if carType == 1 and self.counter_big < self.big:
            self.counter_big += 1
            return True
        elif carType == 1 and self.counter_big >= self.big:
            return False
        elif carType == 2 and self.counter_medium < self.medium:
            self.counter_medium += 1
            return True
        elif carType == 2 and self.counter_medium >= self.medium:
            return False
        elif carType == 3 and self.counter_small < self.small:
            self.counter_small += 1
            return True
        elif carType == 3 and self.counter_small >= self.small:
            return False
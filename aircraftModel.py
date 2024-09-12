class Aircraft:

    def __init__(self, type, speed,fuel_capacity):
        self.type = type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

    def get_string(self):
        return f"name: {self.type}, skill level: {self.speed}, fuel capacity: {self.fuel_capacity}."
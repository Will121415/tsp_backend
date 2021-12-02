# Create class to handle "cities"
import numpy as np
class District:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance(self, district):
        x_dis = abs(self.x - district.x)
        y_dis = abs(self.y - district.y)
        distance = np.sqrt((x_dis ** 2) + (y_dis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.name) + ")"
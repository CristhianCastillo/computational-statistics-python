from coordinate import Coordinate

class Drunk:

    def __init__(self, name, coordinate):
        self.name = name
        self.position = coordinate


    def walk(self, x, y):
        self.position = Coordinate(self.position.x + x, self.position.y + y)
        

    def get_distance_reference_position(self, position):
        delta_x = self.position.x - position.x
        delta_y = self.position.y - position.y

        return (delta_x** 2 + delta_y ** 2)**0.5
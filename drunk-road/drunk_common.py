import random
from drunk import Drunk


class DrunkCommon(Drunk):

    def __init__(self, name, coordinate):
        super().__init__(name, coordinate)
        self.possibility_positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


    def get_walk_possibility(self):
        return random.choice(self.possibility_positions)
class City:

    def __init__(self):
        self.drunk_list = {}


    def add_drunk(self, drunk):
        self.drunk_list[drunk.name] = drunk


    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.get_walk_possibility()
        drunk.walk(delta_x, delta_y)
        self.drunk_list[drunk.name] = drunk
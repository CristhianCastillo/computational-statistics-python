class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)


    def distancia(self, coordenada_inicial):
        delta_x = self.x - coordenada_inicial.x
        delta_y = self.y - coordenada_inicial.y

        return (delta_x** 2 + delta_y ** 2)**0.5
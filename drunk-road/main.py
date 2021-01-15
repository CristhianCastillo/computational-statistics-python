from city import City
from drunk_common import DrunkCommon
from coordinate import Coordinate
from bokeh.plotting import figure, show

def grafhic(x, y):
    graf = figure(title='Camino aleatorio', x_axis_label ='pasos_x', y_axis_label='pasos_y')
    graf.line(x, y, legend='Distancia Recorrida')

    show(graf)


def simulate_walk(city, drunk, steps):
    road_x = []
    road_y = []
    road_x.append(drunk.position.x)
    road_y.append(drunk.position.y)
    for _ in range(steps):
        city.move_drunk(drunk)
        road_x.append(drunk.position.x)
        road_y.append(drunk.position.y)
    
    return road_x, road_y


if __name__ == "__main__":
    step_list = [10, 100, 1000, 10000]
    attempts = 100

    drunk_man = DrunkCommon('Cristhian', Coordinate(0, 0))

    city = City()
    city.add_drunk(drunk_man)
    road_x, road_y = simulate_walk(city, drunk_man, 10000)
    grafhic(road_x, road_y)
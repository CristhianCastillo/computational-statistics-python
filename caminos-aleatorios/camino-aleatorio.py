from borracho import BorrachoComun
from campo import Campo
from coordenada import Coordenada
from bokeh.plotting import figure, show


def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label ='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend='Distancia Media')

    show(grafica)

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho(name='Cristhian')
    origen = Coordenada(0, 0)
    distancias = []

    for _ in range(numero_intentos):
        campo = Campo()
        campo.add_borracho(borracho, origen)
        simular_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simular_caminata, 1))

    return distancias


def main(distancias_caminata, numero_intentos, tipo_borracho):
    distancias_media_caminata = []

    for pasos in distancias_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancias_media_caminata.append(distancia_media)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Maxima = {distancia_maxima}')
        print(f'Minima = {distancia_minima}')

    graficar(distancias_caminata, distancias_media_caminata)

if __name__ == "__main__":
    distancias_caminata = [10, 100, 1000, 10000]
    numero_intentos = 100
    main(distancias_caminata, numero_intentos, BorrachoComun)


    
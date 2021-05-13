from Vehiculos import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, patente, color, velocidad_maxima, plegable, estilo):
        super().__init__(marca, modelo, patente, color, velocidad_maxima)
        self.plegable = plegable
        self.estilo = estilo

    def encender(self):
        print('Comenzando a pedalear')

    def apagar(self):
            print('Dejando de pedalear')

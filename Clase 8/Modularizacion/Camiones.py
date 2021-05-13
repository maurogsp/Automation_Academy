from Vehiculos import Vehiculo

class Camion(Vehiculo):
        def __init__(self, marca, modelo, patente, color, velocidad_maxima, puertas, carga):
            Vehiculo.__init__(self, marca, modelo, patente, color, velocidad_maxima)
            self.puertas = puertas
            self.carga = carga
            self.CargaActual = 0

        def cargar(self,tn):
            self.CargaActual = self.CargaActual + tn

        def descargar(self,tn):
            self.CargaActual = self.CargaActual - tn

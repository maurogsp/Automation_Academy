#Ejemplo Herencia

class Vehiculos:
    def __init__(self, marca, modelo, patente, color, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False

    def acelerar(self,velocidad):
        if self.encendido:
            if self.velocidad_actual + velocidad < self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_actual + velocidad
            else:
                self.velocidad_actual = self.velocidad_maxima
        else:
            print('No puede acelerar, el auto está apagado')


    def acelerar_2(self,velocidad):
        if self.encendido:
            try:
                velocidad_final = self.velocidad_actual + velocidad
                if velocidad_final < self.velocidad_maxima:
                    self.velocidad_actual = velocidad_final
                else:
                    self.velocidad_actual = self.velocidad_maxima
            except TypeError:
                print('No puedo acelerar eso')
            except ValueError:
                print('El parámetro pasado no es un integer')
            except:
                print('Excepcion atrapada')
            finally:
                print('Se intento acelarar con: '+str(velocidad))
        else:
            print('No puede acelerar, el auto está apagado')

    def frenar(self, velocidad):
        if self.encendido:
            try:
                velocidad_final = self.velocidad_actual - velocidad
                if velocidad_final > 0:
                    self.velocidad_actual = velocidad_final
                else:
                    self.velocidad_actual = 0
            except TypeError:
                print('No puedo frenar eso')
            except ValueError:
                print('El parámetro pasado no es un integer')
            except:
                print('Excepcion atrapada')
            finally:
                print('Se intento frenar con: '+str(velocidad))
        else:
            print('No puede frenar, el vehiculo está apagado')

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print('El vehiculo se encendio')
        else:
            print('El vehiculo ya está encendido')

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print('El vehiculo se apagó')
        else:
            print ('El vehiculo ya está apagado')

    def mostrar_informacion(self):
        print ('Este vehiculo es un '+self.marca+' '+self.modelo+' y esta andando a '+str(self.velocidad_actual))


class Automovil(Vehiculos):
    def __init__(self, marca, modelo, patente, color, velocidad_maxima, puertas):
        Vehiculos.__init__(self, marca, modelo, patente, color, velocidad_maxima)
        self.puertas = puertas

class Camion(Vehiculos):
        def __init__(self, marca, modelo, patente, color, velocidad_maxima, puertas, carga):
            Vehiculos.__init__(self, marca, modelo, patente, color, velocidad_maxima)
            self.puertas = puertas
            self.carga = carga
            self.CargaActual = 0

        def cargar(self,tn):
            self.CargaActual = self.CargaActual + tn

        def descargar(self,tn):
            self.CargaActual = self.CargaActual - tn

class Bicicleta(Vehiculos):
    def __init__(self, marca, modelo, patente, color, velocidad_maxima, plegable, estilo):
        super().__init__(marca, modelo, patente, color, velocidad_maxima)
        self.plegable = plegable
        self.estilo = estilo

    def encender(self):
        print('Comenzando a pedalear')

    def apagar(self):
            print('Dejando de pedalear')

auto = Automovil('ford','fiesta','aaa111','naranja',160,4)
print(auto.marca)
print(auto.puertas)
auto.encender()
auto.apagar()

camion = Camion('mercedes','truck','aaa111','negro',100,2,1500)
print(camion.marca)
print(camion.puertas)
print(camion.carga)

bici = Bicicleta('Aurora','Monataña','bbb222','azul',45, True, 'Paseo')
bici.encender()
bici.apagar()

class Autos:
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
            print('No puede frenar, el auto está apagado')

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print('El auto se encendio')
        else:
            print('El auto ya está encendido')

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print('El auto se apagó')
        else:
            print ('El auto ya está apagado')

    def mostrar_informacion(self):
        print ('Este auto es un '+self.marca+' '+self.modelo+' y esta andando a '+str(self.velocidad_actual))

mi_auto = Autos('Ford','Fiesta', 'egr 456', 'dorado', 180)

print(mi_auto.marca)

mi_auto.mostrar_informacion()

mi_auto.encender()

mi_auto.acelerar(50)

mi_auto.mostrar_informacion()

mi_auto.acelerar_2(70)

mi_auto.mostrar_informacion()

mi_auto.acelerar_2('papa')

mi_auto.frenar(20)

mi_auto.frenar('choclo')

mi_auto.apagar()

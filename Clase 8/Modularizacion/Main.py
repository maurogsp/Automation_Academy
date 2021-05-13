from Automoviles import Automovil
from Camiones import Camion
from Bicicletas import Bicicleta

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

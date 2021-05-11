#Ejemplo herencia multiple

class Humano:
    def __init__(self,nombre,apellido,documento):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento

class Maquina:
    def __init__(self,modelo,serie,so):
        self.modelo = modelo
        self.serie = serie
        self.so = so

class Androide(Humano,Maquina):
    def __init__(self,nombre,apellido,documento,modelo,serie,so,conversion):
        Humano.__init__(self,nombre,apellido,documento)
        Maquina.__init__(self,modelo,serie,so)
        self.conversion = conversion

androide = Androide('Jorge','Perez','123456789','T1000','2244BB','Linux',2019)
print(androide.documento)
print(androide.serie)
print(androide.conversion)

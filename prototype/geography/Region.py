class Region():
    def __init__(self, nombre):
        self.nombre = nombre
        self.provincias = []

    def añadir_provincia(self, provincia):
        self.provincias.append(provincia)

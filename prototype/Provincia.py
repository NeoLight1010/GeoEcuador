from console import console
import json
import os

class Region():
    def __init__(self, nombre):
        self.nombre = nombre
        self.provincias = []

    def añadir_provincia(self, provincia):
        self.provincias.append(provincia)


class Provincia():
    def __init__(self, nombre, region, descripcion, ciudades, capital, puntos_interes=[], bandera="", paisaje=""):
        self.nombre = nombre
        self.region = region
        self.descripcion = descripcion
        self.ciudades = ciudades
        self.capital = capital
        self.puntos_interes = puntos_interes
        self.bandera = bandera
        self.paisaje = paisaje

    def mostrar_informacion(self):
        console.clear()

        console.print(f'''
[bold red]{self.nombre}[/]\n
[green]Región:[/] {self.region.nombre}\n
[green]Capital:[/] {self.capital}\n
[green]Descripción:[/]\n\n{self.descripcion}\n 
[green]Puntos de interés:[/]\n\n[white]{", ".join(self.puntos_interes)}
        ''')


def leer_descripcion(path):
    dirname = os.path.dirname(__file__)

    descripcion = ""
    with open(os.path.join(dirname, "data/provincias", path), 'r', encoding='utf-8') as file:
        descripcion = file.read()

    return descripcion



def cargar_provincias():
    dirname = os.path.dirname(__file__)

    sierra = Region("Sierra")
    costa = Region("Costa")
    amazonia = Region("Amazonía")
    insular = Region("Galápagos")

    json_provincias = None

    with open(os.path.join(dirname, "data/provincias/provincias.json"), "r", encoding="utf-8") as json_file:
        json_provincias = json.load(json_file)

    provincias = {}
    
    for provincia in json_provincias.keys():
        nombre = provincia
        region = json_provincias[nombre]["Región"]
        descripcion = leer_descripcion(json_provincias[nombre]["Descripción"])
        ciudades = json_provincias[nombre]["Ciudades"]        
        capital = json_provincias[nombre]["Capital"]
        puntos_interes = json_provincias[nombre]["Puntos de Interés"]

        if (region == "Sierra"):
            region = sierra
        elif region == "Costa":
            region = costa
        elif region == "Amazonía":
            region = amazonia
        elif region == "Insular":
            region = insular
        else:
            region = None
        

        nueva_provincia = Provincia(nombre, region, descripcion, ciudades, capital, puntos_interes)
        provincias[nombre] = nueva_provincia

    return provincias
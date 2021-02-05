import os
import json
from geography.Provincia import Provincia
from geography.Region import Region
from utils.provincia import leer_descripcion


def cargar_provincias():
    dirname = os.path.dirname(os.path.abspath("requirements.txt"))

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
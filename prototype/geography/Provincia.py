from utils.console import console


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

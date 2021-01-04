#TODO: Create class to reuse menus.

import Provincia
from console import console
from minijuego import iniciar_minijuego


def mostrar_menu_principal(provincias):
    # Título
    console.print("[bold redred]GeoEcuador", justify="center")

    # Lista de opciones
    opciones = {
        "Información": menu_informacion,
        "Minijuego": iniciar_minijuego
    }

    for i, opcion in enumerate(opciones.keys()):
        console.print(f"[green]{i+1}.[/] {opcion}")

    # Input
    try:
        eleccion = int(console.input(": "))
        eleccion = eleccion -1
        eleccion = list(opciones.keys())[eleccion]
        if eleccion == "Información":
            opciones[eleccion](provincias)
        else:
            opciones[eleccion]()
        
    except:
        console.print("Error. Intente de nuevo.")


def menu_informacion(provincias):
    nombres_provincias = list(provincias.keys())

    console.print("[bold red]Ingresar el número de la provincia: \n")

    for i, nombre in enumerate(nombres_provincias):
        console.print(f"[green]{i+1}.[/] {nombre}")

    print()
    eleccion = 0

    while True:
        try: 
            eleccion = int(input(": ")) - 1

            if not (eleccion >= 0 and eleccion <= len(nombres_provincias)):
                raise("Elección fuera de límites.")

            provincia = nombres_provincias[eleccion]
            provincia = provincias[provincia]

            provincia.mostrar_informacion()
            break
        except:
            console.print("Número inválido, intente de nuevo.")


if __name__ == "__main__":
    console.clear()
    provincias = Provincia.cargar_provincias()
    
    mostrar_menu_principal(provincias)
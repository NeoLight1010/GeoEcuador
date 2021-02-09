# TODO: Guardar puntaje
# TODO: Evitar preguntas repetidas.
# TODO: Importar y utilizar rich para mejorar la presentación.

# Minijuego de la aplicación GeoEcuador: comprueba tu conocimiento.
from utils.console import console
from trivia.SetPreguntas import SetPreguntas
import random


def iniciar_minijuego():
    console.clear()

    nucleos_capitales = {
        "Azuay": "Cuenca",
        "Bolívar": "Guaranda",
        "Cañar": "Azogues",
        "Carchi": "Tulcán",
        "Chimborazo": "Riobamba",
        "Cotopaxi": "Latacunga",
        "El Oro": "Machala",
        "Esmeraldas": "Esmeraldas",
        "Galápagos": "Puerto Baquerizo Moreno",
        "Guayas": "Guayaquil",
        "Imbabura": "Ibarra",
        "Loja": "Loja",
        "Los Ríos": "Babahoyo",
        "Manabí": "Portoviejo",
        "Morona Santiago": "Macas",
        "Napo": "Tena",
        "Orellana": "Coca",
        "Pastaza": "Puyo",
        "Pichincha": "Quito",
        "Santa Elena": "Santa Elena",
        "Santo Domingo de los Tsáchilas": "Santo Domingo",
        "Sucumbíos": "Nueva Loja",
        "Tungurahua": "Ambato",
        "Zamora Chinchipe": "Zamora"
    }
    nucleos_regiones = {
        "Azuay": "Sierra",
        "Bolívar": "Sierra",
        "Cañar": "Sierra",
        "Carchi": "Sierra",
        "Chimborazo": "Sierra",
        "Cotopaxi": "Sierra",
        "El Oro": "Costa",
        "Esmeraldas": "Costa",
        "Galápagos": "Insular",
        "Guayas": "Costa",
        "Imbabura": "Sierra",
        "Loja": "Sierra",
        "Los Ríos": "Costa",
        "Manabí": "Costa",
        "Morona Santiago": "Amazonía",
        "Napo": "Amazonía",
        "Orellana": "Amazonía",
        "Pastaza": "Amazonía",
        "Pichincha": "Sierra",
        "Santa Elena": "Costa",
        "Santo Domingo de los Tsáchilas": "Sierra",
        "Sucumbíos": "Amazonía",
        "Tungurahua": "Sierra",
        "Zamora Chinchipe": "Amazonía"
    }
    nucleos_puntos_interes = {
        "Azuay": "Parque Nacional Cajas",
        "Bolívar": "Carnaval de Guaranda",
        "Cañar": "Ruinas de Ingapirca",
        "Carchi": "Cementerio Municipal de Tulcán",
        "Chimborazo": "Volcán Chimborazo",
        "Cotopaxi": "Volcán Cotopaxi",
        "El Oro": "Archipiélago de Jambelí",
        "Esmeraldas": "Playa de Tonsupa",
        "Galápagos": "Bahía Tortuga",
        "Guayas": "Las Peñas",
        "Imbabura": "Laguna de Cuicocha",
        "Loja": "Parque Nacional Podocarpus",
        "Los Ríos": "La Casa de Olmedo",
        "Manabí": "Playa de los Frailes",
        "Morona Santiago": "Laguna Negra",
        "Napo": "Río Misahuallí",
        "Orellana": "Parque Nacional Yasuní",
        "Pastaza": "Ruta de los Shamanes",
        "Pichincha": "Centro histórico de Quito",
        "Santa Elena": "Punto rocoso de La Chocolatera",
        "Santo Domingo de los Tsáchilas": "Parque Zaracay",
        "Sucumbíos": "Reserva de Producción Faunística Cuyabeno",
        "Tungurahua": "Baños de Agua Santa",
        "Zamora Chinchipe": "Centinela del Cóndor"
    }

    # Inicializar sets de preguntas.
    set_capitales = SetPreguntas("Capitales", nucleos_capitales,
                                 lambda provincia:
                                 f"¿Cuál es la capital de {provincia}?",
                                 lambda provincia, capital:
                                 f"La capital de {provincia} es {capital}.")
    set_regiones = SetPreguntas("Regiones", nucleos_regiones,
                                lambda provincia:
                                f"¿En qué región se encuentra la provincia de {provincia}?",
                                lambda provincia, region:
                                f"{provincia} se encuentra en la región {region}.")
    set_puntos_interes = SetPreguntas("Puntos de Interés", nucleos_puntos_interes,
        lambda provincia:
        f"¿Cuál de los siguientes es un punto de interés o un evento representativo de la provincia de {provincia}?",
        lambda provincia, punto:
        f"{punto} es un punto de interés o evento representativo de {provincia}")

    lista_sets = [set_capitales, set_regiones, set_puntos_interes]
    n_preguntas = 3

    for n in range(n_preguntas):
        tipo = SetPreguntas.tipo.VF
        # Elegir un set aleatorio
        random_set = random.choice(lista_sets)
        random_nucleo = random_set.obtener_nucleo_aleatorio()
        random_pregunta_nucleo_sec = random_set.obtener_pregunta(random_nucleo,
                                                                 tipo=tipo)
        random_question = random_pregunta_nucleo_sec[0]
        random_nucleo_2 = random_pregunta_nucleo_sec[1]
        respuesta_correcta = random_set.obtener_respuesta(random_nucleo,
                                                          random_nucleo_2,
                                                          tipo=tipo)
        opciones = random_set.obtener_opciones(respuesta_correcta,
                                               tipo=tipo)

        console.print(f"[bold red]{random_question}\n", justify="center")

        # Imprimir opciones
        for i, opcion in enumerate(opciones):
            console.print(f"[bold green]{i+1}.[/] {opcion}")

        # Pedir input
        while True:
            try:
                eleccion = int(input("(1/2): "))
                eleccion = eleccion - 1
                respuesta_elegida = opciones[eleccion]
                break
            except Exception:
                print("Input inválido.")
                continue

        # Revisar respuesta elegida
        if respuesta_elegida == respuesta_correcta:
            print("\n¡Muy bien! ¡Respuesta correcta!")
        else:
            print(
                f"Lo siento, es incorrecto. :( La respuesta correcta es {respuesta_correcta}"
            )

    print("\nFin del juego. Gracias por jugar c:")


# For testing
if __name__ == "__main__":
    iniciar_minijuego()

import random


class SetPreguntas:
    """Clase que representa un conjunto de preguntas que
    son consideradas del mismo tipo/categoría."""

    def __init__(self, nombre, nucleos, formato):
        """
        Construir un SetPreguntas.

        Parámetros
        ----------
            nombre {str} -- nombre del set.
            nucleos {dict} -- pares key-value de "núcleos" de pregunta con su respuesta.
                Ej. {"Azuay": "Cuenca", "Pichincha", "Quito"}
            formato {func} -- determina el formato al imprimir la pregunta."
                Ej. lambda nucleo: f"¿Cuál es la capital de {nucleo}?"
        """
        self.nombre = nombre
        self.nucleos = nucleos
        self.formato = formato

    def obtener_pregunta(self, nucleo):
        return self.formato(nucleo)

    def obtener_respuesta(self, nucleo):
        return self.nucleos[nucleo]

    def obtener_nucleo_aleatorio(self):
        nucleos_pregunta = list(self.nucleos.keys())
        nucleo_aleatorio = random.choice(nucleos_pregunta)
        return nucleo_aleatorio

    def obtener_respuestas_aleatorias(self, respuesta_correcta="", n=4):
        """Devuelve una lista de respuestas aleatorias.
        respuesta_correcta será siempre añadida si es provista."""
        nucleos_pregunta = list(self.nucleos.keys())

        options = []

        if respuesta_correcta:
            options.append(respuesta_correcta)

        for i in range(n):
            if nucleos_pregunta:
                rand_pregunta = random.choice(nucleos_pregunta)
                rand_respuesta = self.obtener_respuesta(rand_pregunta)

                if (rand_respuesta not in options
                        and rand_pregunta in nucleos_pregunta):
                    options.append(rand_respuesta)
                    del nucleos_pregunta[nucleos_pregunta.index(rand_pregunta)]
            else:
                nucleos_pregunta = list(self.nucleos.keys())

        random.shuffle(options)
        return options

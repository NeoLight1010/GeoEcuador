import random


class SetPreguntas:
    """Clase que representa un conjunto de preguntas que
    son consideradas del mismo tipo/categoría."""

    NORMAL = "NORMAL"
    VF = "V/F"

    def __init__(self, nombre, nucleos,
                 formato_normal=lambda: "", formato_vf=lambda: ""):
        """
        Construir un SetPreguntas.

        Parámetros
        ----------
            nombre {str} -- nombre del set.
            nucleos {dict} -- pares key-value de "núcleos" de
                              pregunta con su respuesta.
                Ej. {"Azuay": "Cuenca", "Pichincha", "Quito"}
            formato_normal {func} -- determina el formato al
                                     imprimir la pregunta."
                Ej. lambda nucleo: f"¿Cuál es la capital de {nucleo}?"
            formato_vf {func} -- determina el formato al imprimir la pregunta."
                lambda nucleo, respuesta:
                    f"La capital de {nucleo} es {respuesta}"
        """
        self.nombre = nombre
        self.nucleos = nucleos
        self.formato_normal = formato_normal
        self.formato_vf = formato_vf

    def obtener_pregunta(self, nucleo, tipo=NORMAL):
        if tipo == self.NORMAL:
            return self.formato_normal(nucleo)
        elif tipo == self.VF:
            respuesta_correcta = self.obtener_respuesta(nucleo)

            rand_opciones = self.obtener_opciones(
                respuesta_correcta=respuesta_correcta)

            rand_respuesta = random.choice(rand_opciones)

            return (self.formato_vf(nucleo, rand_respuesta),
                    rand_respuesta)

    def obtener_respuesta(self, nucleo, nucleo_2="", tipo=NORMAL):
        if tipo == self.NORMAL:
            return self.nucleos[nucleo]
        elif tipo == self.VF:
            if self.nucleos[nucleo] == nucleo_2:
                return "V"
            else:
                return "F"

    def obtener_nucleo_aleatorio(self):
        nucleos_pregunta = list(self.nucleos.keys())
        nucleo_aleatorio = random.choice(nucleos_pregunta)
        return nucleo_aleatorio

    def obtener_opciones(self, respuesta_correcta="", tipo=NORMAL, n=4):
        """Devuelve una lista de opciones aleatorias.
        respuesta_correcta será siempre añadida si es provista."""
        if tipo == self.NORMAL:
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
        elif tipo == self.VF:
            return ['V', 'F']

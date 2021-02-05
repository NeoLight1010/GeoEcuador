import os


def leer_descripcion(path):
    dirname = os.path.dirname(os.path.abspath("requirements.txt"))

    descripcion = ""
    with open(os.path.join(dirname, "data/provincias", path), 'r', encoding='utf-8') as file:
        descripcion = file.read()

    return descripcion
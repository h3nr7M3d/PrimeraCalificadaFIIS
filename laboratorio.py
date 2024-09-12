import csv


class Polinomio:

    def __init__(self, variable, polinomio):
        """Constructor de Polinomio"""
        # [INICIO]: Implemente el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def representar(self):
        """Genera una representación del polinomio, como una
        cadena de caracteres"""
        # [INICIO]: Implemente representar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def comparar(self, otro_polinomio):
        """Compara dos instancias de polinomio. Devuelve True si son
        equivalentes, False caso contrario."""
        # [INICIO]: Implemente comparar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def derivar(self):
        """Retorna una instance de Polinomio, que representa la primera
        derivada de este objeto."""
        # [INICIO]: Implemente derivar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]


class LectorKindel:

    def __init__(self):
        self.catalogo = []
        with open("libros.csv", "r") as archivo:
            self.catalogo = list(csv.DictReader(archivo))

        # [INICIO]: Complete el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def registrar_usuario(self, nombre_de_usuario):
        # [INICIO]: Implemente registrar_usuario() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def ver_detalle(self, nombre_de_usuario, codigo_libro):
        # [INICIO]: Implemente ver_detalle() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def comprar_libro(self, nombre_de_usuario, codigo_libro):
        # [INICIO]: Implemente comprar_libro() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def ver_compras(self, nombre_de_usuario):
        # [INICIO]: Implemente ver_compras() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]

    def buscar(self, titulo=None, autor=None):
        # [INICIO]: Implemente derivar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        pass
        # [FIN]


if __name__ == "__main__":
    # [INICIO]: Pruebe sus soluciones entre [INICIO] y [FIN].
    # No edite antes de esta línea.
    pass
    # [FIN]

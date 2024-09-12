import csv


class Polinomio:

    def __init__(self, variable, polinomio):
        """Constructor de Polinomio"""
        # [INICIO]: Implemente el constructor entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        self.variable = variable
        self.expresion = polinomio.split('=')[1].strip()
        # [FIN]

    def representar(self):
        """Genera una representación del polinomio, como una
        cadena de caracteres"""
        # [INICIO]: Implemente representar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        terminos = self.expresion.split('+')
        terminos_python = []

        for termino in terminos:
            termino = termino.strip()
            if '^' in termino:
                base, exponente = termino.split('^')
                termino_python = f'{base}**{exponente}'
            else:
                termino_python = termino
            terminos_python.append(termino_python.replace(self.variable,f'*{self.variable}'))
        # [FIN]

    def comparar(self, otro_polinomio):
        """Compara dos instancias de polinomio. Devuelve True si son
        equivalentes, False caso contrario."""
        # [INICIO]: Implemente comparar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        return sorted(self.representar().split('+')) == sorted(otro_polinomio.representar().split('+'))
        # [FIN]

    def derivar(self):
        """Retorna una instance de Polinomio, que representa la primera
        derivada de este objeto."""
        # [INICIO]: Implemente derivar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        terminos = self.expresion.split('+')
        derivada_terminos = []
        for termino in terminos:
            termino = termino.strip()
            if '^' in termino:
                coef,pot = termino.split(self.variable + '^')
                coef = int(coef)
                pot= int(pot)
                if pot ==1:
                    derivada_terminos.append(f'{coef * pot}{self.variable}^{pot-1}')
                elif pot > 1:
                    derivada_terminos.append(f'{coef * pot}{self.variable}^{pot-1}')
            elif self.variable in termino:
                coef = int(termino.replace(self.variable,''))
                derivada_terminos.append(str(coef))
        derivada = ' + '.join(derivada_terminos)
        return Polinomio(self.variable,f'f({self.variable}) = ' + derivada)
        # [FIN]
if __name__== "__main__":
    p1 = Polinomio("x", "f(x) = 2x^3 + 3x")
    p2 = Polinomio("x", "f(x) = 3x + 2x^3")
    print(p1.representar())  # Debería devolver "2*x**3 + 3*x"
    print(p1.comparar(p2))  # Debería devolver True
    print(p1.derivar().representar())  # Debería devolver "6*x**2 + 3"

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

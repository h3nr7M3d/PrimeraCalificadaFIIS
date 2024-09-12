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
                coef, var = base.split(self.variable)
                termino_python = f'{coef.strip()}*{self.variable}**{exponente}'
            elif self.variable in termino:
                coef = termino.replace(self.variable, '').strip()
                termino_python = f'{coef}*{self.variable}'
            else:
                termino_python = termino
            terminos_python.append(termino_python)
        return ' + '.join(terminos_python)
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
                coef, pot = termino.split(self.variable + '^')
                coef = int(coef) if coef.strip() != '' else 1
                pot = int(pot)
                if pot == 1:
                    derivada_terminos.append(f'{coef * pot}')
                elif pot > 1:
                    derivada_terminos.append(f'{coef * pot}{self.variable}^{pot-1}')
            elif self.variable in termino:
                coef = int(termino.replace(self.variable, '').strip() or '1')
                derivada_terminos.append(str(coef))
        derivada = ' + '.join(derivada_terminos)
        return Polinomio(self.variable, f'f({self.variable}) = ' + derivada)
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
        self.usuario = set()
        self.compras = {}
        # [FIN]

    def registrar_usuario(self, nombre_de_usuario):
        # [INICIO]: Implemente registrar_usuario() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        usuario_normalizado = nombre_de_usuario.lower()
        if usuario_normalizado in self.usuario:
            raise ValueError("El usuario ya está registrado.")
        self.usuario.add(usuario_normalizado)
        # [FIN]

    def comprar_libro(self, nombre_de_usuario, codigo_libro):
        # [INICIO]: Implemente comprar_libro() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if nombre_de_usuario.lower() not in self.usuarios:
            raise ValueError("El usuario no existe.")
        if any(libro['Text#'] == str(codigo_libro) for libro in self.catalogo):
            if codigo_libro in self.compras.values():
                raise ValueError("El libro ya ha sido comprado por otro usuario.")
            self.compras[nombre_de_usuario.lower()] = codigo_libro
        else:
            raise ValueError("No existe un libro con el código proporcionado.")
        # [FIN]

    def ver_detalle(self, nombre_de_usuario, codigo_libro):
        # [INICIO]: Implemente ver_detalle() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if nombre_de_usuario.lower() not in self.usuarios:
             raise ValueError("El usuario no existe.")
        if self.compras.get(nombre_de_usuario.lower()) != codigo_libro:
            raise ValueError("El libro no ha sido comprado por el usuario.")
         
        libro = next((libro for libro in self.catalogo if libro['Text#'] == str(codigo_libro)), None)
        if libro is None:
            raise ValueError("No existe el libro.")
        
        return {
            "titulo": libro['Title'],
            "autores": libro['Authors'],
            "fecha": libro['Issued'],
            "temas": libro['Subjects']
        }
        # [FIN]

    def ver_compras(self, nombre_de_usuario):
        # [INICIO]: Implemente ver_compras() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        if nombre_de_usuario.lower() not in self.usuarios:
            raise ValueError("El usuario no existe.")
        return [self.compras[nombre_de_usuario.lower()]]
        # [FIN]

    def buscar(self, titulo=None, autor=None):
        # [INICIO]: Implemente derivar() entre [INICIO] y [FIN].
        # No edite antes de esta línea.
        resultados = []
        for libro in self.catalogo:
            if libro['Text#'] in self.compras.values():
                continue
            titulo_cond = titulo.lower() in libro['Title'].lower() if titulo else True
            autor_cond = autor.lower() in libro['Authors'].lower() if autor else True
            if titulo_cond and autor_cond:
                resultados.append(int(libro['Text#']))
        return resultados
        # [FIN]


if __name__ == "__main__":
    # [INICIO]: Pruebe sus soluciones entre [INICIO] y [FIN].
    # No edite antes de esta línea.
    lector = LectorKindel()
    lector.registrar_usuario("Carlos")
    try:
        lector.comprar_libro("Carlos", 320)
        detalle_libro = lector.ver_detalle("Carlos", 320)
        print(detalle_libro)
        compras = lector.ver_compras("Carlos")
        print(compras)
        libros = lector.buscar(titulo="vida", autor="anonymous")
        print(libros)
    except ValueError as e:
        print(e)
    # [FIN]

import laboratorio
import pytest


def test_p1_representar():
    polinomio: str = "f(x) = 2x^3 + 3x"
    variable: str = "x"
    mi_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    assert mi_polinomio.representar() == "2*x**3 + 3*x"


def test_p1_representar_otra_variable():
    polinomio: str = "f(a) = 2a^3 + 3a"
    variable: str = "a"
    mi_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    assert mi_polinomio.representar() == "2*a**3 + 3*a"


def test_p1_comparar_equivalentes():
    polinomio: str = "f(x) = 2x^3 + 3x"
    variable: str = "x"
    mi_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    polinomio = "f(x) = 3x + 2x^3"
    variable: str = "x"
    otro_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    assert mi_polinomio.comparar(otro_polinomio)


def test_p1_comparar_diferentes():
    polinomio: str = "f(x) = 2x^3 + 3x"
    variable: str = "x"
    mi_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    polinomio = "f(x) = 2x^4 + 3x"
    variable: str = "x"
    otro_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    assert not mi_polinomio.comparar(otro_polinomio)


def test_p1_derivar_grado_3():
    polinomio: str = "f(x) = 2x^3 + 3x"
    variable: str = "x"
    mi_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    primera_derivada: laboratorio.Polinomio = mi_polinomio.derivar()
    elementos_derivada: str = primera_derivada.representar().split(" + ")
    assert len(elementos_derivada) == 2
    assert "6*x**2" in elementos_derivada
    assert "3" in elementos_derivada

    derivada_esperada = laboratorio.Polinomio(variable, "f(x) = 6x^2 + 3")
    assert derivada_esperada.comparar(primera_derivada)


def test_p1_derivar_grado_2():
    polinomio: str = "f(x) = 6x^2 + 3"
    variable: str = "x"
    mi_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    primera_derivada: laboratorio.Polinomio = mi_polinomio.derivar()
    elementos_derivada: str = primera_derivada.representar().split(" + ")
    assert len(elementos_derivada) == 1
    assert "12*x" in elementos_derivada

    derivada_esperada = laboratorio.Polinomio(variable, "f(x) = 12x")
    assert derivada_esperada.comparar(primera_derivada)


def test_p1_derivar_grado_1():
    polinomio: str = "f(x) = 12x"
    variable: str = "x"
    mi_polinomio: laboratorio.Polinomio = laboratorio.Polinomio(variable, polinomio)

    primera_derivada: laboratorio.Polinomio = mi_polinomio.derivar()
    elementos_derivada: str = primera_derivada.representar().split(" + ")
    assert len(elementos_derivada) == 1
    assert "12" in elementos_derivada

    derivada_esperada = laboratorio.Polinomio(variable, "f(x) = 12")
    assert derivada_esperada.comparar(primera_derivada)


def test_p2_buscar_titulo():
    lector = laboratorio.LectorKindel()

    codigo_libros = lector.buscar(titulo="novelas y")
    assert len(codigo_libros) == 2
    assert 15115 in codigo_libros
    assert 25074 in codigo_libros


def test_p2_buscar_autor():
    lector = laboratorio.LectorKindel()

    codigo_libros = lector.buscar(autor="cervantes saavedra")
    assert len(codigo_libros) == 5
    assert 2000 in codigo_libros
    assert 57955 in codigo_libros
    assert 61202 in codigo_libros
    assert 15115 in codigo_libros
    assert 16110 in codigo_libros


def test_p2_busqueda_vacia():
    lector = laboratorio.LectorKindel()

    codigo_libros = lector.buscar(autor="cervantes saavedra", titulo="viaje")
    assert len(codigo_libros) == 0


def test_p2_buscar_autor_titulo():
    lector = laboratorio.LectorKindel()

    codigo_libros = lector.buscar(autor="cervantes saavedra", titulo="novelas")
    assert len(codigo_libros) == 2
    assert 61202 in codigo_libros
    assert 15115 in codigo_libros


def test_p2_registrar_usuario():
    lector = laboratorio.LectorKindel()

    lector.registrar_usuario("carlos")

    with pytest.raises(ValueError):
        lector.registrar_usuario("CARLOS")


def test_p2_comprar_libro_sin_usuario():
    lector = laboratorio.LectorKindel()

    with pytest.raises(ValueError):
        lector.comprar_libro("carlos", 2000)


def test_p2_comprar_libro_mal_codigo():
    lector = laboratorio.LectorKindel()
    lector.registrar_usuario("carlos")

    with pytest.raises(ValueError):
        lector.comprar_libro("carlos", -1)


def test_p2_comprar_libro_no_disponible():
    lector = laboratorio.LectorKindel()
    lector.registrar_usuario("carlos")

    lector.comprar_libro("carlos", 2000)
    with pytest.raises(ValueError):
        lector.comprar_libro("carlos", 2000)


def test_p2_buscar_libro_comprado():
    lector = laboratorio.LectorKindel()
    libros = lector.buscar(titulo="don quijote", autor="cervantes")
    assert len(libros) == 1

    lector.registrar_usuario("carlos")
    lector.comprar_libro("carlos", 2000)

    libros = lector.buscar(titulo="don quijote", autor="cervantes")
    assert len(libros) == 0


def test_p2_ver_compras_usuario_incorrecto():
    lector = laboratorio.LectorKindel()

    with pytest.raises(ValueError):
        lector.ver_compras("carlos")


def test_p2_ver_compras_nuevo_usuario():
    lector = laboratorio.LectorKindel()
    lector.registrar_usuario("carlos")

    compras = lector.ver_compras("carlos")
    assert len(compras) == 0


def test_p2_ver_compras():
    lector = laboratorio.LectorKindel()
    lector.registrar_usuario("carlos")
    lector.registrar_usuario("jose")

    lector.comprar_libro("carlos", 2000)
    compras = lector.ver_compras("carlos")

    assert {2000} == set(compras)

    lector.comprar_libro("jose", 57955)
    lector.comprar_libro("jose", 61202)

    compras = lector.ver_compras("jose")
    assert {57955, 61202} == set(compras)


def test_p2_ver_detalle_sin_comprar():
    lector = laboratorio.LectorKindel()

    with pytest.raises(ValueError):
        lector.ver_detalle("carlos", 2000)


def test_p2_ver_detalle_libro_comprado():
    lector = laboratorio.LectorKindel()
    lector.registrar_usuario("carlos")

    with pytest.raises(ValueError):
        lector.ver_detalle("carlos", 2000)

    lector.comprar_libro("carlos", 2000)
    detalle_libro = lector.ver_detalle("carlos", 2000)

    assert detalle_libro == {
        "titulo": "Don Quijote",
        "autores": "Cervantes Saavedra, Miguel de, 1547-1616",
        "fecha": "1999-12-01",
        "temas": "Spain -- Social life and customs -- 16th century "
        "-- Fiction; Knights and knighthood -- Spain -- Fiction; "
        "Picaresque literature; Romances",
    }

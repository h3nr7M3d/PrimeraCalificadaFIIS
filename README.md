[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hCetjK3u)
# SW 305: Primera Práctica Calificada

## Instrucciones

- Para evitar inconvenientes, se requiere que envíen sus soluciones parciales a la nube (haciendo *Commit* y *Push*) por lo menos cada media hora.
- Está permitido consultar el material de clase (diapositivas, código fuente, y apuntes personales). **Consultar recursos como Google, ChatGPT, u otros compañeros está estrictamente prohibido, y será reportado al consejo de facultad de ser detectado.**
- Utilice la notación y el estilo de programación desarrollado en clase. Se disminuirá puntaje en caso contrario.
- Sólamente ingrese código en las secciones marcadas como `[INICIO]` y `[FIN]`. No edite otras partes de `laboratorio.py`, u otros archivos.
- La instrucción `pass` es un texto temporal. Puede eliminarlo para implementar su solución.
- El uso de `import` está prohibido. No está permitido importar o instalar librerías externas. 
- Utilice la sección final de `laboratorio.py` para probar sus soluciones. Todas sus soluciones deben contener pruebas, que demuestren su funcionamiento.

## Primer Problema (10 puntos)

En el archivo `laboratorio.py`, complete la implementación de la clase `Polinomio`. Considere lo siguiente:

- El constructor tiene dos parámetros que son cadenas de caracteres: la variable del polinomio, y el polinomio en [formato LaTeX](https://aprendeconalf.es/latex-manual/formulas.html). Por ejemplo, representar el polinomio $f(x) = 2x^3 + 3x$ se haría de la siguiente forma:

  ```python
  variable = "x"
  polinomio = "f(x) = 2x^3 + 3x"
  mi_polinomio = Polinomio(variable, polinomio)
  ```

  Note lo siguiente: 1) El símbolo de exponente es `^`, 2) los términos están separados por `+` (con espacios), y 3) El coeficiente y la variable están juntos.

- El método `representar` devuelve una cadena de caracteres, que transforma un polinomio en una expresión compatible con Python. Por ejemplo:

  ```python
  polinomio = "f(a) = 2a^3 + 3a"
  variable = "a"
  mi_polinomio = Polinomio(variable, polinomio)

  mi_polinomio.representar() # Debe retornar: "2*a**3 + 3*a"
  ```

  Note lo siguiente: 1) El símbolo de exponente es `**`, 2) los términos están separados por `+` (con espacios), y 3) Entre el coeficiente y la variable se encuentra el operador de multiplicación `*`.

- El método `comparar` devuelve `True` en caso se compare con un polinomio equivalente, y `False` en case contrario. Por ejemplo:

  ```python
  polinomio = "f(x) = 2x^3 + 3x"
  variable = "x"
  mi_polinomio = Polinomio(variable, polinomio)

  polinomio = "f(x) = 3x + 2x^3"
  variable = "x"
  otro_polinomio = Polinomio(variable, polinomio)

  mi_polinomio.comparar(otro_polinomio) # Debe retornar: True
  ```

  Note lo siguiente: Los términos de ambos polinomios pueden estar en diferente orden, en sus representaciones como cadena.

- El método `derivar` devuelve una nueva instancia de Polinomio, que representa a [la primera derivada del polinomio original](https://www.funciones.xyz/derivada-de-un-polinomio/). Por ejemplo:

  ```python
  polinomio = "f(x) = 6x^2 + 3"
  variable = "x"
  mi_polinomio Polinomio = Polinomio(variable, polinomio)

  primera_derivada = mi_polinomio.derivar()
  derivada_esperada = laboratorio.Polinomio(variable, "f(x) = 12x")

  derivada_esperada.comparar(primera_derivada) # Debe retornar: True
  ```

  Note lo siguiente: 1) El término constante `3` no está acompañado de `x^0` y 2) El termino lineal es `12x`, no `12x^1`.

## Segundo Problema (10 puntos)

En el archivo `laboratorio.py`, complete la implementación de la clase `LectorKindel`, usada para controlar un [lector de libros electrónicos](https://es.wikipedia.org/wiki/Amazon_Kindle). Esta clase ya contiene un catálogo de libros, almacenados en el atributo
`catalogo` como una lista de diccionarios. Por ejemplo:

```python
lector = LectorKindel()
print(lector.catalogo[:2])
# Resultado:
#   [
#     {'Text#': '320', 'Type': 'Text', 'Issued': '1995-09-01', 'Title': 'Vida De Lazarillo De Tormes Y De Sus Fortunas Y Adversidades', 'Language': 'es', 'Authors': 'Anonymous', 'Subjects': 'Spanish fiction; Spain -- Social conditions -- 16th century -- Fiction; Picaresque literature, Spanish', 'LoCC': 'PQ', 'Bookshelves': '6 Best Loved Spanish Literary Classics; Browsing: Culture/Civilization/Society; Browsing: Literature; Browsing: Fiction'},

#     {'Text#': '1619', 'Type': 'Text', 'Issued': '1999-01-01', 'Title': 'La Celestina', 'Language': 'es', 'Authors': 'Rojas, Fernando de, -1541', 'Subjects': 'Spanish fiction', 'LoCC': 'PQ', 'Bookshelves': '6 Best Loved Spanish Literary Classics; Browsing: Culture/Civilization/Society; Browsing: Literature; Browsing: Fiction'}
#   ]
```

Note lo siguiente: 1) El código de cada libro está almacenado en la llave `Text#` y 2) El título de cada libro está almacenado en la llave `Title`, 3) La fecha de publicación de cada libro está almacenada en la llave `Issued`, 4) Los autores de cada libro están almacenados en la llave `Authors`, y 5) Los temas del cada libro están almacenados en la llave `Subjects`.

- El método `registrar_usuario` se usa para registrar usuarios en la plataforma. Los usuarios deben ser únicos, y no distinguen entre mayúsculas y minúsculas (por ejemplo, el usuario `carlos` es equivalente al usuario `Carlos`). En caso se intente registrar un usuario duplicado, lanzar la excepción `ValueError`. Por ejemplo:

  ```python
    lector = LectorKindel()

    lector.registrar_usuario("carlos")
    lector.registrar_usuario("CARLOS") # Debe lanzar ValueError.
  ```

- El método `comprar_libro` permite a usuarios de nombre `nombre_de_usuario` comprar libros con código `codigo_libro` (número entero). No es posible comprar libros en los siguientes casos: 1) el usuario no existe, 2) No existe un libro con código `codigo_libro`, 3) El libro con código `codigo_libro` ha sido comprado por otro usuario. Por ejemplo:

  ```python
    lector = LectorKindel()
    lector.registrar_usuario("carlos")

    lector.comprar_libro("carlos", 2000)
    lector.comprar_libro("gabriel", 2000) # Debe lanzar ValueError.
  ```

- El método `ver_detalle` permite a un usuario de nombre `nombre_de_usuario` ver el detalle del libro `codigo_libro` (número entero) **que haya comprado anteriormente**. Este método retorna un diccionario con la siguiente información: 1) El título del libro, con la llave `titulo`, 2) Los autores del libro, con la llave `autores`, 3) La fecha de publicación del libro, con la llave `fecha`, 4) Los temas del libro, en la llave `temas`. Por ejemplo:

  ```python
  lector = LectorKindel()
  lector.registrar_usuario("carlos")

  lector.comprar_libro("carlos", 2000)
  detalle_libro = lector.ver_detalle("carlos", 2000)
  print(detalle_libro)

  # Debe mostrar:
  #{
  #    "titulo": "Don Quijote",
  #    "autores": "Cervantes Saavedra, Miguel de, 1547-1616",
  #    "fecha": "1999-12-01",
  #    "temas": "Spain -- Social life and customs -- 16th century "
  #    "-- Fiction; Knights and knighthood -- Spain -- Fiction; "
  #    "Picaresque literature; Romances",
  #}
  ```

  En caso el usuario no exista, el libro no exista, o el usuario no haya comprado el libro, lanzar una excepción `ValueError`.

- El método `ver_compras` devuelve una lista con los códigos de los libros (números enteros) que el usuario de nombre `nombre_de_usuario` ha comprado. Por ejemplo:

  ```python
  lector = laboratorio.LectorKindel()
  lector.registrar_usuario("carlos")
  lector.comprar_libro("carlos", 2000)
  compras = lector.ver_compras("carlos")
  print(compras) # Debe mostrar: [2000]
  ```

  En caso no exista un usuario de nombre `nombre_de_usuario`, lanzar una excepción `ValueError`.

- El método `buscar` permite buscar libros por título y autor **de manera parcial, sin distinguir entre mayúsculas y minúsculas**. El método retorna una lista de enteros, conteniendo los códigos de los libros (números enteros) que satisfacen los criterios de búsqueda. Tengan en cuenta que los resultados de la búsqueda **no deben incluir** libros que hayan sido comprados. Por ejemplo:

  ```python
  lector = LectorKindel()
  libros = lector.buscar(titulo="don quijote", autor="cervantes") # Debe mostrar: [2000]

  lector.registrar_usuario("carlos")
  lector.comprar_libro("carlos", 2000)

  libros = lector.buscar(titulo="don quijote", autor="cervantes") # Debe mostrar: []
  ```

# Cadenas de texto (`str`) en Python

**Asignatura:** Pensamiento Computacional  
**Nivel:** introductorio  
**Requisito:** Python 3; los ejemplos no necesitan bibliotecas adicionales.

## Objetivo de aprendizaje

Declarar cadenas, transformar y consultar texto, elegir métodos apropiados y distinguirlos de funciones y operadores.

## 1. ¿Qué es una cadena de texto?

Una cadena es una secuencia de caracteres Unicode representada por el tipo `str`. Permite almacenar nombres, mensajes, letras, espacios y símbolos. Un número escrito entre comillas también es texto: `"25"` no es el entero `25`.

### Declaración con comillas

Las comillas de apertura y cierre deben coincidir. Las simples y dobles tienen el mismo propósito; elegir una u otra facilita incluir comillas dentro del contenido. Las comillas triples, simples o dobles, permiten escribir varias líneas.

```python
nombre = 'Ana'                       # Comillas simples.
materia = "Pensamiento Computacional"  # Comillas dobles.
mensaje = 'Ella dijo: "Hola".'        # Comillas dobles dentro del texto.
aviso = """Primera línea
Segunda línea"""                     # Conserva el salto de línea.
otro_aviso = '''Una línea
Otra línea'''
vacia = ""                           # Cadena sin caracteres.
salto = "Hola\nPython"                # \n representa un salto de línea.

print(nombre)                        # Ana
print(mensaje)                       # Ella dijo: "Hola".
print(aviso)
# Salida de la última instrucción:
# Primera línea
# Segunda línea
```

**Observación:** una cadena entre comillas triples sigue siendo una cadena. No es, por sí misma, un comentario; los comentarios de Python comienzan con `#`.

### Inmutabilidad

Una cadena no se puede modificar carácter por carácter. Los métodos que transforman texto devuelven un resultado; para conservarlo se puede asignar a una variable.

```python
texto = "hola"
resultado = texto.upper()
print(texto)                         # hola: conserva su contenido.
print(resultado)                     # HOLA

texto = texto.upper()                # La variable pasa a referirse al resultado.
print(texto)                         # HOLA

# texto[0] = "H"                     # Si se ejecuta, provoca TypeError.
```

## 2. ¿Cómo se utiliza un método?

Un método se llama con un punto después del objeto: `cadena.metodo(argumentos)`. Los paréntesis son necesarios incluso si no hay argumentos: `texto.lower()`.

Los métodos no siempre devuelven texto: también pueden producir listas, posiciones, cantidades, valores booleanos o tuplas. En los ejemplos, los comentarios junto a `print()` indican la salida esperada. Cada bloque se puede ejecutar de forma independiente.

## 3. Cambiar mayúsculas y minúsculas

### 3.1. `lower()`

Devuelve el texto con las letras que admiten conversión en minúsculas.

```python
texto = "HOLA, Python"
print(texto.lower())                 # hola, python
```

### 3.2. `upper()`

Devuelve el texto con las letras que admiten conversión en mayúsculas.

```python
texto = "Hola, Python"
print(texto.upper())                 # HOLA, PYTHON
```

### 3.3. `capitalize()`

Pone el primer carácter en forma de título, cuando corresponde, y el resto en minúsculas. No pone en mayúscula la primera letra de cada palabra.

```python
texto = "pYTHON ES ÚTIL"
print(texto.capitalize())            # Python es útil
```

### 3.4. `title()`

Convierte el inicio de cada grupo de letras a forma de título y el resto a minúsculas. Es útil para ejercicios de presentación de palabras, pero no interpreta las reglas editoriales del español ni los nombres propios.

```python
texto = "pensamiento computacional"
print(texto.title())                 # Pensamiento Computacional
```

### 3.5. `swapcase()`

Intercambia las letras mayúsculas y minúsculas.

```python
texto = "Hola PYTHON"
print(texto.swapcase())              # hOLA python
```

### 3.6. `casefold()`

Prepara texto para comparaciones sin distinguir mayúsculas y minúsculas. Es más amplio que `lower()` para determinados caracteres Unicode. No elimina acentos ni espacios.

```python
# La letra alemana ß permite observar la diferencia.
palabra = "Straße"
print(palabra.lower())               # straße
print(palabra.casefold())            # strasse
print(palabra.casefold() == "STRASSE".casefold())  # True
```

## 4. Limpiar y sustituir contenido

### 4.1. `strip()`, `lstrip()` y `rstrip()`

Sin argumentos, eliminan espacios en blanco de los extremos: espacios, tabulaciones y saltos de línea, entre otros. `strip()` actúa en ambos extremos, `lstrip()` en el izquierdo y `rstrip()` en el derecho. No eliminan los espacios interiores.

```python
texto = "  Ana Pérez  "
# repr() hace visibles las comillas para distinguir los espacios conservados.
print(repr(texto.strip()))           # 'Ana Pérez'
print(repr(texto.lstrip()))          # 'Ana Pérez  '
print(repr(texto.rstrip()))          # '  Ana Pérez'
print("\tHola\n".strip())            # Hola

# Con argumento se elimina un conjunto de caracteres de los extremos.
print("..hola!!".strip(".!"))         # hola
```

**Observación:** el argumento no es un prefijo o sufijo literal. Por ejemplo, `strip("ab")` elimina cualquier combinación de `a` y `b` en los extremos. Para quitar un prefijo exacto existe `removeprefix()` y para un sufijo exacto, `removesuffix()` (Python 3.9 o posterior).

### 4.2. `replace(anterior, nuevo, count)`

Sustituye apariciones de un fragmento. El tercer argumento es opcional y limita cuántas sustituciones se realizan, empezando por la izquierda. La búsqueda distingue mayúsculas de minúsculas.

```python
texto = "rojo, rojo, azul"
print(texto.replace("rojo", "verde"))     # verde, verde, azul
print(texto.replace("rojo", "verde", 1))  # verde, rojo, azul
```

## 5. Separar y unir texto

### 5.1. `split(sep, maxsplit)` y `rsplit(sep, maxsplit)`

Dividen una cadena y devuelven una lista. `sep` indica el separador; `maxsplit` limita el número de divisiones. Ambos argumentos son opcionales. `rsplit()` comienza a dividir desde la derecha cuando se establece un límite; la lista conserva el orden del texto.

```python
texto = "uno-dos-tres"
print(texto.split("-"))              # ['uno', 'dos', 'tres']
print(texto.split("-", 1))           # ['uno', 'dos-tres']
print(texto.rsplit("-", 1))          # ['uno-dos', 'tres']

# Sin separador, agrupa espacios en blanco y omite vacíos de los extremos.
print("  Ana   Luis\tEva  ".split())  # ['Ana', 'Luis', 'Eva']

# Un separador explícito sí puede producir elementos vacíos.
print("a,,b".split(","))             # ['a', '', 'b']
```

**Observación:** `maxsplit=1` permite una división y, por tanto, como máximo dos elementos. El separador explícito no puede ser `""`: provocaría `ValueError`.

### 5.2. `join(iterable)`

Une cadenas usando como separador la cadena sobre la cual se llama el método. Todos los elementos deben ser cadenas.

```python
palabras = ["Aprendo", "Python", "hoy"]
print(" ".join(palabras))            # Aprendo Python hoy
print("-".join(palabras))            # Aprendo-Python-hoy

numeros = [1, 2, 3]
# str() convierte cada entero en texto antes de unirlo.
print(", ".join(str(n) for n in numeros))  # 1, 2, 3
```

### 5.3. `partition(sep)`

Divide en la primera aparición del separador y devuelve una tupla de tres elementos: texto anterior, separador y texto posterior. Si no lo encuentra, devuelve la cadena original y dos cadenas vacías. Requiere un separador no vacío.

```python
print("nombre=Ana".partition("="))   # ('nombre', '=', 'Ana')
print("nombre".partition("="))       # ('nombre', '', '')

clave, separador, valor = "curso=Python".partition("=")
print(clave)                        # curso
print(valor)                        # Python
```

### 5.4. `splitlines(keepends=False)`

Separa el texto por límites de línea y devuelve una lista. Si se indica `True`, conserva los caracteres de fin de línea.

```python
texto = "Ana\nLuis\n"
print(texto.splitlines())            # ['Ana', 'Luis']
print(texto.splitlines(True))        # ['Ana\n', 'Luis\n']
```

**Observación:** un salto de línea al final no añade una línea vacía extra en `splitlines()`. Además, reconoce distintos límites de línea, como `\n` y `\r\n`.

## 6. Buscar y contar

Las posiciones comienzan en **0**. Por ejemplo, en `"casa"` la primera `a` está en la posición `1`.

### 6.1. `find(sub)` y `rfind(sub)`

Devuelven la posición de la primera o última aparición, respectivamente. Si el fragmento no existe, devuelven `-1`.

```python
texto = "banana"
print(texto.find("na"))              # 2
print(texto.rfind("na"))             # 4
print(texto.find("uva"))             # -1
```

**Observación:** no uses directamente `if texto.find(fragmento):`: la posición `0` se considera falsa y `-1` se considera verdadero. Para comprobar existencia utiliza `fragmento in texto` o compara el resultado con `-1`.

### 6.2. `index(sub)`

Devuelve la posición de la primera aparición. A diferencia de `find()`, genera una excepción `ValueError` si no encuentra el fragmento.

```python
texto = "banana"
print(texto.index("na"))             # 2

# Capturamos la excepción para que el programa pueda continuar.
try:
    print(texto.index("uva"))
except ValueError:
    print("No se encontró el fragmento.")
# Salida: No se encontró el fragmento.
```

### 6.3. `count(sub)`

Cuenta apariciones que no se superponen.

```python
print("banana".count("a"))           # 3
print("aaaa".count("aa"))            # 2
print("banana".count("x"))           # 0
```

`find()`, `rfind()`, `index()` y `count()` también aceptan límites `start` y `end`: el inicio se incluye y el final se excluye.

```python
print("banana".find("a", 2, 5))      # 3: busca en las posiciones 2, 3 y 4.
```

### 6.4. `startswith(prefix)` y `endswith(suffix)`

Comprueban si el texto comienza o termina con un fragmento. Devuelven `True` o `False` y distinguen mayúsculas de minúsculas. También admiten límites de búsqueda.

```python
archivo = "reporte.pdf"
print(archivo.startswith("reporte")) # True
print(archivo.endswith(".pdf"))      # True
print(archivo.endswith(".PDF"))      # False
# Una tupla permite comprobar varias terminaciones.
print(archivo.endswith((".pdf", ".txt")))  # True
```

## 7. Comprobar el contenido

Estos métodos devuelven valores booleanos. Los métodos de esta sección devuelven `False` para la cadena vacía.

### 7.1. `isalpha()`

Comprueba que haya al menos un carácter y que todos sean letras Unicode. Los espacios y los signos de puntuación no cuentan como letras.

```python
print("Árbol".isalpha())             # True
print("Ana María".isalpha())         # False: contiene un espacio.
```

### 7.2. `isdigit()`

Comprueba que todos los caracteres sean dígitos y que exista al menos uno. Incluye algunos caracteres Unicode, como superíndices.

```python
print("2026".isdigit())              # True
print("²".isdigit())                 # True
print("-15".isdigit())               # False: el signo no es un dígito.
```

### 7.3. `isnumeric()`

Comprueba que todos los caracteres sean numéricos y que exista al menos uno. Abarca más caracteres que `isdigit()`, como algunas fracciones.

```python
print("123".isnumeric())             # True
print("½".isnumeric())               # True
print("½".isdigit())                 # False
print("3.14".isnumeric())            # False: contiene un punto.
```

**Observación:** estos métodos no verifican cualquier número válido para `int()` o `float()`. Por ejemplo, `int("²")` falla aunque `"²".isdigit()` sea verdadero. Para convertir una entrada numérica general, utiliza la conversión apropiada y captura `ValueError`.

### 7.4. `isalnum()`

Comprueba que haya al menos un carácter y que todos sean letras o caracteres numéricos. No acepta espacios ni guiones bajos.

```python
print("Alumno123".isalnum())         # True
print("Alumno_123".isalnum())        # False
```

### 7.5. `isspace()`

Comprueba que haya al menos un carácter y que todos sean espacios en blanco, incluidas tabulaciones y saltos de línea.

```python
print(" \t\n".isspace())             # True
print("".isspace())                  # False
print(" a ".isspace())               # False
```

### 7.6. `islower()` e `isupper()`

Comprueban si todas las letras que tienen distinción de caso están en minúsculas o mayúsculas, respectivamente. Debe existir al menos una de esas letras; los números y signos no impiden que el resultado sea verdadero.

```python
print("hola 123!".islower())         # True
print("HOLA 123!".isupper())         # True
print("Hola".islower())              # False
print("123".isupper())               # False
```

## 8. Alinear y rellenar texto

### 8.1. `center(width, fillchar)`, `ljust(width, fillchar)` y `rjust(width, fillchar)`

Alinean el texto al centro, a la izquierda o a la derecha, respectivamente, dentro de una anchura mínima. El relleno predeterminado es un espacio; si se especifica, debe ser un solo carácter. No recortan el texto si ya ocupa la anchura solicitada o más.

```python
texto = "Sol"
print(texto.center(9, "-"))          # ---Sol---
print(texto.ljust(9, "."))           # Sol......
print(texto.rjust(9, "."))           # ......Sol
print(texto.center(2, "-"))          # Sol
```

### 8.2. `zfill(width)`

Rellena con ceros a la izquierda hasta alcanzar una anchura mínima. Si existe un signo inicial `+` o `-`, coloca los ceros después del signo.

```python
print("42".zfill(5))                 # 00042
print("-42".zfill(6))                # -00042
print("12345".zfill(3))              # 12345
```

**Observación:** el resultado sigue siendo texto, útil para folios o códigos. No cambia el valor de una variable numérica.

## 9. Insertar valores con `format()`

### `str.format()`

Sustituye campos entre llaves por valores y permite controlar su presentación. Los campos pueden ser posicionales o tener nombre. La especificación `:.2f` presenta un número con dos decimales.

```python
plantilla = "Alumno: {}; calificación: {:.2f}"
print(plantilla.format("Ana", 9.5))  # Alumno: Ana; calificación: 9.50

plantilla = "Curso: {curso}; grupo: {grupo}"
print(plantilla.format(curso="Python", grupo=2))
# Salida: Curso: Python; grupo: 2

# Las llaves literales se escriben duplicadas.
print("Conjunto: {{{}}}".format("a, b"))  # Conjunto: {a, b}
```

Las **f-strings** son otra forma de insertar expresiones, pero son una sintaxis del lenguaje, no un método:

```python
nombre = "Ana"
calificacion = 9.5
print(f"{nombre}: {calificacion:.2f}")  # Ana: 9.50
```

## 10. Funciones, operadores e indexación: no son métodos

| Categoría | Ejemplo | Propósito |
| --- | --- | --- |
| Método de una cadena | `texto.upper()` | Se llama sobre el objeto con un punto. |
| Función incorporada | `len(texto)` | Recibe el texto como argumento y devuelve su longitud. |
| Constructor de tipo | `str(25)` | Convierte un valor a texto. |
| Operador `+` | `"Hola " + "Ana"` | Concatena cadenas. |
| Operador `*` | `"ha" * 3` | Repite una cadena. |
| Operadores `in`, `not in` | `"Py" in "Python"` | Comprueban pertenencia de un fragmento. |
| Operadores `==`, `!=` | `"hola" == "Hola"` | Comparan el contenido. |
| Indexación | `texto[0]` | Obtiene un carácter por su posición. |
| Rebanado o *slicing* | `texto[0:3]` | Obtiene un fragmento; excluye la posición final. |

```python
texto = "Python"
print(len(texto))                    # 6
print(str(25) + " años")             # 25 años
print("Hola " + "Ana")               # Hola Ana
print("ha" * 3)                     # hahaha
print("Py" in texto)                # True
print("java" not in texto)          # True
print("hola" == "Hola")              # False
print(texto[0])                     # P
print(texto[-1])                    # n: último carácter.
print(texto[0:3])                   # Pyt
```

**Observaciones didácticas:**

- `len(texto)` cuenta puntos de código Unicode; un símbolo visual formado por varios puntos de código puede contar como más de uno.
- Una posición fuera de rango provoca `IndexError`; por ejemplo, `"abc"[3]`.
- `+` exige cadenas a ambos lados cuando concatena texto: `"Edad: " + 20` falla; usa `str(20)` o una f-string.
- Existe también la función incorporada `format(valor, especificacion)`. Es distinta del método `plantilla.format(...)`.

## 11. Ejemplo integrador: preparar nombres de estudiantes

El siguiente programa aplica una secuencia sencilla: **separar, limpiar, presentar y unir**. Usamos nombres simples para que `title()` sea adecuado para este ejercicio.

```python
entrada = "  ana lópez, LUIS PÉREZ, eva ruiz  "
estudiantes = entrada.split(",")
nombres_limpios = []

for estudiante in estudiantes:
    # Quita espacios de los extremos y ajusta la presentación.
    nombre = estudiante.strip().title()
    nombres_limpios.append(nombre)

reporte = "; ".join(nombres_limpios)
print(reporte)                      # Ana López; Luis Pérez; Eva Ruiz
print("Total: {}".format(len(nombres_limpios)))  # Total: 3
```

Aquí `append()` pertenece a una **lista**, no a una cadena. `len(nombres_limpios)` cuenta los elementos de esa lista. En un sistema real conviene conservar la escritura elegida por cada persona para su nombre.

## 12. Resumen de consulta rápida

| Necesidad | Métodos principales |
| --- | --- |
| Cambiar el caso | `lower`, `upper`, `capitalize`, `title`, `swapcase` |
| Comparar sin distinguir mayúsculas | `casefold` |
| Limpiar extremos | `strip`, `lstrip`, `rstrip` |
| Sustituir fragmentos | `replace` |
| Dividir o unir | `split`, `rsplit`, `join` |
| Separar en tres partes o en líneas | `partition`, `splitlines` |
| Encontrar posiciones | `find`, `rfind`, `index` |
| Contar apariciones | `count` |
| Comprobar inicio o final | `startswith`, `endswith` |
| Comprobar clases de caracteres | `isalpha`, `isdigit`, `isnumeric`, `isalnum`, `isspace` |
| Comprobar el caso | `islower`, `isupper` |
| Alinear o rellenar | `center`, `ljust`, `rjust`, `zfill` |
| Insertar valores en una plantilla | `format` |

Antes de elegir una operación, identifica qué resultado necesitas: **otra cadena, una lista, una posición, una cantidad o un valor booleano**. Recuerda que las cadenas son inmutables y que buscar una coincidencia suele distinguir entre mayúsculas y minúsculas.

## 13. Actividades breves

1. Declara `correo = "  ANA@ESCUELA.MX  "`. Obtén `"ana@escuela.mx"` combinando dos métodos.
2. Para `"rojo|verde|azul"`, crea una lista y después une sus elementos con `", "`.
3. Explica qué diferencia hay entre `"casa".find("z")` y `"casa".index("z")`.
4. Predice el resultado de `"12.5".isdigit()` y justifica tu respuesta.

### Respuestas orientativas

```python
correo = "  ANA@ESCUELA.MX  "
print(correo.strip().lower())        # ana@escuela.mx

colores = "rojo|verde|azul".split("|")
print(", ".join(colores))           # rojo, verde, azul

print("casa".find("z"))              # -1
# "casa".index("z") genera ValueError porque no hay coincidencia.

print("12.5".isdigit())              # False: el punto no es un dígito.
```

## 14. Referencias para ampliar

- Python Software Foundation. [Tipo de secuencia de texto `str` y métodos de cadenas](https://docs.python.org/es/3/library/stdtypes.html#text-sequence-type-str).
- Python Software Foundation. [Función incorporada `len()`](https://docs.python.org/es/3/library/functions.html#len).
- Python Software Foundation. [Introducción a las cadenas](https://docs.python.org/es/3/tutorial/introduction.html#text).

Los ejemplos de este apunte son originales y están pensados para ejecutarse en Python 3.

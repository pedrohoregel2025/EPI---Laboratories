# TC1038 – Métodos principales de listas en Python

**Asignatura:** Pensamiento Computacional  
**Dirigido a:** estudiantes universitarios de diversas ingenierías  
**Lenguaje:** Python 3

## 1. ¿Qué es una lista?

Una **lista** es una colección ordenada de elementos. Conserva el orden en que se colocan sus elementos, permite valores repetidos y puede contener objetos de distintos tipos. Es útil para representar mediciones, calificaciones, componentes de un sistema o registros de una simulación.

Se declara con **corchetes `[]`**, separando sus elementos con comas:

```python
vacia = []                              # Lista sin elementos.
temperaturas = [22.5, 24.0, 21.8]        # Homogénea: todos son float.
materiales = ["acero", "aluminio"]       # Homogénea: todos son str.
sensor = ["S01", 24.5, True]             # Mixta: str, float y bool.
repetidos = [10, 10, 20]                 # Los duplicados están permitidos.
print(vacia, temperaturas, materiales, sensor, repetidos)
```

### Índices desde 0

Cada posición tiene un **índice**. El primero es `0`; el último índice positivo es `len(lista) - 1`. Los índices negativos cuentan desde el final: `-1` es el último elemento.

```python
mediciones = [12, 15, 18]
print(mediciones[0])    # 12
print(mediciones[2])    # 18
print(mediciones[-1])   # 18

try:
    print(mediciones[3])  # No existe esta posición.
except IndexError:
    print("Índice fuera de rango")
```

### Mutabilidad

Las listas son **mutables**: podemos cambiar, agregar o eliminar elementos después de crearlas. Asignar un nuevo valor a una posición modifica la misma lista.

```python
mediciones = [12, 15, 18]
mediciones[1] = 16
print(mediciones)  # [12, 16, 18]
```

Un **método** es una operación asociada a un objeto. Se invoca con un punto: `lista.metodo(argumentos)`. En las siguientes sintaxis, `lista`, `valor` e `iterable` representan objetos que debes sustituir en tu programa. Un iterable es un objeto que puede recorrerse, como otra lista, una cadena o un `range`.

## 2. Métodos incorporados de `list`

Los once métodos siguientes constituyen los métodos públicos propios de `list`. Cada bloque de esta sección es independiente y puede ejecutarse en Python 3.

### 2.1. `append`: agregar un elemento al final

**Descripción:** agrega el objeto recibido como **un solo elemento**. Modifica la lista y devuelve `None`.

**Sintaxis:** `lista.append(valor)`

```python
lecturas = [10, 12]
resultado = lecturas.append(14)
print(lecturas)  # [10, 12, 14]
print(resultado)  # None

# Una lista pasada a append se agrega como un elemento anidado.
lecturas.append([16, 18])
print(lecturas)  # [10, 12, 14, [16, 18]]
```

### 2.2. `extend`: agregar los elementos de un iterable

**Descripción:** recorre un iterable y agrega sus elementos al final. Modifica la lista y devuelve `None`.

**Sintaxis:** `lista.extend(iterable)`

```python
lecturas = [10, 12]
lecturas.extend([14, 16])
print(lecturas)  # [10, 12, 14, 16]

letras = ["A"]
letras.extend("BC")  # Una cadena aporta sus caracteres.
print(letras)  # ['A', 'B', 'C']
```

**`append` vs. `extend`:** `append([14, 16])` agrega una lista completa como un elemento; `extend([14, 16])` agrega dos elementos. `extend` no aplana estructuras anidadas de manera recursiva.

### 2.3. `insert`: insertar antes de una posición

**Descripción:** inserta un valor antes del índice indicado y desplaza los elementos posteriores. Modifica la lista y devuelve `None`.

**Sintaxis:** `lista.insert(indice, valor)`

```python
etapas = ["diseño", "pruebas"]
etapas.insert(1, "construcción")
print(etapas)  # ['diseño', 'construcción', 'pruebas']

etapas.insert(0, "análisis")  # Inserta al inicio.
etapas.insert(100, "entrega")  # Un índice muy grande inserta al final.
print(etapas)
# ['análisis', 'diseño', 'construcción', 'pruebas', 'entrega']
```

A diferencia del acceso por índice, `insert` ajusta los índices fuera de los límites: uno demasiado grande inserta al final y uno demasiado negativo, al inicio; no produce `IndexError` por ese motivo.

### 2.4. `remove`: eliminar por valor

**Descripción:** elimina la **primera aparición** de un valor igual al indicado. Modifica la lista y devuelve `None`. Si el valor no existe, lanza `ValueError`.

**Sintaxis:** `lista.remove(valor)`

```python
codigos = [101, 202, 101, 303]
codigos.remove(101)
print(codigos)  # [202, 101, 303]

try:
    codigos.remove(999)
except ValueError:
    print("El código no está en la lista")
```

También puedes comprobar `if valor in lista:` antes de eliminarlo, si la ausencia es una situación esperada.

### 2.5. `pop`: eliminar por posición y recuperar el elemento

**Descripción:** elimina y **devuelve** el elemento del índice indicado. Sin argumento elimina el último. Lanza `IndexError` si la lista está vacía o el índice no existe.

**Sintaxis:** `lista.pop()` o `lista.pop(indice)`

```python
pendientes = ["modelar", "simular", "documentar"]
ultima = pendientes.pop()
print(ultima)  # documentar

primera = pendientes.pop(0)
print(primera)    # modelar
print(pendientes)  # ['simular']

try:
    pendientes.pop(5)
except IndexError:
    print("No existe esa posición")

vacia = []
try:
    vacia.pop()
except IndexError:
    print("No hay elementos para extraer")
```

**`remove` vs. `pop`:** `remove(10)` busca el **valor** `10`; `pop(10)` extrae el elemento de la **posición** `10`. Solo `pop` devuelve el elemento eliminado.

### 2.6. `clear`: vaciar la lista

**Descripción:** elimina todos los elementos. Modifica la misma lista y devuelve `None`; aplicarlo a una lista vacía también es válido.

**Sintaxis:** `lista.clear()`

```python
resultados = [8.1, 9.3, 7.4]
resultados.clear()
print(resultados)  # []
```

### 2.7. `index`: buscar la posición de un valor

**Descripción:** devuelve el índice de la primera aparición del valor. No modifica la lista. Lanza `ValueError` si el valor no se encuentra en el intervalo de búsqueda.

**Sintaxis:** `lista.index(valor)`, `lista.index(valor, inicio)` o `lista.index(valor, inicio, fin)`

El intervalo incluye `inicio` y excluye `fin`. El índice devuelto corresponde a la lista original.

```python
materiales = ["acero", "cobre", "acero", "aluminio"]
print(materiales.index("acero"))        # 0
print(materiales.index("acero", 1))     # 2
print(materiales.index("acero", 1, 3))  # 2

try:
    materiales.index("titanio")
except ValueError:
    print("Material no encontrado")
```

### 2.8. `count`: contar apariciones

**Descripción:** devuelve cuántos elementos son iguales al valor buscado. No modifica la lista. Si el valor no aparece, devuelve `0`.

**Sintaxis:** `lista.count(valor)`

```python
estados = ["OK", "FALLA", "OK", "OK"]
print(estados.count("OK"))        # 3
print(estados.count("PENDIENTE"))  # 0
```

### 2.9. `sort`: ordenar la misma lista

**Descripción:** ordena la lista **in-place**, es decir, modifica el mismo objeto, y devuelve `None`. Por defecto, el orden es ascendente. `reverse=True` solicita orden descendente; `key` permite indicar una función para obtener el criterio de ordenación.

**Sintaxis:** `lista.sort(key=None, reverse=False)`

```python
tiempos = [3.2, 1.8, 2.5]
resultado = tiempos.sort()
print(tiempos)    # [1.8, 2.5, 3.2]
print(resultado)  # None

tiempos.sort(reverse=True)
print(tiempos)  # [3.2, 2.5, 1.8]

componentes = ["resistencia", "led", "motor"]
componentes.sort(key=len)  # Ordena por longitud del texto.
print(componentes)  # ['led', 'motor', 'resistencia']
```

Los elementos —o las claves que devuelve `key`— deben poder compararse entre sí. Ordenar `[10, "20"]` con el criterio predeterminado produce `TypeError`. La ordenación es **estable**: los elementos con la misma clave conservan su orden relativo.

**`sort` vs. `sorted`:** `sort` es un método que modifica una lista. `sorted` es una función incorporada que recibe un iterable y devuelve una **nueva lista** ordenada.

```python
original = [30, 10, 20]
ordenada = sorted(original)
print(original)  # [30, 10, 20]
print(ordenada)  # [10, 20, 30]
```

### 2.10. `reverse`: invertir el orden actual

**Descripción:** invierte la secuencia de elementos de la misma lista y devuelve `None`. No compara valores ni los ordena por magnitud.

**Sintaxis:** `lista.reverse()`

```python
datos = [30, 10, 20]
datos.reverse()
print(datos)  # [20, 10, 30]
```

**`reverse` vs. `reversed`:** `reverse()` modifica la lista; la función `reversed(lista)` devuelve un **iterador** que recorre sus elementos en orden inverso y no modifica la lista. Para obtener otra lista, usa `list(reversed(lista))`.

```python
original = [30, 10, 20]
invertida = list(reversed(original))
print(original)  # [30, 10, 20]
print(invertida)  # [20, 10, 30]
```

Invertir `[30, 10, 20]` produce `[20, 10, 30]`; ordenarla de mayor a menor produce `[30, 20, 10]`. Son operaciones distintas.

### 2.11. `copy`: crear una copia superficial

**Descripción:** devuelve una nueva lista con referencias a los mismos elementos. No modifica la lista original. La copia es **superficial**: las listas u otros objetos mutables anidados siguen compartiéndose.

**Sintaxis:** `nueva = lista.copy()`

```python
original = [10, 20, 30]
copia = original.copy()
copia[0] = 99
print(original)  # [10, 20, 30]
print(copia)     # [99, 20, 30]

matriz = [[1, 2], [3, 4]]
otra = matriz.copy()
otra[0][0] = 99  # Modifica una fila compartida por ambas listas.
print(matriz)   # [[99, 2], [3, 4]]
print(otra)     # [[99, 2], [3, 4]]
```

La asignación `otra = matriz` ni siquiera crea una lista exterior nueva: ambos nombres se refieren al mismo objeto. Cuando se necesita copiar también estructuras anidadas, puede utilizarse `copy.deepcopy`:

```python
from copy import deepcopy

matriz = [[1, 2], [3, 4]]
independiente = deepcopy(matriz)
independiente[0][0] = 99
print(matriz)         # [[1, 2], [3, 4]]
print(independiente)  # [[99, 2], [3, 4]]
```

## 3. Tabla resumen de métodos

| Método | Propósito | ¿Modifica la lista? | Devuelve | Excepción relevante |
|---|---|---|---|---|
| `append(x)` | Agregar un elemento al final | Sí | `None` | — |
| `extend(iterable)` | Agregar elementos de un iterable | Sí | `None` | `TypeError` si no es iterable |
| `insert(i, x)` | Insertar antes de una posición | Sí | `None` | No falla por índice fuera de límites |
| `remove(x)` | Eliminar la primera coincidencia | Sí | `None` | `ValueError` si no existe |
| `pop(i)` | Extraer una posición; última por defecto | Sí | Elemento eliminado | `IndexError` |
| `clear()` | Eliminar todos los elementos | Sí | `None` | — |
| `index(x)` | Buscar la primera posición | No | Índice entero | `ValueError` si no existe |
| `count(x)` | Contar coincidencias | No | Cantidad entera | — |
| `sort(...)` | Ordenar in-place | Sí | `None` | `TypeError` si no puede comparar |
| `reverse()` | Invertir el orden actual | Sí | `None` | — |
| `copy()` | Crear una copia superficial | No | Nueva lista | — |

La tabla destaca las excepciones más habituales; no enumera todos los errores posibles por argumentos de tipo incorrecto.

**Regla práctica sobre `None`:** `append`, `extend`, `insert`, `remove`, `clear`, `sort` y `reverse` modifican la lista y devuelven `None`. `pop` es la excepción entre estos métodos de modificación: devuelve lo que elimina. Evita escribir `datos = datos.sort()`; esa asignación reemplaza la referencia a la lista con `None`.

## 4. Operaciones útiles que no son métodos de `list`

Estas operaciones pertenecen a funciones, operadores o instrucciones de Python. No se escriben como métodos de la lista.

| Operación | Uso | Observación |
|---|---|---|
| `len(lista)` | Número de elementos | Una lista vacía tiene longitud `0` |
| `x in lista`, `x not in lista` | Comprobar pertenencia | Devuelven `True` o `False` |
| `lista1 + lista2` | Concatenar listas | Crea una nueva lista exterior |
| `lista * n` | Repetir los elementos | Repite referencias, no hace copias profundas |
| `lista[inicio:fin:paso]` | Obtener un segmento o *slice* | Excluye `fin`; crea una copia superficial |
| `del lista[i]` | Eliminar una posición | No devuelve el elemento; puede lanzar `IndexError` |
| `del lista[inicio:fin]` | Eliminar un segmento | Modifica la lista |
| `sum(lista)` | Sumar elementos numéricos | En una lista vacía devuelve `0` por defecto |
| `min(lista)`, `max(lista)` | Obtener el menor o mayor | Requieren elementos comparables; vacía sin `default` produce `ValueError` |
| `sorted(iterable)` | Obtener una lista ordenada | No modifica la lista de origen |
| `reversed(lista)` | Recorrer en orden inverso | Devuelve un iterador |

```python
valores = [8, 3, 5, 2]
print(len(valores))         # 4
print(3 in valores)         # True
print(10 not in valores)    # True
print(valores + [7, 9])     # [8, 3, 5, 2, 7, 9]
print([0] * 3)              # [0, 0, 0]
print(valores[1:3])         # [3, 5]
print(valores[:2])          # [8, 3]
print(valores[::2])         # [8, 5]
print(valores[::-1])        # [2, 5, 3, 8]

del valores[1]
print(valores)              # [8, 5, 2]
del valores[1:]
print(valores)              # [8]

mediciones = [8, 3, 5, 2]
print(sum(mediciones))      # 18
print(min(mediciones))      # 2
print(max(mediciones))      # 8
print(sum(mediciones) / len(mediciones))  # 4.5

vacia = []
print(sum(vacia))                  # 0
print(min(vacia, default=None))    # None
print(max(vacia, default=None))    # None
```

Antes de calcular un promedio, comprueba que la lista tenga elementos para evitar dividir entre cero. `sum` se usa aquí para números; no sirve para concatenar cadenas. `min` y `max` también pueden aplicarse a otros tipos comparables, como cadenas.

**Slices:** acceder a `lista[100]` puede fallar, pero un segmento como `lista[:100]` se ajusta a los límites existentes. Un paso de `0` en un slice produce `ValueError`.

**Cuidado con la repetición de listas anidadas:**

```python
filas_compartidas = [[0, 0]] * 3
filas_compartidas[0][0] = 1
print(filas_compartidas)  # [[1, 0], [1, 0], [1, 0]]

# Cada iteración crea una fila independiente.
filas_independientes = [[0, 0] for _ in range(3)]
filas_independientes[0][0] = 1
print(filas_independientes)  # [[1, 0], [0, 0], [0, 0]]
```

## 5. Ejercicio didáctico con análisis EPS

**Problema:** un laboratorio registra temperaturas en °C. Por una convención del equipo, `-999.0` indica una lectura inválida. Elimina esas lecturas, conserva los datos originales y calcula cantidad de lecturas válidas, promedio, mínimo y máximo. Muestra además las temperaturas válidas ordenadas.

**EPS** significa **Entrada, Proceso y Salida**.

| Etapa | Especificación |
|---|---|
| **Entrada** | Lista de números; `-999.0` representa un error del sensor |
| **Proceso** | Crear una lista de lecturas válidas; contar sus elementos; si hay datos, calcular suma/cantidad, mínimo y máximo; obtener una nueva lista ordenada |
| **Salida** | Lista válida, cantidad, promedio, mínimo, máximo y lista ordenada; si no hay lecturas válidas, informar esa condición |

**Algoritmo:**

1. Crear una lista vacía para las temperaturas válidas.
2. Recorrer la entrada y agregar con `append` cada valor distinto de `-999.0`.
3. Calcular la cantidad con `len`.
4. Si la cantidad es mayor que cero, calcular los estadísticos y ordenar una copia con `sorted`.
5. En caso contrario, mostrar que no hay lecturas válidas.

```python
temperaturas = [23.5, -999.0, 24.0, 22.5, -999.0, 26.0]
validas = []

for temperatura in temperaturas:
    if temperatura != -999.0:
        validas.append(temperatura)

cantidad = len(validas)
print("Lecturas válidas:", validas)
print("Cantidad:", cantidad)

if cantidad > 0:
    promedio = sum(validas) / cantidad
    print(f"Promedio: {promedio:.2f} °C")
    print("Mínimo:", min(validas))
    print("Máximo:", max(validas))
    print("Ordenadas:", sorted(validas))
else:
    print("No hay lecturas válidas para calcular estadísticos")

print("Original:", temperaturas)  # La entrada permanece intacta.
```

**Resultado esperado:**

```text
Lecturas válidas: [23.5, 24.0, 22.5, 26.0]
Cantidad: 4
Promedio: 24.00 °C
Mínimo: 22.5
Máximo: 26.0
Ordenadas: [22.5, 23.5, 24.0, 26.0]
Original: [23.5, -999.0, 24.0, 22.5, -999.0, 26.0]
```

**Casos para probar:** una lista vacía, una lista con solo valores `-999.0` y una con una única lectura válida. Los primeros dos casos deben informar que no hay lecturas válidas; con una sola lectura, promedio, mínimo y máximo coinciden.

## 6. Ejemplo integrador: tiempos de pruebas de un prototipo

El siguiente programa reúne altas, corrección de datos, búsqueda, extracción, copia, ordenación e inversión. Los tiempos se expresan en segundos.

```python
tiempos = [12.4, 11.8, 13.0]

# Registrar nuevas pruebas.
tiempos.append(12.1)
tiempos.extend([11.8, 12.6])
tiempos.insert(0, 14.0)

# Se confirmó que 14.0 fue una lectura incorrecta.
if 14.0 in tiempos:
    tiempos.remove(14.0)

# Retirar la última prueba y conservar el valor para su revisión.
retirada = tiempos.pop()
print("Prueba retirada:", retirada)  # 12.6
print("Repeticiones de 11.8:", tiempos.count(11.8))  # 2
print("Primera posición de 11.8:", tiempos.index(11.8))  # 1

# Los números son inmutables: la copia superficial es suficiente aquí.
ordenados = tiempos.copy()
ordenados.sort()
print("Orden de registro:", tiempos)  # [12.4, 11.8, 13.0, 12.1, 11.8]
print("Ascendente:", ordenados)      # [11.8, 11.8, 12.1, 12.4, 13.0]

ordenados.reverse()
print("Descendente:", ordenados)     # [13.0, 12.4, 12.1, 11.8, 11.8]

if tiempos:
    promedio = sum(tiempos) / len(tiempos)
    print(f"Promedio: {promedio:.2f} s")  # Promedio: 12.22 s
    print("Mejor tiempo:", min(tiempos))  # 11.8

# Limpiar únicamente la lista auxiliar al terminar.
ordenados.clear()
print("Auxiliar:", ordenados)  # []
```

Aquí el orden descendente se obtiene al invertir una lista que ya estaba ordenada de menor a mayor. En general, `reverse()` por sí solo no ordena.

## 7. Observaciones y errores frecuentes

- **Distingue valor de posición:** `remove` usa un valor; `pop`, `insert` y el acceso con corchetes usan índices.
- **No confundas cambio y resultado:** los métodos que devuelven `None` se invocan en una instrucción independiente. Para una lista ordenada nueva, utiliza `sorted`.
- **Comprueba los límites:** una lista de longitud `n` admite índices positivos de `0` a `n - 1`. En una lista vacía no hay un índice válido para acceder o extraer.
- **La igualdad determina las coincidencias:** `remove`, `index`, `count` y `in` comparan valores; no exigen que sean el mismo objeto.
- **Cuida las referencias:** `b = a` comparte la lista; `a.copy()` y `a[:]` crean copias superficiales. Las estructuras anidadas requieren atención adicional.
- **Evita eliminar elementos de la misma lista mientras la recorres:** al desplazarse los índices podrías omitir elementos. Para filtrar, construye otra lista, como en el ejercicio EPS.
- **Elige tipos coherentes con el problema:** una lista mixta es válida, pero algunas operaciones como sumar u ordenar requieren tipos compatibles.
- **El orden tiene significado:** conserva una copia si necesitas mantener el orden de captura antes de usar `sort` o `reverse`.

## 8. Comprobación del apunte

Los bloques de Python se verificaron mediante ejecución independiente. Se comprobaron también las salidas indicadas en comentarios, los casos vacíos del ejercicio EPS, las excepciones descritas y el comportamiento de las copias superficiales.

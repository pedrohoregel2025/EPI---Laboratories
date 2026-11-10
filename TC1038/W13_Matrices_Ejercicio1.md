# TC1038 — Actividad: análisis de una matriz 10 × 10 y sumatoria de fila o columna

**Dirigida a:** estudiantes de ingeniería que inician en programación con Python.  
**Modalidad sugerida:** individual, con discusión de resultados en parejas.  
**Duración sugerida:** 90 a 120 minutos.  
**Requisitos:** listas, variables, funciones, condicionales y ciclos `for` y `while`.  
**Material:** Python 3, editor de código y este documento.

## 1. Objetivo de aprendizaje

Analizar y ejecutar un programa que suma los diez elementos de una fila o columna de una matriz, utilizando indexación bidimensional, un acumulador, validación de entradas y descomposición en funciones y procedimientos. Justificar el resultado mediante pruebas de escritorio y distinguir entre calcular un valor y mostrarlo en pantalla.

Al finalizar, podrás:

- Identificar la entrada, el proceso y la salida de la solución.
- Explicar qué índice permanece fijo y cuál cambia en cada recorrido.
- Rastrear la actualización de un acumulador en diez iteraciones.
- Reconocer los alcances y las limitaciones de las validaciones existentes.
- Relacionar las responsabilidades de cada subprograma con el flujo principal.

## 2. Planteamiento del problema

Una matriz puede representar mediciones de un proceso de ingeniería: cada fila podría corresponder a un punto de medición y cada columna a una condición de operación. Para esta actividad, los números son datos didácticos sin unidades físicas asignadas.

El programa ya contiene una matriz de **10 filas y 10 columnas**. El usuario elige `F` para sumar una fila o `C` para sumar una columna; después indica un índice de **0 a 9**. El programa calcula y muestra un único total por ejecución.

**Consigna:** analiza primero el código sin modificarlo. Predice los resultados, realiza los recorridos manualmente y después ejecuta el programa para contrastar tus respuestas. No sustituyas los ciclos por `sum()` en el análisis solicitado.

La última fila es `[110, 120, 130, 140, 150, 160, 170, 180, 190, 200]`. Es distinta de la progresión de las filas anteriores y debe conservarse. No supongas que contiene valores de 1000 a 1090.

## 3. Análisis EPS: Entrada–Proceso–Salida

| Elemento | Datos o acciones | Tipo / condición |
|---|---|---|
| Entrada del usuario | Opción de operación: `F` o `C` | `str`; se convierte a mayúsculas |
| Entrada del usuario | Número de fila o columna | Se convierte a `int`; rango permitido: 0–9 |
| Datos internos | Matriz predefinida con 100 enteros | Lista de 10 listas, cada una con 10 elementos |
| Proceso | Definir e imprimir la matriz; solicitar y validar la opción y el índice | La validación del índice presupone que la conversión a entero fue exitosa |
| Proceso | Inicializar `suma = 0`; recorrer diez posiciones; acumular sus valores | Seleccionar `sumar_fila` o `sumar_columna` |
| Salida | Tipo de recorrido, índice elegido y total | Texto en pantalla; el total calculado es un `int` |

La matriz no se captura por teclado: la proporciona `definir_matriz()`.

## 4. Indexación: `matriz[fila][columna]`

En Python, esta matriz se representa mediante una lista de listas:

- El primer índice selecciona una fila.
- El segundo selecciona un elemento dentro de esa fila, es decir, una columna.
- Los índices empiezan en cero: la primera fila es la fila 0 y la décima es la fila 9.
- `range(10)` produce los valores 0, 1, 2, …, 9; no incluye 10.

| Expresión | Interpretación | Valor |
|---|---|---:|
| `matriz[0][0]` | Primera fila, primera columna | 100 |
| `matriz[0][9]` | Primera fila, décima columna | 190 |
| `matriz[1][0]` | Segunda fila, primera columna | 200 |
| `matriz[2][3]` | Tercera fila, cuarta columna | 330 |
| `matriz[3][2]` | Cuarta fila, tercera columna | 420 |
| `matriz[9][0]` | Décima fila, primera columna | 110 |
| `matriz[9][9]` | Décima fila, décima columna | 200 |

Intercambiar los índices puede cambiar el valor: `matriz[2][3]` y `matriz[3][2]` no representan la misma celda.

Python admite índices negativos en listas; por ejemplo, `matriz[-1]` seleccionaría la última fila. Sin embargo, **este programa los rechaza**, porque su especificación solo permite índices entre 0 y 9.

## 5. Pasos de análisis del algoritmo

1. **Delimitar el problema.** Se necesita sumar una sola fila o una sola columna de la matriz fija.
2. **Identificar los datos.** Localiza `matriz`, `opcion`, `indice`, `suma` y `resultado`; indica su tipo y función.
3. **Leer el punto de entrada.** La condición `if __name__ == "__main__":` llama a `main()` cuando el archivo se ejecuta directamente.
4. **Seguir la preparación.** `main()` obtiene la matriz mediante `definir_matriz()` y la envía a `imprimir_matriz()`.
5. **Analizar la captura de la opción.** `solicitar_datos()` lee una cadena y aplica `.upper()`. Mientras no sea `F` ni `C`, vuelve a solicitarla.
6. **Analizar la captura del índice.** Se intenta convertir la entrada a entero. Si la conversión funciona, el ciclo rechaza valores menores que 0 o mayores que 9.
7. **Identificar la selección.** Si la opción es `F`, se llama a `sumar_fila(matriz, indice)`; de lo contrario se llama a `sumar_columna(matriz, indice)`. Este `else` corresponde a `C` porque la opción ya fue validada.
8. **Rastrear el recorrido.** Antes del ciclo, `suma` vale 0. En cada iteración se lee una celda y se agrega su valor al acumulador.
9. **Seguir el retorno.** La función de suma devuelve el total, que `main()` guarda en `resultado`.
10. **Identificar la salida.** `mostrar_resultado()` imprime el tipo de sumatoria, el índice y el total. El programa termina; no tiene un menú para repetir operaciones.

**Actividad:** escribe estos pasos con tus propias palabras y elabora un diagrama de flujo o pseudocódigo que muestre las dos validaciones y la selección de la operación.

## 6. Diferencia entre sumar una fila y sumar una columna

| Aspecto | Sumar fila | Sumar columna |
|---|---|---|
| Índice fijo | `num_fila` | `num_columna` |
| Índice que cambia | `j`, de 0 a 9 | `i`, de 0 a 9 |
| Acceso | `matriz[num_fila][j]` | `matriz[i][num_columna]` |
| Recorrido | Horizontal, dentro de una fila | Vertical, pasando por las filas |
| Cantidad de elementos | 10 | 10 |

Fragmentos del código original:

```python
# Fila fija; cambia la columna.
suma = 0
for j in range(10):
    suma += matriz[num_fila][j]
```

```python
# Columna fija; cambia la fila.
suma = 0
for i in range(10):
    suma += matriz[i][num_columna]
```

La expresión `suma += valor` equivale aquí a `suma = suma + valor`. Inicializar el acumulador en cero permite comenzar sin agregar una cantidad ajena a los datos. Después de cada iteración, contiene la suma de los elementos visitados hasta ese momento.

Las letras `i` y `j` son una convención; su significado depende de la posición que ocupan en el acceso a la matriz.

**Observación:** imprimir la matriz requiere dos ciclos anidados y visita 100 celdas. Sumar una fila o columna requiere un solo ciclo y visita 10 celdas. Si se generalizara a una matriz cuadrada de tamaño n, imprimirla visitaría n² celdas y una sumatoria visitaría n.

## 7. Funciones y procedimientos

En esta actividad se usa la distinción didáctica: una **función** devuelve un dato útil y un **procedimiento** realiza acciones sin devolver explícitamente un resultado útil. En Python ambos se definen con `def`; si no hay un `return` explícito, la llamada devuelve `None`.

| Subprograma | Clasificación didáctica | Recibe | Devuelve / efecto |
|---|---|---|---|
| `definir_matriz()` | Función | Sin parámetros | Devuelve la matriz (`list`) |
| `solicitar_datos()` | Función con entrada/salida | Sin parámetros; lee el teclado | Devuelve una tupla `(opcion, indice)`, con `str` e `int` |
| `sumar_fila(matriz, num_fila)` | Función | Matriz e índice de fila | Devuelve el total (`int`) |
| `sumar_columna(matriz, num_columna)` | Función | Matriz e índice de columna | Devuelve el total (`int`) |
| `imprimir_matriz(matriz)` | Procedimiento | Matriz | Imprime la matriz; retorna implícitamente `None` |
| `mostrar_resultado(opcion, indice, resultado)` | Procedimiento | Opción, índice y total | Imprime el resultado; retorna implícitamente `None` |
| `main()` | Procedimiento principal | Sin parámetros | Coordina las llamadas; retorna implícitamente `None` |

La instrucción `opcion, indice = solicitar_datos()` desempaqueta los dos elementos de la tupla. Las funciones de suma no imprimen el total: lo devuelven para que otro subprograma lo muestre.

## 8. Validaciones y límites del código original

### Opción F/C

`.upper()` permite que `f` y `c` se acepten como `F` y `C`. La condición:

```python
while opcion != 'F' and opcion != 'C':
```

repite la solicitud únicamente cuando la opción es diferente de ambas alternativas. Usar `or` en lugar de `and` en esa condición impediría aceptar cualquier opción: una cadena no puede ser simultáneamente `F` y `C`.

El código original no usa `.strip()`: una entrada como ` F `, con espacios, se rechaza.

### Índice 0–9

La condición `indice < 0 or indice > 9` rechaza cualquiera de los dos extremos inválidos. Los valores 0 y 9 sí se aceptan.

**Limitación importante:** `int(input())` lanza `ValueError` si la entrada no puede interpretarse como entero, por ejemplo `hola`, `3.5` o una cadena vacía. Esto ocurre antes de evaluar el rango y termina el programa si no se captura la excepción. La misma limitación existe al volver a solicitar el índice dentro del `while`.

Las funciones de suma suponen una matriz de 10 × 10 y un índice válido; no realizan validaciones propias. Los valores 10 están fijados en sus ciclos.

## 9. Pruebas de escritorio y resultados de referencia

**Instrucción:** completa primero tus cálculos sin ejecutar el programa. Después compara con estas referencias y registra el resultado obtenido al ejecutarlo.

### 9.1 Fila 0: opción F, índice 0

Secuencia: 100 + 110 + 120 + 130 + 140 + 150 + 160 + 170 + 180 + 190 = **1450**.

| Iteración | j | Celda | Valor leído | suma antes | suma después |
|---:|---:|---|---:|---:|---:|
| 1 | 0 | `matriz[0][0]` | 100 | 0 | 100 |
| 2 | 1 | `matriz[0][1]` | 110 | 100 | 210 |
| 3 | 2 | `matriz[0][2]` | 120 | 210 | 330 |
| 4 | 3 | `matriz[0][3]` | 130 | 330 | 460 |
| 5 | 4 | `matriz[0][4]` | 140 | 460 | 600 |
| 6 | 5 | `matriz[0][5]` | 150 | 600 | 750 |
| 7 | 6 | `matriz[0][6]` | 160 | 750 | 910 |
| 8 | 7 | `matriz[0][7]` | 170 | 910 | 1080 |
| 9 | 8 | `matriz[0][8]` | 180 | 1080 | 1260 |
| 10 | 9 | `matriz[0][9]` | 190 | 1260 | 1450 |

Comprobación aritmética independiente: 10 × (100 + 190) / 2 = **1450**.

### 9.2 Columna 0: opción C, índice 0

Secuencia: 100 + 200 + 300 + 400 + 500 + 600 + 700 + 800 + 900 + 110 = **4610**.

| Iteración | i | Celda | Valor leído | suma antes | suma después |
|---:|---:|---|---:|---:|---:|
| 1 | 0 | `matriz[0][0]` | 100 | 0 | 100 |
| 2 | 1 | `matriz[1][0]` | 200 | 100 | 300 |
| 3 | 2 | `matriz[2][0]` | 300 | 300 | 600 |
| 4 | 3 | `matriz[3][0]` | 400 | 600 | 1000 |
| 5 | 4 | `matriz[4][0]` | 500 | 1000 | 1500 |
| 6 | 5 | `matriz[5][0]` | 600 | 1500 | 2100 |
| 7 | 6 | `matriz[6][0]` | 700 | 2100 | 2800 |
| 8 | 7 | `matriz[7][0]` | 800 | 2800 | 3600 |
| 9 | 8 | `matriz[8][0]` | 900 | 3600 | 4500 |
| 10 | 9 | `matriz[9][0]` | 110 | 4500 | 4610 |

Comprobación aritmética independiente: 100 × (1 + 2 + … + 9) + 110 = 4500 + 110 = **4610**.

### 9.3 Casos adicionales y validaciones

En la columna «Entradas sucesivas», cada elemento separado por una flecha se captura cuando el programa lo solicita.

| Caso | Entradas sucesivas | Comportamiento esperado del código original |
|---|---|---|
| Primera fila | `F → 0` | Total 1450 |
| Primera columna | `C → 0` | Total 4610 |
| Última fila | `F → 9` | Total 1550 |
| Última columna | `C → 9` | Total 5510 |
| Fila intermedia | `F → 4` | Total 5450 |
| Columna intermedia | `C → 4` | Total 5010 |
| Minúscula | `c → 0` | Se acepta; total 4610 |
| Opción incorrecta | `X → F → 0` | Repite opción; total 1450 tras corregir |
| Índice negativo | `F → -1 → 0` | Repite índice; total 1450 tras corregir |
| Índice mayor que 9 | `C → 10 → 9` | Repite índice; total 5510 tras corregir |
| Opción con espacios | ` F → F → 0` (la primera opción tiene un espacio inicial) | Rechaza la primera opción; acepta la segunda |
| Texto como índice | `F → hola` | Lanza `ValueError`; no calcula un total |
| Decimal como texto | `C → 3.5` | Lanza `ValueError`; no calcula un total |
| Índice vacío | `F → Enter sin escribir` | Lanza `ValueError`; no calcula un total |
| Texto al reintentar | `F → 10 → hola` | Primero repite índice; después lanza `ValueError` |

**Referencia completa de totales comprobados:**

| Índice | Total de fila | Total de columna |
|---:|---:|---:|
| 0 | 1450 | 4610 |
| 1 | 2450 | 4710 |
| 2 | 3450 | 4810 |
| 3 | 4450 | 4910 |
| 4 | 5450 | 5010 |
| 5 | 6450 | 5110 |
| 6 | 7450 | 5210 |
| 7 | 8450 | 5310 |
| 8 | 9450 | 5410 |
| 9 | 1550 | 5510 |

## 10. Desarrollo de la actividad

1. **Predicción individual (15 min).** Escribe el EPS e identifica los valores de cinco celdas, incluyendo `matriz[2][3]`, `matriz[3][2]` y `matriz[9][0]`.
2. **Lectura guiada (20 min).** Describe cada subprograma y traza el orden de llamadas desde `main()`. Señala parámetros, retornos y variables locales.
3. **Recorrido manual (20 min).** Reproduce las pruebas de fila 0 y columna 0. Elabora además una tabla completa para fila 9 o columna 9 con índice variable, valor leído y acumulador.
4. **Ejecución (20 min).** Copia el código íntegro de la sección 14 a un archivo `matriz_sumatorias.py`. Ejecútalo con Python 3. Reinícialo para cada caso y registra al menos ocho pruebas: cuatro válidas, una opción inválida, dos índices fuera del rango y una entrada no numérica.
5. **Explicación (15 min).** Compara predicción y ejecución, explica cualquier diferencia y responde las preguntas de la sección 11.
6. **Extensión opcional (20 min).** En una copia del programa, prueba la mejora de la sección 13. Documenta qué comportamiento cambia.

Para cada prueba ejecutada usa esta plantilla:

| Entradas | Resultado predicho | Resultado observado | ¿Coinciden? | Explicación |
|---|---|---|---|---|
| Completar | Completar | Completar | Sí / No | Completar |

## 11. Preguntas de análisis

1. ¿Por qué una matriz de diez filas utiliza índices del 0 al 9?
2. ¿Qué diferencia hay entre `matriz[2][3]` y `matriz[3][2]`? Indica sus valores.
3. Al sumar la fila 4, ¿qué índice permanece fijo y cuáles son la primera y la última celda visitadas?
4. Al sumar la columna 4, ¿qué cambia en cada iteración?
5. ¿Por qué `suma` se inicializa antes del ciclo? ¿Qué ocurriría si se reiniciara dentro de cada iteración?
6. ¿Por qué las funciones de suma no necesitan dos ciclos anidados?
7. ¿Qué pasaría si se usara `range(11)` en lugar de `range(10)`?
8. ¿Por qué la validación de la opción usa `and` y la del índice usa `or`?
9. ¿Qué devuelve `solicitar_datos()` y cómo recibe esos valores `main()`?
10. ¿Cuál es la diferencia entre `return suma` y `print(suma)` para quien llama a la función?
11. ¿Por qué la columna 0 suma 4610? Explica la contribución de la fila 9.
12. ¿Qué validación falta para que `hola` no termine el programa? ¿Por qué el `while` original no basta?
13. Si la matriz cambiara a 8 × 12, ¿qué límites y recorridos necesitarías revisar?
14. ¿Cómo comprobarías que las sumas de todas las filas y las de todas las columnas acumulan el mismo total?

## 12. Entregables y rúbrica

Entrega:

- Un reporte Markdown o PDF con identificación, EPS, pasos del algoritmo, explicación de índices y respuestas a las preguntas.
- Tres pruebas de escritorio completas: fila 0, columna 0 y fila 9 o columna 9.
- Una tabla con al menos ocho pruebas ejecutadas y evidencia de resultados, incluida la limitación de la entrada no numérica.
- El archivo `matriz_sumatorias.py` con el código base. Si realizas la mejora opcional, entrega una segunda versión e identifica sus cambios.

**Rúbrica: 100 puntos.** El trabajo opcional no es necesario para obtener la calificación máxima.

| Criterio | Valor | Logro completo | Logro parcial | Sin evidencia |
|---|---:|---|---|---|
| EPS y pasos del algoritmo | 20 | 20: identifica datos, validaciones, selección, cálculo y salida en orden | 10: presenta el flujo con omisiones relevantes | 0: no presenta el análisis |
| Indexación y diferencia de recorridos | 20 | 20: explica ambos índices, límites y qué permanece fijo en cada suma | 10: explica solo un recorrido o confunde algún índice | 0: no explica los accesos |
| Funciones y procedimientos | 15 | 15: identifica responsabilidades, parámetros, retornos y coordinación | 8: identifica parcialmente la descomposición | 0: no la analiza |
| Pruebas de escritorio | 20 | 20: entrega tres tablas completas y correctas, con acumuladores y totales | 10: tablas incompletas o con errores de seguimiento | 0: no hay tablas |
| Ejecución y validaciones | 15 | 15: documenta ocho casos requeridos y explica `ValueError` | 8: faltan casos o no explica la limitación | 0: no hay evidencia de ejecución |
| Respuestas y presentación | 10 | 10: responde las preguntas con justificación y entrega archivos legibles | 5: respuestas incompletas o archivos poco claros | 0: no entrega evidencia evaluable |

## 13. Mejora opcional separada: captura robusta

**Esta propuesta no forma parte del código original.** En una copia, sustituye únicamente `solicitar_datos()` por la siguiente versión. Mantiene la elección F/C y el índice 0–9; agrega manejo de entradas no numéricas y elimina espacios externos de la opción.

```python
def solicitar_datos():
    """Solicita una opción F/C y un índice entero entre 0 y 9."""
    print("\n--- MENU DE OPCIONES ---")
    print("[F] - Sumar una Fila")
    print("[C] - Sumar una Columna")

    opcion = input("Ingrese su opción (F/C): ").strip().upper()
    while opcion not in ('F', 'C'):
        opcion = input("Opción inválida. Ingrese F o C: ").strip().upper()

    while True:
        try:
            indice = int(input("Ingrese el número (0 al 9): "))
        except ValueError:
            print("Entrada inválida. Escriba un número entero.")
            continue

        if 0 <= indice <= 9:
            return opcion, indice

        print("Índice inválido. Debe ser entre 0 y 9.")
```

`try/except ValueError` permite volver a pedir el índice cuando falla la conversión; la comprobación posterior controla el rango. Una entrada como `3.5` sigue siendo inválida como entero, pero ahora se informa el problema y se vuelve a solicitar el dato.

**Prueba de la mejora:** introduce ` F ` como opción; después escribe `hola`, `3.5`, una entrada vacía, `-1`, `10` y finalmente `0`. Debe aceptar la opción con espacios, rechazar cada índice inválido sin terminar y producir **1450** al recibir 0.

## 14. Código íntegro suministrado por el usuario

Se normalizaron exclusivamente los escapes de presentación: barras invertidas al final de línea, escapes delante de comentarios y guiones bajos, y entidades HTML de espacios. Se conservaron las instrucciones, comentarios, datos, mensajes y lógica originales, incluidos los usos de `int(input())`. Los escapes `\n` dentro de las cadenas se conservan porque pertenecen al código Python.

```python
# ============================================================
# EJERCICIO: MATRIZ 10x10 Y SUMATORIA DE FILAS / COLUMNAS
# Uso exclusivo de funciones y procedimientos
# ============================================================

# ------------------------------------------------------------
# FUNCIONES (Devuelven datos)
# ------------------------------------------------------------

def definir_matriz():
    """
    FUNCION: Define explícitamente una matriz de 10x10 con números
             de 3 cifras (múltiplos de 10).
    SI devuelve datos (list).
    """
    matriz = [
        [100, 110, 120, 130, 140, 150, 160, 170, 180, 190],
        [200, 210, 220, 230, 240, 250, 260, 270, 280, 290],
        [300, 310, 320, 330, 340, 350, 360, 370, 380, 390],
        [400, 410, 420, 430, 440, 450, 460, 470, 480, 490],
        [500, 510, 520, 530, 540, 550, 560, 570, 580, 590],
        [600, 610, 620, 630, 640, 650, 660, 670, 680, 690],
        [700, 710, 720, 730, 740, 750, 760, 770, 780, 790],
        [800, 810, 820, 830, 840, 850, 860, 870, 880, 890],
        [900, 910, 920, 930, 940, 950, 960, 970, 980, 990],
        [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]
    ]
    return matriz


def solicitar_datos():
    """
    FUNCION: Solicita al usuario si desea sumar una fila o columna
             y el número de la misma (del 0 al 9).
    SI devuelve datos (str, int).
    """
    print("\n--- MENU DE OPCIONES ---")
    print("[F] - Sumar una Fila")
    print("[C] - Sumar una Columna")
    
    opcion = input("Ingrese su opción (F/C): ").upper()
    
    # Validación de la opción
    while opcion != 'F' and opcion != 'C':
        opcion = input("Opción inválida. Ingrese F o C: ").upper()
        
    indice = int(input("Ingrese el número (0 al 9): "))
    
    # Validación del índice
    while indice < 0 or indice > 9:
        indice = int(input("Índice inválido. Debe ser entre 0 y 9: "))
        
    return opcion, indice


def sumar_fila(matriz, num_fila):
    """
    FUNCION: Suma todos los elementos de una fila específica.
    SI devuelve datos (int).
    """
    suma = 0
    for j in range(10):
        suma += matriz[num_fila][j]
    return suma


def sumar_columna(matriz, num_columna):
    """
    FUNCION: Suma todos los elementos de una columna específica.
    SI devuelve datos (int).
    """
    suma = 0
    for i in range(10):
        suma += matriz[i][num_columna]
    return suma


# ------------------------------------------------------------
# PROCEDIMIENTOS (No devuelven datos, solo ejecutan)
# ------------------------------------------------------------

def imprimir_matriz(matriz):
    """
    PROCEDIMIENTO: Imprime la matriz en pantalla sin encabezados.
    NO devuelve datos.
    """
    print("\n=================================================")
    print("                 MATRIZ 10x10                    ")
    print("=================================================\n")
    
    for i in range(10):
        for j in range(10):
            # Imprimimos cada número con un ancho de 4 espacios para alinear
            print(f"{matriz[i][j]:4}", end="  ")
        print()
        
    print("\n=================================================")


def mostrar_resultado(opcion, indice, resultado):
    """
    PROCEDIMIENTO: Muestra el resultado de la sumatoria.
    NO devuelve datos.
    """
    print("\n=================================================")
    if opcion == 'F':
        print(f"RESULTADO: Sumatoria de la Fila {indice}")
    else:
        print(f"RESULTADO: Sumatoria de la Columna {indice}")
    print(f"Total: {resultado}")
    print("=================================================")


def main():
    """
    PROCEDIMIENTO PRINCIPAL: Coordina la ejecución del programa.
    NO devuelve datos.
    """
    # 1. Obtener la matriz predefinida
    matriz = definir_matriz()
    
    # 2. Imprimir la matriz
    imprimir_matriz(matriz)
    
    # 3. Solicitar datos al usuario
    opcion, indice = solicitar_datos()
    
    # 4. Calcular la sumatoria
    if opcion == 'F':
        resultado = sumar_fila(matriz, indice)
    else:
        resultado = sumar_columna(matriz, indice)
        
    # 5. Mostrar el resultado
    mostrar_resultado(opcion, indice, resultado)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
```

## 15. Lista de comprobación antes de entregar

- [ ] Distingo fila y columna mediante la posición de sus índices.
- [ ] Explico el acumulador y las diez iteraciones de cada sumatoria.
- [ ] Mis tablas confirman fila 0 = 1450 y columna 0 = 4610.
- [ ] Conservé los datos de la última fila.
- [ ] Probé límites, opción incorrecta y entrada no numérica.
- [ ] Distingo la validación del rango de la validación de la conversión.
- [ ] Entrego el código base y separo cualquier mejora opcional.

# TC1038 · Actividad académica: Sopa de Letras 15 × 15
## Word Search Puzzle: listas, matrices, funciones y búsqueda rectilínea

**Dirigida a:** estudiantes de ingeniería de nivel introductorio.  
**Modalidad sugerida:** parejas; análisis individual y contraste de resultados.  
**Duración sugerida:** 100–120 minutos.  
**Recursos:** Python 3, editor de texto y terminal. No requiere bibliotecas externas.

## 1. Propósito y resultados de aprendizaje

Una **sopa de letras** se llama en inglés **Word Search Puzzle**, también abreviado *Word Search*. Consiste en localizar secuencias de letras dentro de una cuadrícula.

Al terminar la actividad, el estudiante podrá:

- Formular un análisis de Entrada–Proceso–Salida (EPS).
- Representar una matriz mediante listas anidadas y acceder con `matriz[fila][columna]`.
- Descomponer un problema en funciones, identificar parámetros y valores de retorno.
- Encontrar posiciones iniciales y explorar las ocho celdas vecinas.
- Mantener una dirección constante y controlar los límites de la matriz.
- Justificar resultados con pruebas de escritorio y ejecución del programa.

**Reto:** explicar y ejecutar el programa proporcionado para localizar palabras en una matriz fija de 15 filas y 15 columnas. La validación exige letras consecutivas en una misma línea horizontal, vertical o diagonal.

## 2. Condiciones del problema y fidelidad del código

El código completo de la sección 12 procede del último mensaje del usuario en la conversación de referencia. Únicamente se corrigieron escapes de transcripción: barras invertidas al final de las líneas, escapes delante de `#`, `*` y `_`, y entidades `&#x20;` que representaban espacios. Se conservaron las instrucciones, los comentarios, los mensajes, la matriz y la lógica. Los escapes válidos de Python, como `\n`, permanecen.

**Verificación de las frutas anunciadas:** PERA, KIWI, MORA, LIMON, SANDIA y UVA sí están presentes en la matriz original. No hay discrepancia entre esa lista y las palabras presentes. **UVA tiene dos apariciones**; el programa solo informa la primera que encuentra.

Las búsquedas se realizan con las letras tal como están almacenadas. La matriz usa `LIMON` y `SANDIA`, sin acentos. Escribir `LIMÓN` o `SANDÍA` produce un resultado distinto. La conversión a mayúsculas no elimina acentos ni espacios.

## 3. Análisis EPS

| Elemento | Descripción |
| --- | --- |
| Entrada fija | Matriz predefinida de 15 × 15 con caracteres en mayúsculas. |
| Entrada del usuario | Una palabra escrita como cadena y una respuesta para continuar o terminar. |
| Preparación | Aplicar `upper()` y convertir la palabra con `list()`. |
| Proceso | Reunir todas las coordenadas de la primera letra; examinar ocho vecinos; filtrar por la segunda letra; verificar cada dirección candidata completa sin cambiar de rumbo. |
| Salida de búsqueda | Una tupla de tres elementos: mensaje, dirección y coordenada inicial. |
| Salida en pantalla | Matriz, resultado, dirección y coordenada inicial cuando hay éxito; mensaje de fallo o de entrada vacía cuando corresponde. |
| Repetición | Una nueva búsqueda mientras la respuesta convertida a minúsculas sea exactamente `s`. |

**Ejemplo EPS:** entrada `pera` → lista `['P', 'E', 'R', 'A']` → búsqueda → resultado `("Encontrada", "Derecha", [1, 1])`. La interfaz imprime la coordenada como `[1][1]`.

El programa acepta cualquier secuencia introducida; no restringe la búsqueda a las frutas del encabezado.

## 4. Listas, matriz y coordenadas

Una lista es una colección ordenada y modificable. Se declara entre corchetes; por ejemplo, `letras = ['P', 'E', 'R', 'A']`. La matriz es una lista cuyas 15 entradas son, a su vez, listas de 15 caracteres.

Los índices empiezan en **0** y terminan en **14**:

- `matriz[0][0]`: primera fila, primera columna; contiene `Q`.
- `matriz[1][1]`: segunda fila, segunda columna; contiene `P`.
- `[fila, columna]`: una lista que guarda una posición.
- `matriz[fila][columna]`: acceso al carácter en esa posición.

La fila crece hacia abajo y la columna hacia la derecha. Para convertir a numeración humana de 1 a 15, se suma 1 a cada índice: `[1][1]` corresponde a fila 2, columna 2. Todas las coordenadas de este documento utilizan índices de Python.

### Las ocho direcciones

La pareja `(df, dc)` indica el cambio de fila y columna por cada letra. Se exploran en el orden exacto del programa:

| Orden | Dirección | df | dc |
| --- | --- | ---: | ---: |
| 1 | Arriba-Izquierda | -1 | -1 |
| 2 | Arriba | -1 | 0 |
| 3 | Arriba-Derecha | -1 | 1 |
| 4 | Izquierda | 0 | -1 |
| 5 | Derecha | 0 | 1 |
| 6 | Abajo-Izquierda | 1 | -1 |
| 7 | Abajo | 1 | 0 |
| 8 | Abajo-Derecha | 1 | 1 |

Representación de los vecinos de una celda central:

```text
(f-1,c-1)  (f-1,c)  (f-1,c+1)
(f,  c-1)  (f,  c)  (f,  c+1)
(f+1,c-1)  (f+1,c)  (f+1,c+1)
```

El movimiento `(0, 0)` se excluye porque repetiría la misma celda. Los ocho vecinos constituyen una vecindad de ocho posiciones; aquí no se calcula una distancia ni se elige un único vecino por proximidad.

Para la letra de índice `k`, partiendo del origen `(f0, c0)`:

```text
fila(k)    = f0 + k * df
columna(k) = c0 + k * dc
```

Durante una verificación, `df` y `dc` permanecen constantes. Antes de acceder a cada celda, se exige `0 <= fila < 15` y `0 <= columna < 15`. Esto también impide que los índices negativos de Python accedan por accidente al final de una lista.

## 5. Procedimiento detallado de búsqueda

1. **Crear e imprimir la matriz.** Se muestra el tablero y se conserva la lista anidada devuelta.
2. **Solicitar la palabra.** Se lee una cadena, se convierte a mayúsculas y después a lista. No se aplica `strip()`.
3. **Atender la entrada vacía.** La función de búsqueda devuelve `("Palabra vacía", "", [])` si recibe una lista vacía. En la interacción normal, `main()` detecta este caso antes de llamarla.
4. **Identificar letras iniciales.** La primera letra es `palabra[0]`; la segunda es `palabra[1]` si existe.
5. **Reunir todos los orígenes posibles.** Se recorre la matriz por filas y, dentro de cada fila, por columnas. Cada aparición de la primera letra se agrega como `[fila, columna]`.
6. **Probar cada origen en ese orden.** Si la palabra tiene una sola letra, basta con encontrarla; se devuelve su primera aparición y una dirección no específica.
7. **Examinar los ocho movimientos.** Se calcula la coordenada del vecino desde el origen, se comprueba que esté dentro del tablero y se compara su contenido con la segunda letra.
8. **Verificar la dirección candidata.** Si el vecino coincide, se llama a `verificar_direccion()` con el origen y el movimiento. Aunque su comentario habla del “resto de la palabra”, la función compara **toda la palabra desde la primera letra**.
9. **Avanzar en línea recta.** Para cada letra se comprueban límites y coincidencia; luego se suman `df` y `dc`. Una diferencia o una salida del tablero devuelve `False`.
10. **Retomar el origen tras un intento fallido.** Se prueba el siguiente movimiento desde `fila_origen` y `col_origen`. Si ninguno funciona, se pasa al siguiente origen posible. No se cambia de rumbo a mitad de la palabra.
11. **Terminar al primer éxito.** Se devuelve mensaje, nombre de dirección y posición inicial. Si se agotan todos los intentos, se devuelve `("No encontrada", "", [])`.
12. **Mostrar el resultado y decidir si se repite.** Solo una respuesta equivalente a `s` tras `lower()` continúa el ciclo.

**¿Cómo “regresa” al origen?** No se desplaza un cursor dentro de la matriz ni se modifica el tablero. Las variables de fila y columna que avanza `verificar_direccion()` son locales a esa llamada. El origen permanece disponible en la función que coordina la búsqueda.

**Regla de validez:** que la segunda letra sea vecina solo identifica una dirección candidata; no demuestra que la palabra completa exista. Si varios vecinos coinciden con la segunda letra, deben probarse hasta encontrar un éxito o agotar las opciones.

## 6. Funciones y flujo del programa

| Función | Parámetros | Retorno | Responsabilidad |
| --- | --- | --- | --- |
| `crear_e_imprimir_matriz()` | Ninguno | Lista de listas | Construye, imprime y devuelve el tablero. |
| `solicitar_palabra()` | Ninguno | Lista de caracteres | Lee una cadena y aplica `list(palabra_str.upper())`. |
| `buscar_todas_las_coincidencias(matriz, letra)` | Tablero y carácter | Lista de coordenadas | Obtiene todos los posibles orígenes en orden por filas. |
| `verificar_direccion(matriz, palabra, fila, col, df, dc)` | Tablero, lista, origen y movimiento | Booleano | Comprueba toda la secuencia en una dirección fija. |
| `buscar_palabra_en_sopa(matriz, palabra)` | Tablero y lista de caracteres | Tupla: `str, str, list` | Coordina orígenes y direcciones; devuelve el primer éxito. |
| `main()` | Ninguno | `None` implícito | Coordina la interacción y las búsquedas sucesivas. |

En Python todas estas definiciones son funciones. Aunque el comentario original llama “PROCEDIMIENTO” a `crear_e_imprimir_matriz()`, esta sí devuelve un valor. En `main()`, la asignación `resultado, direccion, coordenadas = ...` desempaqueta los tres elementos de una tupla.

`enumerate(movimientos)` aporta el índice y el movimiento: ese índice permite consultar el nombre correspondiente en `nombres_dir`. Las dos listas deben conservar el mismo orden.

La condición `if __name__ == "__main__":` inicia la interacción cuando el archivo se ejecuta directamente. Al importarlo para probar sus funciones, no se inicia el ciclo de preguntas.

## 7. Pruebas de escritorio y resultados verificados

Se ejecutó el código recuperado y se contrastaron las frutas mediante un recorrido independiente de las 225 celdas en las ocho direcciones. Se verificó que el tablero contiene exactamente 15 filas de 15 caracteres.

### 7.1 Frutas anunciadas

| Palabra | Resultado | Inicio | Dirección devuelta | Final |
| --- | --- | --- | --- | --- |
| PERA | Encontrada | [1][1] | Derecha | [1][4] |
| KIWI | Encontrada | [3][5] | Abajo | [6][5] |
| MORA | Encontrada | [2][10] | Abajo-Derecha | [5][13] |
| LIMON | Encontrada | [8][2] | Derecha | [8][6] |
| SANDIA | Encontrada | [6][12] | Abajo | [11][12] |
| UVA | Encontrada | [7][10] | Derecha | [7][12] |

La coordenada final se calculó para documentar la prueba; el programa original solo devuelve la inicial.

**Segunda aparición de UVA:** `[11][4] → [12][5] → [13][6]`, dirección Abajo-Derecha. El recorrido encuentra antes el origen `[7][10]`, por lo que no llega a devolver esta segunda aparición. Las otras cinco frutas tienen una aparición cada una en las ocho direcciones verificadas.

### 7.2 Traza de PERA: descartar un origen y continuar

Las posiciones de `P`, en el orden que devuelve la función, son:

```text
[0,9], [1,1], [3,0], [3,12], [6,6], [7,5], [9,5], [11,5], [14,0]
```

En `[0][9]`, las direcciones hacia arriba salen de la matriz. Los vecinos válidos contienen `O`, `A`, `G`, `J` y `K`; ninguno es `E`. Se descarta ese origen.

En `[1][1]`, el vecino de la derecha es `E`. Se verifica el movimiento `(0, 1)`:

| k | Letra esperada | Coordenada | Letra en matriz | Resultado |
| --- | --- | --- | --- | --- |
| 0 | P | [1][1] | P | Coincide |
| 1 | E | [1][2] | E | Coincide |
| 2 | R | [1][3] | R | Coincide |
| 3 | A | [1][4] | A | Coincide |

### 7.3 Traza de MORA: dirección diagonal

Con origen `[2][10]` y movimiento `(1, 1)`, se leen `M` en `[2][10]`, `O` en `[3][11]`, `R` en `[4][12]` y `A` en `[5][13]`. Se conservan ambos incrementos durante toda la verificación.

### 7.4 Cobertura de las ocho direcciones en la matriz original

Estas son **secuencias de prueba**, no frutas añadidas al enunciado. Cada una comienza en `[7][7]`; el programa devuelve `Encontrada` con esa coordenada y la dirección indicada.

| Secuencia | Movimiento | Dirección | Final |
| --- | --- | --- | --- |
| RPWCJ | (-1, -1) | Arriba-Izquierda | [3][3] |
| RAJZF | (-1, 0) | Arriba | [3][7] |
| RSLJO | (-1, 1) | Arriba-Derecha | [3][11] |
| RQPON | (0, -1) | Izquierda | [7][3] |
| RSTUV | (0, 1) | Derecha | [7][11] |
| RNPGO | (1, -1) | Abajo-Izquierda | [11][3] |
| RQSSK | (1, 0) | Abajo | [11][7] |
| RWFWF | (1, 1) | Abajo-Derecha | [11][11] |

### 7.5 Casos límite y de entrada

| Entrada o llamada | Resultado verificado | Interpretación |
| --- | --- | --- |
| `pera` mediante la interfaz | Encontrada, Derecha, [1][1] | `upper()` convierte la entrada. |
| `AREP` | Encontrada, Izquierda, [1][4] | Se permite leer una secuencia en sentido inverso. |
| `Q` | Encontrada, “Cualquiera (es de 1 letra)”, [0][0] | No requiere segunda letra. |
| `Ñ` | No encontrada, dirección vacía, coordenadas [] | No existen orígenes posibles. |
| Cadena vacía mediante la interfaz | “No se ingresó ninguna palabra.” | `main()` no llama a la búsqueda. |
| Lista vacía enviada directamente a la búsqueda | (“Palabra vacía”, “”, []) | Protección interna de la función. |
| ` PERA ` | No encontrada | Los espacios forman parte de la entrada. |
| `LIMÓN` | No encontrada | La tilde se conserva. |
| `SANDÍA` | No encontrada | La matriz contiene I sin tilde. |
| `QWERTYUIOPASDFG` | Encontrada, Derecha, [0][0] | Coincide con la fila superior completa. |
| `QWERTYUIOPASDFGA` | No encontrada | La continuación saldría de la matriz. |

**Intento fallido en una dirección válida:** para `PERX` desde `[1][1]` hacia la derecha, coinciden P, E y R; se espera X en `[1][4]`, pero hay A. `verificar_direccion()` devuelve `False`. El resultado global también es “No encontrada”.

## 8. Instrucciones para los alumnos

1. **Antes de ejecutar (15 min).** Lean el problema y completen su propia tabla EPS. Predigan los resultados de PERA, MORA y UVA e identifiquen qué datos debe devolver la búsqueda.
2. **Representación (15 min).** Dibujen una cuadrícula con índices 0–14. Marquen las coordenadas iniciales y finales de las seis frutas. Expliquen la diferencia entre `[fila, columna]` y `matriz[fila][columna]`.
3. **Análisis de funciones (20 min).** Construyan un esquema de llamadas desde `main()`; señalen parámetros, retornos, variables locales y condición de salida del ciclo.
4. **Búsqueda por vecinos (20 min).** Reproduzcan la traza de PERA, documenten el intento PERX y elaboren una traza propia de KIWI o SANDIA. Incluyan letra esperada, coordenada, letra observada y decisión.
5. **Ejecución y contraste (20 min).** Copien únicamente el bloque Python de la sección 12 en un archivo `sopa_de_letras.py` guardado como UTF-8 y ejecútenlo con `python3 sopa_de_letras.py` (o `python sopa_de_letras.py`, si ese comando corresponde a Python 3). Reproduzcan las pruebas de la sección 7, incluida la cobertura de ocho direcciones. Registren predicción, resultado real y explicación de cualquier diferencia.
6. **Discusión y entrega (10–20 min).** Respondan las preguntas de la sección 10 y presenten evidencia suficiente para que otra pareja pueda reproducir sus conclusiones.

No modifiquen la matriz ni la lógica en la entrega base. Si realizan una extensión opcional, colóquenla en otro archivo e identifiquen con claridad sus cambios.

**Entregables:**

- Reporte con integrantes, EPS, esquema de funciones, tabla de direcciones y trazas.
- Tabla de pruebas con resultados esperados y observados, incluyendo UVA, entrada vacía, una letra, espacios, tilde y límites.
- Código base ejecutado y evidencia de al menos una búsqueda exitosa y una fallida.
- Respuestas justificadas a las preguntas de análisis.

## 9. Criterios de evaluación

| Criterio | Puntos | Evidencia esperada |
| --- | ---: | --- |
| Análisis EPS | 15 | Distingue entradas, procesamiento, retornos e interacción. |
| Matriz y coordenadas | 15 | Usa índices 0–14, orden fila/columna y límites correctamente. |
| Vecinos y dirección rectilínea | 25 | Explica las ocho direcciones, el filtro de segunda letra y la reanudación desde el origen. |
| Funciones y flujo | 15 | Relaciona parámetros, retornos y llamadas; explica el primer éxito. |
| Pruebas y contraste | 20 | Resultados reproducibles, casos límite y ambas apariciones de UVA. |
| Claridad y fidelidad | 10 | Código íntegro, explicación propia y respuestas fundamentadas. |
| **Total** | **100** | |

Para cada criterio: evidencia completa y correcta obtiene el total; evidencia correcta pero incompleta obtiene aproximadamente la mitad; ausencia de evidencia o explicación incompatible con el código obtiene cero. El docente puede asignar valores intermedios según la calidad de la justificación.

## 10. Preguntas de análisis

1. ¿Por qué se recopilan todas las apariciones de la primera letra en lugar de usar solo la primera?
2. ¿Por qué encontrar la segunda letra en un vecino no garantiza encontrar toda la palabra?
3. ¿Qué impide que el algoritmo gire después de encontrar la segunda letra?
4. ¿Qué ocurre si dos vecinos contienen la segunda letra y solo el segundo conduce a la palabra completa?
5. ¿Qué variables preservan el origen y cuáles cambian durante la verificación?
6. ¿Qué error lógico podría provocar un índice negativo si no se comprobara el límite inferior?
7. ¿Por qué UVA devuelve [7][10] y no [11][4]? ¿Qué efecto tendría cambiar el orden de recorrido?
8. ¿En qué se diferencia buscar una letra, una cadena vacía y una palabra cuya inicial no aparece?
9. ¿Por qué “pera” funciona y “ PERA ” o “LIMÓN” no producen el mismo resultado?
10. ¿Qué devuelve realmente cada función? ¿Coinciden todos los comentarios originales con su comportamiento exacto?
11. ¿Qué modificaciones serían necesarias para devolver todas las apariciones sin detenerse en el primer éxito?
12. ¿Por qué cambiar el tamaño de la matriz requiere revisar los valores fijos `15` del programa?

**Profundización:** si el tablero tuviera R filas, C columnas y la palabra L letras, el recorrido inicial cuesta O(R·C). Si hay K orígenes candidatos, se prueban hasta ocho direcciones de hasta L letras: O(R·C + 8·K·L), que en el peor caso se expresa como O(R·C·L). La lista de orígenes requiere O(K) espacio adicional.

## 11. Observaciones y extensiones opcionales

El programa está preparado para un tablero fijo de 15 × 15. No valida dimensiones arbitrarias; no elimina espacios o tildes; devuelve solo una coincidencia; y no informa la coordenada final ni el recorrido completo. Son características del código conservado, no correcciones aplicadas.

Se propone, únicamente como trabajo adicional:

- Calcular dimensiones con `len()` y validar que la matriz sea rectangular.
- Definir explícitamente una política para espacios y acentos.
- Devolver todas las coincidencias y sus recorridos.
- Mostrar coordenadas de 1 a 15 sin modificar los índices internos.
- Comparar los resultados de la extensión con los de la versión base.

## 12. Código Python original completo

El siguiente bloque conserva la lógica original; solo se repararon los escapes de la transcripción descritos en la sección 2.

```python
# ============================================================
# PROYECTO FINAL: SOPA DE LETRAS 15x15
# Búsqueda con lógica de vecinos, direcciones y coordenadas
# ============================================================

def crear_e_imprimir_matriz():
    """
    PROCEDIMIENTO: Crea la matriz predefinida de 15x15, la imprime
    en pantalla y la devuelve para su uso posterior.
    """
    matriz = [
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G'],
        ['H', 'P', 'E', 'R', 'A', 'S', 'D', 'F', 'G', 'J', 'K', 'L', 'Z', 'X', 'C'],
        ['C', 'V', 'B', 'N', 'M', 'Q', 'W', 'E', 'R', 'T', 'M', 'Y', 'U', 'I', 'O'],
        ['P', 'L', 'K', 'J', 'H', 'K', 'G', 'F', 'D', 'S', 'A', 'O', 'P', 'A', 'S'],
        ['M', 'N', 'B', 'V', 'C', 'I', 'X', 'Z', 'L', 'K', 'J', 'H', 'R', 'F', 'D'],
        ['A', 'S', 'D', 'F', 'G', 'W', 'H', 'J', 'K', 'L', 'Q', 'W', 'E', 'A', 'R'],
        ['T', 'Y', 'U', 'I', 'O', 'I', 'P', 'A', 'S', 'D', 'F', 'G', 'S', 'H', 'J'],
        ['K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'A', 'W', 'X'],
        ['Z', 'X', 'L', 'I', 'M', 'O', 'N', 'Q', 'W', 'A', 'E', 'R', 'N', 'T', 'Y'],
        ['T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'D', 'J', 'K'],
        ['L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Q', 'W', 'E', 'I', 'R', 'T'],
        ['Y', 'U', 'I', 'O', 'U', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'A', 'M', 'B'],
        ['V', 'C', 'X', 'Z', 'A', 'V', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M'],
        ['N', 'B', 'V', 'C', 'X', 'Z', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'W', 'Q', 'A', 'S', 'D', 'F', 'G']
    ]

    print("=================================================")
    print("                 SOPA DE LETRAS                  ")
    print("=================================================")
    print("Frutas a buscar: PERA, KIWI, MORA, LIMON, SANDIA, UVA")
    print("=================================================\n")
    
    for i in range(15):
        for j in range(15):
            print(matriz[i][j], end="  ")
        print()
    print("\n=================================================")
    
    return matriz


def solicitar_palabra():
    """
    FUNCION: Solicita al usuario una palabra y la convierte en una lista.
    SI devuelve datos (list).
    """
    palabra_str = input("\nIngrese la palabra a buscar (ej. PERA): ")
    palabra_lista = list(palabra_str.upper())
    return palabra_lista


def buscar_todas_las_coincidencias(matriz, letra):
    """
    FUNCION: Busca todas las apariciones de una letra en la matriz.
    SI devuelve datos (list de listas).
    """
    coordenadas = []
    for i in range(15):
        for j in range(15):
            if matriz[i][j] == letra:
                coordenadas.append([i, j])
    return coordenadas


def verificar_direccion(matriz, palabra, fila, col, df, dc):
    """
    FUNCION: Verifica si el resto de la palabra coincide en una dirección dada.
    SI devuelve datos (bool).
    """
    for i in range(len(palabra)):
        if fila < 0 or fila >= 15 or col < 0 or col >= 15:
            return False
        if matriz[fila][col] != palabra[i]:
            return False
        fila += df
        col += dc
    return True


def buscar_palabra_en_sopa(matriz, palabra):
    """
    FUNCION: Orquesta la búsqueda aplicando la lógica de vecinos.
    SI devuelve datos (str, str, list). (Mensaje, Dirección, Coordenadas)
    """
    if len(palabra) == 0:
        return "Palabra vacía", "", []

    primera_letra = palabra[0]
    segunda_letra = palabra[1] if len(palabra) > 1 else None

    posiciones_iniciales = buscar_todas_las_coincidencias(matriz, primera_letra)

    movimientos = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    nombres_dir = [
        "Arriba-Izquierda", "Arriba", "Arriba-Derecha",
        "Izquierda", "Derecha",
        "Abajo-Izquierda", "Abajo", "Abajo-Derecha"
    ]

    for pos in posiciones_iniciales:
        fila_origen = pos[0]
        col_origen = pos[1]

        if segunda_letra is None:
            return "Encontrada", "Cualquiera (es de 1 letra)", pos

        for idx, mov in enumerate(movimientos):
            df = mov[0]
            dc = mov[1]
            fila_vecino = fila_origen + df
            col_vecino = col_origen + dc

            if 0 <= fila_vecino < 15 and 0 <= col_vecino < 15:
                if matriz[fila_vecino][col_vecino] == segunda_letra:
                    if verificar_direccion(matriz, palabra, fila_origen, col_origen, df, dc):
                        # Si se encuentra, devolvemos también la coordenada 'pos'
                        return "Encontrada", nombres_dir[idx], pos

    return "No encontrada", "", []


def main():
    """
    FUNCION PRINCIPAL: Coordina la ejecución del programa.
    """
    matriz_sopa = crear_e_imprimir_matriz()
    
    while True:
        palabra = solicitar_palabra()
        
        if len(palabra) > 0:
            print("\nBuscando la palabra:", palabra)
            
            # Ahora recibimos 3 valores de la función
            resultado, direccion, coordenadas = buscar_palabra_en_sopa(matriz_sopa, palabra)
            
            if resultado == "Encontrada":
                print("\n[EXITO] ¡La palabra '" + "".join(palabra) + "' fue encontrada!")
                print("Se lee en dirección:", direccion)
                # Imprimimos las coordenadas con el formato solicitado
                print("Coordenada inicial: [" + str(coordenadas[0]) + "][" + str(coordenadas[1]) + "]")
            else:
                print("\n[FALLO] La palabra '" + "".join(palabra) + "' no está en la sopa de letras.")
        else:
            print("\nNo se ingresó ninguna palabra.")
            
        continuar = input("\n¿Desea buscar otra palabra? (s/n): ").lower()
        if continuar != 's':
            print("\nGracias por jugar a la sopa de letras. ¡Hasta luego!")
            break
        print("\n" + "="*50)

if __name__ == "__main__":
    main()
```

## 13. Control de verificación del material

- Archivo Markdown guardado en UTF-8, con el código completo en un bloque Python.
- Código extraído del documento comprobado sintácticamente y comparado con la versión recuperada tras corregir escapes.
- Matriz de 15 × 15 comprobada en ejecución.
- Seis frutas contrastadas con una búsqueda independiente de todas sus apariciones.
- Ocho direcciones probadas sobre la matriz original.
- Casos de entrada y límites contrastados mediante funciones e interacción simulada.
- Sin cambios en la matriz, mensajes o lógica del programa proporcionado.


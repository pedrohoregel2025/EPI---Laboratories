# TC1038 — Apunte: generación de una sopa de letras de 15 × 15 en Python

## 1. Descripción general

El programa construye e imprime una **sopa de letras**, conocida en inglés como *word search* o *word search puzzle*. Utiliza una matriz de 15 filas y 15 columnas, coloca seis nombres de frutas en posiciones aleatorias y rellena los espacios restantes con letras mayúsculas.

Las palabras son **PERA, KIWI, MORA, LIMON, PLATANO y UVA**. Sus posiciones y direcciones se eligen mediante el módulo `random`. La colocación permite tres sentidos: hacia la derecha, hacia abajo y en diagonal hacia abajo y a la derecha.

El código genera el tablero y muestra la lista de frutas; no solicita palabras al usuario ni implementa un algoritmo para buscarlas. Además, comprueba que cada palabra quepa en el tablero, pero **no comprueba si las celdas ya contienen otras palabras**. Por ello, una inserción posterior puede sobrescribir letras de una anterior y el tablero final no garantiza que todas las frutas anunciadas sigan presentes.

## 2. Organización y flujo del programa

El archivo importa `random`, define `main()` y termina con el punto de entrada:

```python
if __name__ == "__main__":
    main()
```

Cuando el archivo se ejecuta directamente, `__name__` vale `"__main__"` y se llama a `main()`. Si se importa como módulo, esta condición evita ejecutar automáticamente la generación del tablero.

Toda la lógica se encuentra dentro de `main()`, organizada en cinco etapas:

1. Crear una matriz con 225 espacios en blanco.
2. Definir la lista de palabras.
3. Intentar colocar cada palabra en una posición y dirección aleatorias hasta que quepa.
4. Sustituir los espacios restantes por letras aleatorias.
5. Imprimir el encabezado y la matriz.

Desde la distinción didáctica entre función y procedimiento, `main()` actúa como un **procedimiento principal**: realiza acciones y muestra información, sin un `return` explícito. En Python se define como una función mediante `def` y devuelve implícitamente `None`. La matriz es una variable local y no se devuelve al finalizar.

## 3. Datos de entrada, proceso y salida

| Elemento | Descripción |
|---|---|
| Datos internos | Dimensiones 15 × 15, lista de seis frutas y abecedario de 26 letras |
| Entrada por teclado | No existe; el programa no utiliza `input()` |
| Selecciones aleatorias | Fila inicial, columna inicial, dirección y letras de relleno |
| Proceso | Construir la matriz, insertar palabras que quepan y rellenar celdas vacías |
| Salida | Encabezado, lista de frutas y tablero de 15 filas con 15 letras cada una |

El tablero puede cambiar entre ejecuciones. Como la aleatoriedad no obliga a obtener resultados diferentes, también es posible repetir una selección o incluso un resultado.

## 4. Creación de la matriz e indexación

Una matriz se representa aquí como una **lista de listas**. La lista exterior contiene las filas y cada lista interior contiene las celdas de una fila.

```python
matriz = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(" ")
    matriz.append(fila)
```

El ciclo exterior se repite 15 veces. En cada repetición crea una nueva lista `fila`. El ciclo interior agrega 15 cadenas de un espacio (`" "`) mediante `append()`. Después, la fila completa se agrega a `matriz`.

Crear `fila = []` dentro del ciclo exterior hace que cada fila sea una lista independiente. Al terminar, existen 15 filas de 15 elementos: **225 celdas**. Los espacios sirven como marca de celda vacía.

El acceso tiene la forma `matriz[fila][columna]`:

| Expresión | Posición |
|---|---|
| `matriz[0][0]` | Esquina superior izquierda |
| `matriz[0][14]` | Esquina superior derecha |
| `matriz[14][0]` | Esquina inferior izquierda |
| `matriz[14][14]` | Esquina inferior derecha |

Los índices van de **0 a 14**. `range(15)` recorre esos valores y excluye el 15. Al aumentar el primer índice se avanza hacia abajo; al aumentar el segundo, hacia la derecha. Las letras `i` y `j` son nombres de variables, no instrucciones especiales de Python.

## 5. Lista de palabras y variables de control

```python
palabras = ["PERA", "KIWI", "MORA", "LIMON", "PLATANO", "UVA"]
```

El ciclo `for palabra in palabras` procesa las frutas **en el orden de la lista**. Lo aleatorio es su posición y dirección, no el orden de procesamiento.

| Variable | Función |
|---|---|
| `longitud` | Guarda `len(palabra)`, la cantidad de letras de la fruta actual |
| `colocada` | Indica si la palabra actual ya se escribió en una posición que cabe |
| `fila_aleatoria` | Fila inicial del intento |
| `columna_aleatoria` | Columna inicial del intento |
| `direccion` | Selecciona una de las tres orientaciones |

Cada palabra comienza con `colocada = False`. El ciclo `while not colocada` sigue haciendo intentos mientras esa variable sea falsa. Tras una inserción válida se asigna `True`, lo que permite salir del `while` y pasar a la siguiente fruta.

## 6. Uso del módulo `random`

| Expresión | Resultado posible |
|---|---|
| `random.randint(0, filas - 1)` | Entero de 0 a 14 para la fila inicial |
| `random.randint(0, columnas - 1)` | Entero de 0 a 14 para la columna inicial |
| `random.randint(0, 2)` | Entero 0, 1 o 2 para la dirección |
| `random.choice(abecedario)` | Un carácter tomado del abecedario |

`randint(a, b)` incluye ambos extremos; en cambio, `range(b)` excluye su límite superior. Esta diferencia explica el uso de `filas - 1` y `columnas - 1` al elegir coordenadas.

`random` produce valores pseudoaleatorios. El código no fija una semilla. Para una demostración reproducible se podría establecer una semilla con `random.seed(...)`, como modificación separada del original.

## 7. Colocación de las palabras y validación de límites

Para una palabra de longitud **L** que comienza en **(f, c)**, las celdas se recorren usando `i` desde 0 hasta L − 1:

| Dirección | Valor | Celda de la letra `i` | Última celda | Condición para que quepa |
|---|---:|---|---|---|
| Horizontal a la derecha | 0 | `[f][c + i]` | `[f][c + L - 1]` | `c + L <= columnas` |
| Vertical hacia abajo | 1 | `[f + i][c]` | `[f + L - 1][c]` | `f + L <= filas` |
| Diagonal abajo-derecha | 2 | `[f + i][c + i]` | `[f + L - 1][c + L - 1]` | Se cumplen ambas condiciones anteriores |

### Horizontal

La fila permanece fija y aumenta la columna:

```python
matriz[fila_aleatoria][columna_aleatoria + i] = palabra[i]
```

Por ejemplo, **PERA** desde `[2][10]` ocupa `[2][10]`, `[2][11]`, `[2][12]` y `[2][13]`. Cabe porque 10 + 4 ≤ 15.

### Vertical

La columna permanece fija y aumenta la fila:

```python
matriz[fila_aleatoria + i][columna_aleatoria] = palabra[i]
```

Por ejemplo, **KIWI** desde `[10][3]` termina en `[13][3]`. Cabe porque 10 + 4 ≤ 15.

### Diagonal

Ambos índices aumentan en cada paso:

```python
matriz[fila_aleatoria + i][columna_aleatoria + i] = palabra[i]
```

Por ejemplo, **UVA** desde `[12][12]` ocupa `[12][12]`, `[13][13]` y `[14][14]`. Cabe porque 12 + 3 ≤ 15 en las dos dimensiones.

### Por qué se usa `inicio + longitud <= límite`

La última posición es `inicio + longitud - 1`. Para mantenerla dentro de la matriz debe ser menor o igual a 14. Por eso, para una dimensión de 15 celdas:

`inicio + longitud - 1 <= 14` equivale a `inicio + longitud <= 15`.

Una palabra de cuatro letras que empieza en la columna 11 termina exactamente en la 14 y sí cabe. Si empieza en la 12, intentaría terminar en la 15 y se rechaza antes de escribirla.

Si un intento no cabe, no se escribe ninguna letra y `colocada` sigue siendo falsa. La siguiente vuelta del `while` genera nuevamente **la fila, la columna y la dirección**. No se conserva la posición anterior ni se revisan sistemáticamente todas las posibilidades.

## 8. Alcance de las comprobaciones: posibles sobrescrituras

Las condiciones del programa verifican los bordes del tablero, pero no revisan el contenido de las celdas de destino. Las asignaciones escriben las nuevas letras aunque ya haya otras.

Un ejemplo posible ilustra el efecto:

1. Se inserta **PERA** horizontalmente desde `[0][0]`: P en `[0][0]`, E en `[0][1]`, R en `[0][2]` y A en `[0][3]`.
2. Posteriormente se inserta **KIWI** verticalmente desde `[0][1]`.
3. La K reemplaza la E de `[0][1]`; esa aparición de PERA queda alterada como **PKRA**.

Ambas colocaciones cumplen los límites. Por tanto, `colocada = True` significa que la escritura de la palabra actual se completó, **no que todas las palabras anteriores sigan intactas**. Un cruce con letras iguales no produce ese conflicto; uno con letras distintas sí.

La lista impresa de frutas es fija y no se contrasta con el tablero final. Puede anunciar una palabra cuya colocación original fue dañada. También pueden aparecer otras palabras por coincidencia en el relleno.

Como mejora conceptual, antes de insertar una palabra se podrían revisar **todas** sus celdas y aceptar únicamente espacios vacíos o letras iguales a las que se desean colocar. Si alguna celda entra en conflicto, se rechazaría el intento completo sin modificar el tablero. Esta comprobación no está implementada en el código original.

## 9. Relleno con letras aleatorias

Una vez procesadas las frutas, dos ciclos recorren las 225 celdas:

```python
if matriz[i][j] == " ":
    matriz[i][j] = random.choice(abecedario)
```

Solo se reemplazan los espacios. Las letras ya escritas durante la colocación se conservan en esta etapa. El relleno, por tanto, no causa las sobrescrituras descritas ni repara las que ocurrieron antes.

El abecedario contiene las 26 letras de A a Z; no incluye Ñ ni vocales acentuadas. Las palabras están escritas en mayúsculas y sin acentos, de forma consistente con ese conjunto.

## 10. Impresión del tablero

El encabezado se muestra con varias llamadas a `print()`. Después, un ciclo exterior recorre las filas y uno interior recorre sus columnas:

```python
print(matriz[i][j], end="  ")
```

El argumento `end="  "` coloca dos espacios después de cada letra en lugar del salto de línea habitual. Cuando termina una fila, `print()` sin argumentos produce el salto de línea. Así se muestran 15 renglones de 15 letras.

La secuencia `\n` dentro de una cadena también produce un salto de línea. El programa no imprime coordenadas ni guarda las posiciones de las frutas en una estructura adicional.

## 11. Consideraciones sobre repetición y alcance

- **Tres sentidos de colocación.** No se generan palabras hacia la izquierda, hacia arriba ni en las otras diagonales; tampoco se cambia de dirección a mitad de una palabra.
- **Cantidad de letras objetivo.** Las longitudes suman 28 letras: 4 + 4 + 4 + 5 + 7 + 3. Esto no implica ocupar 28 celdas distintas, porque puede haber superposiciones.
- **Número variable de intentos.** La creación, el relleno y la impresión tienen recorridos definidos. La colocación depende de cuántos intentos aleatorios se rechacen.
- **Sin límite de reintentos.** Para las frutas actuales existen posiciones válidas y se espera que se coloquen, pero no hay un máximo de intentos que garantice terminar en una cantidad fija de pasos.
- **Palabras demasiado largas.** Si se agregara una palabra de más de 15 letras, ninguna de las tres direcciones permitiría colocarla y el `while` no terminaría. El programa no detecta este caso.
- **Generación sin búsqueda.** No hay captura de respuestas, verificación de aciertos ni solución automática de la sopa de letras.

## 12. Código completo proporcionado

Se reproduce a continuación el código suministrado, conservando sus datos, comentarios y lógica. Las posibles mejoras mencionadas en el apunte no se incorporan a esta versión.

```python
# ============================================================
# SOPA DE LETRAS 15x15 - CON POSICIONES ALEATORIAS
# ============================================================
import random

def main():
    filas = 15
    columnas = 15
    
    # 1. Crear matriz vacía
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(" ")
        matriz.append(fila)
        
    # 2. Definir las palabras
    palabras = ["PERA", "KIWI", "MORA", "LIMON", "PLATANO", "UVA"]
    
    # 3. Colocar cada palabra aleatoriamente
    for palabra in palabras:
        longitud = len(palabra)
        colocada = False
        
        # El ciclo while se repite hasta que la palabra se coloque con éxito
        while not colocada:
            # Generar posición y dirección aleatoria (0=Horizontal, 1=Vertical, 2=Diagonal)
            fila_aleatoria = random.randint(0, filas - 1)
            columna_aleatoria = random.randint(0, columnas - 1)
            direccion = random.randint(0, 2)
            
            # Validar si la palabra cabe en la matriz según su dirección
            if direccion == 0: # Horizontal
                if columna_aleatoria + longitud <= columnas:
                    for i in range(longitud):
                        matriz[fila_aleatoria][columna_aleatoria + i] = palabra[i]
                    colocada = True
                    
            elif direccion == 1: # Vertical
                if fila_aleatoria + longitud <= filas:
                    for i in range(longitud):
                        matriz[fila_aleatoria + i][columna_aleatoria] = palabra[i]
                    colocada = True
                    
            elif direccion == 2: # Diagonal
                if (fila_aleatoria + longitud <= filas) and (columna_aleatoria + longitud <= columnas):
                    for i in range(longitud):
                        matriz[fila_aleatoria + i][columna_aleatoria + i] = palabra[i]
                    colocada = True
                    
    # 4. Rellenar los espacios vacíos con letras aleatorias
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == " ":
                matriz[i][j] = random.choice(abecedario)

    # 5. Imprimir la matriz
    print("=================================================")
    print("                 SOPA DE LETRAS                  ")
    print("=================================================")
    print("Frutas a buscar: PERA, KIWI, MORA, LIMON, PLATANO, UVA")
    print("=================================================\n")
    
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j], end="  ")
        print()
        
    print("\n=================================================")

if __name__ == "__main__":
    main()
```

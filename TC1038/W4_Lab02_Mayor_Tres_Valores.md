# TC1038 – Pensamiento Computacional
## Determinar el mayor de tres números (PSeInt)

### Planteamiento
Leer tres números y mostrar el mayor. Resolver primero **sin operadores lógicos** (`Y`, `O`, `NO`) y sin comparar más de dos valores en cada condición. Posteriormente, desarrollar una alternativa utilizando `Y` (equivalente lógico de `and`) y comparar ambas.

> **Convención:** se admiten valores iguales; el resultado debe ser el mayor aunque haya empate. En PSeInt, las asignaciones se realizan con `<-`, las comparaciones con `>` o `>=` y la conjunción lógica con `Y`.

## 1. Análisis EPS (Entrada – Proceso – Salida)

| Elemento | Descripción |
|---|---|
| **Entrada** | Tres valores numéricos: `num1`, `num2`, `num3`. |
| **Proceso** | Comparar los valores, identificar el mayor y conservarlo en la variable `mayor`. |
| **Salida** | Mostrar el número mayor. |

## 2. Solución 1: sin operadores lógicos

**Idea:** asumir inicialmente que el primer valor es el mayor; después comparar el segundo y el tercero contra el mayor provisional. En cada `Si` se comparan exactamente dos valores.

```pseint
Algoritmo MayorDeTres_SinOperadoresLogicos
    Definir num1, num2, num3, mayor Como Real

    Escribir "Ingrese el primer numero:"
    Leer num1
    Escribir "Ingrese el segundo numero:"
    Leer num2
    Escribir "Ingrese el tercer numero:"
    Leer num3

    mayor <- num1

    Si num2 > mayor Entonces
        mayor <- num2
    FinSi

    Si num3 > mayor Entonces
        mayor <- num3
    FinSi

    Escribir "El numero mayor es: ", mayor
FinAlgoritmo
```

**Explicación:** `mayor` inicia con `num1`. La primera condición lo actualiza si `num2` es más grande. La segunda lo actualiza si `num3` supera al mayor encontrado. Si existen empates, la variable conserva correctamente el valor máximo.

## 3. Solución 2: utilizando el operador lógico `Y`

**Idea:** comprobar con una sola condición compuesta si el primer número es mayor o igual que los otros dos. Si no lo es, evaluar el segundo número frente a los otros; de lo contrario, el tercero es el mayor (o comparte el máximo).

```pseint
Algoritmo MayorDeTres_ConOperadorY
    Definir num1, num2, num3, mayor Como Real

    Escribir "Ingrese el primer numero:"
    Leer num1
    Escribir "Ingrese el segundo numero:"
    Leer num2
    Escribir "Ingrese el tercer numero:"
    Leer num3

    Si num1 >= num2 Y num1 >= num3 Entonces
        mayor <- num1
    SiNo
        Si num2 >= num1 Y num2 >= num3 Entonces
            mayor <- num2
        SiNo
            mayor <- num3
        FinSi
    FinSi

    Escribir "El numero mayor es: ", mayor
FinAlgoritmo
```

**Nota:** en PSeInt el operador lógico correspondiente a `and` es **`Y`**. El uso de `>=` permite manejar correctamente los números repetidos.

## 4. Pruebas de escritorio

| Caso | `num1` | `num2` | `num3` | Salida esperada (ambas soluciones) |
|---|---:|---:|---:|---:|
| Primer número mayor | 9 | 4 | 2 | 9 |
| Segundo número mayor | 3 | 12 | 7 | 12 |
| Tercer número mayor | 1 | 5 | 15 | 15 |
| Todos negativos | -8 | -2 | -10 | -2 |
| Dos valores iguales y máximos | 6 | 6 | 1 | 6 |
| Tres valores iguales | 4 | 4 | 4 | 4 |
| Cero y negativos | 0 | -5 | -1 | 0 |

### Ejemplo detallado (3, 12, 7)

**Solución 1:** `mayor <- 3`; se comprueba `12 > 3` (verdadero), por lo que `mayor <- 12`; luego `7 > 12` (falso); se imprime `12`.

**Solución 2:** se evalúa `3 >= 12 Y 3 >= 7` (falso); se pasa a `12 >= 3 Y 12 >= 7` (verdadero); se asigna `mayor <- 12` y se imprime `12`.

## 5. Comparación y evaluación

### ¿Cuál solución es más clara para las personas?

La **solución 1** suele ser más clara para quienes comienzan: sigue una secuencia de dos decisiones independientes y actualiza una única variable. La solución 2 expresa de forma directa «este número es mayor o igual que los otros dos», pero exige comprender condiciones compuestas y anidadas.

### ¿Cuál solución es más rápida para determinar el mayor?

En términos del número de **comparaciones entre números**, la **solución 1 es más eficiente y predecible**: siempre realiza exactamente **2**. La solución 2 puede efectuar entre **2 y 4 comparaciones** según la rama seguida y la evaluación de expresiones lógicas. Ambas tienen complejidad temporal **O(1)** y la diferencia práctica para solo tres números es insignificante.

### ¿Cuál es el mínimo y máximo de comparaciones?

| Solución | Mínimo | Máximo | Explicación |
|---|---:|---:|---|
| **1. Sin operadores lógicos** | **2** | **2** | Se ejecutan dos condiciones simples, siempre. |
| **2. Con `Y`** | **2** | **4** | Hay hasta dos condiciones compuestas, con dos comparaciones numéricas cada una. |

**Precisión importante:** los valores **2–4** para la solución 2 corresponden a contar las comparaciones numéricas que realmente se evalúan si `Y` utiliza **evaluación de cortocircuito** (se omite el segundo operando cuando el primero ya es falso). Sin cortocircuito, se ejecutan **2 o 4 comparaciones numéricas**: dos si la primera condición es verdadera y cuatro si es falsa. Por tanto, su mínimo y máximo continúan siendo 2 y 4 en ambos modelos, aunque el conteo de casos intermedios puede variar. No se cuentan aquí las comprobaciones internas del operador lógico `Y` como comparaciones numéricas adicionales.

**Ejemplos del conteo con cortocircuito:**

- `(9, 4, 2)`: la primera condición es verdadera y evalúa las dos comparaciones → **2**.
- `(3, 12, 7)`: la primera condición falla en su primera comparación; la segunda evalúa dos comparaciones → **3**.
- `(5, 4, 9)`: la primera condición efectúa dos comparaciones antes de ser falsa; la segunda falla en su primera comparación → **3**.

**¿Por qué el máximo con cortocircuito es 3?** Si `num1 >= num2` es verdadero pero `num1 >= num3` es falso, entonces `num2 >= num1` solo podría ser verdadero en caso de igualdad entre `num1` y `num2`. Cuando son iguales, el segundo `Si` también evalúa su segunda comparación, resultando en **4 comparaciones** (por ejemplo, `5, 5, 9`). Por tanto, **el máximo correcto con cortocircuito también es 4**.

**Recuento final correcto según el modo de evaluación:**

| Modelo de evaluación de `Y` | Mínimo | Máximo |
|---|---:|---:|
| Con cortocircuito | **2** | **4** |
| Sin cortocircuito | **2** | **4** |

En PSeInt, el comportamiento de evaluación lógica puede variar según configuración o traducción; para un análisis independiente de dicho detalle, se puede contabilizar hasta **4 comparaciones escritas en las condiciones**.

### ¿Cuál solución prefieres y por qué?

**Prefiero la solución 1:** es más sencilla de leer, no necesita operadores lógicos, requiere siempre solo dos comparaciones numéricas y facilita explicar el razonamiento paso a paso. La solución 2 es una buena práctica para aprender a combinar condiciones mediante `Y`.

## 6. Observaciones didácticas

1. No se deben confundir **comparaciones de números** con la cantidad de instrucciones `Si`.
2. Usar `>=` en la solución 2 permite manejar empates de manera explícita.
3. Aunque una condición compuesta parezca «una sola condición», puede ejecutar **dos comparaciones numéricas**.
4. Ambas soluciones emplean memoria constante **O(1)**.
5. Los algoritmos muestran el **valor máximo**, no cuál de las posiciones lo contiene; si se necesita la posición o detectar un empate, habría que adaptar la salida.

## 7. Resumen de resultados

- **Solución 1:** dos condiciones simples, siempre **2 comparaciones numéricas**, sin operadores lógicos.
- **Solución 2:** condiciones compuestas con `Y`, **2 a 4 comparaciones numéricas**, con o sin cortocircuito (aunque el conteo de algunos casos cambia).
- **Claridad y recomendación:** la primera solución es la opción didáctica preferida para este ejercicio.
- **Verificación:** las pruebas de escritorio incluyen máximos en las tres posiciones, valores negativos y empates.

**Asignatura:** TC1038 – Pensamiento Computacional.

# TC1038 – Pensamiento Computacional

## Ejercicio: Determinar el mayor de tres números

**Objetivo:** Leer tres valores numéricos, determinar el mayor y comparar dos estrategias: una sin operadores lógicos ni `max()`, y otra utilizando `and`.

## 1. Análisis EPS (Entrada – Proceso – Salida)

| Elemento | Descripción |
|---|---|
| **Entrada** | Tres números (`a`, `b` y `c`), de tipo `float`. |
| **Proceso** | Comparar valores de dos en dos hasta identificar el mayor. Evaluar una segunda estrategia con condiciones compuestas mediante `and`. |
| **Salida** | Mostrar el valor mayor de los tres números. |

**Consideración:** Los números pueden ser negativos, positivos o iguales. Si hay empates en el valor máximo, se imprime ese valor una sola vez.

## 2. Solución 1: sin operadores lógicos y sin `max()`

### Idea del algoritmo

1. Leer tres números.
2. Suponer que `a` es el mayor.
3. Comparar `b` con el mayor provisional y actualizarlo si corresponde.
4. Comparar `c` con el mayor provisional y actualizarlo si corresponde.
5. Imprimir el mayor.

### Código Python

```python
# Entrada: leer tres valores numéricos.
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

# Proceso: asumir que a es el mayor.
mayor = a

# Cada if compara solamente dos valores.
if b > mayor:
    mayor = b

if c > mayor:
    mayor = c

# Salida: presentar el resultado.
print("El número mayor es:", mayor)
```

**Explicación:** `mayor` conserva el valor máximo encontrado hasta ese momento. No se utilizan `and`, `or`, `not` ni `max()`; cada `if` compara exactamente dos valores. El algoritmo realiza **siempre dos comparaciones** entre números.

## 3. Solución 2: utilizando el operador lógico `and`

### Idea del algoritmo

Se comprueba con una condición compuesta si `a` es al menos tan grande como los otros dos. De no ser así, se evalúa si `b` es al menos tan grande como los otros dos. Si ninguna condición se cumple, `c` es el mayor (o comparte el máximo).

### Código Python

```python
# Entrada: leer tres valores numéricos.
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

# Proceso: condiciones compuestas con and.
if a >= b and a >= c:
    mayor = a
elif b >= a and b >= c:
    mayor = b
else:
    mayor = c

# Salida: presentar el resultado.
print("El número mayor es:", mayor)
```

**Explicación:** Cada condición compuesta utiliza `and` para comprobar, en una sola expresión lógica, dos comparaciones entre números. La evaluación de `and` en Python es **de cortocircuito**: si la primera comparación es falsa, la segunda no se realiza. El algoritmo efectúa **entre dos y cuatro comparaciones numéricas**, según los datos y las ramas recorridas.

> **Nota didáctica:** En la primera solución se prohibieron los operadores lógicos, pero en esta segunda parte el enunciado solicita expresamente utilizar `and`.

## 4. Verificación: pruebas de escritorio

| Caso | `a` | `b` | `c` | Mayor esperado | Solución 1 | Solución 2 | Comparaciones S1 | Comparaciones S2 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Primero es mayor | 9 | 4 | 2 | 9 | 9 | 9 | 2 | 2 |
| Segundo es mayor | 3 | 8 | 1 | 8 | 8 | 8 | 2 | 3 |
| Tercero es mayor | 1 | 5 | 10 | 10 | 10 | 10 | 2 | 4 |
| Todos iguales | 7 | 7 | 7 | 7 | 7 | 7 | 2 | 2 |
| Negativos | -8 | -3 | -6 | -3 | -3 | -3 | 2 | 3 |
| Empate en el máximo | 5 | 5 | 2 | 5 | 5 | 5 | 2 | 2 |

Los resultados esperados coinciden con ambas soluciones en los casos evaluados. Las cantidades de comparaciones se obtienen siguiendo el flujo de ejecución de cada código, incluida la evaluación de cortocircuito de `and`.

### Ejemplo detallado: `a = 1`, `b = 5`, `c = 10`

**Solución 1**

1. Inicialmente `mayor = 1`.
2. ¿`5 > 1`? Sí → `mayor = 5` (1.ª comparación).
3. ¿`10 > 5`? Sí → `mayor = 10` (2.ª comparación).
4. Se imprime `10`.

**Solución 2**

1. ¿`1 >= 5`? No → se omite `1 >= 10` por cortocircuito (1.ª comparación).
2. ¿`5 >= 1`? Sí (2.ª comparación).
3. ¿`5 >= 10`? No (3.ª comparación).
4. Se ejecuta `else`, asignando `mayor = 10`. En este caso se realizan **tres comparaciones**, no cuatro.

**Precisión importante:** Aunque la segunda solución *puede* realizar cuatro comparaciones, para `a = 1, b = 5, c = 10` hace **tres**. Un caso que sí necesita cuatro es `a = 5, b = 1, c = 10`: primero `a >= b` es verdadero, `a >= c` falso; después `b >= a` es falso, por lo que se ejecuta `else`.

## 5. Comparación y evaluación de ambas soluciones

### ¿Cuál es más clara para las personas?

La **solución 1** suele ser más sencilla para quienes comienzan a programar: parte de un máximo provisional y lo actualiza mediante dos decisiones simples. La **solución 2** puede resultar intuitiva para quien prefiere expresar directamente “este número es mayor o igual que los otros dos”, pero sus condiciones compuestas requieren comprender `and` y el cortocircuito.

### ¿Cuál es más rápida para determinar el mayor?

La **solución 1** es más predecible y eficiente respecto al número de comparaciones: siempre utiliza dos. La solución 2 realiza entre dos y cuatro. No se debe afirmar una diferencia importante de tiempo real sin medirla: para únicamente tres valores, ambas son prácticamente instantáneas.

### ¿Cuántas comparaciones realiza cada solución?

Se cuentan solamente las **comparaciones numéricas** (`>`, `>=`), no las asignaciones, lecturas ni operadores `and`.

| Solución | Mínimo | Máximo | ¿Por qué? |
|---|---:|---:|---|
| **1. Comparaciones simples** | **2** | **2** | Ejecuta siempre sus dos instrucciones `if`. |
| **2. Con `and`** | **2** | **4** | Las condiciones se evalúan con cortocircuito y la segunda rama solo se comprueba cuando falla la primera. |

**Ejemplos de la solución 2:**

- **2 comparaciones:** `a = 9`, `b = 4`, `c = 2`. La primera condición es verdadera y termina la decisión.
- **3 comparaciones:** `a = 1`, `b = 5`, `c = 10`. Las primeras comprobaciones de cada condición no permiten elegir `a` ni `b`.
- **4 comparaciones:** `a = 5`, `b = 5`, `c = 10`. Se evalúan las dos comparaciones de cada condición compuesta antes de llegar a `else`.

### Corrección rigurosa del conteo de la solución 2

Para que la primera condición `a >= b and a >= c` consuma **dos** comparaciones y sea falsa, necesariamente `a >= b` es verdadera y `a >= c` es falsa. Esto implica `b <= a < c`. Por lo tanto, al llegar a `elif b >= a and b >= c`, la primera comparación `b >= a` solo puede ser verdadera si `b = a`; en ese caso, se evalúa además `b >= c`, que es falsa. Así, **sí pueden ocurrir cuatro comparaciones** cuando `a = b < c`, por ejemplo `a = 5`, `b = 5`, `c = 10`:

1. `a >= b`: `5 >= 5` → verdadero.
2. `a >= c`: `5 >= 10` → falso.
3. `b >= a`: `5 >= 5` → verdadero.
4. `b >= c`: `5 >= 10` → falso.

Finalmente se ejecuta `else` y se imprime `10`.

Por tanto, para la solución 2 **el mínimo es 2 y el máximo es 4**, incluso cuando hay números iguales. Si se restringieran los tres valores a ser distintos, el máximo sería 3 con el orden de condiciones elegido.

### ¿Cuál solución prefiero?

**Prefiero la solución 1**, porque es fácil de leer, cumple la restricción inicial y siempre utiliza el mínimo de dos comparaciones para encontrar el máximo entre tres valores, sin requerir condiciones compuestas.

## 6. Observaciones importantes

1. **Igualdad:** Usar `>=` en la solución 2 permite gestionar empates de forma directa. Ambas soluciones imprimen el valor máximo correctamente si hay igualdad.
2. **Números negativos:** No se debe inicializar `mayor = 0`, porque esto daría un resultado incorrecto si los tres números fueran negativos. Conviene iniciarlo con `a`.
3. **Cortocircuito:** Con `and`, Python puede evitar evaluar una segunda comparación si la primera es falsa.
4. **Métrica utilizada:** El análisis distingue entre comparaciones numéricas y evaluaciones completas de condiciones. Para eficiencia algorítmica, ambas soluciones tienen complejidad temporal constante, **O(1)**, para tres entradas.
5. **Datos de entrada:** `float()` acepta decimales; si se requiere validar entradas no numéricas, habría que agregar manejo de errores, lo cual no forma parte de este ejercicio.

## 7. Resumen de resultados

| Criterio | Solución 1 | Solución 2 |
|---|---|---|
| ¿Usa `and`? | No | Sí |
| ¿Usa `max()`? | No | No |
| Comparaciones mínimas | 2 | 2 |
| Comparaciones máximas | 2 | 4 |
| Ventaja principal | Simplicidad y eficiencia predecible | Expresa las relaciones mediante condiciones compuestas |
| Recomendación didáctica | **Preferida** | Útil para practicar `and` y cortocircuito |

**Conclusión:** Las dos soluciones determinan correctamente el mayor entre tres valores. Para este ejercicio introductorio, la primera resulta más sencilla y garantiza exactamente dos comparaciones.

# TC1037 — Pensamiento Algoritmico

## Ejercicio: determinar el mayor de tres valores

**Objetivo:** diseñar y comparar dos algoritmos en pseudocódigo PSeInt que leen tres números y muestran el mayor. El primero usa únicamente comparaciones entre dos valores en cada `Si`; el segundo utiliza el operador lógico `Y` para combinar condiciones.

## 1. Análisis EPS (Entrada — Proceso — Salida)

| Elemento | Descripción |
|---|---|
| **Entrada** | Tres valores numéricos: `a`, `b`, `c`. Pueden ser positivos, negativos, cero o repetidos. |
| **Proceso, parte 1** | Guardar inicialmente `a` como mayor; compararlo con `b` y actualizar si corresponde; después compararlo con `c` y actualizar. Cada `Si` evalúa una sola comparación entre dos valores. |
| **Proceso, parte 2** | Verificar mediante condiciones con `Y` si `a` es al menos tan grande como ambos valores; de no ser así, verificar lo mismo para `b`; en otro caso el mayor es `c`. |
| **Salida** | El valor mayor de los tres números. |

> **Criterio de igualdad:** se usa `>=` para reconocer correctamente empates; en PSeInt se escribe `>=` y el operador lógico se escribe `Y`.

## 2. Parte 1: solución sin operadores lógicos

### Pseudocódigo PSeInt

```pseint
Algoritmo MayorDeTres_SinY
    Definir a, b, c, mayor Como Real

    Escribir "Ingresa el primer numero:"
    Leer a
    Escribir "Ingresa el segundo numero:"
    Leer b
    Escribir "Ingresa el tercer numero:"
    Leer c

    mayor <- a

    Si b > mayor Entonces
        mayor <- b
    FinSi

    Si c > mayor Entonces
        mayor <- c
    FinSi

    Escribir "El numero mayor es: ", mayor
FinAlgoritmo
```

### Explicación

1. El primer número es el **mayor provisional**.
2. Se compara `b` con `mayor`. Si `b` es más grande, se actualiza `mayor`.
3. Se compara `c` con `mayor`. Si `c` es más grande, se actualiza `mayor`.
4. Se imprime el valor guardado en `mayor`.

**Número de comparaciones numéricas:** siempre **2**, sin importar el orden o si existen empates. Las asignaciones no se cuentan como comparaciones.

## 3. Parte 2: solución alternativa con el operador lógico `Y`

### Pseudocódigo PSeInt

```pseint
Algoritmo MayorDeTres_ConY
    Definir a, b, c, mayor Como Real

    Escribir "Ingresa el primer numero:"
    Leer a
    Escribir "Ingresa el segundo numero:"
    Leer b
    Escribir "Ingresa el tercer numero:"
    Leer c

    Si (a >= b) Y (a >= c) Entonces
        mayor <- a
    SiNo
        Si (b >= a) Y (b >= c) Entonces
            mayor <- b
        SiNo
            mayor <- c
        FinSi
    FinSi

    Escribir "El numero mayor es: ", mayor
FinAlgoritmo
```

### Explicación

- La primera condición verifica **en una misma expresión lógica** si `a` es mayor o igual que `b` **y** mayor o igual que `c`.
- Si no lo es, la segunda expresión lógica evalúa si `b` es mayor o igual que los otros dos valores.
- En caso contrario, `c` tiene el mayor valor.
- El uso de `>=` contempla empates sin generar resultados incorrectos.

**Importante:** una condición compuesta no equivale a una sola comparación numérica: `(a >= b) Y (a >= c)` contiene **dos comparaciones**. El número realmente ejecutado puede depender de si el intérprete evalúa ambas partes o aplica evaluación de cortocircuito.

## 4. Pruebas de escritorio

| `a` | `b` | `c` | Mayor esperado | Parte 1 | Parte 2 |
|---:|---:|---:|---:|---:|---:|
| 9 | 4 | 2 | 9 | 9 | 9 |
| 2 | 9 | 4 | 9 | 9 | 9 |
| 2 | 4 | 9 | 9 | 9 | 9 |
| -5 | -2 | -8 | -2 | -2 | -2 |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 7 | 7 | 3 | 7 | 7 | 7 |
| 3 | 7 | 7 | 7 | 7 | 7 |
| 7 | 3 | 7 | 7 | 7 | 7 |

Las salidas indicadas se obtienen al seguir manualmente la lógica de ambos algoritmos; no se presupone una ejecución automatizada de PSeInt.

## 5. Comparación y evaluación

### ¿Cuál solución es más clara para las personas?

La **Parte 1** suele resultar más fácil para principiantes: mantiene una variable `mayor` y la actualiza en pasos simples. La **Parte 2** expresa de forma más directa la idea matemática de «ser mayor o igual que los otros dos», pero requiere comprender condiciones compuestas y el operador `Y`.

### ¿Cuál solución es más rápida para determinar el mayor?

En términos de **comparaciones numéricas**, la Parte 1 es más predecible y eficiente: realiza exactamente **2**. La Parte 2 puede realizar más comparaciones dependiendo de los datos y de la estrategia de evaluación del operador `Y`. Para tres números, la diferencia de tiempo real normalmente es insignificante; ambos algoritmos tienen complejidad temporal **O(1)**.

### ¿Cuál es el mínimo y el máximo de comparaciones?

Contamos solamente comparaciones relacionales como `a >= b` o `b > mayor`; no contamos las evaluaciones del operador lógico `Y`, las asignaciones ni la lectura de datos.

| Solución | Mínimo | Máximo | Observación |
|---|---:|---:|---|
| Parte 1, sin `Y` | **2** | **2** | Siempre se realizan dos comparaciones. |
| Parte 2, con `Y`, si se evalúan todos los operandos | **2** | **4** | Primera condición: 2; si es falsa, segunda condición: otras 2. |
| Parte 2, con `Y`, si hay evaluación de cortocircuito | **2** | **4** | Pueden evitarse algunas evaluaciones cuando una primera comparación resulta falsa. |

**Ejemplos concretos:**

- `a=9, b=4, c=2`: la Parte 2 resuelve el caso con **2** comparaciones, porque la primera condición es verdadera.
- `a=2, b=9, c=4`: la Parte 2 hace **4** comparaciones si evalúa los dos operandos de ambas condiciones; con cortocircuito, hace **3** (la primera falla en `a >= b`, y la segunda evalúa sus dos comparaciones).
- `a=2, b=4, c=9`: la Parte 2 puede requerir **4** comparaciones incluso con cortocircuito (`a >= b` falla; `b >= a` es verdadero, pero `b >= c` falla).

> **Nota sobre PSeInt:** no es necesario asumir cortocircuito para asegurar la corrección de estas soluciones. Para una comparación de costos estrictamente independiente de los detalles del intérprete, se considera la evaluación completa de las expresiones: la segunda solución efectúa 2 o 4 comparaciones.

### ¿Cuál solución prefieres? Justifica tu elección

**Prefiero la Parte 1.** Es más sencilla de leer para estudiantes que comienzan, no exige condiciones compuestas, realiza exactamente dos comparaciones y resulta fácil de ampliar a más números. La Parte 2 es igualmente correcta y muy útil para practicar expresiones lógicas con `Y`.

## 6. Conclusiones y observaciones didácticas

1. **Las dos soluciones calculan correctamente el mayor**, incluso con números negativos o valores iguales.
2. El primer algoritmo respeta la restricción de **comparar solo dos valores por cada `Si`**.
3. El segundo algoritmo utiliza `Y` para expresar que un candidato debe superar o igualar **simultáneamente** a los otros dos.
4. **Una condición con `Y` puede incorporar varias comparaciones**: no se debe confundir el número de instrucciones `Si` con el número de comparaciones numéricas.
5. Ambas soluciones son de tiempo constante para exactamente tres valores. La primera requiere un número fijo y mínimo de dos comparaciones.

**Recomendación para TC1038:** implementar y probar primero la Parte 1; después contrastar la Parte 2 con una tabla de pruebas que incluya los tres órdenes posibles del mayor y casos de empate.

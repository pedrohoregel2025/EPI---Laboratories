# TC1038 – Ejercicios de listas en Python

**Asignatura:** Pensamiento Computacional  
**Lenguaje:** Python 3  
**Objetivo:** practicar recorridos, clasificación, cálculos y métodos de listas.

Los intervalos de números aleatorios incluyen ambos extremos y permiten repeticiones. Cada solución puede ejecutarse por separado. `random.randint(a, b)` genera un entero entre `a` y `b`, incluidos. Los resultados cambian entre ejecuciones.

## Ejercicio 1. Separar números pares e impares

### Enunciado

1. Genera una lista de **50 números enteros aleatorios entre 1 y 100**.
2. Recorre la lista y separa sus elementos en dos listas: `pares` e `impares`.
3. Conserva las repeticiones y el orden de aparición en cada grupo.
4. Muestra la lista original, las dos listas resultantes y la cantidad de elementos de cada una.

**Pista:** un número es par si el residuo de dividirlo entre 2 es cero: `numero % 2 == 0`.

### Análisis EPS

| Entrada | Proceso | Salida |
|---|---|---|
| 50 enteros aleatorios entre 1 y 100 | Generar la lista; recorrerla; evaluar el residuo entre 2; agregar cada elemento al grupo correspondiente | Lista original, pares, impares y cantidades |

### Solución propuesta

```python
import random

numeros = []
pares = []
impares = []

for _ in range(50):
    numeros.append(random.randint(1, 100))

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Lista original:", numeros)
print("Pares:", pares)
print("Cantidad de pares:", len(pares))
print("Impares:", impares)
print("Cantidad de impares:", len(impares))
print("Total clasificado:", len(pares) + len(impares))
```

### Comprobación

- La lista original debe tener 50 elementos, todos entre 1 y 100.
- Todos los elementos de `pares` deben ser divisibles entre 2.
- Todos los elementos de `impares` deben tener residuo 1 al dividirlos entre 2.
- La suma de las cantidades de ambos grupos debe ser 50.

**Ejemplo pequeño:** con `[4, 7, 4, 9, 2]`, se obtiene `pares = [4, 4, 2]` e `impares = [7, 9]`.

## Ejercicio 2. Clasificar números respecto de la media

### Enunciado

1. Genera una lista de **50 números enteros aleatorios entre 1 y 20**.
2. Calcula la **media aritmética** de todos los elementos:

   `media = suma de los elementos / cantidad de elementos`

3. Forma una lista `izquierda` con los valores **menores que la media** y otra `derecha` con los valores **mayores que la media**.
4. Si existen valores exactamente iguales a la media, guárdalos en `iguales` para no perder elementos.
5. Muestra la lista original, la media y las tres listas con sus cantidades. Conserva el orden de aparición y las repeticiones.

**Interpretación:** izquierda y derecha se refieren a la ubicación de los valores en la recta numérica respecto de la media, no a las posiciones de la lista. La media no tiene que ser un entero ni aparecer en la lista. La lista `iguales` puede quedar vacía.

### Análisis EPS

| Entrada | Proceso | Salida |
|---|---|---|
| 50 enteros aleatorios entre 1 y 20 | Sumar y dividir entre 50; recorrer la lista; comparar cada valor con la media; agregarlo a su grupo | Lista original, media, valores menores, mayores e iguales y sus cantidades |

### Solución propuesta

```python
import random

numeros = []
for _ in range(50):
    numeros.append(random.randint(1, 20))

media = sum(numeros) / len(numeros)
izquierda = []
derecha = []
iguales = []

for numero in numeros:
    if numero < media:
        izquierda.append(numero)
    elif numero > media:
        derecha.append(numero)
    else:
        iguales.append(numero)

print("Lista original:", numeros)
print(f"Media: {media:.2f}")
print("A la izquierda de la media:", izquierda)
print("Cantidad a la izquierda:", len(izquierda))
print("A la derecha de la media:", derecha)
print("Cantidad a la derecha:", len(derecha))
print("Iguales a la media:", iguales)
print("Cantidad de iguales:", len(iguales))
print("Total clasificado:", len(izquierda) + len(derecha) + len(iguales))
```

**Nota:** `:.2f` muestra dos decimales; no modifica la variable `media`. La clasificación utiliza la media calculada sin redondearla. Con estos datos enteros, la igualdad exacta es adecuada: solo puede haber coincidencias si la media es un entero.

### Comprobación

- La media debe estar entre 1 y 20.
- Cada elemento de `izquierda` debe ser menor que la media; cada elemento de `derecha`, mayor.
- Cada elemento de `iguales` debe coincidir con la media.
- Las tres cantidades deben sumar 50.

**Ejemplo pequeño con igualdad:** para `[2, 4, 6, 8, 10]`, la media es `6.0`; se obtiene `izquierda = [2, 4]`, `derecha = [8, 10]` e `iguales = [6]`.

**Ejemplo pequeño sin igualdad:** para `[1, 2, 4, 8]`, la media es `3.75`; se obtiene `izquierda = [1, 2]`, `derecha = [4, 8]` e `iguales = []`.

## Ejercicio 3. Análisis de resultados de un grupo — nivel medio

### Enunciado

Un grupo de ingeniería presenta una evaluación de Pensamiento Computacional. Cada estudiante obtiene una calificación entera entre 0 y 100. Una calificación de **70 o más** es aprobatoria.

Desarrolla un programa que:

1. Genere una lista de **30 calificaciones aleatorias entre 0 y 100**.
2. Calcule el promedio, la calificación mínima y la máxima.
3. Separe las calificaciones en listas de aprobadas y reprobadas.
4. Cree una lista de calificaciones **sin valores repetidos**, conservando el orden de su primera aparición.
5. Genere otra lista con las **cinco calificaciones distintas más altas**, ordenadas de mayor a menor. Si hay menos de cinco valores distintos, debe mostrar los disponibles.
6. Muestre cuántas veces aparece cada una de esas calificaciones en la lista original.
7. Conserve la lista original en su orden de captura.

**Restricción didáctica:** resuelve con listas, ciclos y condicionales; no uses conjuntos (`set`) ni diccionarios. Puedes usar `append`, `count`, `sort`, `in`, `sum`, `len`, `min`, `max` y slices.

### Análisis EPS

| Entrada | Proceso | Salida |
|---|---|---|
| 30 calificaciones enteras entre 0 y 100 | Calcular estadísticos; clasificar por aprobación; construir una lista sin repetidos; ordenar una copia; seleccionar hasta cinco valores; contar sus apariciones | Lista original, promedio, mínimo, máximo, aprobadas, reprobadas, lista sin repetidos y cinco mejores valores con sus frecuencias |

### Estrategia

1. Generar las calificaciones y crear listas auxiliares vacías.
2. Recorrer las calificaciones para clasificarlas.
3. Agregar un valor a `sin_repetidos` solamente si aún no está en ella.
4. Copiar `sin_repetidos`, ordenar la copia de mayor a menor y tomar `[:5]`.
5. Recorrer los mejores valores y consultar sus frecuencias con `count` sobre la lista original.

### Solución propuesta

```python
import random

calificaciones = []
for _ in range(30):
    calificaciones.append(random.randint(0, 100))

aprobadas = []
reprobadas = []
sin_repetidos = []

for calificacion in calificaciones:
    if calificacion >= 70:
        aprobadas.append(calificacion)
    else:
        reprobadas.append(calificacion)

    # Esta condición es independiente de la clasificación anterior.
    if calificacion not in sin_repetidos:
        sin_repetidos.append(calificacion)

# Se generan 30 calificaciones, por lo que la lista no está vacía.
promedio = sum(calificaciones) / len(calificaciones)

# Ordenar una copia conserva el orden de primera aparición.
ordenadas = sin_repetidos.copy()
ordenadas.sort(reverse=True)
mejores_cinco = ordenadas[:5]

print("Calificaciones originales:", calificaciones)
print(f"Promedio: {promedio:.2f}")
print("Mínima:", min(calificaciones))
print("Máxima:", max(calificaciones))
print("Aprobadas:", aprobadas)
print("Cantidad de aprobadas:", len(aprobadas))
print("Reprobadas:", reprobadas)
print("Cantidad de reprobadas:", len(reprobadas))
print("Sin repetidos, en orden de aparición:", sin_repetidos)
print("Cinco mejores calificaciones distintas:", mejores_cinco)

for calificacion in mejores_cinco:
    frecuencia = calificaciones.count(calificacion)
    print(f"Calificación {calificacion}: {frecuencia} aparición(es)")
```

### Comprobación con datos conocidos

Para verificar la lógica, sustituye temporalmente la generación aleatoria por:

```python
calificaciones = [70, 95, 60, 95, 80, 100, 70, 50, 90, 80]
```

Los resultados esperados son:

| Resultado | Valor esperado |
|---|---|
| Promedio | `79.0` |
| Mínima / máxima | `50` / `100` |
| Aprobadas | `[70, 95, 95, 80, 100, 70, 90, 80]` |
| Reprobadas | `[60, 50]` |
| Sin repetidos | `[70, 95, 60, 80, 100, 50, 90]` |
| Cinco mejores valores distintos | `[100, 95, 90, 80, 70]` |
| Frecuencias de esos cinco valores | `1, 2, 1, 2, 2`, respectivamente |

Prueba también con todas las calificaciones iguales: la lista sin repetidos y la lista de mejores calificaciones deben tener un solo elemento.

## Observaciones generales

- Separar elementos no significa eliminarlos de la lista original: utiliza listas auxiliares y `append`.
- No se deben descartar las repeticiones en los ejercicios 1 y 2: cada aparición representa un dato.
- En el ejercicio 3 se eliminan duplicados únicamente en la lista auxiliar de valores distintos; las frecuencias se calculan con los datos originales.
- `sort` modifica la lista y devuelve `None`. Utiliza `ordenadas.sort(reverse=True)`, sin asignar su resultado a una variable.
- Para reproducir resultados durante una prueba, puedes colocar `random.seed(1038)` después de `import random` y antes de generar los números.
- Si adaptas estos programas para recibir cantidades variables, comprueba que la lista no esté vacía antes de dividir entre `len(lista)` o usar `min` y `max` sin un valor predeterminado.

**Verificación:** las tres soluciones se ejecutaron y se comprobaron sus clasificaciones, cantidades, conservación de los datos originales y resultados con datos conocidos.

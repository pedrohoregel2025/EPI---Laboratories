# TC1037 · Pensamiento Algorítmico

# Ciclo `while`: fundamentos y tres ejercicios de aplicación

**Dirigido a:** estudiantes de nuevo ingreso de Ingeniería  
**Lenguaje:** Python 3  
**Temas:** ciclos condicionales, condiciones de terminación, acumuladores, contadores, banderas, `break` y ciclos anidados.

## Objetivos de aprendizaje

Al finalizar esta actividad, el estudiante será capaz de:

1. Explicar el funcionamiento de la estructura `while`.
2. Identificar una condición de continuación y demostrar que el ciclo puede terminar.
3. Utilizar correctamente contadores, acumuladores y banderas.
4. Distinguir el uso de `while True` con `break` frente a un ciclo controlado por una bandera.
5. Resolver tres situaciones prácticas usando ciclos simples y anidados.

---

## 1. ¿Cómo funciona el ciclo `while`?

`while` (*mientras*) es una estructura de repetición que **evalúa una condición antes de cada iteración**. Si la condición es verdadera (`True`), ejecuta el bloque indentado; después vuelve a comprobarla. Cuando es falsa (`False`), continúa con la siguiente instrucción fuera del ciclo. Si la condición es falsa desde el inicio, el cuerpo no se ejecuta ninguna vez.

```python
contador = 1                  # Inicialización
while contador <= 3:         # Condición de continuación
    print(contador)           # Acción que se repite
    contador += 1             # Actualización

print("Fin del ciclo")
```

**Salida:** `1`, `2`, `3` y `Fin del ciclo` (en líneas separadas).

### Elementos indispensables para evitar ciclos infinitos

| Elemento | Pregunta de revisión | Ejemplo |
|---|---|---|
| Inicialización | ¿En qué estado comienza el ciclo? | `contador = 1` |
| Condición | ¿Cuándo debe seguir iterando? | `contador <= 3` |
| Actualización | ¿Qué dato cambia en cada repetición? | `contador += 1` |
| Terminación | ¿Existe una forma de que la condición sea falsa? | Cuando `contador` llega a 4 |
| Validación | ¿Qué ocurre con entradas inválidas? | Repetir la solicitud, no calcular con datos erróneos |

**Error común:**

```python
contador = 1
while contador <= 3:
    print(contador)
    # ERROR: falta actualizar contador; permanece en 1.
```

En ese ejemplo, la condición nunca cambia. También pueden existir ciclos intencionalmente indefinidos (por ejemplo, un servidor), pero necesitan mecanismos definidos para detenerse.

### `while True` y `break`

`while True` mantiene la condición siempre verdadera. Se usa cuando la **decisión de terminar ocurre dentro del bloque**, especialmente después de leer una opción o un valor centinela. `break` interrumpe inmediatamente el ciclo más interno que lo contiene.

```python
while True:
    dato = input("Escribe SALIR para terminar: ").strip().upper()
    if dato == "SALIR":
        break                 # Sale de este while
    print("Dato recibido:", dato)
```

**Ventajas:** la condición de salida se escribe cerca de la entrada que la determina y permite terminar desde un punto claro. **Precauciones:** sin un `break` alcanzable, el ciclo no finaliza; en ciclos anidados, `break` solo abandona el ciclo más cercano.

### Ciclo controlado por una bandera (`bandera = True`)

Una *bandera* es una variable booleana que representa un estado, por ejemplo, `continuar`, `acceso_concedido` o `buscando`.

```python
bandera = True
while bandera:
    dato = input("Escribe SALIR para terminar: ").strip().upper()
    if dato == "SALIR":
        bandera = False      # La siguiente evaluación detendrá el ciclo
    else:
        print("Dato recibido:", dato)
```

**Ventajas:** el estado de continuación queda explícito, puede combinarse con otras condiciones y facilita comprender por qué sigue el ciclo. **Precauciones:** la bandera debe actualizarse correctamente; cambiarla a `False` **no interrumpe al instante** el resto del cuerpo de esa iteración (a diferencia de `break`). En Python se escribe `while bandera:` con minúsculas y dos puntos, no `While Bandera`.

| Criterio | `while True` + `break` | `while bandera` |
|---|---|---|
| Terminación | Inmediata al ejecutar `break` | Al volver a evaluar la condición |
| Control | Se decide dentro del cuerpo | Lo expresa una variable booleana |
| Útil cuando | Hay valor centinela o menú de salida | El proceso depende de un estado o evento |
| Riesgo frecuente | Olvidar o hacer inalcanzable el `break` | Olvidar cambiar la bandera |

No existe una única opción universalmente mejor: la elección depende de cómo se expresa más claramente la condición de salida.

---

# Ejercicio 1. La Alcancía Digital

## Enunciado

Un estudiante desea ahorrar para un viaje. Debe ingresar depósitos, uno por uno, hasta escribir **`0`** para finalizar. El programa mostrará el **total ahorrado** y la **cantidad de depósitos válidos**. Un monto negativo debe producir un mensaje de error y no debe sumarse ni contarse como depósito.

## Análisis EPS

| Elemento | Descripción |
|---|---|
| **Entrada** | Montos numéricos ingresados individualmente. El `0` es el centinela de salida. |
| **Proceso** | Iniciar `total = 0` y `cantidad = 0`; leer monto; si es negativo, informar error; si es positivo, acumularlo e incrementar el contador; repetir hasta ingresar cero. |
| **Salida** | Total ahorrado y cantidad de depósitos válidos. Mensajes de error ante valores negativos o entradas no numéricas. |

## Pasos de análisis

1. Inicializar el **acumulador** `total` y el **contador** `cantidad` en cero.
2. Repetir la lectura del depósito con `while True`.
3. Si la entrada no representa un número, informar el error y volver a solicitarla.
4. Si el depósito es `0`, ejecutar `break`.
5. Si el depósito es negativo, mostrar el error **sin modificar** `total` o `cantidad`.
6. En caso positivo, sumar al acumulador e incrementar el contador.
7. Al salir del ciclo, mostrar ambos resultados.

## Solución en Python

```python
# EJERCICIO 1: La Alcancía Digital
# Variante didáctica: while True con break y acumulador.

total = 0.0                  # Acumulador de los depósitos válidos
cantidad = 0                 # Contador de depósitos válidos

while True:
    entrada = input("Depósito (0 para terminar): ")

    try:
        deposito = float(entrada)
    except ValueError:
        print("Error: ingrese un monto numérico.")
        continue            # Reinicia la siguiente iteración

    if deposito == 0:
        break               # El valor centinela termina el ciclo

    if deposito < 0:
        print("Error: no se aceptan depósitos negativos.")
        continue            # No se suma ni se cuenta

    total += deposito       # Sumar únicamente depósitos positivos
    cantidad += 1           # Contar únicamente depósitos positivos

print(f"Total ahorrado: ${total:.2f}")
print(f"Cantidad de depósitos: {cantidad}")
```

> **Nota técnica:** `float` es suficiente para practicar ciclos, pero puede producir pequeñas imprecisiones decimales. En una aplicación monetaria real conviene emplear `Decimal` o almacenar centavos enteros. Esta variante también presupone valores numéricos finitos; se puede ampliar la validación con `math.isfinite()`.

## Prueba de escritorio

| Entrada | Acción | Total | Cantidad |
|---:|---|---:|---:|
| `100` | Depósito válido | 100 | 1 |
| `50.50` | Depósito válido | 150.50 | 2 |
| `-20` | Error: se ignora | 150.50 | 2 |
| `30` | Depósito válido | 180.50 | 3 |
| `0` | Finaliza | **180.50** | **3** |

**Casos límite:** ingresar `0` inmediatamente (total 0 y cantidad 0); ingresar varios negativos; escribir texto en vez de un número.

**Preguntas para el alumno:** ¿Por qué `cantidad` no se incrementa cuando el depósito es negativo? ¿Qué ocurriría si se omitiera `break` al ingresar cero? ¿Qué variable es contador y cuál es acumulador?

---

# Ejercicio 2. Acceso al Sistema

## Enunciado

Un módulo didáctico de acceso utiliza la contraseña maestra **`"python2024"`**. El usuario dispone de un **máximo de tres intentos**. Si acierta, se muestra `Acceso concedido`. Si agota sus tres intentos, se muestra `Acceso denegado. Cuenta bloqueada.`

> **Contexto académico:** colocar una contraseña fija en el código es únicamente un ejercicio de lógica de control. No es una práctica segura para un sistema bancario real: deben utilizarse mecanismos seguros de almacenamiento y autenticación.

## Análisis EPS

| Elemento | Descripción |
|---|---|
| **Entrada** | Una contraseña ingresada en cada intento. |
| **Proceso** | Inicializar `intentos = 0` y `acceso_concedido = False`. Mientras haya menos de 3 intentos y no se haya concedido el acceso, solicitar una contraseña, contar el intento y comparar con la clave. Si coincide, actualizar la bandera. |
| **Salida** | `Acceso concedido`, o bien `Acceso denegado. Cuenta bloqueada.` al agotar el límite. |

## Pasos de análisis

1. Definir la contraseña correcta y el máximo de intentos.
2. Inicializar el contador `intentos = 0` y la bandera `acceso_concedido = False`.
3. Mantener el `while` mientras **no** se haya concedido acceso **y** queden intentos.
4. Leer una contraseña e incrementar el contador.
5. Comparar con la contraseña correcta. Si coincide, cambiar la bandera a `True`.
6. Al terminar, revisar la bandera para presentar el mensaje correspondiente.

## Solución en Python

```python
# EJERCICIO 2: Acceso al Sistema
# Variante didáctica: while con contador y bandera.

CLAVE_CORRECTA = "python2024"
MAX_INTENTOS = 3

intentos = 0
acceso_concedido = False    # Bandera: comienza sin acceso

while intentos < MAX_INTENTOS and not acceso_concedido:
    clave = input("Ingrese la contraseña: ")
    intentos += 1            # Se contabiliza cada intento realizado

    if clave == CLAVE_CORRECTA:
        acceso_concedido = True  # Terminará en la próxima evaluación
    else:
        print("Contraseña incorrecta.")

if acceso_concedido:
    print("Acceso concedido")
else:
    print("Acceso denegado. Cuenta bloqueada.")
```

**Observación sobre banderas:** aquí `acceso_concedido` expresa el estado de autenticación. No es imprescindible crear otra bandera llamada `bandera`; la variable booleana puede tener un nombre descriptivo. El `while` controla **dos condiciones**: número de intentos y estado de acceso.

### Variante equivalente con una bandera `continuar`

Para distinguir el patrón solicitado `bandera = True; while bandera`, puede escribirse así:

```python
CLAVE_CORRECTA = "python2024"
intentos = 0
bandera = True               # Indica si deben continuar los intentos
acceso_concedido = False

while bandera:
    clave = input("Ingrese la contraseña: ")
    intentos += 1

    if clave == CLAVE_CORRECTA:
        acceso_concedido = True
        bandera = False      # Contraseña correcta: terminar
    elif intentos >= 3:
        bandera = False      # Tres errores: terminar
    else:
        print("Contraseña incorrecta. Intente nuevamente.")

if acceso_concedido:
    print("Acceso concedido")
else:
    print("Acceso denegado. Cuenta bloqueada.")
```

**Diferencia:** la primera versión expresa directamente el límite y el estado en la condición del `while`. La segunda concentra la decisión de continuar en una bandera que cambia a `False` en las dos condiciones de salida. Las dos resuelven correctamente el problema.

## Pruebas de escritorio

| Secuencia de entradas | Intentos utilizados | Bandera final | Resultado |
|---|---:|---|---|
| `python2024` | 1 | `True` | Acceso concedido |
| `abc`, `python2024` | 2 | `True` | Acceso concedido |
| `abc`, `123`, `xyz` | 3 | `False` | Acceso denegado; cuenta bloqueada |
| `abc`, `123`, `python2024` | 3 | `True` | Acceso concedido |

En la tabla, la columna *bandera final* se refiere a `acceso_concedido`, no a `bandera` en la variante alternativa.

**Preguntas para el alumno:** ¿Por qué se incrementa el contador incluso si la contraseña es correcta? ¿Qué error se produciría si `intentos` nunca aumentara? ¿Se necesita `break` cuando ya se actualiza una bandera que controla la condición?

---

# Ejercicio 3. Generador de Tablas de Multiplicar

## Enunciado

Solicitar un entero positivo `N` y generar las tablas de multiplicar desde **1 hasta N**, mostrando para cada tabla los productos desde **1 hasta 10**. Es obligatorio usar **dos ciclos `while` anidados**.

## Análisis EPS

| Elemento | Descripción |
|---|---|
| **Entrada** | Entero positivo `N` que representa la última tabla a imprimir. |
| **Proceso** | Validar `N > 0`. Iniciar `tabla = 1`; repetir mientras `tabla <= N`. Para cada tabla, reiniciar `multiplicador = 1`, calcular y mostrar diez productos mientras `multiplicador <= 10`; aumentar ambos contadores en sus respectivos ciclos. |
| **Salida** | Tablas completas del 1 al N, cada una con diez multiplicaciones. Mensajes de validación si `N` no es entero positivo. |

## Pasos de análisis

1. Solicitar `N` y comprobar que sea un entero mayor que cero.
2. Inicializar el contador externo `tabla = 1`.
3. Mientras `tabla <= N`, imprimir el encabezado de la tabla actual.
4. **Reiniciar** el contador interno `multiplicador = 1` en cada iteración externa.
5. Mientras `multiplicador <= 10`, calcular `tabla * multiplicador` y mostrar la multiplicación.
6. Incrementar `multiplicador` dentro del ciclo interno.
7. Cuando termine el ciclo interno, incrementar `tabla` dentro del ciclo externo.
8. Finalizar cuando `tabla` sea mayor que `N`.

## Solución en Python

```python
# EJERCICIO 3: Generador de Tablas de Multiplicar
# Variante didáctica: dos ciclos while anidados.

while True:
    entrada = input("Ingrese el número máximo de tabla (N > 0): ")

    try:
        n = int(entrada)
    except ValueError:
        print("Error: ingrese un número entero.")
        continue

    if n <= 0:
        print("Error: N debe ser mayor que cero.")
        continue

    break                      # Ya se obtuvo un N válido

tabla = 1                      # Contador del ciclo externo

while tabla <= n:
    print(f"\n--- Tabla del {tabla} ---")

    multiplicador = 1         # Se reinicia para CADA nueva tabla
    while multiplicador <= 10:
        producto = tabla * multiplicador
        print(f"{tabla} x {multiplicador} = {producto}")
        multiplicador += 1   # Avanza el ciclo interno

    tabla += 1                # Avanza el ciclo externo
```

## Prueba de escritorio reducida (N = 3)

| Iteración externa | `tabla` | Valores del contador interno | Primer producto | Último producto |
|---:|---:|---|---|---|
| 1 | 1 | 1, 2, ..., 10 | `1 x 1 = 1` | `1 x 10 = 10` |
| 2 | 2 | 1, 2, ..., 10 | `2 x 1 = 2` | `2 x 10 = 20` |
| 3 | 3 | 1, 2, ..., 10 | `3 x 1 = 3` | `3 x 10 = 30` |

Para `N = 3` se imprimen **30 multiplicaciones**: tres tablas × diez productos por tabla.

**Errores comunes:** no reiniciar `multiplicador` al comenzar una nueva tabla (solo se imprime la primera); olvidar incrementar `multiplicador` (ciclo interno infinito); olvidar incrementar `tabla` (ciclo externo infinito); utilizar `<` en lugar de `<=` y omitir el último valor.

**Preguntas para el alumno:** ¿Por qué `multiplicador = 1` debe estar dentro del ciclo externo? ¿Cuántos resultados se generan si `N = 7`? ¿Qué diferencia hay entre el ciclo de validación y los ciclos que imprimen las tablas?

---

## 5. Comparación de los tres ejercicios

| Ejercicio | Tipo de `while` | Variables centrales | Criterio de salida |
|---|---|---|---|
| Alcancía digital | `while True` + `break` | Acumulador `total`, contador `cantidad` | Depósito igual a `0` |
| Acceso al sistema | Condicional con contador y bandera | `intentos`, `acceso_concedido` | Contraseña correcta o tres intentos |
| Tablas de multiplicar | Dos `while` anidados | `tabla`, `multiplicador` | `tabla > N`; para cada tabla, `multiplicador > 10` |

## 6. Actividad para entregar

**Instrucciones:** implementar individualmente los tres ejercicios y entregar un solo documento PDF o Markdown (según indique el docente) con:

1. El **análisis EPS** de cada ejercicio.
2. El código Python ejecutable y comentado.
3. Una **prueba de escritorio** por ejercicio, incluyendo al menos un caso especial o inválido.
4. Una explicación de **cómo termina cada ciclo**.
5. Las respuestas a las preguntas de reflexión indicadas en cada apartado.

**Extensiones opcionales:**

- **Alcancía:** mostrar también el depósito más alto, sin considerar valores inválidos.
- **Acceso:** mostrar cuántos intentos quedaron cuando se logró entrar.
- **Tablas:** permitir seleccionar el límite superior del multiplicador en vez de fijarlo en 10.

### Rúbrica sugerida (100 puntos)

| Criterio | Puntos |
|---|---:|
| Análisis EPS correcto en los tres ejercicios | 20 |
| Funcionamiento de los tres programas | 35 |
| Uso correcto de contador, acumulador, bandera y ciclos anidados | 20 |
| Validación de entradas y terminación de los ciclos | 15 |
| Pruebas de escritorio y explicación del código | 10 |
| **Total** | **100** |

## 7. Conclusiones

- `while` es adecuado cuando la cantidad de iteraciones depende de una condición y no se conoce necesariamente de antemano.
- **Contador**: registra cuántas veces ocurre un evento; **acumulador**: suma cantidades; **bandera**: representa un estado lógico.
- `while True` junto con `break` resulta conveniente si se reconoce un valor de salida dentro del ciclo.
- Una bandera permite hacer explícito el estado que controla la repetición. Debe actualizarse en las condiciones de salida.
- En ciclos anidados, se debe controlar **por separado** el progreso y la terminación de cada nivel.
- Toda solución debe verificarse con casos habituales, límites y entradas inválidas para evitar ciclos infinitos y errores de ejecución.

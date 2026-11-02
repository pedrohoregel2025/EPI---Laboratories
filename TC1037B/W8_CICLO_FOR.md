# Pensamiento algorítmico: ciclo FOR

Se resuelven los cuatro enunciados. Cada solución se puede ejecutar por separado.

**Convenciones:** Para en PSeInt equivale a for en Python. PSeInt incluye el límite final; range en Python lo excluye. MOD y % calculan el residuo. Se supone que la entrada de los ejercicios 1 y 2 es un entero válido. No se utilizan ciclos WHILE.

## 1. Función para determinar si un número es primo

Un número primo es un entero mayor que 1 con exactamente dos divisores positivos: 1 y él mismo. Por ejemplo, 7 es primo; 9 no lo es porque también es divisible entre 3. Los negativos, 0 y 1 no son primos.

### EPS: Entrada - Proceso - Salida

| Elemento | Descripción |
| --- | --- |
| Entrada | Un número entero. |
| Proceso | Descartar los valores menores o iguales a 1. Recorrer con FOR los posibles divisores de 2 a n - 1. Si alguno divide sin residuo, el número no es primo. |
| Salida | Valor lógico verdadero o falso; el programa de ejemplo muestra un mensaje. |

### Pseudocódigo en PSeInt

```pseint
Funcion resultado <- EsPrimo(numero)
    Definir divisor Como Entero;
    Definir resultado Como Logico;
    resultado <- numero > 1;
    // Para 2, no hay divisores que comprobar.
    Si numero > 2 Entonces
        Para divisor <- 2 Hasta numero - 1 Hacer
            Si numero MOD divisor = 0 Entonces
                resultado <- Falso;
            FinSi
        FinPara
    FinSi
FinFuncion

Algoritmo ComprobarPrimo
    Definir numero Como Entero;
    Escribir "Ingrese un numero entero:";
    Leer numero;
    Si EsPrimo(numero) Entonces
        Escribir "Es primo.";
    SiNo
        Escribir "No es primo.";
    FinSi
FinAlgoritmo
```

<!-- pagebreak -->

## 1. Implementación y verificación

### Código documentado en Python

```python
def es_primo(numero: int) -> bool:
    """Devuelve True si el entero tiene exactamente dos divisores."""
    if numero <= 1:
        return False

    # range excluye su limite final: prueba de 2 a numero - 1.
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False  # Se encontro un divisor adicional.

    # En el caso de 2, el for no se ejecuta y se devuelve True.
    return True

# Ejemplo de uso de la funcion con un dato introducido por el usuario.
numero = int(input("Ingrese un número entero: "))
if es_primo(numero):
    print("Es primo.")
else:
    print("No es primo.")
```

### Pruebas y resultado

| Entrada | Resultado esperado | Motivo |
| --- | --- | --- |
| -7, 0, 1 | Falso | No son mayores que 1. |
| 2 | Verdadero | Solo tiene los divisores 1 y 2. |
| 7 | Verdadero | No tiene divisores adicionales. |
| 9 | Falso | Es divisible entre 3. |

En PSeInt se conserva un resultado lógico y se completa el recorrido. Python devuelve False al encontrar el primer divisor; ambas funciones producen la misma clasificación. Para 2, el intervalo de prueba está vacío.

<!-- pagebreak -->

## 2. Función para determinar si un número es perfecto

Un número perfecto es un entero positivo igual a la suma de sus divisores propios positivos, es decir, sus divisores sin incluirlo a él mismo. Por ejemplo, 6 = 1 + 2 + 3. El 1 no es perfecto: la suma de sus divisores propios es 0.

### EPS: Entrada - Proceso - Salida

| Elemento | Descripción |
| --- | --- |
| Entrada | Un número entero. |
| Proceso | Descartar los valores menores o iguales a 1. Inicializar la suma en cero. Recorrer con FOR desde 1 hasta la mitad entera del número y sumar los valores que lo dividen sin residuo. Comparar la suma con el número. |
| Salida | Valor lógico verdadero o falso; el programa de ejemplo muestra un mensaje. |

### Pseudocódigo en PSeInt

```pseint
Funcion resultado <- EsPerfecto(numero)
    Definir divisor, suma Como Entero;
    Definir resultado Como Logico;
    suma <- 0;
    resultado <- Falso;
    Si numero > 1 Entonces
        // Ningun divisor propio supera la mitad del numero.
        Para divisor <- 1 Hasta Trunc(numero / 2) Hacer
            Si numero MOD divisor = 0 Entonces
                suma <- suma + divisor;
            FinSi
        FinPara
        resultado <- suma = numero;
    FinSi
FinFuncion

Algoritmo ComprobarPerfecto
    Definir numero Como Entero;
    Escribir "Ingrese un numero entero:";
    Leer numero;
    Si EsPerfecto(numero) Entonces
        Escribir "Es perfecto.";
    SiNo
        Escribir "No es perfecto.";
    FinSi
FinAlgoritmo
```

<!-- pagebreak -->

## 2. Implementación y verificación

### Código documentado en Python

```python
def es_perfecto(numero: int) -> bool:
    """Comprueba si el entero es igual a la suma de divisores propios."""
    if numero <= 1:
        return False

    suma = 0
    # // calcula la mitad entera; +1 incluye esa mitad en el for.
    for divisor in range(1, numero // 2 + 1):
        if numero % divisor == 0:
            suma += divisor  # Acumula un divisor propio positivo.

    return suma == numero

# Ejemplo de uso de la funcion con un dato introducido por el usuario.
numero = int(input("Ingrese un número entero: "))
if es_perfecto(numero):
    print("Es perfecto.")
else:
    print("No es perfecto.")
```

### Pruebas y resultado

| Entrada | Resultado esperado | Suma de divisores propios |
| --- | --- | --- |
| -6, 0, 1 | Falso | Se descartan antes del FOR. |
| 6 | Verdadero | 1 + 2 + 3 = 6. |
| 28 | Verdadero | 1 + 2 + 4 + 7 + 14 = 28. |
| 12 | Falso | 1 + 2 + 3 + 4 + 6 = 16. |

Para un entero mayor que 1, ningún divisor propio positivo supera n / 2. Por eso basta recorrer hasta Trunc(n / 2) en PSeInt o numero // 2 en Python.

<!-- pagebreak -->

## 3. Programa: los primeros 20 números primos

Se reutiliza la función del ejercicio 1 y se examinan candidatos en orden creciente. Cada vez que se identifica un primo, se muestra y se incrementa el contador.

### EPS: Entrada - Proceso - Salida

| Elemento | Descripción |
| --- | --- |
| Entrada | No requiere datos del usuario. Se fijan la cantidad 20 y el límite de búsqueda 100. |
| Proceso | Recorrer con FOR los enteros de 2 a 100. Consultar EsPrimo para cada candidato hasta reunir 20 resultados. Contar únicamente los números primos encontrados. |
| Salida | Los primeros 20 números primos, uno por línea. |

### Pseudocódigo en PSeInt

```pseint
Funcion resultado <- EsPrimo(numero)
    Definir divisor Como Entero;
    Definir resultado Como Logico;
    resultado <- numero > 1;
    // Para 2, no hay divisores que comprobar.
    Si numero > 2 Entonces
        Para divisor <- 2 Hasta numero - 1 Hacer
            Si numero MOD divisor = 0 Entonces
                resultado <- Falso;
            FinSi
        FinPara
    FinSi
FinFuncion

Algoritmo PrimerosPrimos
    Definir numero, contador Como Entero;
    contador <- 0;
    Para numero <- 2 Hasta 100 Hacer
        Si contador < 20 Entonces
            Si EsPrimo(numero) Entonces
                Escribir numero;
                contador <- contador + 1;
            FinSi
        FinSi
    FinPara
FinAlgoritmo
```

<!-- pagebreak -->

## 3. Implementación y verificación

### Código documentado en Python

```python
def es_primo(numero: int) -> bool:
    """Devuelve True si el entero tiene exactamente dos divisores."""
    if numero <= 1:
        return False

    # range excluye su limite final: prueba de 2 a numero - 1.
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False  # Se encontro un divisor adicional.

    # En el caso de 2, el for no se ejecuta y se devuelve True.
    return True

contador = 0
# Se recorren candidatos en orden creciente, incluyendo 100.
for numero in range(2, 101):
    if es_primo(numero):
        print(numero)
        contador += 1
        if contador == 20:
            break  # Termina el for al completar la cantidad solicitada.
```

### Pruebas y resultado

**Salida esperada** (cada valor se imprime en una línea):

```text
2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
31, 37, 41, 43, 47, 53, 59, 61, 67, 71
```

El límite 100 es suficiente para esta cantidad: el vigésimo primo es 71. Python usa break para terminar al reunir 20; en PSeInt el FOR termina su recorrido hasta 100, pero el contador impide comprobar o imprimir más candidatos después del vigésimo resultado.

<!-- pagebreak -->

## 4. Programa: los primeros 4 números perfectos

Se reutiliza la función del ejercicio 2. Los candidatos se revisan en orden creciente y solo se muestran aquellos cuya suma de divisores propios coincide con el número.

### EPS: Entrada - Proceso - Salida

| Elemento | Descripción |
| --- | --- |
| Entrada | No requiere datos del usuario. Se fijan la cantidad 4 y el límite de búsqueda 10000. |
| Proceso | Recorrer con FOR los enteros de 2 a 10000. Consultar EsPerfecto hasta reunir 4 resultados. Incrementar el contador únicamente cuando se encuentre un número perfecto. |
| Salida | Los primeros 4 números perfectos, uno por línea. |

### Pseudocódigo en PSeInt

```pseint
Funcion resultado <- EsPerfecto(numero)
    Definir divisor, suma Como Entero;
    Definir resultado Como Logico;
    suma <- 0;
    resultado <- Falso;
    Si numero > 1 Entonces
        // Ningun divisor propio supera la mitad del numero.
        Para divisor <- 1 Hasta Trunc(numero / 2) Hacer
            Si numero MOD divisor = 0 Entonces
                suma <- suma + divisor;
            FinSi
        FinPara
        resultado <- suma = numero;
    FinSi
FinFuncion

Algoritmo PrimerosPerfectos
    Definir numero, contador Como Entero;
    contador <- 0;
    Para numero <- 2 Hasta 10000 Hacer
        Si contador < 4 Entonces
            Si EsPerfecto(numero) Entonces
                Escribir numero;
                contador <- contador + 1;
            FinSi
        FinSi
    FinPara
FinAlgoritmo
```

<!-- pagebreak -->

## 4. Implementación y verificación

### Código documentado en Python

```python
def es_perfecto(numero: int) -> bool:
    """Comprueba si el entero es igual a la suma de divisores propios."""
    if numero <= 1:
        return False

    suma = 0
    # // calcula la mitad entera; +1 incluye esa mitad en el for.
    for divisor in range(1, numero // 2 + 1):
        if numero % divisor == 0:
            suma += divisor  # Acumula un divisor propio positivo.

    return suma == numero

contador = 0
# Se recorren candidatos en orden creciente, incluyendo 10000.
for numero in range(2, 10001):
    if es_perfecto(numero):
        print(numero)
        contador += 1
        if contador == 4:
            break  # Termina el for al completar la cantidad solicitada.
```

### Pruebas y resultado

**Salida esperada:**

```text
6
28
496
8128
```

El límite 10000 es suficiente: el cuarto perfecto es 8128. Python termina con break al encontrarlo. PSeInt completa el recorrido, pero el contador evita evaluar candidatos adicionales. Son límites elegidos para estas cantidades concretas; si se piden más resultados, hay que revisar los límites de búsqueda.

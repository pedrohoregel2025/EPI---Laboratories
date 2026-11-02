# Pensamiento algorítmico: ciclo WHILE

Soluciones para estudiantes de ingeniería. Cada programa se ejecuta por separado.

## Criterios generales

- `Mientras` en PSeInt equivale a `while` en Python: repite instrucciones mientras una condición sea verdadera.
- La variable `continuar` inicia en `"S"` para permitir la primera ejecución. Al terminar cada operación se pregunta: **¿Desea continuar S/N?**
- `S` inicia otra operación y `N` termina el programa. Se aceptan minúsculas; cualquier otra respuesta vuelve a solicitarse mediante un segundo ciclo.
- Se supone que los datos numéricos se escriben correctamente. La validación de texto no numérico queda fuera del alcance de estos ejercicios.

## 1. División de dos números enteros

### EPS: Entrada - Proceso - Salida

| Elemento | Descripción |
| --- | --- |
| Entrada | Dividendo y divisor, ambos enteros; respuesta S/N. |
| Proceso | Verificar que el divisor sea diferente de cero. Calcular el cociente con `/` y el residuo con `MOD` (PSeInt) o `%` (Python). Si el residuo es cero, la división es exacta; en otro caso, no es exacta. Repetir mientras la respuesta sea S. |
| Salida | Cociente y mensaje que indica si la división es exacta. Si el divisor es cero, mostrar que la operación no se puede realizar. |

### Explicación

Una división entre enteros es **exacta si su residuo es cero**. Por ejemplo, 12 entre 3 es exacta; 13 entre 3 no lo es. No se determina la exactitud por la cantidad de decimales mostrados. Si el divisor es cero, no se calcula ni el cociente ni el residuo; después se pregunta si se desea continuar.

<!-- pagebreak -->

### Pseudocódigo en PSeInt

```pseint
Algoritmo DivisionConMientras
    Definir dividendo, divisor, residuo Como Entero;
    Definir cociente Como Real;
    Definir continuar Como Caracter;
    continuar <- "S";

    Mientras continuar = "S" Hacer
        Escribir "Ingrese el dividendo entero:";
        Leer dividendo;
        Escribir "Ingrese el divisor entero:";
        Leer divisor;

        Si divisor = 0 Entonces
            Escribir "No se puede dividir entre cero.";
        SiNo
            cociente <- dividendo / divisor;
            residuo <- dividendo MOD divisor;
            Escribir "Cociente: ", cociente;
            Si residuo = 0 Entonces
                Escribir "La division es exacta.";
            SiNo
                Escribir "La division no es exacta.";
            FinSi
        FinSi

        Escribir "¿Desea continuar S/N?";
        Leer continuar;
        continuar <- Mayusculas(continuar);
        Mientras continuar <> "S" Y continuar <> "N" Hacer
            Escribir "Respuesta invalida. Escriba S o N:";
            Leer continuar;
            continuar <- Mayusculas(continuar);
        FinMientras
    FinMientras
FinAlgoritmo
```

<!-- pagebreak -->

## 1. División: implementación y pruebas

### Código documentado en Python

```python
# Programa 1: división de dos enteros con un ciclo while.
continuar = "S"  # Permite entrar al ciclo por primera vez.

while continuar == "S":
    dividendo = int(input("Ingrese el dividendo entero: "))
    divisor = int(input("Ingrese el divisor entero: "))

    # Antes de dividir, comprobamos que el divisor no sea cero.
    if divisor == 0:
        print("No se puede dividir entre cero.")
    else:
        cociente = dividendo / divisor
        residuo = dividendo % divisor  # Resto de la división.
        print("Cociente:", cociente)

        # El residuo determina si la división es exacta.
        if residuo == 0:
            print("La división es exacta.")
        else:
            print("La división no es exacta.")

    # upper() admite s/n; strip() elimina espacios exteriores.
    continuar = input("¿Desea continuar S/N? ").strip().upper()
    while continuar != "S" and continuar != "N":
        continuar = input(
            "Respuesta inválida. Escriba S o N: "
        ).strip().upper()
```

### Casos de prueba

| Dividendo | Divisor | Resultado esperado |
| --- | --- | --- |
| 12 | 3 | Cociente 4.0; división exacta. |
| 13 | 3 | Cociente aproximado 4.3333; división no exacta. |
| 0 | 5 | Cociente 0.0; división exacta. |
| -12 | 3 | Cociente -4.0; división exacta. |
| 7 | 0 | Mensaje: no se puede dividir entre cero. |

**Prueba del ciclo:** ingresar 12 y 3, responder `s`, ingresar 13 y 3 y responder `n`. El programa debe realizar dos divisiones y terminar. Una respuesta como `X` debe provocar que se solicite nuevamente S/N.

**Observación:** Python puede mostrar más decimales que la tabla. La clasificación usa el residuo de los enteros y no depende del redondeo del cociente.

<!-- pagebreak -->

## 2. Cercanía del tercer número

### EPS: Entrada - Proceso - Salida

| Elemento | Descripción |
| --- | --- |
| Entrada | Tres números: primero, segundo y tercero; respuesta S/N. Se admiten enteros y decimales. |
| Proceso | Calcular distancia1 = valor absoluto de (tercero - primero) y distancia2 = valor absoluto de (tercero - segundo). Comparar las distancias. Repetir mientras la respuesta sea S. |
| Salida | Mensaje que indica si el tercero está más cerca del primero, del segundo o a la misma distancia de ambos. |

### Explicación

La distancia entre dos números se obtiene con el **valor absoluto de su diferencia**. El valor absoluto elimina el signo: por ejemplo, el valor absoluto de -5 es 5. La menor distancia indica el número más cercano.

Si el primero es 2, el segundo es 10 y el tercero es 7, las distancias son |7 - 2| = 5 y |7 - 10| = 3. Por tanto, el tercero está más cerca del segundo. Si las dos distancias son iguales, se informa un empate, incluso cuando el primero y el segundo son iguales.

### Relación entre los dos lenguajes

| PSeInt | Python | Función |
| --- | --- | --- |
| Mientras ... Hacer | while ...: | Repetir mientras la condición sea verdadera. |
| MOD | % | Obtener el residuo de una división entera. |
| Abs(...) | abs(...) | Obtener el valor absoluto. |
| Mayusculas(...) | .upper() | Convertir una respuesta a mayúsculas. |
| <- | = | Asignar un valor a una variable. |
| = | == | Comparar si dos valores son iguales. |

<!-- pagebreak -->

### Pseudocódigo en PSeInt

```pseint
Algoritmo CercaniaConMientras
    Definir primero, segundo, tercero Como Real;
    Definir distancia1, distancia2 Como Real;
    Definir continuar Como Caracter;
    continuar <- "S";

    Mientras continuar = "S" Hacer
        Escribir "Ingrese el primer numero:";
        Leer primero;
        Escribir "Ingrese el segundo numero:";
        Leer segundo;
        Escribir "Ingrese el tercer numero:";
        Leer tercero;

        distancia1 <- Abs(tercero - primero);
        distancia2 <- Abs(tercero - segundo);

        Si distancia1 < distancia2 Entonces
            Escribir "El tercero esta mas cerca del primero.";
        SiNo
            Si distancia2 < distancia1 Entonces
                Escribir "El tercero esta mas cerca del segundo.";
            SiNo
                Escribir "El tercero esta a igual distancia de ambos.";
            FinSi
        FinSi

        Escribir "¿Desea continuar S/N?";
        Leer continuar;
        continuar <- Mayusculas(continuar);
        Mientras continuar <> "S" Y continuar <> "N" Hacer
            Escribir "Respuesta invalida. Escriba S o N:";
            Leer continuar;
            continuar <- Mayusculas(continuar);
        FinMientras
    FinMientras
FinAlgoritmo
```

<!-- pagebreak -->

## 2. Cercanía: implementación y pruebas

### Código documentado en Python

```python
# Programa 2: determinar a qué número está más cerca el tercero.
continuar = "S"  # Permite ejecutar la primera comparación.

while continuar == "S":
    # float permite leer números enteros o con decimales.
    primero = float(input("Ingrese el primer número: "))
    segundo = float(input("Ingrese el segundo número: "))
    tercero = float(input("Ingrese el tercer número: "))

    # abs() obtiene la distancia sin importar el signo.
    distancia1 = abs(tercero - primero)
    distancia2 = abs(tercero - segundo)

    # La distancia menor identifica el número más cercano.
    if distancia1 < distancia2:
        print("El tercero está más cerca del primero.")
    elif distancia2 < distancia1:
        print("El tercero está más cerca del segundo.")
    else:
        print("El tercero está a igual distancia de ambos.")

    # Validamos la respuesta antes de repetir o terminar.
    continuar = input("¿Desea continuar S/N? ").strip().upper()
    while continuar != "S" and continuar != "N":
        continuar = input(
            "Respuesta inválida. Escriba S o N: "
        ).strip().upper()
```

### Casos de prueba

| Primero | Segundo | Tercero | Distancias (1, 2) | Resultado esperado |
| --- | --- | --- | --- | --- |
| 2 | 10 | 3 | 1, 7 | Más cerca del primero. |
| 2 | 10 | 7 | 5, 3 | Más cerca del segundo. |
| 2 | 10 | 6 | 4, 4 | Igual distancia de ambos. |
| -8 | -2 | -7 | 1, 5 | Más cerca del primero. |
| 5 | 5 | 9 | 4, 4 | Igual distancia de ambos. |
| 1.5 | 4.5 | 4 | 2.5, 0.5 | Más cerca del segundo. |

**Prueba del ciclo:** ingresar 2, 10 y 3, responder `S`; después ingresar 2, 10 y 6 y responder `N`. Debe mostrar primero cercanía al primero y después igual distancia, y terminar.

**Uso de decimales:** en Python se escriben con punto, por ejemplo `1.5`. Los números `float` tienen precisión limitada; estos ejercicios comparan directamente las distancias calculadas. Para los casos sencillos de la tabla, las comparaciones son exactas.


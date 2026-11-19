# W13 Integración por fracciones parciales

**Asignatura:** Cálculo Diferencial e Integral  
**Actividad:** Laboratorio de la semana 13  
**Documento de origen:** s13-a01-laboratorio.docx

Se resuelven las cuatro integrales del laboratorio y el modelo de crecimiento poblacional. Cada solución incluye la factorización del denominador, el cálculo de las constantes, la integración y una comprobación. En el modelo se distingue la familia general de soluciones de la solución que satisface la condición inicial.

## Ideas para aplicar el método

Las fracciones parciales permiten expresar una función racional como suma de fracciones más sencillas. Antes de comenzar, verificamos que el grado del numerador sea menor que el del denominador; si no lo es, primero hacemos una división de polinomios.

Para un factor lineal simple se propone un numerador constante. Para un factor cuadrático que no se puede factorizar en números reales se propone un numerador lineal:

$$
\frac{A}{x-a},\qquad
\frac{Bx+D}{x^2+px+q}.
$$

Las letras representan constantes por determinar. Al multiplicar por el denominador común se obtiene una identidad polinómica. Podemos calcular las constantes sustituyendo valores convenientes o igualando coeficientes.

Usaremos las fórmulas:

$$
\int\frac{dx}{x-a}=\ln|x-a|+C,
$$

$$
\int\frac{f'(x)}{f(x)}\,dx=\ln|f(x)|+C,
$$

$$
\int\frac{dz}{z^2+a^2}
=\frac1a\arctan\left(\frac za\right)+C,
\qquad a>0.
$$

La letra \(C\) será la constante de integración. Las antiderivadas se entienden en cada intervalo del dominio; las constantes pueden ser diferentes en intervalos separados por singularidades.

## Ejercicio 1

$$
I_1=\int\frac{2x+3}{x^2-x-6}\,dx.
$$

### Paso 1 Factorizar el denominador

Buscamos dos números cuyo producto sea \(-6\) y cuya suma sea \(-1\): son \(-3\) y \(2\). Entonces:

$$
x^2-x-6=(x-3)(x+2).
$$

El dominio excluye \(x=3\) y \(x=-2\).

### Paso 2 Proponer las fracciones parciales

Como los factores son lineales y distintos:

$$
\frac{2x+3}{(x-3)(x+2)}
=\frac{A}{x-3}+\frac{B}{x+2}.
$$

Multiplicamos por el denominador común:

$$
2x+3=A(x+2)+B(x-3).
$$

### Paso 3 Calcular las constantes

Sustituimos \(x=3\) en la identidad polinómica:

$$
9=5A\quad\Longrightarrow\quad A=\frac95.
$$

Sustituimos \(x=-2\):

$$
-1=-5B\quad\Longrightarrow\quad B=\frac15.
$$

Estas sustituciones se hacen en la identidad obtenida tras eliminar denominadores, no en la fracción original, que no está definida en esos puntos.

La descomposición es:

$$
\boxed{\frac{2x+3}{x^2-x-6}
=\frac{9}{5(x-3)}+\frac{1}{5(x+2)}}.
$$

### Paso 4 Integrar

$$
I_1=\frac95\int\frac{dx}{x-3}
+\frac15\int\frac{dx}{x+2}.
$$

$$
\boxed{I_1=\frac95\ln|x-3|+\frac15\ln|x+2|+C}.
$$

### Comprobación

Derivamos y reunimos las fracciones:

$$
\begin{aligned}
I_1'&=\frac{9}{5(x-3)}+\frac{1}{5(x+2)}\\
&=\frac{9(x+2)+(x-3)}{5(x-3)(x+2)}\\
&=\frac{10x+15}{5(x-3)(x+2)}
=\frac{2x+3}{x^2-x-6}.
\end{aligned}
$$

## Ejercicio 2

$$
I_2=\int\frac5{x^3-x}\,dx.
$$

### Paso 1 Factorizar el denominador

Extraemos el factor común y aplicamos diferencia de cuadrados:

$$
x^3-x=x(x^2-1)=x(x-1)(x+1).
$$

El dominio excluye \(x=-1\), \(x=0\) y \(x=1\).

### Paso 2 Proponer las fracciones parciales

Usamos una constante para cada factor lineal:

$$
\frac5{x(x-1)(x+1)}
=\frac A{x}+\frac B{x-1}+\frac D{x+1}.
$$

Multiplicamos por el denominador común:

$$
5=A(x-1)(x+1)+Bx(x+1)+Dx(x-1).
$$

### Paso 3 Calcular las constantes

Para \(x=0\):

$$
5=-A\quad\Longrightarrow\quad A=-5.
$$

Para \(x=1\):

$$
5=2B\quad\Longrightarrow\quad B=\frac52.
$$

Para \(x=-1\):

$$
5=2D\quad\Longrightarrow\quad D=\frac52.
$$

Por tanto:

$$
\boxed{\frac5{x^3-x}
=-\frac5x+\frac5{2(x-1)}+\frac5{2(x+1)}}.
$$

### Paso 4 Integrar

$$
I_2=-5\int\frac{dx}{x}
+\frac52\int\frac{dx}{x-1}
+\frac52\int\frac{dx}{x+1}.
$$

$$
\boxed{I_2=-5\ln|x|+\frac52\ln|x-1|+\frac52\ln|x+1|+C}.
$$

Una forma equivalente, en el mismo dominio, es:

$$
I_2=\frac52\ln|x^2-1|-5\ln|x|+C.
$$

### Comprobación

Derivando la forma equivalente:

$$
\begin{aligned}
I_2'&=\frac52\frac{2x}{x^2-1}-\frac5x\\
&=\frac{5x^2-5(x^2-1)}{x(x^2-1)}\\
&=\frac5{x^3-x}.
\end{aligned}
$$

## Ejercicio 3

$$
I_3=\int\frac1{(x-1)(x+2)}\,dx.
$$

### Paso 1 Identificar los factores

El denominador ya está factorizado en dos factores lineales distintos. El dominio excluye \(x=1\) y \(x=-2\).

### Paso 2 Proponer las fracciones parciales

$$
\frac1{(x-1)(x+2)}=\frac A{x-1}+\frac B{x+2}.
$$

Eliminamos los denominadores:

$$
1=A(x+2)+B(x-1).
$$

### Paso 3 Calcular las constantes

Para \(x=1\):

$$
1=3A\quad\Longrightarrow\quad A=\frac13.
$$

Para \(x=-2\):

$$
1=-3B\quad\Longrightarrow\quad B=-\frac13.
$$

Así:

$$
\boxed{\frac1{(x-1)(x+2)}
=\frac1{3(x-1)}-\frac1{3(x+2)}}.
$$

### Paso 4 Integrar

$$
I_3=\frac13\int\frac{dx}{x-1}
-\frac13\int\frac{dx}{x+2}.
$$

$$
\boxed{I_3=\frac13\ln|x-1|-\frac13\ln|x+2|+C}.
$$

También puede escribirse:

$$
I_3=\frac13\ln\left|\frac{x-1}{x+2}\right|+C.
$$

### Comprobación

$$
\begin{aligned}
I_3'&=\frac1{3(x-1)}-\frac1{3(x+2)}\\
&=\frac{(x+2)-(x-1)}{3(x-1)(x+2)}\\
&=\frac1{(x-1)(x+2)}.
\end{aligned}
$$

## Ejercicio 4

$$
I_4=\int\frac{x^2+3x+2}{(x+1)(x^2+2x+3)}\,dx.
$$

### Paso 1 Analizar la factorización

El numerador se factoriza como:

$$
x^2+3x+2=(x+1)(x+2).
$$

El factor cuadrático del denominador no tiene raíces reales, pues:

$$
\Delta=2^2-4(1)(3)=-8<0.
$$

Al completar el cuadrado:

$$
x^2+2x+3=(x+1)^2+2>0.
$$

Por tanto, el único valor excluido del dominio original es \(x=-1\).

### Paso 2 Proponer las fracciones parciales

Para mostrar el procedimiento solicitado, proponemos una constante sobre el factor lineal y un numerador lineal sobre el cuadrático:

$$
\frac{x^2+3x+2}{(x+1)(x^2+2x+3)}
=\frac A{x+1}+\frac{Bx+D}{x^2+2x+3}.
$$

Multiplicamos por el denominador común:

$$
x^2+3x+2=A(x^2+2x+3)+(Bx+D)(x+1).
$$

### Paso 3 Calcular las constantes

Al expandir y agrupar:

$$
x^2+3x+2=(A+B)x^2+(2A+B+D)x+(3A+D).
$$

Igualamos coeficientes:

$$
\begin{cases}
A+B=1,\\
2A+B+D=3,\\
3A+D=2.
\end{cases}
$$

De la primera y tercera ecuaciones:

$$
B=1-A,\qquad D=2-3A.
$$

Sustituimos en la segunda:

$$
2A+(1-A)+(2-3A)=3
\quad\Longrightarrow\quad -2A=0.
$$

Entonces:

$$
\boxed{A=0,\qquad B=1,\qquad D=2}.
$$

La descomposición queda:

$$
\frac{x^2+3x+2}{(x+1)(x^2+2x+3)}
=\frac{x+2}{x^2+2x+3},\qquad x\ne-1.
$$

Esto también se obtiene cancelando el factor común \(x+1\). La cancelación simplifica la expresión, pero conservamos la exclusión \(x=-1\) del problema original.

### Paso 4 Separar el numerador

La derivada del denominador es \(2x+2\). Escribimos:

$$
x+2=\frac12(2x+2)+1.
$$

Así:

$$
I_4=\frac12\int\frac{2x+2}{x^2+2x+3}\,dx
+\int\frac{dx}{x^2+2x+3}.
$$

La primera integral produce un logaritmo:

$$
\frac12\int\frac{2x+2}{x^2+2x+3}\,dx
=\frac12\ln(x^2+2x+3).
$$

No necesitamos valor absoluto porque el argumento es siempre positivo.

### Paso 5 Integrar el término cuadrático

Completamos el cuadrado y usamos \(z=x+1\), con \(dz=dx\):

$$
\int\frac{dx}{x^2+2x+3}
=\int\frac{dz}{z^2+2}
=\frac1{\sqrt2}\arctan\left(\frac z{\sqrt2}\right).
$$

Por tanto:

$$
\boxed{I_4=\frac12\ln(x^2+2x+3)
+\frac1{\sqrt2}\arctan\left(\frac{x+1}{\sqrt2}\right)+C},
\qquad x\ne-1.
$$

### Comprobación

El término con tangente inversa tiene derivada:

$$
\frac{d}{dx}\left[\frac1{\sqrt2}\arctan\left(\frac{x+1}{\sqrt2}\right)\right]
=\frac{1/2}{1+(x+1)^2/2}
=\frac1{x^2+2x+3}.
$$

En consecuencia:

$$
\begin{aligned}
I_4'&=\frac{x+1}{x^2+2x+3}+\frac1{x^2+2x+3}\\
&=\frac{x+2}{x^2+2x+3}\\
&=\frac{x^2+3x+2}{(x+1)(x^2+2x+3)},\qquad x\ne-1.
\end{aligned}
$$

## Ejercicio 5 Modelo de crecimiento poblacional

El modelo proporcionado es:

$$
\frac{dP}{dt}=\frac{P}{t^2+t},\qquad P(1)=P_0.
$$

Aquí \(P(t)\) representa la población y \(P_0\) es su valor en el instante \(t=1\). Aunque el subíndice sea cero, la condición inicial está dada en 1.

### Paso 1 Establecer el dominio y separar variables

Factorizamos:

$$
t^2+t=t(t+1).
$$

La ecuación no está definida en \(t=0\) ni en \(t=-1\). El intervalo máximo que contiene el instante inicial \(t=1\) es \(t>0\).

Para una población positiva podemos dividir entre \(P\):

$$
\frac{dP}{P}=\frac{dt}{t(t+1)}.
$$

La solución \(P(t)=0\), que se pierde temporalmente al dividir entre \(P\), también satisface la ecuación y se recuperará en la familia final.

### Paso 2 Descomponer la fracción racional

$$
\frac1{t(t+1)}=\frac A{t}+\frac B{t+1}.
$$

Multiplicamos por el denominador:

$$
1=A(t+1)+Bt=(A+B)t+A.
$$

Igualando coeficientes:

$$
A=1,\qquad A+B=0\quad\Longrightarrow\quad B=-1.
$$

Entonces:

$$
\boxed{\frac1{t(t+1)}=\frac1t-\frac1{t+1}}.
$$

### Paso 3 Integrar y obtener la solución general

$$
\int\frac{dP}{P}=\int\left(\frac1t-\frac1{t+1}\right)dt.
$$

Así:

$$
\ln|P|=\ln|t|-\ln|t+1|+C.
$$

Para \(t>0\), el cociente \(t/(t+1)\) es positivo. Al exponenciar y absorber la constante multiplicativa, obtenemos:

$$
\boxed{P(t)=K\frac{t}{t+1}},\qquad t>0.
$$

Esta es la familia general en el intervalo de interés. Para poblaciones positivas, \(K>0\). También admite \(K=0\), que representa la población nula. Como solución matemática, la misma fórmula vale en cualquier intervalo que no cruce 0 ni \(-1\), con una constante propia de cada intervalo.

### Paso 4 Aplicar la condición inicial

Usamos \(P(1)=P_0\):

$$
P_0=K\frac1{1+1}=\frac K2.
$$

Por tanto:

$$
K=2P_0.
$$

La solución particular es:

$$
\boxed{P(t)=\frac{2P_0t}{t+1}},\qquad t>0.
$$

Si se estudia solamente la evolución a partir del dato inicial, se toma \(t\ge1\).

### Paso 5 Comprobar la ecuación y el dato inicial

Derivamos:

$$
P'(t)=2P_0\frac{(t+1)-t}{(t+1)^2}
=\frac{2P_0}{(t+1)^2}.
$$

Evaluamos el lado derecho del modelo:

$$
\frac{P(t)}{t^2+t}
=\frac{2P_0t}{t+1}\frac1{t(t+1)}
=\frac{2P_0}{(t+1)^2}=P'(t).
$$

Además:

$$
P(1)=\frac{2P_0}{2}=P_0.
$$

Se cumplen tanto la ecuación diferencial como la condición inicial.

### Interpretación del modelo

Si \(P_0>0\), entonces \(P'(t)>0\): la población aumenta. Sin embargo, su tasa de crecimiento disminuye con el tiempo:

$$
P''(t)=-\frac{4P_0}{(t+1)^3}<0,\qquad t>0.
$$

Su comportamiento a largo plazo es:

$$
\lim_{t\to\infty}P(t)
=2P_0\lim_{t\to\infty}\frac{t}{t+1}
=\boxed{2P_0}.
$$

De acuerdo con este modelo, la población se aproxima al doble de su valor en el instante inicial. Para \(t\ge1\) y \(P_0>0\), se cumple \(P_0\le P(t)<2P_0\); no alcanza el valor límite en un tiempo finito.

## Resumen de resultados

### Integral 1

$$
\int\frac{2x+3}{x^2-x-6}\,dx
=\frac95\ln|x-3|+\frac15\ln|x+2|+C.
$$

Dominio: \(x\ne3,-2\).

### Integral 2

$$
\int\frac5{x^3-x}\,dx
=-5\ln|x|+\frac52\ln|x-1|+\frac52\ln|x+1|+C.
$$

Dominio: \(x\ne-1,0,1\).

### Integral 3

$$
\int\frac1{(x-1)(x+2)}\,dx
=\frac13\ln|x-1|-\frac13\ln|x+2|+C.
$$

Dominio: \(x\ne1,-2\).

### Integral 4

$$
\begin{aligned}
\int\frac{x^2+3x+2}{(x+1)(x^2+2x+3)}\,dx
&=\frac12\ln(x^2+2x+3)\\
&\quad+\frac1{\sqrt2}\arctan\left(\frac{x+1}{\sqrt2}\right)+C.
\end{aligned}
$$

Dominio original: \(x\ne-1\).

### Modelo poblacional

Solución general en el intervalo que contiene el dato inicial:

$$
P(t)=K\frac{t}{t+1},\qquad t>0.
$$

Solución con \(P(1)=P_0\):

$$
P(t)=\frac{2P_0t}{t+1},\qquad t>0.
$$

## Aspectos para recordar

- **Factoriza antes de descomponer.** Cada factor del denominador determina la forma de una fracción parcial.
- **Usa un numerador lineal para un factor cuadrático irreducible.** Su término con \(x\) puede ser necesario, como ocurre en el ejercicio 4.
- **Conserva las restricciones del dominio original.** Cancelar un factor no permite reincorporar automáticamente los valores excluidos.
- **Incluye valor absoluto en los logaritmos cuando corresponda.** Esto permite expresar las primitivas en intervalos donde los factores lineales son negativos.
- **Distingue la solución general de la particular.** La condición inicial determina la constante del modelo.
- **Comprueba derivando.** En una ecuación diferencial, verifica también que se cumpla el dato inicial.

Las expresiones dentro del texto usan delimitadores `\( ... \)` y las ecuaciones independientes usan bloques `$$ ... $$`. Las fórmulas se presentan fuera de tablas para conservar el formato que funcionó en los documentos anteriores. No se requieren imágenes externas.

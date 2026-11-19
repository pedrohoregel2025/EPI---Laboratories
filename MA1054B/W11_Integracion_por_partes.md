# W11 Integración por partes y potencias trigonométricas

**Asignatura:** Cálculo Diferencial e Integral  
**Actividad:** Laboratorio individual  
**Documento de origen:** Laboratorio individualcolaborativa int partes y pot trig-1.docx

Este documento desarrolla las diez integrales del laboratorio, en su orden original. En cada ejercicio se explica la elección del método, se muestra el procedimiento y se comprueba la respuesta mediante derivación.

## Integrales identificadas

### Integral 1

$$
\int x^3\cos x\,dx
$$

**Método:** Integración por partes repetida.

### Integral 2

$$
\int 3x^4\sin(2x)\,dx
$$

**Método:** Integración por partes repetida.

### Integral 3

$$
\int\sin^2 x\,dx
$$

**Método:** Reducción de potencia.

### Integral 4

$$
\int(2x+3)\ln x\,dx
$$

**Método:** Integración por partes.

### Integral 5

$$
\int e^{2x}(2x+1)^2\,dx
$$

**Método:** Integración por partes repetida.

### Integral 6

$$
\int\sin^3(2x)\cos^5(2x)\,dx
$$

**Método:** Identidad trigonométrica y sustitución.

### Integral 7

$$
\int\sec^3 x\,dx
$$

**Método:** Integración por partes y despeje.

### Integral 8

$$
\int 8x\arctan(x)\,dx
$$

**Método:** Integración por partes.

### Integral 9

$$
\int\sin^4 x\cos^2 x\,dx
$$

**Método:** Reducción de potencias.

### Integral 10

$$
\int\sec^5 x\tan x\,dx
$$

**Método:** Sustitución.

**Notas de lectura del original.** Las expresiones se recuperaron de las ecuaciones incrustadas de Word, conservando exponentes y argumentos. En el ejercicio 3 el original omite el diferencial; se completa con \(dx\). En el ejercicio 8 aparece \(\tan^{-1}(x)\), que aquí se interpreta como la función inversa \(\arctan(x)\), cuya derivada es \(1/(1+x^2)\); no como el recíproco \(1/\tan x\). La notación «sen» del original se escribe como \(\sin\).

## Herramientas que utilizaremos

La fórmula de integración por partes se obtiene de la regla de derivación de un producto:

$$
d(uv)=u\,dv+v\,du
\quad\Longrightarrow\quad
\boxed{\int u\,dv=uv-\int v\,du}.
$$

Conviene elegir \(u\) de modo que su derivada simplifique el problema, y \(dv\) de modo que podamos integrarlo. En un producto de un polinomio y una función trigonométrica o exponencial, derivar el polinomio reduce su grado. En un producto que contiene un logaritmo o una función trigonométrica inversa, suele convenir derivar esa función.

Para las potencias trigonométricas emplearemos:

$$
\sin^2 t+\cos^2 t=1,\qquad
\tan^2 t=\sec^2 t-1,
$$

$$
\sin^2 t=\frac{1-\cos(2t)}2,\qquad
\cos^2 t=\frac{1+\cos(2t)}2.
$$

Todos los ángulos se consideran en radianes. La letra \(C\) representa una constante arbitraria de integración. En los cálculos auxiliares se omiten las constantes y se añade una sola \(C\) al resultado final.

## Ejercicio 1

$$
I_1=\int x^3\cos x\,dx.
$$

**Elección del método.** Aplicamos integración por partes tres veces, porque cada derivación de \(x^3\) reduce su grado.

**Paso 1.** Elegimos:

$$
u=x^3,\quad du=3x^2\,dx,
\qquad dv=\cos x\,dx,\quad v=\sin x.
$$

Entonces:

$$
I_1=x^3\sin x-3\int x^2\sin x\,dx.
$$

**Paso 2.** Para \(J=\int x^2\sin x\,dx\), tomamos:

$$
u=x^2,\quad du=2x\,dx,
\qquad dv=\sin x\,dx,\quad v=-\cos x.
$$

Así:

$$
J=-x^2\cos x+2\int x\cos x\,dx.
$$

**Paso 3.** Para \(K=\int x\cos x\,dx\), elegimos \(u=x\) y \(dv=\cos x\,dx\):

$$
K=x\sin x-\int\sin x\,dx=x\sin x+\cos x.
$$

**Paso 4.** Sustituimos de regreso:

$$
J=-x^2\cos x+2x\sin x+2\cos x,
$$

$$
\boxed{I_1=x^3\sin x+3x^2\cos x-6x\sin x-6\cos x+C}.
$$

**Comprobación.** Al derivar, los términos adicionales se cancelan:

$$
\begin{aligned}
I_1'&=3x^2\sin x+x^3\cos x
+6x\cos x-3x^2\sin x\\
&\quad-6\sin x-6x\cos x+6\sin x\\
&=x^3\cos x.
\end{aligned}
$$

## Ejercicio 2

$$
I_2=\int 3x^4\sin(2x)\,dx.
$$

**Elección del método.** Derivamos el polinomio e integramos la función trigonométrica repetidamente. Hay que conservar los factores \(1/2\) que aparecen al integrar funciones con argumento \(2x\).

**Paso 1.** Tomamos:

$$
u=3x^4,\quad du=12x^3\,dx,
\qquad dv=\sin(2x)\,dx,\quad v=-\frac12\cos(2x).
$$

Por partes:

$$
I_2=-\frac32x^4\cos(2x)+6\int x^3\cos(2x)\,dx.
$$

**Paso 2.** Llamamos \(A=\int x^3\cos(2x)\,dx\). Elegimos \(u=x^3\), \(du=3x^2\,dx\), \(dv=\cos(2x)\,dx\) y \(v=\frac12\sin(2x)\):

$$
A=\frac12x^3\sin(2x)-\frac32\int x^2\sin(2x)\,dx.
$$

**Paso 3.** Para \(B=\int x^2\sin(2x)\,dx\), usamos \(u=x^2\), \(du=2x\,dx\), \(dv=\sin(2x)\,dx\) y \(v=-\frac12\cos(2x)\):

$$
B=-\frac12x^2\cos(2x)+\int x\cos(2x)\,dx.
$$

**Paso 4.** Para \(D=\int x\cos(2x)\,dx\), elegimos \(u=x\) y \(dv=\cos(2x)\,dx\):

$$
D=\frac12x\sin(2x)-\frac12\int\sin(2x)\,dx
=\frac12x\sin(2x)+\frac14\cos(2x).
$$

**Paso 5.** Sustituimos:

$$
B=-\frac12x^2\cos(2x)+\frac12x\sin(2x)+\frac14\cos(2x),
$$

$$
A=\frac12x^3\sin(2x)+\frac34x^2\cos(2x)
-\frac34x\sin(2x)-\frac38\cos(2x).
$$

Finalmente:

$$
\boxed{
\begin{aligned}
I_2={}&-\frac32x^4\cos(2x)+3x^3\sin(2x)
+\frac92x^2\cos(2x)\\
&-\frac92x\sin(2x)-\frac94\cos(2x)+C.
\end{aligned}}
$$

**Comprobación.** Agrupando las cancelaciones en la derivada:

$$
\begin{aligned}
I_2'={}&3x^4\sin(2x)
+(-6x^3+6x^3)\cos(2x)\\
&+(9x^2-9x^2)\sin(2x)
+(9x-9x)\cos(2x)\\
&+\left(-\frac92+\frac92\right)\sin(2x)
=3x^4\sin(2x).
\end{aligned}
$$

## Ejercicio 3

$$
I_3=\int\sin^2 x\,dx.
$$

**Elección del método.** La potencia es par. La identidad de reducción de potencia transforma el integrando en una suma de funciones que podemos integrar directamente.

**Paso 1.** Aplicamos:

$$
\sin^2 x=\frac{1-\cos(2x)}2.
$$

**Paso 2.** Separamos e integramos:

$$
\begin{aligned}
I_3&=\frac12\int 1\,dx-\frac12\int\cos(2x)\,dx\\
&=\frac{x}{2}-\frac14\sin(2x)+C.
\end{aligned}
$$

$$
\boxed{I_3=\frac{x}{2}-\frac{\sin(2x)}4+C}.
$$

**Comprobación.**

$$
\frac{d}{dx}\left(\frac{x}{2}-\frac{\sin(2x)}4\right)
=\frac12-\frac12\cos(2x)=\sin^2 x.
$$

**Observación didáctica.** No se puede aplicar directamente la regla de potencias como si \(\sin x\) fuera la variable de integración: para sustituir \(t=\sin x\) haría falta el factor \(\cos x\,dx\).

## Ejercicio 4

$$
I_4=\int(2x+3)\ln x\,dx,\qquad x>0.
$$

**Elección del método.** Derivar \(\ln x\) produce \(1/x\), que simplifica el producto con una primitiva del polinomio.

**Paso 1.** Elegimos:

$$
u=\ln x,\quad du=\frac1x\,dx,
\qquad dv=(2x+3)\,dx,\quad v=x^2+3x.
$$

**Paso 2.** Aplicamos la fórmula:

$$
I_4=(x^2+3x)\ln x-\int\frac{x^2+3x}{x}\,dx.
$$

**Paso 3.** Simplificamos e integramos:

$$
I_4=(x^2+3x)\ln x-\int(x+3)\,dx.
$$

$$
\boxed{I_4=(x^2+3x)\ln x-\frac{x^2}{2}-3x+C},\qquad x>0.
$$

**Comprobación.**

$$
\begin{aligned}
I_4'&=(2x+3)\ln x+\frac{x^2+3x}{x}-x-3\\
&=(2x+3)\ln x.
\end{aligned}
$$

**Dominio.** El integrando original contiene \(\ln x\), de modo que en números reales se trabaja con \(x>0\).

## Ejercicio 5

$$
I_5=\int e^{2x}(2x+1)^2\,dx.
$$

**Elección del método.** Derivamos el factor polinómico e integramos el exponencial. Dos aplicaciones de integración por partes bastan para eliminar el polinomio de la integral restante.

**Paso 1.** Elegimos:

$$
u=(2x+1)^2,\quad du=4(2x+1)\,dx,
\qquad dv=e^{2x}\,dx,\quad v=\frac12e^{2x}.
$$

Así:

$$
I_5=\frac12e^{2x}(2x+1)^2-2\int e^{2x}(2x+1)\,dx.
$$

**Paso 2.** Sea \(J=\int e^{2x}(2x+1)\,dx\). Tomamos:

$$
u=2x+1,\quad du=2\,dx,
\qquad dv=e^{2x}\,dx,\quad v=\frac12e^{2x}.
$$

Entonces:

$$
J=\frac12e^{2x}(2x+1)-\int e^{2x}\,dx
=\frac12e^{2x}(2x+1)-\frac12e^{2x}.
$$

**Paso 3.** Sustituimos y simplificamos:

$$
\begin{aligned}
I_5&=\frac12e^{2x}(2x+1)^2-e^{2x}(2x+1)+e^{2x}+C\\
&=e^{2x}\left[\frac12(4x^2+4x+1)-(2x+1)+1\right]+C.
\end{aligned}
$$

$$
\boxed{I_5=e^{2x}\left(2x^2+\frac12\right)+C}.
$$

**Comprobación.**

$$
\begin{aligned}
I_5'&=2e^{2x}\left(2x^2+\frac12\right)+4xe^{2x}\\
&=e^{2x}(4x^2+4x+1)=e^{2x}(2x+1)^2.
\end{aligned}
$$

## Ejercicio 6

$$
I_6=\int\sin^3(2x)\cos^5(2x)\,dx.
$$

**Elección del método.** Las dos potencias son impares. Podemos reservar un factor seno o un factor coseno. Reservaremos \(\sin(2x)\,dx\) y convertiremos el seno restante en una expresión de coseno.

**Paso 1.** Usamos \(\sin^2(2x)=1-\cos^2(2x)\):

$$
I_6=\int[1-\cos^2(2x)]\cos^5(2x)\sin(2x)\,dx.
$$

**Paso 2.** Hacemos la sustitución:

$$
t=\cos(2x),\qquad dt=-2\sin(2x)\,dx,
\qquad\sin(2x)\,dx=-\frac12dt.
$$

Por tanto:

$$
I_6=-\frac12\int(1-t^2)t^5\,dt
=-\frac12\int(t^5-t^7)\,dt.
$$

**Paso 3.** Integramos y regresamos a \(x\):

$$
I_6=-\frac{t^6}{12}+\frac{t^8}{16}+C.
$$

$$
\boxed{I_6=-\frac{\cos^6(2x)}{12}+\frac{\cos^8(2x)}{16}+C}.
$$

**Comprobación.**

$$
\begin{aligned}
I_6'&=\cos^5(2x)\sin(2x)-\cos^7(2x)\sin(2x)\\
&=\cos^5(2x)\sin(2x)[1-\cos^2(2x)]\\
&=\sin^3(2x)\cos^5(2x).
\end{aligned}
$$

**Observación didáctica.** El factor \(-1/2\) es indispensable: proviene de la regla de la cadena aplicada al argumento \(2x\).

## Ejercicio 7

$$
I_7=\int\sec^3 x\,dx.
$$

**Elección del método.** Escribimos \(\sec^3 x=\sec x\sec^2 x\). Al integrar por partes reaparece la integral original, lo que permite despejarla.

**Paso 1.** Elegimos:

$$
u=\sec x,\quad du=\sec x\tan x\,dx,
\qquad dv=\sec^2 x\,dx,\quad v=\tan x.
$$

Obtenemos:

$$
I_7=\sec x\tan x-\int\sec x\tan^2 x\,dx.
$$

**Paso 2.** Aplicamos \(\tan^2 x=\sec^2 x-1\):

$$
\begin{aligned}
I_7&=\sec x\tan x-\int\sec x(\sec^2 x-1)\,dx\\
&=\sec x\tan x-I_7+\int\sec x\,dx.
\end{aligned}
$$

Por tanto, trabajando con primitivas y reuniendo las constantes al final:

$$
2I_7=\sec x\tan x+\int\sec x\,dx.
$$

**Paso 3.** Para la integral restante, multiplicamos por una fracción igual a uno:

$$
\int\sec x\,dx
=\int\frac{\sec x\tan x+\sec^2 x}{\sec x+\tan x}\,dx.
$$

Con \(t=\sec x+\tan x\) se tiene \(dt=(\sec x\tan x+\sec^2 x)\,dx\). Así:

$$
\int\sec x\,dx=\int\frac{dt}{t}=\ln|\sec x+\tan x|+C.
$$

**Paso 4.** Sustituimos y dividimos entre dos:

$$
\boxed{I_7=\frac12\sec x\tan x+\frac12\ln|\sec x+\tan x|+C}.
$$

**Comprobación.** Primero:

$$
\frac{d}{dx}\ln|\sec x+\tan x|
=\frac{\sec x\tan x+\sec^2 x}{\sec x+\tan x}=\sec x.
$$

Entonces:

$$
\begin{aligned}
I_7'&=\frac12(\sec x\tan^2 x+\sec^3 x)+\frac12\sec x\\
&=\frac12\sec x(\sec^2 x-1)+\frac12\sec^3 x+\frac12\sec x\\
&=\sec^3 x.
\end{aligned}
$$

**Dominio.** La respuesta se aplica en cada intervalo donde \(\cos x\ne0\), es decir, sin cruzar los puntos \(x=\pi/2+k\pi\), con \(k\in\mathbb Z\). En estos intervalos \(\sec x+\tan x\) nunca es cero, pues \((\sec x+\tan x)(\sec x-\tan x)=1\).

## Ejercicio 8

$$
I_8=\int 8x\tan^{-1}(x)\,dx
=\int 8x\arctan(x)\,dx.
$$

**Elección del método.** Derivamos la función inversa tangente para obtener una función racional e integramos el factor \(8x\).

**Paso 1.** Tomamos:

$$
u=\arctan x,\quad du=\frac{dx}{1+x^2},
\qquad dv=8x\,dx,\quad v=4x^2.
$$

Por partes:

$$
I_8=4x^2\arctan x-4\int\frac{x^2}{1+x^2}\,dx.
$$

**Paso 2.** Reescribimos la fracción:

$$
\frac{x^2}{1+x^2}
=\frac{(1+x^2)-1}{1+x^2}
=1-\frac1{1+x^2}.
$$

**Paso 3.** Integramos:

$$
\begin{aligned}
I_8&=4x^2\arctan x-4\int\left(1-\frac1{1+x^2}\right)dx\\
&=4x^2\arctan x-4x+4\arctan x+C.
\end{aligned}
$$

$$
\boxed{I_8=4(x^2+1)\arctan x-4x+C}.
$$

**Comprobación.**

$$
I_8'=8x\arctan x+4\frac{x^2+1}{1+x^2}-4
=8x\arctan x.
$$

## Ejercicio 9

$$
I_9=\int\sin^4 x\cos^2 x\,dx.
$$

**Elección del método.** Ambas potencias son pares. Usamos reducción de potencias hasta obtener una suma de cosenos de distintos múltiplos de \(x\).

**Paso 1.** Sea \(c=\cos(2x)\), como abreviatura algebraica, sin cambiar la variable de integración. Entonces:

$$
\begin{aligned}
\sin^4 x\cos^2 x
&=\left(\frac{1-c}{2}\right)^2\left(\frac{1+c}{2}\right)\\
&=\frac18(1-2c+c^2)(1+c)\\
&=\frac18(1-c-c^2+c^3).
\end{aligned}
$$

**Paso 2.** Reducimos las potencias de \(c\):

$$
c^2=\cos^2(2x)=\frac{1+\cos(4x)}2.
$$

La identidad del ángulo triple \(\cos(3t)=4\cos^3t-3\cos t\) nos da:

$$
c^3=\cos^3(2x)=\frac{3\cos(2x)+\cos(6x)}4.
$$

**Paso 3.** Sustituimos y reunimos términos:

$$
\begin{aligned}
\sin^4 x\cos^2 x
&=\frac18\left[1-\cos(2x)-\frac{1+\cos(4x)}2
+\frac{3\cos(2x)+\cos(6x)}4\right]\\
&=\frac1{16}-\frac1{32}\cos(2x)
-\frac1{16}\cos(4x)+\frac1{32}\cos(6x).
\end{aligned}
$$

**Paso 4.** Integramos cada término, recordando que \(\int\cos(kx)\,dx=\sin(kx)/k\):

$$
\boxed{I_9=\frac{x}{16}-\frac{\sin(2x)}{64}
-\frac{\sin(4x)}{64}+\frac{\sin(6x)}{192}+C}.
$$

**Comprobación.**

$$
I_9'=\frac1{16}-\frac{\cos(2x)}{32}
-\frac{\cos(4x)}{16}+\frac{\cos(6x)}{32}
=\sin^4 x\cos^2 x,
$$

por la identidad obtenida en el paso 3.

## Ejercicio 10

$$
I_{10}=\int\sec^5 x\tan x\,dx.
$$

**Elección del método.** La derivada de \(\sec x\) es \(\sec x\tan x\). Reservamos ese producto para hacer una sustitución directa.

**Paso 1.** Separamos:

$$
I_{10}=\int\sec^4 x\,[\sec x\tan x\,dx].
$$

**Paso 2.** Elegimos:

$$
t=\sec x,\qquad dt=\sec x\tan x\,dx.
$$

Entonces:

$$
I_{10}=\int t^4\,dt=\frac{t^5}{5}+C.
$$

**Paso 3.** Volvemos a la variable original:

$$
\boxed{I_{10}=\frac{\sec^5 x}{5}+C}.
$$

**Comprobación.**

$$
\frac{d}{dx}\left(\frac{\sec^5 x}{5}\right)
=\frac15\cdot5\sec^4 x\cdot\sec x\tan x
=\sec^5 x\tan x.
$$

**Dominio.** La respuesta es válida en cada intervalo donde \(\cos x\ne0\).

## Resumen de resultados

En todas las respuestas se incluye una constante arbitraria \(C\).

### Resultado 1

$$
x^3\sin x+3x^2\cos x-6x\sin x-6\cos x+C
$$

### Resultado 2

$$
\begin{aligned} &-\frac32x^4\cos(2x)+3x^3\sin(2x)+\frac92x^2\cos(2x)\\ &\quad-\frac92x\sin(2x)-\frac94\cos(2x)+C. \end{aligned}
$$

### Resultado 3

$$
\frac{x}{2}-\frac{\sin(2x)}4+C
$$

### Resultado 4

$$
(x^2+3x)\ln x-\frac{x^2}{2}-3x+C
$$

Válido para \(x>0\).

### Resultado 5

$$
e^{2x}(2x^2+\frac12)+C
$$

### Resultado 6

$$
-\frac{\cos^6(2x)}{12}+\frac{\cos^8(2x)}{16}+C
$$

### Resultado 7

$$
\frac12\sec x\tan x+\frac12\ln\lvert\sec x+\tan x\rvert+C
$$

### Resultado 8

$$
4(x^2+1)\arctan x-4x+C
$$

### Resultado 9

$$
\frac{x}{16}-\frac{\sin(2x)}{64}-\frac{\sin(4x)}{64}+\frac{\sin(6x)}{192}+C
$$

### Resultado 10

$$
\frac{\sec^5 x}{5}+C
$$

En los ejercicios 7 y 10 se excluyen los puntos \(x=\pi/2+k\pi\), \(k\in\mathbb Z\). La constante puede ser diferente en cada intervalo separado del dominio. Los demás ejercicios, salvo el 4, tienen integrandos definidos en todos los números reales.

## Recomendaciones para resolver ejercicios similares

- **Antes de integrar, identifica la estructura.** Un producto no obliga a usar integración por partes: en el ejercicio 10 la sustitución resuelve el problema directamente.
- **En integración por partes, busca simplificar la integral restante.** Derivar un polinomio reduce su grado; derivar un logaritmo o una función trigonométrica inversa suele producir una función racional.
- **Con potencias impares de seno o coseno, reserva un factor para el diferencial.** Convierte los factores restantes mediante \(\sin^2 t+\cos^2 t=1\).
- **Con potencias pares de seno y coseno, usa reducción de potencias.** Repite las identidades hasta obtener funciones integrables directamente.
- **Conserva los factores de la regla de la cadena y revisa los signos.** En particular, \(\int\sin(2x)\,dx=-\cos(2x)/2\).
- **Comprueba derivando.** La derivada de tu respuesta debe reproducir exactamente el integrando original.

**Lectura del archivo:** las fórmulas dentro del texto usan los delimitadores `\( ... \)` y las ecuaciones independientes usan bloques `$$ ... $$`. El visor debe admitir estos delimitadores matemáticos para mostrar las fórmulas. No se requieren imágenes externas.

# W12 Antiderivadas

**Asignatura:** Cálculo Diferencial e Integral  
**Actividad:** Laboratorio de la semana 12  
**Documento de origen:** Actividad Laboratorio semana 12-1.docx

Este documento resuelve las tres partes del laboratorio: elección del método, identificación de los elementos de integración por partes y desarrollo de las integrales. Se incluyen procedimientos, resultados y comprobaciones.

La notación «sen» del original se representa como \(\sin\), y «arcsen» como \(\arcsin\). Para precisar los argumentos, expresiones como «ln9x» se escriben \(\ln(9x)\), y «cos4x³» se escribe \(\cos(4x^3)\). Los ángulos se consideran en radianes.

## Herramientas de trabajo

Una antiderivada de una función \(f\) es una función \(F\) cuya derivada es \(f\). En un intervalo, las antiderivadas de una misma función difieren en una constante:

$$
F'(x)=f(x)
\quad\Longrightarrow\quad
\int f(x)\,dx=F(x)+C.
$$

Para integrar por partes utilizamos:

$$
\boxed{\int u\,dv=uv-\int v\,du}.
$$

Elegimos \(u\) de modo que su derivada simplifique el problema y \(dv\) de modo que podamos integrarlo. Si el integrando contiene una función compuesta junto con un factor proporcional a la derivada de su argumento, conviene considerar primero una sustitución.

Para una integral definida con integrando continuo en el intervalo:

$$
\int_a^b f(x)\,dx=F(b)-F(a).
$$

En las integrales indefinidas se añade \(C\). En las definidas, las constantes se cancelan al evaluar los extremos.

## Parte I Elección del método

La actividad pide identificar cuáles integrales conviene resolver por partes. Aunque el enunciado utiliza el singular, **los incisos b y d se resuelven naturalmente por partes**. Los incisos a y c admiten sustitución directa.

### Inciso a

$$
\int\frac{\ln t}{4t}\,dt.
$$

**Método recomendado: sustitución.** El factor \(1/t\) es la derivada de \(\ln t\).

Tomamos:

$$
z=\ln t,\qquad dz=\frac{dt}{t}.
$$

Entonces:

$$
\int\frac{\ln t}{4t}\,dt
=\frac14\int z\,dz
=\frac{z^2}{8}+C.
$$

$$
\boxed{\int\frac{\ln t}{4t}\,dt=\frac{(\ln t)^2}{8}+C},\qquad t>0.
$$

**Comprobación:**

$$
\frac{d}{dt}\left(\frac{(\ln t)^2}{8}\right)
=\frac{2\ln t}{8t}=\frac{\ln t}{4t}.
$$

### Inciso b

$$
\int x\sin(8x)\,dx.
$$

**Método recomendado: integración por partes.** Derivar \(x\) lo convierte en una constante; integrar \(\sin(8x)\) es directo.

Los elementos son:

$$
u=x,\qquad du=dx,
\qquad dv=\sin(8x)\,dx,\qquad v=-\frac18\cos(8x).
$$

El resultado, desarrollado y comprobado en la parte III, inciso a, es:

$$
\boxed{\int x\sin(8x)\,dx
=-\frac{x\cos(8x)}8+\frac{\sin(8x)}{64}+C}.
$$

### Inciso c

$$
\int x^2\cos(4x^3)\,dx.
$$

**Método recomendado: sustitución.** La derivada del argumento \(4x^3\) es \(12x^2\), proporcional al factor exterior.

Tomamos:

$$
z=4x^3,\qquad dz=12x^2\,dx,
\qquad x^2\,dx=\frac{dz}{12}.
$$

Por tanto:

$$
\int x^2\cos(4x^3)\,dx
=\frac1{12}\int\cos z\,dz.
$$

$$
\boxed{\int x^2\cos(4x^3)\,dx=\frac{\sin(4x^3)}{12}+C}.
$$

**Comprobación:**

$$
\frac{d}{dx}\left(\frac{\sin(4x^3)}{12}\right)
=\frac1{12}\cos(4x^3)\cdot12x^2
=x^2\cos(4x^3).
$$

### Inciso d

$$
\int4\arcsin(7x)\,dx.
$$

**Método recomendado: integración por partes.** Podemos pensar el integrando como el producto de \(\arcsin(7x)\) por la constante \(4\). Derivar la función inversa seno permite resolver la integral restante por sustitución.

Elegimos:

$$
u=\arcsin(7x),\qquad du=\frac7{\sqrt{1-49x^2}}\,dx,
\qquad dv=4\,dx,\qquad v=4x.
$$

El resultado, desarrollado y comprobado en la parte III, inciso b, es:

$$
\boxed{\int4\arcsin(7x)\,dx
=4x\arcsin(7x)+\frac47\sqrt{1-49x^2}+C}.
$$

La comprobación por derivación se realiza para \(-1/7<x<1/7\). El integrando y la expresión obtenida también tienen valores continuos en los extremos \(x=\pm1/7\).

## Parte II Elementos de integración por partes

Se presentan los cuatro elementos solicitados, \(u\), \(dv\), \(du\) y \(v\), junto con la solución de cada integral. **La cuarta y la quinta entrada de la tabla original son idénticas**, por lo que comparten elementos y resultado.

### Primera entrada

$$
\int x^2\ln x\,dx,\qquad x>0.
$$

**Elementos solicitados:**

$$
u=\ln x,\qquad dv=x^2\,dx,
$$

$$
du=\frac{dx}{x},\qquad v=\frac{x^3}{3}.
$$

**Razón de la elección.** La derivada del logaritmo elimina esa función y deja una potencia de \(x\) fácil de integrar.

Aplicamos la fórmula:

$$
\begin{aligned}
\int x^2\ln x\,dx
&=\frac{x^3}{3}\ln x-\int\frac{x^3}{3}\frac{dx}{x}\\
&=\frac{x^3}{3}\ln x-\frac13\int x^2\,dx.
\end{aligned}
$$

$$
\boxed{\int x^2\ln x\,dx=\frac{x^3\ln x}{3}-\frac{x^3}{9}+C}.
$$

**Comprobación:**

$$
\frac{d}{dx}\left(\frac{x^3\ln x}{3}-\frac{x^3}{9}\right)
=x^2\ln x+\frac{x^2}{3}-\frac{x^2}{3}=x^2\ln x.
$$

### Segunda entrada

$$
\int11\arctan(6x)\,dx.
$$

**Elementos solicitados:**

$$
u=\arctan(6x),\qquad dv=11\,dx,
$$

$$
du=\frac6{1+36x^2}\,dx,\qquad v=11x.
$$

**Paso 1.** Aplicamos integración por partes:

$$
\int11\arctan(6x)\,dx
=11x\arctan(6x)-66\int\frac{x}{1+36x^2}\,dx.
$$

**Paso 2.** En la integral restante usamos:

$$
z=1+36x^2,\qquad dz=72x\,dx.
$$

Así:

$$
\int\frac{x}{1+36x^2}\,dx
=\frac1{72}\int\frac{dz}{z}
=\frac1{72}\ln(1+36x^2).
$$

Como \(1+36x^2>0\) para todo número real, no hace falta valor absoluto en este logaritmo.

**Resultado:**

$$
\boxed{\int11\arctan(6x)\,dx
=11x\arctan(6x)-\frac{11}{12}\ln(1+36x^2)+C}.
$$

**Comprobación:**

$$
\begin{aligned}
\frac{d}{dx}\left[11x\arctan(6x)-\frac{11}{12}\ln(1+36x^2)\right]
&=11\arctan(6x)+\frac{66x}{1+36x^2}-\frac{66x}{1+36x^2}\\
&=11\arctan(6x).
\end{aligned}
$$

### Tercera entrada

$$
\int7\ln(9x)\,dx,\qquad x>0.
$$

**Elementos solicitados:**

$$
u=\ln(9x),\qquad dv=7\,dx,
$$

$$
du=\frac{dx}{x},\qquad v=7x.
$$

Al derivar el logaritmo se aplica la regla de la cadena:

$$
\frac{d}{dx}\ln(9x)=\frac9{9x}=\frac1x.
$$

Por partes:

$$
\int7\ln(9x)\,dx
=7x\ln(9x)-\int7x\frac{dx}{x}
=7x\ln(9x)-7x+C.
$$

$$
\boxed{\int7\ln(9x)\,dx=7x\ln(9x)-7x+C}.
$$

**Comprobación:**

$$
\frac{d}{dx}[7x\ln(9x)-7x]
=7\ln(9x)+7-7=7\ln(9x).
$$

### Cuarta entrada

$$
I=\int_0^\pi4x^2\sin(3x)\,dx.
$$

**Elementos solicitados para la primera aplicación:**

$$
u=4x^2,\qquad dv=\sin(3x)\,dx,
$$

$$
du=8x\,dx,\qquad v=-\frac13\cos(3x).
$$

**Paso 1.** Aplicamos integración por partes conservando los límites:

$$
I=\left[-\frac43x^2\cos(3x)\right]_0^\pi
+\frac83\int_0^\pi x\cos(3x)\,dx.
$$

**Paso 2.** Para la integral auxiliar \(J\), aplicamos partes de nuevo:

$$
J=\int_0^\pi x\cos(3x)\,dx,
$$

$$
u=x,\qquad du=dx,
\qquad dv=\cos(3x)\,dx,\qquad v=\frac13\sin(3x).
$$

Entonces:

$$
\begin{aligned}
J&=\left[\frac{x\sin(3x)}3\right]_0^\pi
-\frac13\int_0^\pi\sin(3x)\,dx\\
&=\left[\frac{x\sin(3x)}3+\frac{\cos(3x)}9\right]_0^\pi.
\end{aligned}
$$

Como \(\sin(3\pi)=0\), \(\cos(3\pi)=-1\), \(\sin0=0\) y \(\cos0=1\):

$$
J=-\frac19-\frac19=-\frac29.
$$

**Paso 3.** Evaluamos el término de frontera y sustituimos:

$$
\left[-\frac43x^2\cos(3x)\right]_0^\pi=\frac{4\pi^2}{3}.
$$

$$
\boxed{I=\frac{4\pi^2}{3}-\frac{16}{27}}.
$$

**Comprobación con una primitiva.** Las dos aplicaciones de partes producen:

$$
F(x)=-\frac43x^2\cos(3x)+\frac89x\sin(3x)+\frac8{27}\cos(3x).
$$

Su derivada es:

$$
\begin{aligned}
F'(x)&=-\frac83x\cos(3x)+4x^2\sin(3x)
+\frac89\sin(3x)+\frac83x\cos(3x)-\frac89\sin(3x)\\
&=4x^2\sin(3x).
\end{aligned}
$$

Además:

$$
F(\pi)-F(0)
=\left(\frac{4\pi^2}{3}-\frac8{27}\right)-\frac8{27}
=\frac{4\pi^2}{3}-\frac{16}{27}.
$$

### Quinta entrada

El documento vuelve a presentar exactamente:

$$
\int_0^\pi4x^2\sin(3x)\,dx.
$$

Por ello, los elementos que completan la quinta entrada son:

$$
\boxed{u=4x^2,\qquad dv=\sin(3x)\,dx,
\qquad du=8x\,dx,\qquad v=-\frac13\cos(3x)}.
$$

El procedimiento es el de la cuarta entrada y su valor es:

$$
\boxed{\frac{4\pi^2}{3}-\frac{16}{27}}.
$$

## Parte III Resolución de las integrales

### Inciso a

$$
I_a=\int x\sin(8x)\,dx.
$$

**Paso 1.** Elegimos:

$$
u=x,\qquad du=dx,
\qquad dv=\sin(8x)\,dx,\qquad v=-\frac18\cos(8x).
$$

**Paso 2.** Aplicamos integración por partes:

$$
I_a=-\frac{x\cos(8x)}8+\frac18\int\cos(8x)\,dx.
$$

**Paso 3.** Integramos el término restante:

$$
\int\cos(8x)\,dx=\frac18\sin(8x).
$$

$$
\boxed{I_a=-\frac{x\cos(8x)}8+\frac{\sin(8x)}{64}+C}.
$$

**Comprobación:**

$$
\frac{d}{dx}\left[-\frac{x\cos(8x)}8+\frac{\sin(8x)}{64}\right]
=-\frac{\cos(8x)}8+x\sin(8x)+\frac{\cos(8x)}8
=x\sin(8x).
$$

### Inciso b

$$
I_b=\int4\arcsin(7x)\,dx.
$$

**Paso 1.** Elegimos:

$$
u=\arcsin(7x),\qquad du=\frac7{\sqrt{1-49x^2}}\,dx,
\qquad dv=4\,dx,\qquad v=4x.
$$

**Paso 2.** Aplicamos integración por partes:

$$
I_b=4x\arcsin(7x)-28\int\frac{x}{\sqrt{1-49x^2}}\,dx.
$$

**Paso 3.** Resolvemos la integral restante por sustitución:

$$
z=1-49x^2,\qquad dz=-98x\,dx.
$$

Por tanto:

$$
\begin{aligned}
\int\frac{x}{\sqrt{1-49x^2}}\,dx
&=-\frac1{98}\int z^{-1/2}\,dz\\
&=-\frac1{49}\sqrt z
=-\frac1{49}\sqrt{1-49x^2}.
\end{aligned}
$$

**Paso 4.** Sustituimos y simplificamos:

$$
I_b=4x\arcsin(7x)+\frac{28}{49}\sqrt{1-49x^2}+C.
$$

$$
\boxed{I_b=4x\arcsin(7x)+\frac47\sqrt{1-49x^2}+C}.
$$

**Comprobación**, para \(|x|<1/7\):

$$
\begin{aligned}
I_b'&=4\arcsin(7x)+\frac{28x}{\sqrt{1-49x^2}}
-\frac{28x}{\sqrt{1-49x^2}}\\
&=4\arcsin(7x).
\end{aligned}
$$

### Inciso c

$$
I_c=\int7\ln(9x)\,dx,\qquad x>0.
$$

Esta integral coincide con la tercera entrada de la parte II. Sus elementos son:

$$
u=\ln(9x),\qquad du=\frac{dx}{x},
\qquad dv=7\,dx,\qquad v=7x.
$$

Aplicando la fórmula:

$$
I_c=7x\ln(9x)-\int7x\frac{dx}{x}
=7x\ln(9x)-7\int dx.
$$

$$
\boxed{I_c=7x\ln(9x)-7x+C}.
$$

La comprobación es \(I_c'=7\ln(9x)+7-7=7\ln(9x)\).

### Inciso d

$$
I_d=\int_3^4\frac{7\ln(7x)}{x^9}\,dx.
$$

**Lectura de la ecuación.** Los límites son 3 y 4; el numerador es \(7\ln(7x)\) y el denominador es \(x^9\). El integrando es continuo en todo el intervalo \([3,4]\).

**Paso 1.** Escribimos el integrando como un producto y elegimos los elementos:

$$
\frac{7\ln(7x)}{x^9}=\ln(7x)\cdot7x^{-9},
$$

$$
u=\ln(7x),\qquad du=\frac{dx}{x},
\qquad dv=7x^{-9}\,dx,\qquad v=-\frac7{8x^8}.
$$

**Paso 2.** Aplicamos integración por partes con límites:

$$
\begin{aligned}
I_d&=\left[-\frac{7\ln(7x)}{8x^8}\right]_3^4
-\int_3^4\left(-\frac7{8x^8}\right)\frac{dx}{x}\\
&=\left[-\frac{7\ln(7x)}{8x^8}\right]_3^4
+\frac78\int_3^4x^{-9}\,dx.
\end{aligned}
$$

**Paso 3.** Usamos la regla de potencias:

$$
\int x^{-9}\,dx=-\frac1{8x^8}+C.
$$

Por tanto:

$$
I_d=\left[-\frac{7\ln(7x)}{8x^8}-\frac7{64x^8}\right]_3^4
=\left[-\frac{7[8\ln(7x)+1]}{64x^8}\right]_3^4.
$$

**Paso 4.** Evaluamos el extremo superior menos el inferior:

$$
I_d=-\frac{7[8\ln(28)+1]}{64\cdot4^8}
+\frac{7[8\ln(21)+1]}{64\cdot3^8}.
$$

$$
\boxed{I_d=\frac7{64}\left[
\frac{8\ln(21)+1}{3^8}
-\frac{8\ln(28)+1}{4^8}\right]}.
$$

**Comprobación de la primitiva.** Para \(x>0\), sea:

$$
F(x)=-\frac78x^{-8}\ln(7x)-\frac7{64}x^{-8}.
$$

Entonces:

$$
\begin{aligned}
F'(x)&=7x^{-9}\ln(7x)-\frac78x^{-9}+\frac78x^{-9}\\
&=\frac{7\ln(7x)}{x^9}.
\end{aligned}
$$

El valor de la integral es positivo, de acuerdo con que \(\ln(7x)>0\) y \(x^9>0\) en el intervalo de integración.

## Resumen de resultados

### Parte I

**a — Sustitución:**

$$
\int\frac{\ln t}{4t}\,dt=\frac{(\ln t)^2}{8}+C,\qquad t>0.
$$

**b — Por partes:**

$$
\int x\sin(8x)\,dx=-\frac{x\cos(8x)}8+\frac{\sin(8x)}{64}+C.
$$

**c — Sustitución:**

$$
\int x^2\cos(4x^3)\,dx=\frac{\sin(4x^3)}{12}+C.
$$

**d — Por partes:**

$$
\int4\arcsin(7x)\,dx=4x\arcsin(7x)+\frac47\sqrt{1-49x^2}+C.
$$

### Parte II

**Primera entrada:**

$$
\int x^2\ln x\,dx=\frac{x^3\ln x}{3}-\frac{x^3}{9}+C,\qquad x>0.
$$

**Segunda entrada:**

$$
\int11\arctan(6x)\,dx
=11x\arctan(6x)-\frac{11}{12}\ln(1+36x^2)+C.
$$

**Tercera entrada:**

$$
\int7\ln(9x)\,dx=7x\ln(9x)-7x+C,\qquad x>0.
$$

**Cuarta y quinta entradas:**

$$
\int_0^\pi4x^2\sin(3x)\,dx=\frac{4\pi^2}{3}-\frac{16}{27}.
$$

### Parte III

Los incisos a, b y c coinciden, respectivamente, con I-b, I-d y II-tercera entrada. El resultado del inciso d es:

$$
\int_3^4\frac{7\ln(7x)}{x^9}\,dx
=\frac7{64}\left[\frac{8\ln(21)+1}{3^8}-\frac{8\ln(28)+1}{4^8}\right].
$$

## Observaciones para el estudio

- **Un producto no exige integración por partes.** En I-c, la sustitución aprovecha la derivada del argumento del coseno.
- **Un logaritmo o una función trigonométrica inversa puede integrarse por partes aunque no aparezca un factor polinómico.** Podemos usar la constante como parte de \(dv\).
- **La regla de la cadena determina los coeficientes.** Al integrar \(\sin(8x)\) aparece el factor \(-1/8\); al derivar \(\ln(9x)\), el resultado es \(1/x\).
- **En una integral definida se resta el valor en el límite inferior.** Los corchetes de evaluación ayudan a conservar los signos.
- **El valor de una integral definida representa acumulación con signo.** En la integral de \(4x^2\sin(3x)\) hay contribuciones positivas y negativas; su valor no es el área geométrica total.

Las fórmulas dentro del texto usan delimitadores `\( ... \)` y las ecuaciones independientes usan `$$ ... $$`, siguiendo el formato del documento de la semana 11. No se requieren imágenes externas.

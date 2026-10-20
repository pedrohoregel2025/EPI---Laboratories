# Cálculo mental 1 — Ejercicios resueltos

**Curso:** Cálculo Diferencial  
**Documento base:** *Cálculo mental 1*

> Nota: en los ejercicios que solicitan una gráfica se propone una función concreta que satisface la condición. En varios casos existen muchas respuestas correctas posibles.

---

## 1. Función cuya derivada sea de grado dos

Se requiere una función que, al derivarse, produzca un polinomio de grado 2.

Una opción sencilla es:

$$
f(x)=x^3
$$

Derivando:

$$
f'(x)=3x^2
$$

Como $3x^2$ es un polinomio de grado 2, la condición se cumple.

**Respuesta:**

$$
\boxed{f(x)=x^3}
$$

**Observación:** cualquier función cúbica de la forma

$$
f(x)=ax^3+bx^2+cx+d,\qquad a\neq 0
$$

tendrá una derivada de grado 2.

---

## 2. Función con dos puntos donde la segunda derivada sea cero

Se propone:

$$
f(x)=x^4-2x^2
$$

Primera derivada:

$$
f'(x)=4x^3-4x
$$

Segunda derivada:

$$
f''(x)=12x^2-4
$$

Buscamos los puntos donde:

$$
f''(x)=0
$$

Entonces:

$$
12x^2-4=0
$$

$$
12x^2=4
$$

$$
x^2=\frac{1}{3}
$$

$$
\boxed{x=\pm\frac{1}{\sqrt{3}}}
$$

Las coordenadas correspondientes son:

$$
f\left(\pm\frac{1}{\sqrt3}\right)
=
\frac19-\frac23
=
-\frac59
$$

Por tanto:

$$
\boxed{
\left(-\frac1{\sqrt3},-\frac59\right),
\left(\frac1{\sqrt3},-\frac59\right)
}
$$

![Gráfica del ejercicio 2](Calculo_mental_1_material/graficas/ejercicio_02.png)

**Observación:** que $f''(x)=0$ no garantiza por sí solo un punto de inflexión. En este ejemplo sí existe cambio de concavidad en ambos puntos.

---

## 3. Función con dos puntos críticos con $f'(x)=0$

Se propone:

$$
f(x)=x^3-3x
$$

Derivando:

$$
f'(x)=3x^2-3
$$

Buscamos:

$$
f'(x)=0
$$

$$
3x^2-3=0
$$

$$
x^2=1
$$

$$
\boxed{x=-1,\;x=1}
$$

Calculamos las coordenadas:

$$
f(-1)=2,\qquad f(1)=-2
$$

Por tanto, los puntos críticos son:

$$
\boxed{(-1,2)\quad\text{y}\quad(1,-2)}
$$

Además:

$$
f''(x)=6x
$$

Como $f''(-1)<0$, el punto $(-1,2)$ es un **máximo relativo**.  
Como $f''(1)>0$, el punto $(1,-2)$ es un **mínimo relativo**.

![Gráfica del ejercicio 3](Calculo_mental_1_material/graficas/ejercicio_03.png)

---

## 4. Función con dos puntos no derivables

Se requiere que en dos puntos no exista la primera derivada.

Una función sencilla es:

$$
f(x)=|x-1|+|x+1|
$$

Puede expresarse como:

$$
f(x)=
\begin{cases}
-2x, & x<-1\\
2, & -1\le x\le 1\\
2x, & x>1
\end{cases}
$$

En $x=-1$, la pendiente por la izquierda es $-2$ y por la derecha es $0$. Por ello:

$$
\boxed{f'(-1)\text{ no existe}}
$$

En $x=1$, la pendiente por la izquierda es $0$ y por la derecha es $2$. Por ello:

$$
\boxed{f'(1)\text{ no existe}}
$$

Los puntos no derivables son:

$$
\boxed{(-1,2)\quad\text{y}\quad(1,2)}
$$

![Gráfica del ejercicio 4](Calculo_mental_1_material/graficas/ejercicio_04.png)

**Observación:** la función es continua en ambos puntos, pero no es derivable porque presenta esquinas.

---

## 5. Función con máximos absolutos

Se propone:

$$
f(x)=-(x^2-1)^2
$$

Como:

$$
(x^2-1)^2\ge 0
$$

entonces:

$$
-(x^2-1)^2\le 0
$$

El valor máximo posible es $0$. Esto ocurre cuando:

$$
x^2-1=0
$$

$$
x=\pm 1
$$

Así, los dos máximos absolutos son:

$$
\boxed{(-1,0)\quad\text{y}\quad(1,0)}
$$

y el valor máximo absoluto es:

$$
\boxed{f_{\max}=0}
$$

![Gráfica del ejercicio 5](Calculo_mental_1_material/graficas/ejercicio_05.png)

---

## 6. Función con mínimos relativos

Se propone:

$$
f(x)=(x^2-1)^2
$$

Derivando:

$$
f'(x)=4x(x^2-1)
$$

Los puntos críticos satisfacen:

$$
4x(x^2-1)=0
$$

por lo que:

$$
x=-1,\;0,\;1
$$

La segunda derivada es:

$$
f''(x)=12x^2-4
$$

Para $x=-1$ y $x=1$:

$$
f''(\pm1)=8>0
$$

Por ello, ambos son mínimos relativos.

Además:

$$
f(-1)=f(1)=0
$$

Así:

$$
\boxed{(-1,0)\quad\text{y}\quad(1,0)}
$$

son mínimos relativos. En este ejemplo también son mínimos absolutos.

![Gráfica del ejercicio 6](Calculo_mental_1_material/graficas/ejercicio_06.png)

---

## 7. Función cuya primera derivada sea siempre negativa

Se propone:

$$
f(x)=e^{-x}
$$

Derivando:

$$
f'(x)=-e^{-x}
$$

Como:

$$
e^{-x}>0
$$

para todo número real $x$, entonces:

$$
\boxed{f'(x)<0\quad\text{para toda }x}
$$

Por lo tanto, la función es siempre decreciente.

![Gráfica del ejercicio 7](Calculo_mental_1_material/graficas/ejercicio_07.png)

**Idea clave:**

$$
f'(x)<0\quad\Longrightarrow\quad f(x)\text{ es decreciente}
$$

---

## 8. Función que se mueva a razón variable

Interpretamos la función como la posición de un objeto respecto al tiempo:

$$
s(t)=t^2
$$

La velocidad es la derivada de la posición:

$$
v(t)=s'(t)=2t
$$

La velocidad depende del tiempo, por lo que la razón de cambio no es constante.

Por ejemplo:

$$
v(1)=2,\qquad v(2)=4,\qquad v(3)=6
$$

Por ello:

$$
\boxed{\text{el objeto se mueve a razón variable}}
$$

![Gráfica del ejercicio 8](Calculo_mental_1_material/graficas/ejercicio_08.png)

**Observación:** una función lineal no sería adecuada, porque su derivada sería constante.

---

## 9. ¿Qué función derivo y el resultado es $\frac{2}{x}$?

Se busca una función $f(x)$ tal que:

$$
f'(x)=\frac{2}{x}
$$

Integramos:

$$
f(x)=\int \frac{2}{x}\,dx
$$

$$
f(x)=2\int \frac{1}{x}\,dx
$$

Sabemos que:

$$
\int \frac{1}{x}\,dx=\ln|x|
$$

Por tanto:

$$
\boxed{f(x)=2\ln|x|+C}
$$

con:

$$
\boxed{x\neq0}
$$

Verificación:

$$
\frac{d}{dx}\left(2\ln|x|+C\right)=\frac{2}{x}
$$

**Observación:** el valor absoluto es importante porque permite considerar tanto $x>0$ como $x<0$ dentro del dominio correspondiente.

---

## 10. Derivada de $\tan x$

Partimos de:

$$
\tan x=\frac{\sin x}{\cos x}
$$

Aplicamos la regla del cociente:

$$
\frac{d}{dx}(\tan x)
=
\frac{\cos x(\cos x)-\sin x(-\sin x)}{\cos^2x}
$$

$$
=
\frac{\cos^2x+\sin^2x}{\cos^2x}
$$

Usando:

$$
\sin^2x+\cos^2x=1
$$

obtenemos:

$$
\frac{1}{\cos^2x}=\sec^2x
$$

Por tanto:

$$
\boxed{\frac{d}{dx}(\tan x)=\sec^2x}
$$

La expresión es válida donde $\tan x$ está definida:

$$
x\neq \frac{\pi}{2}+k\pi,\qquad k\in\mathbb{Z}
$$

---

# Resumen de respuestas

| Ejercicio | Respuesta principal |
|---|---|
| 1 | $f(x)=x^3$, porque $f'(x)=3x^2$ |
| 2 | $f(x)=x^4-2x^2$; $f''(x)=0$ en $x=\pm1/\sqrt3$ |
| 3 | $f(x)=x^3-3x$; puntos críticos en $(-1,2)$ y $(1,-2)$ |
| 4 | $f(x)=|x-1|+|x+1|$; no derivable en $x=-1,1$ |
| 5 | $f(x)=-(x^2-1)^2$; máximos absolutos en $(-1,0)$ y $(1,0)$ |
| 6 | $f(x)=(x^2-1)^2$; mínimos relativos en $(-1,0)$ y $(1,0)$ |
| 7 | $f(x)=e^{-x}$; $f'(x)=-e^{-x}<0$ |
| 8 | $s(t)=t^2$; $v(t)=2t$, razón variable |
| 9 | $f(x)=2\ln|x|+C$ |
| 10 | $\dfrac{d}{dx}(\tan x)=\sec^2x$ |

---

## Observaciones generales

- $f'(x)=0$ permite localizar candidatos a máximos, mínimos u otros puntos críticos.
- $f''(x)=0$ identifica candidatos a puntos de inflexión, pero debe verificarse el cambio de concavidad.
- Una función puede ser continua y no derivable.
- Si $f'(x)<0$ en todo un intervalo, la función es decreciente en ese intervalo.
- En problemas de movimiento, la derivada de la posición representa la velocidad.
- En el ejercicio 9, la respuesta correcta es $2\ln|x|+C$ porque la expresión solicitada en el documento es $\frac{2}{x}$.

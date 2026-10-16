# Determinación experimental de los coeficientes de fricción

**F1025B: Leyes de movimiento y conservación**  
**Reporte de resolución del análisis manuscrito**

## Alcance y resultado principal

La práctica propone dos mediciones con una ficha sobre una libreta: inclinarla hasta el inicio del deslizamiento para hallar el coeficiente de fricción estática y observar cómo se detiene la ficha sobre una superficie horizontal para hallar el coeficiente de fricción cinética. La aplicación de la segunda ley de Newton conduce a

$$
\boxed{\mu_s=\tan\alpha=\frac{h}{\sqrt{L^2-h^2}}}
\qquad\text{y}\qquad
\boxed{\mu_k=\frac{2d}{gt^2}}.
$$

Aquí $L$ es la longitud inclinada de la libreta, $h$ su altura vertical cuando la ficha *apenas empieza* a deslizarse, $d$ la distancia recorrida desde que termina el impulso hasta detenerse y $t$ el tiempo correspondiente. Usaremos $g=9.81\ \mathrm{m/s^2}$. Ambos coeficientes son adimensionales.

**Estado de las mediciones:** el análisis manuscrito contiene los esquemas y las deducciones; el formato de reporte tiene vacías las tablas de las tres pruebas. Por ello, las expresiones están resueltas, pero no es posible dar valores experimentales numéricos ni promedios sin $L$, $h$, $d$ y $t$.

## 1. Coeficiente de fricción estática en el plano inclinado

### Montaje y diagrama de cuerpo libre descrito

Se coloca la ficha sobre la libreta y se eleva lentamente un extremo. Se registra la altura **en el instante en que la ficha está a punto de deslizarse**, junto con la longitud inclinada de la libreta.

| Elemento | Dirección sobre la ficha |
|---|---|
| Peso $W=mg$ | Vertical hacia abajo |
| Componente $mg\sin\alpha$ | Paralela al plano, hacia abajo |
| Componente $mg\cos\alpha$ | Perpendicular al plano, hacia dentro |
| Normal $N$ | Perpendicular al plano, hacia fuera |
| Fricción estática $f_s$ | Paralela al plano, hacia arriba; se opone a la tendencia de deslizamiento |

Elegimos $x$ paralelo al plano, positivo cuesta arriba, y $y$ perpendicular al plano, positivo hacia fuera. En el umbral de deslizamiento la ficha todavía está en equilibrio y la fricción estática alcanza su **valor máximo**:

$$
\sum F_x=f_{s,\max}-mg\sin\alpha=0,
\qquad
\sum F_y=N-mg\cos\alpha=0.
$$

Como $f_{s,\max}=\mu_sN$, se obtiene

$$
\mu_smg\cos\alpha=mg\sin\alpha
\quad\Longrightarrow\quad
\boxed{\mu_s=\tan\alpha}.
$$

La geometría del triángulo formado por la libreta da $\sin\alpha=h/L$. Así, sin necesidad de medir el ángulo por separado,

$$
\alpha=\arcsin\left(\frac{h}{L}\right),
\qquad
\boxed{\mu_s=\frac{h}{\sqrt{L^2-h^2}}},
\quad 0\leq h<L.
$$

**Aclaración física.** Antes de llegar al umbral, la fricción estática se ajusta a $mg\sin\alpha$ y cumple $f_s\leq\mu_sN$. La igualdad $f_s=\mu_sN$ se usa únicamente cuando la ficha está a punto de moverse. Esta precisión es necesaria para identificar $\mu_s$ a partir del ángulo crítico.

### Registro y cálculo de las tres pruebas

Anotar $L$ y $h$ en metros para cada prueba. Si el largo de la libreta no cambia, se puede repetir el mismo $L$ medido en las tres filas.

| Prueba | $L$ (m) | $h$ (m) | $\alpha=\arcsin(h/L)$ | $\mu_s=h/\sqrt{L^2-h^2}$ |
|:--|--:|--:|--:|--:|
| 1 | Pendiente | Pendiente | Pendiente | Pendiente |
| 2 | Pendiente | Pendiente | Pendiente | Pendiente |
| 3 | Pendiente | Pendiente | Pendiente | Pendiente |
| **Promedio de $\mu_s$** | | | | **$(\mu_{s,1}+\mu_{s,2}+\mu_{s,3})/3$** |

Es preferible calcular $\mu_s$ en cada intento y luego promediar los tres resultados. Así se conserva el efecto de la variación entre pruebas.

## 2. Coeficiente de fricción cinética en la superficie horizontal

### Montaje y diagrama de cuerpo libre descrito

Se da un impulso breve a la ficha. **Al terminar el contacto que produce el impulso**, se inicia el cronómetro y se marca la posición inicial. Se mide la distancia $d$ recorrida hasta detenerse y el tiempo $t$ empleado.

| Elemento | Dirección sobre la ficha mientras se desliza |
|---|---|
| Peso $mg$ | Vertical hacia abajo |
| Normal $N$ | Vertical hacia arriba |
| Fricción cinética $f_k$ | Horizontal, opuesta a la velocidad |

Tomamos $+x$ en el sentido del movimiento inicial. Durante el tramo de frenado, una vez finalizado el impulso, la segunda ley de Newton da

$$
\sum F_x=-f_k=ma,
\qquad
\sum F_y=N-mg=0,
\qquad
f_k=\mu_kN.
$$

Por tanto, $N=mg$ y $a=-\mu_kg$. Para obtener $a$ a partir de las mediciones, suponemos desaceleración aproximadamente constante y usamos $v_f=0$:

$$
0=v_0+at\quad\Longrightarrow\quad v_0=-at,
$$

$$
d=v_0t+\tfrac12at^2=(-at)t+\tfrac12at^2
=-\tfrac12at^2
\quad\Longrightarrow\quad a=-\frac{2d}{t^2}.
$$

Al igualar las dos expresiones para la aceleración,

$$
-\mu_kg=-\frac{2d}{t^2}
\quad\Longrightarrow\quad
\boxed{\mu_k=\frac{2d}{gt^2}}.
$$

**Comprobación de unidades:** $[2d/(gt^2)]=\mathrm{m}/[(\mathrm{m/s^2})\mathrm{s^2}]=1$; el coeficiente no tiene unidades. No es necesario conocer la masa de la ficha porque se cancela.

### Registro y cálculo de las tres pruebas

| Prueba | $d$ (m) | $t$ (s) | $a=-2d/t^2$ (m/s²) | $\mu_k=2d/(gt^2)$ |
|:--|--:|--:|--:|--:|
| 1 | Pendiente | Pendiente | Pendiente | Pendiente |
| 2 | Pendiente | Pendiente | Pendiente | Pendiente |
| 3 | Pendiente | Pendiente | Pendiente | Pendiente |
| **Promedio de $\mu_k$** | | | | **$(\mu_{k,1}+\mu_{k,2}+\mu_{k,3})/3$** |

El tiempo debe corresponder sólo al tramo en que la ficha **se desliza sin recibir otra fuerza de empuje**. Si se cronometra también la duración del impulso, la deducción de $\mu_k$ deja de describir el movimiento medido.

## 3. Análisis e interpretación de resultados

1. **Comparación.** Cuando se cuente con las seis mediciones, comparar $\overline{\mu_s}$ y $\overline{\mu_k}$. Para muchas parejas de superficies se espera $\mu_s>\mu_k$, porque iniciar el deslizamiento suele requerir una fuerza mayor que mantenerlo. La relación debe verificarse con los resultados de esta práctica; no puede afirmarse experimentalmente todavía.
2. **Altura y ángulo.** Inclinar muy rápido la libreta dificulta identificar el primer movimiento. Leer $h$ con paralaje o usar una longitud $L$ distinta de la hipotenusa del triángulo cambia $\mu_s$. Se requiere $0\leq h<L$.
3. **Distancia y tiempo.** La expresión de $\mu_k$ depende de $t^2$, por lo que errores al iniciar o detener un cronómetro manual pueden afectar mucho el resultado. Deben señalarse claramente el punto donde acaba el impulso y el punto donde se detiene la ficha.
4. **Superficies.** La textura de la portada, la cara de contacto de la ficha, el polvo y el desgaste pueden modificar los coeficientes. Usar la misma pareja de superficies y la misma cara de la ficha en las repeticiones mejora la comparación.
5. **Límites del modelo.** Para la parte cinética se supone una superficie horizontal y fricción aproximadamente constante. Un nuevo empuje, una pendiente inadvertida o choques invalidan la ecuación empleada.

## Conclusión

La resolución del análisis manuscrito lleva a $\mu_s=h/\sqrt{L^2-h^2}$ para el umbral del plano inclinado y a $\mu_k=2d/(gt^2)$ para el frenado horizontal después de un impulso breve. Ambos resultados se obtienen de la segunda ley de Newton; el segundo también usa las ecuaciones de movimiento con aceleración constante. **Los coeficientes experimentales y su comparación quedan pendientes de las tres series de mediciones**, que no aparecen en los archivos proporcionados.

## Fuentes del trabajo

- *Determinación del coeficiente de fricción estático y dinámico*, análisis manuscrito proporcionado: bosquejos, diagramas de cuerpo libre y deducciones de $\mu_s$ y $\mu_k$.
- *Formato de reporte de práctica de coeficientes de fricción*, documento proporcionado para F1025B: objetivos, procedimientos, tres pruebas por método y preguntas de reflexión.
- Serway, R. A. y Jewett, J. W., *Física para ciencias e ingeniería*, vol. 1, 10.ª ed., Cengage Learning: leyes de Newton, fricción y movimiento con aceleración constante.

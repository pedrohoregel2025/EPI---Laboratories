"""TC1038: modelo didáctico vertical de cohete de agua.
Basado en los documentos proporcionados por el docente.
No incluye empuje residual del aire ni modela las aletas/estabilidad.
"""
from dataclasses import dataclass
from math import pi, sqrt
import matplotlib.pyplot as plt

PSI_A_PA = 6894.757293168

@dataclass
class Parametros:
    # Valores del PDF: presión manométrica 60 psi, agua inicial 0.60 kg,
    # botella de ejemplo 2 L, densidad del agua ~1000 kg/m³, gamma 1.4.
    presion_manometrica_psi: float = 60.0
    masa_agua_inicial: float = 0.60         # kg
    volumen_total: float = 0.002          # m³ = 2 L
    densidad_agua: float = 1000.0          # kg/m³
    gamma: float = 1.4
    gravedad: float = 9.81                 # m/s²

    # VALORES ILUSTRATIVOS: sustituir por mediciones del equipo.
    presion_atmosferica: float = 78000.0   # Pa, NO medición verificada de Toluca
    masa_botella_vacia: float = 0.15       # kg
    densidad_aire: float = 1.10           # kg/m³, NO medición verificada de Toluca
    diametro_boquilla: float = 0.009      # m
    diametro_frontal: float = 0.105       # m
    coeficiente_arrastre: float = 0.50    # adimensional
    dt: float = 0.0005                    # s
    tiempo_maximo: float = 120.0          # s (límite de seguridad numérica)


def validar(p):
    """Evita parámetros incompatibles con el modelo físico."""
    if p.presion_manometrica_psi <= 0 or p.presion_atmosferica <= 0:
        raise ValueError("Las presiones deben ser positivas.")
    if p.masa_agua_inicial <= 0 or p.masa_botella_vacia <= 0:
        raise ValueError("Las masas deben ser positivas.")
    if p.densidad_agua <= 0 or p.densidad_aire <= 0:
        raise ValueError("Las densidades deben ser positivas.")
    if not (0 < p.masa_agua_inicial / p.densidad_agua < p.volumen_total):
        raise ValueError("El agua debe ocupar menos volumen que la botella.")
    if p.gamma <= 1 or p.gravedad <= 0 or p.dt <= 0 or p.tiempo_maximo <= 0:
        raise ValueError("Gamma, gravedad y tiempos no son válidos.")
    if p.diametro_boquilla <= 0 or p.diametro_frontal <= 0 or p.coeficiente_arrastre < 0:
        raise ValueError("Revise diámetros y coeficiente de arrastre.")


def simular(p):
    """Integra altura, velocidad y masa mediante Euler semiimplícito."""
    validar(p)
    area_boquilla = pi * (p.diametro_boquilla / 2) ** 2
    area_frontal = pi * (p.diametro_frontal / 2) ** 2
    presion_inicial_abs = p.presion_atmosferica + p.presion_manometrica_psi * PSI_A_PA
    volumen_aire_inicial = p.volumen_total - p.masa_agua_inicial / p.densidad_agua

    t, h, v, m_agua = 0.0, 0.0, 0.0, p.masa_agua_inicial
    t_hist, h_hist, v_hist = [t], [h], [v]
    ma_hist, masa_total_hist, p_hist = [m_agua], [p.masa_botella_vacia + m_agua], [presion_inicial_abs]
    t_fin_empuje = 0.0
    empuje_terminado = False
    altura_maxima = 0.0
    velocidad_maxima = 0.0

    while t < p.tiempo_maximo:
        masa_total = p.masa_botella_vacia + m_agua
        # Ecuación adiabática: usar presiones ABSOLUTAS.
        vol_aire = p.volumen_total - m_agua / p.densidad_agua
        presion_abs = presion_inicial_abs * (volumen_aire_inicial / vol_aire) ** p.gamma
        delta_p = max(0.0, presion_abs - p.presion_atmosferica)

        # Expulsión de agua: Bernoulli + cantidad de movimiento.
        empuje = 0.0
        flujo_masico = 0.0
        if m_agua > 0 and delta_p > 0:
            velocidad_salida = sqrt(2 * delta_p / p.densidad_agua)
            flujo_masico = p.densidad_agua * area_boquilla * velocidad_salida
            empuje = flujo_masico * velocidad_salida
        elif not empuje_terminado:
            t_fin_empuje = t
            empuje_terminado = True

        # El arrastre se opone tanto al ascenso como al descenso.
        arrastre_con_signo = 0.5 * p.coeficiente_arrastre * p.densidad_aire * area_frontal * v * abs(v)
        aceleracion = (empuje - masa_total * p.gravedad - arrastre_con_signo) / masa_total

        # Integración numérica: primero velocidad, luego altura.
        v = v + aceleracion * p.dt
        h = h + v * p.dt
        t = t + p.dt
        m_agua = max(0.0, m_agua - flujo_masico * p.dt)

        # Detectar momento de agotamiento del agua.
        if not empuje_terminado and m_agua == 0:
            t_fin_empuje = t
            empuje_terminado = True

        # Después del agua no se modela la expulsión residual de aire.
        # La presión interna termodinámica residual se mantiene como valor
        # calculado; NO se supone que haya caído instantáneamente a Patm.
        vol_aire_nuevo = p.volumen_total - m_agua / p.densidad_agua
        presion_registro = presion_inicial_abs * (volumen_aire_inicial / vol_aire_nuevo) ** p.gamma
        t_hist.append(t)
        h_hist.append(max(h, 0.0))
        v_hist.append(v)
        ma_hist.append(m_agua)
        masa_total_hist.append(p.masa_botella_vacia + m_agua)
        p_hist.append(presion_registro)
        altura_maxima = max(altura_maxima, h)
        velocidad_maxima = max(velocidad_maxima, v)

        # h<=0 al regresar al suelo; t>0 evita finalizar en el lanzamiento.
        if h <= 0 and t > p.dt:
            break
    else:
        raise RuntimeError("No se detectó aterrizaje; revise parámetros o tiempo máximo.")

    return {
        "tiempo": t_hist, "altura": h_hist, "velocidad": v_hist,
        "masa_agua": ma_hist, "masa_total": masa_total_hist, "presion_abs": p_hist,
        "altura_maxima": altura_maxima, "velocidad_maxima": velocidad_maxima,
        "tiempo_vuelo": t, "tiempo_empuje": t_fin_empuje,
        "masa_agua_inicial": p.masa_agua_inicial, "masa_agua_final": m_agua,
        "presion_atmosferica": p.presion_atmosferica,
    }


def graficar(r, carpeta="recursos"):
    """Guarda las cuatro gráficas solicitadas en archivos PNG."""
    from pathlib import Path
    Path(carpeta).mkdir(parents=True, exist_ok=True)
    series = [
        ("altura", "Altura (m)", "01_altura.png"),
        ("velocidad", "Velocidad vertical (m/s)", "02_velocidad.png"),
        ("masa_total", "Masa total del cohete (kg)", "03_masa.png"),
        ("presion_abs", "Presión interna absoluta (Pa)", "04_presion.png"),
    ]
    for clave, ylabel, filename in series:
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(r["tiempo"], r[clave], linewidth=1.8)
        ax.set_xlabel("Tiempo (s)")
        ax.set_ylabel(ylabel)
        ax.set_title(f"{ylabel} vs. tiempo")
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.savefig(Path(carpeta) / filename, dpi=150)
        plt.close(fig)


def main():
    parametros = Parametros()
    resultados = simular(parametros)
    print("RESULTADOS DE LA SIMULACIÓN (parámetros ilustrativos)")
    print(f"Altura máxima: {resultados['altura_maxima']:.2f} m")
    print(f"Tiempo total de vuelo: {resultados['tiempo_vuelo']:.3f} s")
    print(f"Velocidad máxima de ascenso: {resultados['velocidad_maxima']:.2f} m/s")
    print(f"Masa inicial de agua: {resultados['masa_agua_inicial']:.3f} kg")
    print(f"Masa final de agua: {resultados['masa_agua_final']:.6f} kg")
    print(f"Duración del empuje: {resultados['tiempo_empuje']:.3f} s")
    graficar(resultados)


if __name__ == "__main__":
    main()

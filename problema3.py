import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ── PROBLEMA 3: Maximización de ingresos ──

# Definimos la variable
x = sp.symbols('x')

# Función de ingresos: I(x) = (80 + x)(4000 - 50x)
I = (80 + x) * (4000 - 50*x)

# Expandir la función
I_expandida = sp.expand(I)
print("Función de ingresos expandida:")
print("I(x) =", I_expandida)

# ── FASE 2: Derivada y punto crítico ──
dI = sp.diff(I, x)
print("\nDerivada I'(x) =", dI)

criticos = sp.solve(dI, x)
print("Punto crítico x =", [float(c) for c in criticos])

x_opt = criticos[0]
precio_opt = 80 + float(x_opt)
suscriptores_opt = 4000 - 50*float(x_opt)
ingreso_opt = float(I.subs(x, x_opt))

print(f"\nIncremento óptimo de precio: x = ${float(x_opt):.2f}")
print(f"Precio óptimo mensual:       ${precio_opt:.2f}/mes")
print(f"Número de suscriptores:      {suscriptores_opt:.0f}")
print(f"Ingreso máximo:              ${ingreso_opt:,.2f}/mes")

# Segunda derivada (verifica que es máximo)
d2I = sp.diff(dI, x)
print("\nSegunda derivada I''(x) =", d2I)
print("En x óptimo:", float(d2I.subs(x, x_opt)), "→ es MÁXIMO si es negativo")

# ── FASE 3: Gráfica ──
x_vals = np.linspace(0, 80, 300)
I_vals = [float(I.subs(x, v)) for v in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, I_vals, color='steelblue', linewidth=2, label='I(x)')
plt.scatter([float(x_opt)], [ingreso_opt],
            color='red', zorder=5, s=100,
            label=f'Óptimo x=${float(x_opt):.2f} → ${ingreso_opt:,.2f}/mes')
plt.axvline(x=float(x_opt), color='red', linestyle='--', alpha=0.4)
plt.title('Problema 3 — Maximización de ingresos')
plt.xlabel('Incremento de precio x ($)')
plt.ylabel('Ingreso total I(x) ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
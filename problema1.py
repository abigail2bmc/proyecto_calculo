import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ── PROBLEMA 1: Diseño óptimo de una lata cilíndrica ──

# Definimos la variable
r = sp.symbols('r', positive=True)

# Función de costo: C(r) = 2πr² + 710/r
C = 2 * sp.pi * r**2 + 710 / r

# ── FASE 2: Derivada y punto crítico ──
dC = sp.diff(C, r)
print("Derivada C'(r) =", dC)

critico = sp.solve(dC, r)
print("Radio óptimo r =", [sp.simplify(c) for c in critico])

r_opt = critico[0]
h_opt = 355 / (sp.pi * r_opt**2)
C_opt = C.subs(r, r_opt)

print(f"\nRadio óptimo:  r = {float(r_opt):.4f} cm")
print(f"Altura óptima: h = {float(h_opt):.4f} cm")
print(f"Costo mínimo:  C = ${float(C_opt) * 0.005:.4f}")

# Segunda derivada (verifica que es mínimo)
d2C = sp.diff(dC, r)
print("\nSegunda derivada C''(r) =", d2C)
print("En r óptimo:", float(d2C.subs(r, r_opt)), "→ es MÍNIMO si es positivo")

# ── FASE 3: Gráfica ──
r_vals = np.linspace(1, 8, 300)
C_vals = [float(C.subs(r, v)) for v in r_vals]

plt.figure(figsize=(8, 5))
plt.plot(r_vals, C_vals, color='steelblue', linewidth=2, label='C(r)')
plt.scatter([float(r_opt)], [float(C_opt)],
            color='red', zorder=5, s=100, label=f'Óptimo r={float(r_opt):.2f} cm')
plt.title('Problema 1 — Costo de fabricación de lata cilíndrica')
plt.xlabel('Radio r (cm)')
plt.ylabel('Área total (cm²)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
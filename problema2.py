import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ── PROBLEMA 2: Tendido de cable entre tierra firme y una isla ──

# Definimos la variable
x = sp.symbols('x', positive=True)

# Función de costo: C(x) = 1500x + 3000 * sqrt(16 + (6-x)²)
C = 1500*x + 3000 * sp.sqrt(16 + (6 - x)**2)

# ── FASE 2: Derivada y punto crítico ──
dC = sp.diff(C, x)
print("Derivada C'(x) =", dC)

criticos = sp.solve(dC, x)
print("Punto crítico x =", [float(c) for c in criticos])

x_opt = criticos[0]
C_opt = C.subs(x, x_opt)

print(f"\nDistancia por tierra:      x = {float(x_opt):.4f} km")
print(f"Distancia bajo el agua:    d = {float(6 - x_opt):.4f} km hasta la isla")
print(f"Costo mínimo:              C = ${float(C_opt):,.2f}")

# Comparar con extremos del intervalo
C_en_0 = float(C.subs(x, 0))
C_en_6 = float(C.subs(x, 6))
print(f"\nCosto en x=0 (todo bajo agua): ${C_en_0:,.2f}")
print(f"Costo en x=6 (mínima tierra):  ${C_en_6:,.2f}")
print(f"Costo en óptimo:               ${float(C_opt):,.2f} ← MÍNIMO")

# Segunda derivada
d2C = sp.diff(dC, x)
print("\nSegunda derivada C''(x) =", d2C)
print("En x óptimo:", float(d2C.subs(x, x_opt)), "→ es MÍNIMO si es positivo")

# ── FASE 3: Gráfica ──
x_vals = np.linspace(0, 6, 300)
C_vals = [float(C.subs(x, v)) for v in x_vals]

plt.figure(figsize=(8, 5))
plt.plot(x_vals, C_vals, color='steelblue', linewidth=2, label='C(x)')
plt.scatter([float(x_opt)], [float(C_opt)],
            color='red', zorder=5, s=100, label=f'Óptimo x={float(x_opt):.2f} km')
plt.axvline(x=float(x_opt), color='red', linestyle='--', alpha=0.4)
plt.title('Problema 2 — Costo de tendido de cable')
plt.xlabel('Distancia por tierra x (km)')
plt.ylabel('Costo total ($)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
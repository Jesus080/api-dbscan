#!/usr/bin/env python3
"""
Script para generar todas las imágenes estáticas del análisis DBSCAN
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.gridspec as gridspec
from sklearn.cluster import DBSCAN
import numpy as np
import os

# Configuración
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
OUTPUT_DIR = 'static/images'

# Crear directorio si no existe
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("🚀 Cargando datos...")
df = pd.read_csv("datasets/creditcard.csv")
df_processed = df.drop(["Time", "Amount"], axis=1)

# Preparar datos
X_v10_v14 = df_processed[["V10", "V14"]].copy()
y = df_processed["Class"].copy()

print("📊 Generando imagen 1: DBSCAN eps=0.10, min_samples=6...")
# Imagen 1: DBSCAN con make_moons (círculos)
from sklearn.datasets import make_moons
X_moons, y_moons = make_moons(n_samples=1000, noise=0.05, random_state=42)
dbscan_moons = DBSCAN(eps=0.1, min_samples=6)
dbscan_moons.fit(X_moons)

# Plot función auxiliar
def plot_dbscan(dbscan, X, title, filename):
    core_mask = np.zeros_like(dbscan.labels_, dtype=bool)
    core_mask[dbscan.core_sample_indices_] = True
    anomalies_mask = dbscan.labels_ == -1
    non_core_mask = ~(core_mask | anomalies_mask)

    cores = dbscan.components_
    anomalies = X[anomalies_mask]
    non_cores = X[non_core_mask]
    
    fig = plt.figure(figsize=(12, 6))
    plt.scatter(cores[:, 0], cores[:, 1],
                c=dbscan.labels_[core_mask], marker='o', s=100, cmap="Paired")
    plt.scatter(cores[:, 0], cores[:, 1], marker='*', s=20, c=dbscan.labels_[core_mask])
    plt.scatter(anomalies[:, 0], anomalies[:, 1],
                c="r", marker=".", s=100)
    plt.scatter(non_cores[:, 0], non_cores[:, 1], c=dbscan.labels_[non_core_mask], marker=".")
    plt.title(title, fontsize=14)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/{filename}', dpi=100, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  ✓ Guardado: {OUTPUT_DIR}/{filename}")

plot_dbscan(dbscan_moons, X_moons, 
            "eps=0.10, min_samples=6", 
            "dbscan_1.png")

print("📊 Generando imagen 2: Etiquetas cluster make_moons...")
# Imagen 2: Scatter simple con etiquetas
fig = plt.figure(figsize=(12, 6))
plt.scatter(X_moons[:,0][y_moons == 0], X_moons[:,1][y_moons == 0], c="g", marker=".")
plt.scatter(X_moons[:,0][y_moons == 1], X_moons[:,1][y_moons == 1], c="r", marker=".")
plt.title("eps=0.10, min_samples=6", fontsize=14)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/dbscan_2.png', dpi=100, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {OUTPUT_DIR}/dbscan_2.png")

print("📊 Generando imagen 3: DBSCAN eps=0.15, V10 vs V14...")
# Imagen 3: DBSCAN con datos reales
dbscan_real = DBSCAN(eps=0.15, min_samples=13)
dbscan_real.fit(X_v10_v14)

plot_dbscan(dbscan_real, X_v10_v14.values,
            "eps=0.15, min_samples=13",
            "dbscan_3.png")

print("📊 Generando imagen 4: Scatter V10 vs V14 con etiquetas...")
# Imagen 4: Scatter V10 vs V14 coloreado por clase
fig = plt.figure(figsize=(12, 6))
plt.scatter(df_processed["V10"][df_processed['Class'] == 0], 
            df_processed["V14"][df_processed['Class'] == 0], 
            c="g", marker=".", s=10, alpha=0.5)
plt.scatter(df_processed["V10"][df_processed['Class'] == 1], 
            df_processed["V14"][df_processed['Class'] == 1], 
            c="r", marker=".", s=30, alpha=0.8)
plt.xlabel("V10", fontsize=14)
plt.ylabel("V14", fontsize=14)
plt.title("eps=0.15, min_samples=13", fontsize=14)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/dbscan_4.png', dpi=100, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {OUTPUT_DIR}/dbscan_4.png")

print("📊 Generando imagen 5: Distribución de todas las características...")
# Imagen 5: Grid de distribuciones
features = df_processed.drop("Class", axis=1)

fig = plt.figure(figsize=(14, 36))
gs = gridspec.GridSpec(8, 4, hspace=0.8, wspace=0.4)

for i, f in enumerate(features):
    ax = plt.subplot(gs[i])
    sns.histplot(df_processed[f][df_processed["Class"] == 1], 
                 kde=True, color='#e74c3c', alpha=0.6, 
                 label='Fraudulenta', ax=ax, stat='density')
    sns.histplot(df_processed[f][df_processed["Class"] == 0], 
                 kde=True, color='#3498db', alpha=0.6, 
                 label='Legítima', ax=ax, stat='density')
    ax.set_xlabel('')
    ax.set_title(f'feature: {str(f)}', fontsize=10)
    if i == 0:
        ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/features_distribution.png', dpi=100, bbox_inches='tight', facecolor='white')
plt.close()
print(f"  ✓ Guardado: {OUTPUT_DIR}/features_distribution.png")

print("\n✅ ¡Todas las imágenes generadas exitosamente!")
print(f"\n📁 Ubicación: {os.path.abspath(OUTPUT_DIR)}/")
print("\n🚀 Ahora ejecuta: python app_static.py")

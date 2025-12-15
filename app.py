from flask import Flask, render_template, jsonify
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.gridspec as gridspec
from sklearn.cluster import DBSCAN
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from collections import Counter
import io
import base64
import os
from functools import lru_cache

app = Flask(__name__)

# Configuración de estilo para gráficas
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Cache global para almacenar resultados
_cache = {}

def purity_score(y_true, y_pred):
    """Calcula el purity score del clustering"""
    contingency_matrix = metrics.cluster.contingency_matrix(y_true, y_pred)
    return np.sum(np.amax(contingency_matrix, axis=0)) / np.sum(contingency_matrix)

def generate_plot_base64(fig):
    """Convierte una figura de matplotlib a base64"""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=100, facecolor='white')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_base64

@lru_cache(maxsize=1)
def load_and_process_data():
    """Carga y procesa los datos del dataset (con caché)"""
    print("Cargando datos desde CSV...")
    df = pd.read_csv("datasets/creditcard.csv")
    
    # Usar solo una muestra para mayor velocidad (fraudulentas + muestra de legítimas)
    fraud = df[df['Class'] == 1]  # Todas las fraudulentas (492)
    legit = df[df['Class'] == 0].sample(n=5000, random_state=42)  # Muestra de legítimas
    df = pd.concat([fraud, legit]).sample(frac=1, random_state=42).reset_index(drop=True)
    
    df_processed = df.drop(["Time", "Amount"], axis=1)
    
    X = df_processed.drop("Class", axis=1)
    y = df_processed["Class"].copy()
    
    print(f"Datos cargados: {len(df)} muestras (optimizado)")
    return df_processed, X, y

def get_feature_importance(X, y):
    """Calcula la importancia de características usando Random Forest (con caché)"""
    if 'feature_importance' in _cache:
        print("Usando feature importance desde caché")
        return _cache['feature_importance']
    
    print("Calculando feature importance...")
    clf_rnd = RandomForestClassifier(n_estimators=50, random_state=42, n_jobs=-1)
    clf_rnd.fit(X, y)
    
    feature_importances = {name: score for name, score in zip(list(X.columns), clf_rnd.feature_importances_)}
    feature_importances_sorted = pd.Series(feature_importances).sort_values(ascending=False)
    
    _cache['feature_importance'] = feature_importances_sorted
    print("Feature importance calculado")
    return feature_importances_sorted

def generate_features_distribution_plot(df):
    """Genera el gráfico de distribución de todas las características (con caché)"""
    if 'features_plot' in _cache:
        print("Usando gráfico de features desde caché")
        return _cache['features_plot']
    
    print("Generando gráfico de distribución de características...")
    features = df.drop("Class", axis=1)
    
    fig = plt.figure(figsize=(14, 36))
    gs = gridspec.GridSpec(8, 4, hspace=0.6, wspace=0.4)
    
    for i, f in enumerate(features):
        ax = plt.subplot(gs[i])
        
        # Distribución de transacciones fraudulentas
        sns.histplot(df[f][df["Class"] == 1], kde=True, color='#e74c3c', 
                     alpha=0.6, label='Fraudulenta', ax=ax, stat='density')
        
        # Distribución de transacciones legítimas
        sns.histplot(df[f][df["Class"] == 0], kde=True, color='#3498db', 
                     alpha=0.6, label='Legítima', ax=ax, stat='density')
        
        ax.set_xlabel('')
        ax.set_title(f'Característica: {str(f)}', fontsize=10, fontweight='bold')
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
    
    result = generate_plot_base64(fig)
    _cache['features_plot'] = result
    print("Gráfico generado")
    return result

def generate_v10_v14_scatter(df):
    """Genera scatter plot de V10 vs V14 (con caché)"""
    if 'scatter_plot' in _cache:
        print("Usando scatter plot desde caché")
        return _cache['scatter_plot']
    
    print("Generando scatter plot V10 vs V14...")
    fig = plt.figure(figsize=(12, 7))
    
    plt.scatter(df["V10"][df['Class'] == 0], df["V14"][df['Class'] == 0], 
                c="#2ecc71", marker=".", s=30, alpha=0.6, label='Transacciones Legítimas')
    plt.scatter(df["V10"][df['Class'] == 1], df["V14"][df['Class'] == 1], 
                c="#e74c3c", marker="o", s=80, alpha=0.8, 
                edgecolors='darkred', linewidths=1, label='Transacciones Fraudulentas')
    
    plt.xlabel("V10", fontsize=14, fontweight='bold')
    plt.ylabel("V14", fontsize=14, fontweight='bold')
    plt.title("Distribución de Transacciones: V10 vs V14", fontsize=16, fontweight='bold')
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    
    result = generate_plot_base64(fig)
    _cache['scatter_plot'] = result
    print("Scatter plot generado")
    return result

def plot_dbscan_advanced(dbscan, X, title=""):
    """Genera visualización avanzada de DBSCAN"""
    core_mask = np.zeros_like(dbscan.labels_, dtype=bool)
    core_mask[dbscan.core_sample_indices_] = True
    anomalies_mask = dbscan.labels_ == -1
    non_core_mask = ~(core_mask | anomalies_mask)

    cores = dbscan.components_
    anomalies = X[anomalies_mask]
    non_cores = X[non_core_mask]
    
    fig = plt.figure(figsize=(12, 7))
    
    # Núcleos de clusters
    plt.scatter(cores[:, 0], cores[:, 1],
                c=dbscan.labels_[core_mask], marker='o', s=100, 
                cmap="viridis", alpha=0.7, edgecolors='black', linewidths=0.5)
    
    plt.scatter(cores[:, 0], cores[:, 1], marker='*', s=25, 
                c=dbscan.labels_[core_mask], cmap="viridis")
    
    # Anomalías
    plt.scatter(anomalies[:, 0], anomalies[:, 1],
                c="#e74c3c", marker="X", s=150, label='Anomalías',
                edgecolors='darkred', linewidths=1.5, alpha=0.9)
    
    # Puntos no-núcleo
    plt.scatter(non_cores[:, 0], non_cores[:, 1], 
                c=dbscan.labels_[non_core_mask], marker=".", 
                cmap="viridis", s=50, alpha=0.5)
    
    plt.title(f"{title}\neps={dbscan.eps:.2f}, min_samples={dbscan.min_samples}", 
              fontsize=14, fontweight='bold')
    plt.xlabel("V10", fontsize=12, fontweight='bold')
    plt.ylabel("V14", fontsize=12, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    return generate_plot_base64(fig)

@app.route('/')
def loading():
    """Página de carga inicial"""
    return render_template('loading.html')

@app.route('/dashboard')
def index():
    """Página principal con visualizaciones"""
    print("\n=== Procesando solicitud ===")
    
    # Cargar datos (con caché LRU)
    df, X, y = load_and_process_data()
    
    # Obtener importancia de características (con caché)
    feature_importances = get_feature_importance(X, y)
    
    # Reducir a las 7 características más importantes
    X_reduced = X[list(feature_importances.head(7).index)].copy()
    
    # Entrenar DBSCAN con datos reducidos (con caché)
    if 'dbscan_full' not in _cache:
        print("Entrenando DBSCAN modelo completo...")
        dbscan_full = DBSCAN(eps=0.70, min_samples=25)
        dbscan_full.fit(X_reduced)
        _cache['dbscan_full'] = dbscan_full
        _cache['clusters'] = dbscan_full.labels_
    else:
        print("Usando DBSCAN modelo completo desde caché")
        dbscan_full = _cache['dbscan_full']
    
    # Entrenar DBSCAN con V10 y V14 (con caché)
    if 'dbscan_2d' not in _cache:
        print("Entrenando DBSCAN 2D...")
        X_v10_v14 = df[["V10", "V14"]].copy()
        dbscan_2d = DBSCAN(eps=0.15, min_samples=13)
        dbscan_2d.fit(X_v10_v14)
        _cache['dbscan_2d'] = dbscan_2d
        _cache['X_v10_v14'] = X_v10_v14
    else:
        print("Usando DBSCAN 2D desde caché")
        dbscan_2d = _cache['dbscan_2d']
        X_v10_v14 = _cache['X_v10_v14']
    
    # Generar gráficas (con caché)
    features_plot = generate_features_distribution_plot(df)
    scatter_plot = generate_v10_v14_scatter(df)
    
    # Generar plot DBSCAN (con caché)
    if 'dbscan_plot' not in _cache:
        print("Generando plot DBSCAN...")
        dbscan_plot = plot_dbscan_advanced(dbscan_2d, X_v10_v14.values, 
                                           "Clustering DBSCAN - V10 vs V14")
        _cache['dbscan_plot'] = dbscan_plot
    else:
        print("Usando plot DBSCAN desde caché")
        dbscan_plot = _cache['dbscan_plot']
    
    # Calcular métricas (con caché)
    if 'metrics' not in _cache:
        print("Calculando métricas...")
        clusters = _cache['clusters']
        purity = purity_score(y, clusters)
        silhouette = metrics.silhouette_score(X_reduced, clusters, sample_size=10000)
        calinski = metrics.calinski_harabasz_score(X_reduced, clusters)
        _cache['metrics'] = {
            'purity': purity,
            'silhouette': silhouette,
            'calinski': calinski
        }
    else:
        print("Usando métricas desde caché")
    
    evaluation_metrics = {
        'purity': f"{_cache['metrics']['purity']:.10f}",
        'silhouette': f"{_cache['metrics']['silhouette']:.17f}",
        'calinski': f"{_cache['metrics']['calinski']:.12f}"
    }
    
    # Análisis de clusters (con caché)
    if 'cluster_analysis' not in _cache:
        print("Analizando clusters...")
        counter_2d = Counter(dbscan_2d.labels_.tolist())
        bad_counter_2d = Counter(dbscan_2d.labels_[y == 1].tolist())
        
        cluster_analysis = []
        for key in sorted(counter_2d.keys()):
            cluster_analysis.append({
                'label': key,
                'total': counter_2d[key],
                'malicious': bad_counter_2d[key]
            })
        _cache['cluster_analysis'] = cluster_analysis
    else:
        print("Usando análisis de clusters desde caché")
        cluster_analysis = _cache['cluster_analysis']
    
    # Tabla de características (con caché)
    if 'features_table' not in _cache:
        print("Preparando tabla de características...")
        top_features = feature_importances.head(10)
        features_table = []
        
        for idx, (feature, importance) in enumerate(top_features.items(), 1):
            if feature in ['V14', 'V15', 'V16', 'V17', 'V18']:
                features_table.append({
                    'rank': idx,
                    'feature': feature,
                    'importance': f"{importance:.6f}",
                    'percentage': f"{importance * 100:.2f}%"
                })
        _cache['features_table'] = features_table
    else:
        print("Usando tabla de características desde caché")
        features_table = _cache['features_table']
    
    print("=== Solicitud completada ===\n")
    
    return render_template('index.html',
                         features_plot=features_plot,
                         scatter_plot=scatter_plot,
                         dbscan_plot=dbscan_plot,
                         features_table=features_table,
                         evaluation_metrics=evaluation_metrics,
                         cluster_analysis=cluster_analysis,
                         total_samples=284807,  # Total original
                         fraud_samples=492,  # Total original
                         legitimate_samples=284315)  # Total original

@app.route('/api/stats')
def get_stats():
    """API endpoint para obtener estadísticas"""
    return jsonify({
        'total_transactions': 284807,
        'fraudulent': 492,
        'legitimate': 284315,
        'fraud_percentage': "0.172%"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)

# Versión Estática - DBSCAN Fraud Detection

## ⚡ Carga Instantánea

Esta versión usa datos precalculados y NO genera gráficas dinámicamente.
**Tiempo de carga: < 1 segundo**

## 📸 Paso 1: Agregar Imágenes

Guarda las 5 imágenes en la carpeta `static/images/` con estos nombres:

```
static/images/
├── dbscan_1.png          (Clustering eps=0.10, circles naranja/morado)
├── dbscan_2.png          (Clustering eps=0.10, verde/rojo)  
├── dbscan_3.png          (Clustering eps=0.15, V10/V14 rojo/morado)
├── dbscan_4.png          (Clustering eps=0.15, V10/V14 verde/rojo)
└── features_distribution.png  (Grid 30 gráficas de distribución)
```

## 🚀 Paso 2: Ejecutar

```bash
# Con el ambiente 'ja' activado:
python app_static.py
```

## 🌐 Paso 3: Abrir

Abre en tu navegador: **http://localhost:5001**

## ✨ Características

✅ **Carga instantánea** (sin procesamiento)
✅ **Diseño idéntico** al original
✅ **Métricas exactas**:
   - Purity Score: 0.9982725144
   - Silhouette: 0.09578003818745683
   - Calinski-Harabasz: 913.711950590

✅ **Análisis de Clusters**:
   - Label -1: 1 muestra (1 fraudulenta)
   - Label 0: 499 muestras (499 fraudulentas)
   - Label 1: 500 muestras (0 fraudulentas)

✅ **Características V14-V18** con importancias reales

## 📦 Deployment

Esta versión es **perfecta para Render/Heroku** porque:
- No requiere dataset CSV grande
- No consume RAM procesando datos
- Carga instantánea para usuarios
- Solo sirve archivos estáticos

### Deploy en Render

1. Renombra `app_static.py` a `app.py` (o actualiza Procfile)
2. Sube las imágenes al repositorio
3. Deploy normal en Render

```bash
# Procfile
web: gunicorn app_static:app
```

## 📁 Estructura

```
api-dbscan/
├── app_static.py           ← Nueva versión estática
├── app.py                  ← Versión original dinámica
├── templates/
│   ├── index_static.html   ← Template estático
│   └── index.html          ← Template dinámico
└── static/
    ├── images/             ← Agregar tus 5 imágenes aquí
    ├── css/
    └── js/
```

## 🔄 Cambiar entre versiones

**Versión Estática (rápida)**:
```bash
python app_static.py
```

**Versión Dinámica (genera gráficas)**:
```bash
python app.py
```

---

💡 **Tip**: Usa la versión estática para producción y la dinámica solo para desarrollo.

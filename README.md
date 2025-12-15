# 🔍 DBSCAN Fraud Detection System

Sistema avanzado de detección de fraude bancario utilizando el algoritmo de clustering DBSCAN (Density-Based Spatial Clustering of Applications with Noise).

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.2-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📊 Descripción

Este proyecto implementa un sistema de detección de transacciones bancarias fraudulentas mediante técnicas de Machine Learning, específicamente utilizando el algoritmo **DBSCAN** para identificar patrones anómalos en transacciones de tarjetas de crédito.

### Características Principales

- ✅ Análisis de **284,807 transacciones** bancarias
- ✅ Detección de **492 transacciones fraudulentas**
- ✅ Visualizaciones interactivas y profesionales
- ✅ Métricas de evaluación del modelo (Purity Score, Silhouette, Calinski-Harabasz)
- ✅ Análisis de importancia de características con Random Forest
- ✅ Interfaz web moderna y responsiva
- ✅ API REST para consulta de estadísticas

## 🚀 Demo en Vivo

🔗 [Ver Demo en Render](https://tu-app.onrender.com) _(Actualizar después del deploy)_

## 📁 Estructura del Proyecto

```
api-dbscan/
├── app.py                      # Aplicación Flask principal
├── requirements.txt            # Dependencias de Python
├── Procfile                    # Configuración para Render
├── runtime.txt                 # Versión de Python
├── datasets/
│   └── creditcard.csv         # Dataset de transacciones
├── templates/
│   └── index.html             # Plantilla HTML principal
├── static/
│   ├── css/
│   │   └── style.css          # Estilos personalizados
│   ├── js/
│   │   └── main.js            # JavaScript interactivo
│   └── images/                # Imágenes estáticas
└── 18_DBSCAN - Detección de transacciones bancarias fraudulentas.ipynb
```

## 🛠️ Tecnologías Utilizadas

- **Backend**: Flask 3.0.0
- **Machine Learning**: Scikit-learn 1.3.2
- **Visualización**: Matplotlib 3.8.2, Seaborn 0.13.0
- **Análisis de Datos**: Pandas 2.1.4, NumPy 1.26.2
- **Deployment**: Gunicorn 21.2.0
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)

## 📦 Instalación Local

### Prerrequisitos

- Python 3.11+
- pip
- Git

### Pasos de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/api-dbscan.git
cd api-dbscan
```

2. **Crear y activar entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**

```bash
python app.py
```

5. **Abrir en el navegador**

```
http://localhost:5000
```

## 🌐 Deployment en Render

### Método 1: Desde GitHub

1. **Subir el código a GitHub**

```bash
git init
git add .
git commit -m "Initial commit: DBSCAN Fraud Detection System"
git branch -M main
git remote add origin https://github.com/tu-usuario/api-dbscan.git
git push -u origin main
```

2. **Configurar en Render**

- Ve a [Render Dashboard](https://dashboard.render.com/)
- Click en "New +" → "Web Service"
- Conecta tu repositorio de GitHub
- Configuración:
  - **Name**: `dbscan-fraud-detection`
  - **Environment**: `Python 3`
  - **Build Command**: `pip install -r requirements.txt`
  - **Start Command**: `gunicorn app:app`
  - **Instance Type**: `Free`

3. **Deploy**

Click en "Create Web Service" y espera a que se complete el deployment.

### Método 2: Deploy Manual

```bash
# Instalar Render CLI
npm install -g @render/cli

# Login en Render
render login

# Deploy
render deploy
```

## 📈 Características del Modelo

### DBSCAN (Density-Based Spatial Clustering)

**Parámetros utilizados:**
- `eps`: 0.70 (para modelo completo) / 0.15 (para visualización 2D)
- `min_samples`: 25 (modelo completo) / 13 (visualización 2D)

### Métricas de Evaluación

```
Purity Score:      0.9982725143693799
Silhouette Score:  0.09578003818745683
Calinski-Harabasz: 913.711950589592
```

### Características Más Importantes (V14-V18)

El modelo utiliza **Random Forest** para determinar las características más relevantes en la detección de fraude.

## 🎨 Diseño y UX

- **Paleta de colores**: Gradientes modernos con tonos púrpura, azul y rosa
- **Tipografía**: Inter (texto) y JetBrains Mono (código/números)
- **Animaciones**: Transiciones suaves, efectos de hover, parallax
- **Responsivo**: Diseño adaptable a móviles, tablets y escritorio
- **Dark Mode**: Diseño optimizado para visualización nocturna

## 📊 Dataset

**Credit Card Fraud Detection Dataset**
- Fuente: [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Transacciones: 284,807
- Fraudulentas: 492 (0.172%)
- Legítimas: 284,315 (99.828%)
- Características: 30 (V1-V28 + Time + Amount)
- Período: 2 días (Septiembre 2013)

## 🔒 Seguridad y Privacidad

- Las características V1-V28 son el resultado de una transformación PCA por confidencialidad
- No se incluyen datos personales identificables
- Dataset anonimizado y público

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre**
- GitHub: [@tu-usuario](https://github.com/tu-usuario)
- LinkedIn: [Tu Perfil](https://linkedin.com/in/tu-perfil)

## 🙏 Agradecimientos

- Dataset proporcionado por Worldline y ULB Machine Learning Group
- Kaggle por alojar el dataset
- Comunidad de Scikit-learn por las herramientas de ML
- Render por el hosting gratuito

## 📚 Referencias

- [DBSCAN Algorithm - Wikipedia](https://en.wikipedia.org/wiki/DBSCAN)
- [Scikit-learn DBSCAN Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)
- [Original Dataset Paper](https://www.researchgate.net/project/Fraud-detection-5)

---

⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub!

#!/bin/bash

# Script para iniciar la aplicación Flask DBSCAN

echo "🚀 Iniciando DBSCAN Fraud Detection System..."

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
fi

# Activar entorno virtual
echo "✅ Activando entorno virtual..."
source venv/bin/activate

# Verificar si Flask está instalado
if ! python -c "import flask" 2>/dev/null; then
    echo "📥 Instalando dependencias..."
    pip install -q Flask Werkzeug pandas numpy matplotlib seaborn scikit-learn gunicorn
fi

# Iniciar la aplicación
echo "🌐 Iniciando servidor en http://localhost:5001"
echo "📊 Presiona Ctrl+C para detener"
echo ""
python app.py

# DBSCAN Fraud Detection - Guía de Deployment

## 🚀 Deployment en Render (Recomendado)

### Paso 1: Preparar el Repositorio en GitHub

1. **Crear un nuevo repositorio en GitHub**
   - Ve a https://github.com/new
   - Nombre: `api-dbscan` o `dbscan-fraud-detection`
   - Descripción: "Sistema de detección de fraude bancario con DBSCAN"
   - Público o Privado (tu elección)
   - Click en "Create repository"

2. **Subir el código a GitHub**

```bash
cd /home/jesus/Documentos/plf/api-dbscan

# Inicializar Git (si no está inicializado)
git init

# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "feat: Sistema completo de detección de fraude con DBSCAN"

# Agregar el remote de GitHub (reemplaza con tu URL)
git remote add origin https://github.com/TU-USUARIO/api-dbscan.git

# Cambiar a la rama main
git branch -M main

# Subir el código
git push -u origin main
```

### Paso 2: Configurar en Render

1. **Crear cuenta en Render**
   - Ve a https://render.com
   - Click en "Get Started" o "Sign Up"
   - Puedes registrarte con GitHub (recomendado)

2. **Crear un nuevo Web Service**
   - En el Dashboard, click en "New +" (botón azul arriba a la derecha)
   - Selecciona "Web Service"
   - Conecta tu repositorio de GitHub
   - Busca y selecciona tu repositorio `api-dbscan`

3. **Configuración del Web Service**

   Completa los siguientes campos:

   ```
   Name: dbscan-fraud-detection
   Region: Oregon (US West) o la más cercana a ti
   Branch: main
   Root Directory: (dejar vacío)
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```

4. **Plan y Variables de Entorno**
   - Instance Type: **Free** (para empezar)
   - Advanced Settings (opcional):
     - Agregar variable de entorno si necesitas:
       ```
       PYTHON_VERSION=3.11.0
       ```

5. **Deploy**
   - Click en "Create Web Service"
   - Espera de 5-10 minutos mientras se construye y despliega
   - Render te dará una URL como: `https://dbscan-fraud-detection.onrender.com`

### Paso 3: Verificar el Deployment

1. Una vez completado, verás el estado "Live" en verde
2. Click en la URL proporcionada para ver tu aplicación
3. La primera carga puede tardar ~1 minuto (plan gratuito)

## 🔄 Actualizaciones Automáticas

Render detecta automáticamente cambios en tu repositorio de GitHub:

```bash
# Hacer cambios en tu código
git add .
git commit -m "feat: nueva característica"
git push

# Render desplegará automáticamente los cambios
```

## ⚠️ Consideraciones Importantes para Render Free Tier

1. **Sleep Mode**: El servicio gratuito se duerme después de 15 minutos de inactividad
   - Primera carga después de dormir: ~30-60 segundos
   - Solución: Usar un servicio de "ping" o actualizar a plan pagado

2. **Límites del Plan Gratuito**:
   - 750 horas/mes de uptime
   - Memoria: 512 MB RAM
   - CPU compartida
   - Suficiente para demos y proyectos personales

3. **Tamaño del Dataset**:
   - El archivo `creditcard.csv` es grande (~150 MB)
   - Asegúrate de que esté en el repositorio
   - Render tiene límite de 500 MB para free tier

## 🐛 Troubleshooting

### Error: "Build failed"

**Problema**: Dependencias no se instalan correctamente

**Solución**:
```bash
# Verificar que requirements.txt tenga versiones compatibles
pip freeze > requirements.txt

# O usar versiones específicas que funcionen
```

### Error: "Application timeout"

**Problema**: La app tarda mucho en cargar los datos

**Solución**: Optimizar la carga de datos en `app.py`:
```python
# Cachear los datos
from functools import lru_cache

@lru_cache(maxsize=1)
def load_data_cached():
    return pd.read_csv("datasets/creditcard.csv")
```

### Error: "Out of memory"

**Problema**: El dataset es muy grande para 512 MB RAM

**Solución**:
1. Usar una muestra más pequeña del dataset
2. Implementar carga lazy de las visualizaciones
3. Actualizar a un plan pagado

## 📊 Alternativas de Deployment

### Opción 2: Heroku

```bash
# Instalar Heroku CLI
curl https://cli-assets.heroku.com/install.sh | sh

# Login
heroku login

# Crear app
heroku create dbscan-fraud-detection

# Deploy
git push heroku main
```

### Opción 3: Railway

1. Ve a https://railway.app
2. "Start a New Project" → "Deploy from GitHub repo"
3. Selecciona tu repositorio
4. Railway detecta automáticamente Python y despliega

### Opción 4: PythonAnywhere

1. Registrarte en https://www.pythonanywhere.com
2. Subir archivos o clonar desde GitHub
3. Configurar WSGI para Flask
4. Más manual pero muy estable

## 🔐 Variables de Entorno (Opcional)

Si necesitas agregar configuración sensible:

1. En Render Dashboard → tu servicio → "Environment"
2. Agregar variables:
   ```
   FLASK_ENV=production
   SECRET_KEY=tu-clave-secreta-aqui
   ```

3. En `app.py`:
   ```python
   import os
   
   app.secret_key = os.environ.get('SECRET_KEY', 'default-key')
   ```

## 📈 Monitoreo

### Logs en Render

- Dashboard → tu servicio → "Logs"
- Muestra errores y actividad en tiempo real
- Útil para debugging

### Métricas

- Dashboard → tu servicio → "Metrics"
- CPU, Memoria, Requests
- Solo disponible en planes pagados

## 💰 Costos

- **Free**: $0/mes - Perfecto para demos
- **Starter**: $7/mes - Sin sleep, más recursos
- **Standard**: $25/mes - Producción pequeña

## ✅ Checklist Final

Antes de considerar el deployment completo:

- [ ] Código subido a GitHub
- [ ] `requirements.txt` completo y correcto
- [ ] `Procfile` configurado
- [ ] `runtime.txt` con versión de Python
- [ ] Dataset incluido o accesible
- [ ] README.md actualizado con URL de demo
- [ ] `.gitignore` configurado correctamente
- [ ] Probado localmente sin errores
- [ ] Web Service creado en Render
- [ ] Deployment exitoso (estado "Live")
- [ ] URL funcional y accesible
- [ ] Todas las visualizaciones cargan correctamente

## 🎉 ¡Listo!

Tu aplicación ahora está en vivo y accesible desde cualquier parte del mundo.

**Recuerda actualizar el README.md** con la URL real de tu deployment:
```markdown
🔗 [Ver Demo en Vivo](https://tu-app.onrender.com)
```

---

¿Problemas? Revisa los logs en Render o crea un issue en GitHub.

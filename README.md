# Compresión de Datos - TP Integrador

API para comprimir y descomprimir texto usando algoritmos **Huffman** y **Shannon-Fano**.

## 🚀 Instalación y ejecución

### Requisitos previos
- Python 3.8 o superior
- pip (viene con Python)

### Pasos para ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/marianosalast/cdd-integrador.git
cd cdd-integrador

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar la API
uvicorn api:app --reload

# Tambien se puede con:
py api.py
python -m uvicorn api:app --reload
```

### Verificar que funciona
- Abre tu navegador y ve a: http://localhost:8000/docs
- Deberías ver la documentación interactiva de la API

## 📡 Cómo usar la API

### Comprimir texto
```bash
curl -X POST "http://localhost:8000/compress" \
     -H "Content-Type: application/json" \
     -d '{"text": "abracadabra"}'
```

### O usar la documentación web
1. Ve a http://localhost:8000/docs
2. Haz clic en "Try it out" en el endpoint `/compress`
3. Ingresa tu texto y ejecuta

## 📊 Endpoints disponibles

- **`POST /compress`** - Comprimir texto con ambos algoritmos
- **`POST /decompress/huffman`** - Descomprimir con Huffman
- **`POST /decompress/shannon_fano`** - Descomprimir con Shannon-Fano
- **`GET /download/{filename}`** - Descargar archivo comprimido

## 🔧 Solución de problemas

### Error: "uvicorn: command not found"
```bash
pip install uvicorn[standard]
```

### Error: "fastapi: command not found"
```bash
pip install fastapi
```

### Puerto ocupado
```bash
uvicorn api:app --reload --port 8001
```

## 📁 Estructura del proyecto

```
TPIntegrador/
├── api.py              # API principal
├── all.py              # Función de compresión
├── huffman.py          # Algoritmo Huffman
├── shannon_fano.py     # Algoritmo Shannon-Fano
├── metrics.py          # Cálculo de métricas
├── descarga.py         # Utilidades
├── requirements.txt    # Dependencias
└── compressed/         # Archivos comprimidos
```

## 🌐 Desplegado en Render
URL: [Agregar tu URL de Render cuando esté lista]
# Compresión de Datos - TP Integrador

API para comprimir y descomprimir texto usando algoritmos **Huffman** y **Shannon-Fano**.

## Instalación y ejecución

```bash
# Clonar
git clone https://github.com/marianosalast/cdd-integrador.git
cd cdd-integrador

# Instalar
pip install -r requirements.txt

# Ejecutar
uvicorn api:app --reload
```

## Endpoints

- **Comprimir**: `POST /compress` - Envía `{"text": "tu texto"}`
- **Descomprimir Huffman**: `POST /decompress/huffman`
- **Descomprimir Shannon-Fano**: `POST /decompress/shannon_fano`
- **Documentación**: http://localhost:8000/docs

## 📊 Respuesta

La API devuelve:
- Datos comprimidos de ambos algoritmos
- Métricas comparativas (compresión, eficiencia)
- Tabla de símbolos y códigos
- Árbol de Huffman para visualización

## 📁 Archivos

- `api.py` - API principal
- `huffman.py` / `shannon_fano.py` - Algoritmos
- `metrics.py` - Cálculo de métricas
- `all.py` - Función principal
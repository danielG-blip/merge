Proyecto de Análisis de Datos de Clientes y Ventas

Este proyecto realiza el análisis de datos de clientes y ventas. Incluye módulos para cargar datos desde archivos CSV, limpiar y procesar la información (como normalizar textos, eliminar duplicados y convertir tipos de datos), y preparar los datos para análisis posteriores. Los datos se almacenan en la carpeta `"data" con subcarpetas para datos crudos y procesados.

1. Asegúrate de tener Python instalado (versión 3.8 o superior recomendada).
2. Crea un entorno virtual (si no existe):
   ```
   python -m venv .venv
   ```
3. Activa el entorno virtual:
   - En Windows: `.venv\Scripts\activate`
   - En macOS/Linux: `source .venv/bin/activate`
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

Para ejecutar el análisis principal, corre el script `analisis.py`:
```
python analisis.py
```
Asegúrate de que los archivos de datos (`clientes.csv` y `ventas.csv`) estén en la carpeta `data/raw/` antes de ejecutar.
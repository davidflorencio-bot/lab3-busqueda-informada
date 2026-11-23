# Laboratorio N° 3 – Búsqueda informada: Greedy Best-First Search y A*

**Curso:** Inteligencia Artificial 2026-II – E.P. Ingeniería de Software, FISI, UNMSM  
**Docente:** Prof. Juan Gamarra Moreno  
**Alumno:** Florencio Valenzuela, David (23200256)

## Descripción

Planificación de rutas sobre una versión simplificada de la red vial del Perú (distancias en km).
Se limpia por código un CSV con errores de calidad, se verifica que la heurística (distancia en
línea recta) es admisible y consistente, y se comparan cinco algoritmos: BFS, DFS, costo uniforme,
Greedy Best-First Search y A* (incluido A* ponderado). Para cada uno se miden los nodos expandidos,
los nodos generados y el tamaño máximo de la frontera.

Problemas resueltos: **Cusco → Lima** y **Cusco → Trujillo**.

## Estructura

```
lab3-busqueda-informada/
├── datos/
│   ├── rutas_peru_sur.csv
│   ├── rutas_peru_norte.csv
│   ├── heuristica_lima.csv
│   └── heuristica_trujillo.csv
├── figuras/
│   └── ponderado.png
├── grafo.py                          # carga, limpieza, grafo y verificación de la heurística
├── busqueda.py                       # BFS, DFS, costo uniforme, Greedy, A* y métricas
├── Lab3_Florencio_Valenzuela.ipynb   # notebook ejecutado: pasos 1 al 11 y actividad propuesta
├── Lab3_Florencio_Valenzuela.pdf     # informe
└── README.md
```

## Requisitos

- Python 3.10 o superior
- matplotlib (el resto son bibliotecas estándar: `csv`, `heapq`, `collections`, `os`)

## Cómo ejecutar

### Opción A: Google Colab (recomendada)

1. Abrir Colab y cargar el notebook con **Archivo → Subir notebook**.
2. En el panel de archivos (ícono de carpeta), crear una carpeta `datos` y subir ahí los cuatro CSV.
3. Ejecutar **Entorno de ejecución → Reiniciar sesión y ejecutar todo**.

### Opción B: entorno local

```bash
git clone https://github.com/davidflorencio-bot/lab3-busqueda-informada.git
cd lab3-busqueda-informada
python -m venv .venv
# Windows (PowerShell): .venv\Scripts\Activate.ps1
# Linux o macOS:        source .venv/bin/activate
pip install matplotlib notebook
jupyter notebook Lab3_Florencio_Valenzuela.ipynb
```

Ejecutar todas las celdas en orden. La gráfica se guarda en `figuras/ponderado.png`.

## Resultados principales

| Problema | Costo óptimo | A* (expandidos) | Costo uniforme (expandidos) | Greedy |
|---|---|---|---|---|
| Cusco → Lima | 1 173 km | 12 | 13 | 1 180 km (+0,6 %) |
| Cusco → Trujillo | 1 738 km | 17 | 18 | 1 862 km (+7,1 %) |

El análisis completo está en el informe.

## Uso de IA

El uso de asistentes de IA se declara en la sección 10 del informe.

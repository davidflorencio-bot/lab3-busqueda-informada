readme = """# Laboratorio N° 3 - Búsqueda informada (Greedy Best-First y A*)

Curso: Inteligencia Artificial - UNMSM
Estudiante: David Abraham Florencio Valenzuela

## Contenido
- `Lab3_Florencio_David.ipynb`: notebook con los 5 algoritmos y la actividad propuesta.
- `datos/`: archivos CSV de rutas y heurísticas.
- `figuras/`: gráfica del compromiso A* ponderado.
- `informe.pdf`: informe con tablas, gráfica y análisis crítico.

## Cómo ejecutar
Abrir el notebook en Google Colab, subir la carpeta `datos/` a `/content/datos`,
y ejecutar todas las celdas en orden (Entorno de ejecución → Reiniciar y ejecutar todo).
"""
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

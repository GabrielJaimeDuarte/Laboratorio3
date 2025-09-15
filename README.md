Laboratorio 3: Algoritmos Genéticos
Autores: Gabriel Jaime Duarte López y Camilo José Cifuentes Garzón
Fecha: Septiembre 2025

Descripción
Este proyecto implementa algoritmos genéticos para resolver tres problemas distintos de optimización:

Búsqueda del máximo global de una función cuadrática

Solución al Problema del Viajante (TSP)

Optimización de horarios escolares

Cada problema demuestra diferentes aplicaciones y configuraciones de algoritmos genéticos, mostrando su versatilidad para resolver problemas complejos.

🏗Estructura del Proyecto
text
lab3-algoritmos-geneticos/
│
├── punto_1.py
├── punto_2.py
├── punto_3.py
├── Explicación_Lab_3.pdf
└── README.md

Problemas Resueltos

Función Cuadrática - Búsqueda del Máximo
Problema: Encontrar el máximo global de la función f(x) = x² - 3x + 4 en el rango [0, 5].

Implementación:

Solución analítica mediante cálculo del vértice

Verificación computacional en el rango especificado

Resultado: El máximo se encuentra en x = 5.0 con f(x) = 14.0

2. Problema del Viajante (TSP)
Problema: Encontrar la ruta más corta que visite 10 ciudades con coordenadas aleatorias y regrese al origen.

Características del Algoritmo Genético:

Representación: Permutación de ciudades

Función de fitness: Inversa de la distancia total

Operador de cruce: Ordered Crossover (OX)

Operador de mutación: Intercambio de dos ciudades

Selección: Por torneo

Tamaño de población: 50 individuos

Generaciones: 100

3. Optimización de Horarios Escolares
Problema: Crear horarios que cumplan con restricciones de:

No superposición de clases para un mismo grupo

Disponibilidad de profesores

Preferencias de horarios para materias

Distribución balanceada de materias

Características del Algoritmo Genético:

Representación: Lista de tuplas (horario, grupo, profesor, materia)

Función de fitness: Puntuación basada en cumplimiento de restricciones

Operadores: Selección por torneo, cruce de dos puntos, mutación por sustitución

Elitismo: Conservación de los 5 mejores individuos

Experimentación con diferentes tasas de mutación (0.01, 0.05, 0.1, 0.2)

Instalación y Ejecución
Requisitos Previos
Python 3.7+

pip (gestor de paquetes de Python)

Instalación de Dependencias
bash
pip install -r requirements.txt
Ejecución de los Programas
Punto 1 - Función Cuadrática:

bash
python punto_1.py
Punto 2 - Problema del Viajante:

bash
python punto_2.py
Punto 3 - Horarios Escolares:

bash
python punto_3.py
Resultados y Análisis
Problema del Viajante
El algoritmo genético demostró ser efectivo para encontrar rutas cortas que visitan todas las ciudades. La convergencia del fitness muestra mejoras progresivas en la calidad de las soluciones.

Optimización de Horarios
Se experimentó con cuatro tasas de mutación diferentes:

Tasa de Mutación	Fitness Final	Observaciones
0.01	876.67	Convergencia estable pero lenta
0.05	871.67	Convergencia más rápida que 0.01
0.1	900.00	Buen balance exploración/explotación
0.2	910.00	Mejor resultado
Conclusión: La tasa de mutación de 0.2 produjo la mejor solución, demostrando la importancia de una adecuada exploración del espacio de búsqueda.

Dependencias
El proyecto requiere las siguientes bibliotecas de Python:

numpy

matplotlib

collections (built-in)

random (built-in)

Visualizaciones
El proyecto genera varias visualizaciones:

Gráfica de la ruta óptima para TSP

Curvas de convergencia para ambos algoritmos genéticos

Comparación de diferentes tasas de mutación

Conceptos Clave de Algoritmos Genéticos Implementados
Representación: Diferentes esquemas de codificación para cada problema

Función de Fitness: Diseñada específicamente para cada dominio problemático

Operadores Genéticos:

Selección por torneo

Cruce ordenado (OX) y de dos puntos

Mutación por intercambio y sustitución

Elitismo: Preservación de los mejores individuos

Parámetros Adjustables: Tasa de mutación, tamaño de población, número de generaciones



Interfaz gráfica para visualización en tiempo real

Paralelización del cálculo de fitness

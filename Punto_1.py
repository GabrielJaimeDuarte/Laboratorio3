import numpy as np

def f(x):
    return x**2 - 3*x + 4

a, b, c = 1, -3, 4  
x_vertex = -b / (2 * a) 
y_vertex = f(x_vertex)

print(f"Vértice en x = {x_vertex}, f(x) = {y_vertex}")

x_values = np.linspace(0, 5, 100)
y_values = [f(x) for x in x_values]

max_value = max(y_values)
max_x = x_values[y_values.index(max_value)]

print(f"Máximo en el rango [0, 5] en x = {max_x}, f(x) = {max_value}")
import numpy as np
import pandas as pd
import math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Circle
from mpl_toolkits.mplot3d import Axes3D


#-------------------------------------------------------------------------------------------------------------------
#----------------------------------------- Graficador simpl de funciones -------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_función(x, y, titulo, x_label, y_label, legend):
  plt.figure(figsize=(6, 6))
  plt.plot(x, y, label=legend)
  plt.title(titulo)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.grid(True)
  plt.show()
  
  
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Graficador de funciones y derivadas ----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def plot_f1_and_f2(f1, f2=None, x_min=-5, x_max=5, label1="f(x)", label2="f'(x)"):
    x = np.linspace(x_min, x_max,100)

    # Setting the axes at the centre.
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, f1(x), 'r', label=label1)
    if not f2 is None:

        if isinstance(f2, np.ndarray):
            plt.plot(x, f2, 'bo', markersize=3, label=label2,)
        else:
            plt.plot(x, f2(x), 'b', label=label2)
    plt.title('f(x) y df/dx')
    plt.legend()
    plt.grid(True)
    plt.show()
  

#-------------------------------------------------------------------------------------------------------------------
#----------------------------------------- Graficador simpl de funciones -------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_función(x, y, titulo, x_label, y_label, legend):
  plt.figure(figsize=(6, 6))
  plt.plot(x, y, label=legend)
  plt.title(titulo)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.grid(True)
  plt.show()
  

#-------------------------------------------------------------------------------------------------------------------
#------------------------------- Graficador de funciones y derivadas numéricas -------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def plot_num_der(x,y, derivada, titulo, label_1, label_2):
  plt.figure(figsize=(10,6))
  plt.title(titulo,fontsize=15)
  plt.plot(x,y,'bo-',label=label_1)
  plt.plot(x[:-1],derivada,'ro--',label=label_2)
  plt.xlabel("x",fontsize=15)
  plt.ylabel("y",fontsize=15)
  plt.legend(fontsize=15)
  plt.grid()
  plt.show()
  
  
#-------------------------------------------------------------------------------------------------------------------
#---------------------------------------- Ejemplo de mínimo global y local -----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def ejemplo_de_minimos():
# Definir la función cuártica
  def quartic_function(x):
     return x**4 - 8*x**3 + 18*x**2

  result_global = minimize(quartic_function, x0=0)
  result_local = minimize(quartic_function, x0=3)
  x_vals = np.linspace(-1, 4, 100)
  y_vals = quartic_function(x_vals)

  # Graficar la función
  plt.plot(x_vals, y_vals, label='f(x) = $x^4 - 8x^3 + 18x^2$')
  plt.scatter(result_global.x, quartic_function(result_global.x), color='red', label='Mínimo Global')
  plt.scatter(result_local.x, quartic_function(result_local.x), color='green', label='Mínimo Local')

  plt.xlabel('x')
  plt.ylabel('f(x)')
  plt.legend()
  plt.title('Función Cuártica con Múltiples Mínimos y Mínimo Global')
  plt.grid(True)
  plt.show()
  
  
#-------------------------------------------------------------------------------------------------------------------
#---------------------------------- Plot de contorno para descenso del gradiente -----------------------------------
#-------------------------------------------------------------------------------------------------------------------

def plot_contorno_dg_2d(x,y,z,trayectoria_descenso):
  plt.contour(x,y,z, levels=20, cmap='viridis')
  plt.plot(trayectoria_descenso[:, 0], trayectoria_descenso[:, 1], marker='o', color='red', label='Descenso del Gradiente')
  plt.xlabel('x1')
  plt.ylabel('x2')
  plt.legend()
  plt.title('Descenso del Gradiente en 2D')
  plt.grid(True)
  plt.show()
  
  
#-------------------------------------------------------------------------------------------------------------------
#-------------------------------- Plot 3D y líneas tangentes: Derivadas parciales ----------------------------------
#-------------------------------------------------------------------------------------------------------------------

def superficie_linea_tangente(X,Y,func, df_dx, df_dy, x_point, y_point):
  Z = func(X,Y)
  fig = plt.figure(figsize=(12, 6))
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, antialiased=False)
  # Punto de interés
  ax.scatter(x_point, y_point, func(x_point, y_point), color='red', s=100, label='Punto de interés')

  # Líneas tangentes para las derivadas parciales
  tangent_x = np.linspace(x_point - 1, x_point + 1, 10)
  tangent_y = x_point + df_dx(x_point, y_point) * (tangent_x - x_point)
  ax.plot(tangent_x, [y_point] * len(tangent_x), func(tangent_x, y_point), color='blue', label='Tangente a x')
  ax.plot([x_point] * len(tangent_y), tangent_y, func(x_point, tangent_y), color='green', label='Tangente a y')

  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_title('Superficie y Derivadas Parciales en el Punto de Interés')
  ax.legend()

  plt.show()
  
  
#-------------------------------------------------------------------------------------------------------------------
#---------------------------------- Plot 3D y plano tangente: Derivadas parciales ----------------------------------
#-------------------------------------------------------------------------------------------------------------------

# Gráfico de la superficie
def superficie_plano_tangente(x,y, func,x_point,y_point):

  def tangential_plane(x, y, x_point, y_point):
    return func(x_point, y_point) + (x - x_point) + 2 * (y - y_point)

  # Visualización del plano tangente y la superficie
  X, Y = np.meshgrid(x, y)
  Z = func(X, Y)

  fig = plt.figure(figsize=(10, 6))
  ax = fig.add_subplot(111, projection='3d')

  # Gráfico de la superficie
  surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, antialiased=False)
  # Gráfico del plano tangente
  tangential_surface = ax.plot_surface(X, Y, tangential_plane(X, Y, x_point, y_point), alpha=0.5, linewidth=0, antialiased=False)

  # Punto de interés
  ax.scatter(x_point, y_point, func(x_point, y_point), color='red', s=100, label='Punto de interés')

  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_title('Superficie y Plano Tangente en el Punto de Interés')
  ax.legend()

  # Barra de colores para la superficie
  fig.colorbar(surface, ax=ax, shrink=0.6, aspect=10)

  plt.show()
  
  
#-------------------------------------------------------------------------------------------------------------------
#--------------------------------------- Plot 3D para descenso del gradiente ---------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def grafica_3d_dg(X,Y,Z, trayectoria_descenso, z_trayectoria_descenso):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_title('Superficie de la Función en 3D')

  # Añadir la trayectoria del descenso del gradiente
  trayectoria_descenso = np.array([[p[0], p[1], z_trayectoria_descenso[i]] for i,p in enumerate(trayectoria_descenso)])
  ax.plot(trayectoria_descenso[:, 0], trayectoria_descenso[:, 1], trayectoria_descenso[:, 2], marker='o', color='red', label='Descenso del Gradiente')

  plt.legend()
  plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#-------------------------------------------------------------------------------------------------------------------
#--------------------------------------- Graficador de ecuaciones lineales -----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def plot_lines(M):
    x_1 = np.linspace(-10,10,100)
    x_2_line_1 = (M[0,2] - M[0,0] * x_1) / M[0,1]
    x_2_line_2 = (M[1,2] - M[1,0] * x_1) / M[1,1]

    _, ax = plt.subplots(figsize=(10, 10))
    ax.plot(x_1, x_2_line_1, '-', linewidth=2, color='#0075ff',
        label=f'$x_2={-M[0,0]/M[0,1]:.2f}x_1 + {M[0,2]/M[0,1]:.2f}$')
    ax.plot(x_1, x_2_line_2, '-', linewidth=2, color='#ff7300',
        label=f'$x_2={-M[1,0]/M[1,1]:.2f}x_1 + {M[1,2]/M[1,1]:.2f}$')

    A = M[:, 0:-1]
    b = M[:, -1::].flatten()
    d = np.linalg.det(A)

    if d != 0:
        solution = np.linalg.solve(A,b)
        ax.plot(solution[0], solution[1], '-o', mfc='none',
            markersize=10, markeredgecolor='#ff0000', markeredgewidth=2)
        ax.text(solution[0]-0.25, solution[1]+0.75, f'$(${solution[0]:.0f}$,{solution[1]:.0f})$', fontsize=14)
    ax.tick_params(axis='x', labelsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.set_xticks(np.arange(-10, 10))
    ax.set_yticks(np.arange(-10, 10))

    plt.xlabel('$x_1$', size=14)
    plt.ylabel('$x_2$', size=14)
    plt.legend(loc='upper right', fontsize=14)
    plt.axis([-10, 10, -10, 10])

    plt.grid()
    plt.gca().set_aspect("equal")

    plt.show()


#-------------------------------------------------------------------------------------------------------------------
#--------------------------------------- Graficador de ecuaciones lineales -----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_soluciones(x, y, A, b,limite, titulo):
  plt.figure()

  for ecuacion in y:
    plt.plot(x, ecuacion)

  try:
    solucion = np.linalg.solve(A,b)
    plt.plot(solucion[0], solucion[1], '-o', mfc='none',markersize=10, markeredgecolor='#ff0000', markeredgewidth=2)
  except np.linalg.LinAlgError as err:
    print(err)

  plt.xlim(-(limite + 2), (limite + 2))
  plt.ylim(-(limite + 2), (limite + 2))
  plt.xlabel('$x$', size=14)
  plt.ylabel('$y$', size=14)
  plt.title(titulo)
  plt.grid()
  plt.show()


#-------------------------------------------------------------------------------------------------------------------
#----------------------------------------- Graficador de simple de vectores ----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def plot_vectors(list_v, list_label, list_color,limit1,limit2):
    _, ax = plt.subplots(figsize=(6, 6))
    ax.tick_params(axis='x', labelsize=6)
    ax.tick_params(axis='y', labelsize=6)
    ax.set_xticks(np.arange(-limit1, limit2))
    ax.set_yticks(np.arange(-limit2, limit2))

    plt.xlim(-limit1, limit1)
    plt.ylim(-limit2,limit2)

    for i, v in enumerate(list_v):
        sgn = 0.4 * np.array([[1] if i==0 else [i] for i in np.sign(v)])
        plt.quiver(v[0], v[1], color=list_color[i], angles='xy', scale_units='xy', scale=1)
        ax.text(v[0]-0.2+sgn[0], v[1]-0.2+sgn[1], list_label[i], fontsize=14, color=list_color[i])

    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5, alpha = 0.5)
    plt.gca().set_aspect("equal")
    plt.title('Vectores en 2D')
    plt.show()


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Graficador de vectores con propiedades -------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def plot_vector_propiedades(vector,limit1,limit2):
  # Cálculo de la magnitud
  magnitud = np.linalg.norm(vector)
  # Cálculo de la dirección (ángulo en radianes con respecto al eje x)
  direccion = np.arctan2(vector[1], vector[0])

  # Plot del vector
  plt.figure(figsize=(6, 6))
  plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector')

  # Configuración del gráfico
  plt.xlim(limit1,limit2)
  plt.ylim(limit1,limit2)
  plt.axhline(0, color='black',linewidth=0.5)
  plt.axvline(0, color='black',linewidth=0.5)
  plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5, alpha = 0.5)

  # Etiquetas y leyenda
  plt.text(vector[0] + 0.1, vector[1] + 0.1, f'Magnitud: {magnitud:.2f}', fontsize=10)
  plt.text(0.5, -0.5, f'Dirección: {direccion:.2f} radianes', fontsize=10)
  plt.title('Vector en 2D')
  plt.legend()
  plt.show()


#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------ Graficador de productos punto ------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def visualizar_dot(v, w):
    # Cálculo del producto punto
    producto_punto = np.dot(v, w)

    # Proyección de w en la dirección de v
    proyeccion_w_en_v = (producto_punto / np.linalg.norm(v)**2) * v

    # Visualización de los vectores
    plt.figure(figsize=(6, 6))
    plt.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='b', label='v')
    plt.quiver(0, 0, w[0], w[1], angles='xy', scale_units='xy', scale=1, color='r', label='w')
    plt.quiver(0, 0, proyeccion_w_en_v[0], proyeccion_w_en_v[1], angles='xy', scale_units='xy', scale=1, color='g', label='Proyección de w en v')

    # Configuración del gráfico
    max_value = max(np.max(v), np.max(w), np.max(proyeccion_w_en_v))
    min_value = min(np.min(v), np.min(w), np.min(proyeccion_w_en_v))

    plt.xlim(min_value - 1, max_value + 1)
    plt.ylim(min_value - 1, max_value + 1)
    plt.axhline(0, color='gray', linewidth=0.5)
    plt.axvline(0, color='gray', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)

    # Etiquetas y leyenda
    plt.text(v[0] + 0.1, v[1] + 0.1, 'v', fontsize=10)
    plt.text(w[0] + 0.1, w[1] + 0.1, 'w', fontsize=10)
    plt.text(proyeccion_w_en_v[0] + 0.1, proyeccion_w_en_v[1] + 0.1, 'Proyección', fontsize=10, color='g')
    plt.title('Vectores en 2D, Proyección de w en v y Producto Punto')
    plt.legend()

    # Mostrar el ángulo entre los vectores
    plt.annotate("", xy=(w[0], w[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))
    plt.annotate("", xy=(v[0], v[1]), xytext=(0, 0), arrowprops=dict(arrowstyle="->"))
    plt.annotate(r'$\theta$', xy=(0.5, 0.8), fontsize=12)

    plt.show()

    # Cálculo del ángulo en radianes
    magnitud_v = np.linalg.norm(v)
    magnitud_w = np.linalg.norm(w)
    cos_theta = producto_punto / (magnitud_v * magnitud_w)
    theta_radianes = np.arccos(cos_theta)

    print(f'Producto Punto: {producto_punto}')
    print(f'Ángulo entre los vectores en radianes: {theta_radianes:.2f}')


#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------ Graficador de productos cruz -------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def visualizar_producto_cruz(v, w):
    # Cálculo del producto cruz
    producto_cruz = np.cross(v, w)

    # Configuración del gráfico
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(0, 0, 0, v[0], v[1], v[2], color='b', label='v')
    ax.quiver(0, 0, 0, w[0], w[1], w[2], color='r', label='w')
    ax.quiver(0, 0, 0, producto_cruz[0], producto_cruz[1], producto_cruz[2], color='g', label='v x w')

    # Configuración de límites
    max_value = max(np.max(v), np.max(w), np.max(producto_cruz))
    min_value = min(np.min(v), np.min(w), np.min(producto_cruz))
    ax.set_xlim([min_value - 1, max_value + 1])
    ax.set_ylim([min_value - 1, max_value + 1])
    ax.set_zlim([min_value - 1, max_value + 1])

    # Etiquetas y leyenda
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.text(v[0] + 0.1, v[1] + 0.1, v[2] + 0.1, 'v', fontsize=10)
    ax.text(w[0] + 0.1, w[1] + 0.1, w[2] + 0.1, 'w', fontsize=10)
    ax.text(producto_cruz[0] + 0.1, producto_cruz[1] + 0.1, producto_cruz[2] + 0.1, 'v x w', fontsize=10, color='g')
    ax.set_title('Producto Cruz en el Espacio Tridimensional')
    ax.legend()

    plt.show()


#-------------------------------------------------------------------------------------------------------------------
#-------------------------------------- Graficador de transformación lineal ----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def transformacion_de_espacio(A):
    # Generar puntos en el círculo unitario
    t = np.linspace(0, 2*np.pi, 100)
    circulo_unitario = np.array([np.cos(t), np.sin(t)])

    # Aplicar la transformación de la matriz A
    circulo_transformado = np.dot(A, circulo_unitario)

    # Configurar el gráfico
    plt.figure(figsize=(6, 6))
    plt.plot(circulo_unitario[0], circulo_unitario[1], label='Círculo Unitario', color='blue')
    plt.plot(circulo_transformado[0], circulo_transformado[1], label='Círculo Transformado', color='orange')

    # Configurar detalles del gráfico
    plt.title('Transformación del Círculo Unitario por la Matriz A')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    plt.legend()
    plt.axis('equal')  # Hacer que los ejes tengan la misma escala

    # Mostrar el resultado
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#---------------------------------------------- Graficador de vectores ---------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficarVectores(vecs,cols,alpha=1):
  # we add two lines for the axis
  plt.axvline(x = 0, color = 'grey', zorder = 0)
  plt.axhline(y = 0, color = 'grey', zorder = 0)

  for i in range(len(vecs)):
    x = np.concatenate([[0,0], vecs[i]])
    plt.quiver([x[0]],
               [x[1]],
               [x[2]],
               [x[3]],
               angles = 'xy', scale_units = 'xy',
               scale = 1,
               color = cols[i],
               alpha = alpha)
    
 
#-------------------------------------------------------------------------------------------------------------------
#----------------------------------- Graficador de Matrices como un espacio vectorial ------------------------------
#-------------------------------------------------------------------------------------------------------------------  

 
def graficarMatriz(matriz, vectorCol=['red','blue']):

  # unit circle
  x = np.linspace(-1,1,100000)
  y = np.sqrt(1-(x**2))

  # transpormed unit circle
  x1 = matriz[0,0]*x + matriz[0,1]*y
  y1 = matriz[1,0]*x + matriz[1,1]*y
  x1_neg = matriz[0,0]*x - matriz[0,1]*y
  y1_neg = matriz[1,0]*x - matriz[1,1]*y

  # vectors
  u1 = [matriz[0,0], matriz[1,0]]
  v1 = [matriz[0,1], matriz[1,1]]

  graficarVectores([u1, v1], cols=[vectorCol[0], vectorCol[1]])

  plt.plot(x1,y1, 'green', alpha = 0.7)
  plt.plot(x1_neg, y1_neg, 'green', alpha = 0.7)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#-------------------------------------------------------------------------------------------------------------------
#------------------------------------- Graficador de distribuciones discretas ---------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_distribucion(X, P, x_label, y_label, title='PMF'):
  plt.figure(figsize=(8,5))
  plt.bar(X, P, color='skyblue', edgecolor='black')
  plt.title(title)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.grid(linestyle='--', alpha=0.7)
  plt.show()


#-------------------------------------------------------------------------------------------------------------------
#------------------------------------- Graficador de distribuciones contínuas --------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_densidad(x, pdf, label, title, x_label, y_label):
  plt.figure(figsize=(8,5))
  plt.plot(x, pdf, label=label)
  plt.fill_between(x, pdf, alpha=0.3)
  plt.title(title)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.grid(linestyle='--', alpha=0.7)
  plt.show()
  

#-------------------------------------------------------------------------------------------------------------------
#------------------------------------- Graficador de distribuciones contínuas --------------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_densidad_intervalo(x, pdf,x_inter, pdf_inter, label, title, x_label, y_label):
  plt.figure(figsize=(8,5))
  plt.plot(x, pdf, label=label)
  plt.fill_between(x_inter, pdf_inter, alpha=0.3, color='red',label=f'Área entre {min(x_inter)} y {max(x_inter)}')
  plt.title(title)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.grid(linestyle='--', alpha=0.7)
  plt.show()


#-------------------------------------------------------------------------------------------------------------------
#------------------------------------ Graficador de distribuciones reconstruidas -----------------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_experimento_sampling(samples, x_values, pdf_values, title):
  plt.figure(figsize=(8,5))
  plt.hist(samples, bins=50, density=True, alpha=0.6, color='g', label='Histograma de Muestras', edgecolor='black')
  plt.plot(x_values, pdf_values, 'r-', lw=2, label='Distribución Teórica')
  plt.xlabel('x')
  plt.ylabel('Densidad de probabilidad')
  plt.title(title)
  plt.legend()
  plt.grid(linestyle='--', alpha=0.7)
  plt.show()
  

#-------------------------------------------------------------------------------------------------------------------
#------------------------------ Graficador de distribuciones reconstruidas con humbral -----------------------------
#-------------------------------------------------------------------------------------------------------------------

def graficar_muestra_umbral(x, muestra, umbral, pdf, title):
  plt.figure(figsize=(8, 5))
  plt.hist(muestra, bins=30, density=True, alpha=0.6, color='g', label='Muestra',edgecolor='black')
  xmin, xmax = plt.xlim()
  x = np.linspace(xmin, xmax, 100)
  p = pdf
  plt.plot(x, p, 'k', linewidth=2, label='Distribución Teórica')
  plt.axvline(umbral, color='r', linestyle='--', label='Umbral')
  plt.title(title)
  plt.xlabel('Valor')
  plt.ylabel('Densidad')
  plt.legend()
  plt.grid(linestyle='--', alpha=0.7)
  plt.show()
  
  
#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------- Comparador de plots de barras -----------------------------------------
#-------------------------------------------------------------------------------------------------------------------
  
def comparador_bar(x, y_1, y_2, title, label_1, label_2):
  plt.figure(figsize=(8, 5))
  plt.bar(x, y_2, color='green', edgecolor='black', label=label_2, alpha=0.7)
  plt.bar(x, y_1, color='skyblue', edgecolor='black', label=label_1, alpha=0.5)
  plt.title(title)
  plt.xlabel('X')
  plt.ylabel('P(X)')
  plt.legend()
  plt.grid(linestyle='--', alpha=0.7)
  plt.show()
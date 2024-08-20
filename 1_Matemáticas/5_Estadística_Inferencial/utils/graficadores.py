import random
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal
import scipy.stats as stats


#-------------------------------------------------------------------------------------------------------------------
#--------------------- Graficador de histograma de muestras, modelo y parámetro poblacional ------------------------
#-------------------------------------------------------------------------------------------------------------------

def histograma_frecuencias(data, parametro, bins, title, x_label='data (X)', y_label='Frecuencia', kde=True, data_label=None, color='blue'):
    
  plt.figure(figsize=(8, 4))
  sns.histplot(data, bins=bins, kde=kde, color=color, label=data_label)
  plt.axvline(parametro, color=color, linestyle='dashed', linewidth=2)
  plt.title(title)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.legend()
  plt.grid(linestyle='--', alpha=0.7)
  plt.show()
  

#-------------------------------------------------------------------------------------------------------------------
#----------------------------- Graficador de ejemplo binomial de los grandes números -------------------------------
#-------------------------------------------------------------------------------------------------------------------
  
  
def ley_grandes_numeros(prob_head, n_trials):
    # Simulamos lanzamientos de una moneda justa
    results = np.random.binomial(1, prob_head, n_trials)
    # Calculamos la media muestral acumulada
    cumulative_mean = np.cumsum(results) / np.arange(1, n_trials + 1)
    plt.figure(figsize=(8, 4))
    plt.plot(cumulative_mean, label='Media Muestral')
    plt.axhline(y=prob_head, color='r', linestyle='--', label='Valor Esperado (0.5)')
    plt.xlabel('Número de Lanzamientos')
    plt.ylabel('Media Muestral')
    plt.title('Ley de los Grandes Números: Convergencia de la Media Muestral')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()  
    

#-------------------------------------------------------------------------------------------------------------------
#------------------------------- Graficador de ejemplo TLC para medias muestrales ----------------------------------
#-------------------------------------------------------------------------------------------------------------------


def graficar_media_muestal(medias):
    plt.figure(figsize=(8, 4))
    plt.hist(medias, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    mu, std = np.mean(medias), np.std(medias)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    plt.title('Distribución de Medias Muestrales y Aproximación Normal')
    plt.xlabel('Media Muestral')
    plt.ylabel('Densidad')
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#-------------------------------- Graficador de ejemplo teorema del límite central ---------------------------------
#-------------------------------------------------------------------------------------------------------------------

  
def graficacion_TLC(pmf, mu, std):
    plt.figure(figsize=(8, 4))
    plt.bar(list(pmf.keys()), list(pmf.values()), color='skyblue', edgecolor='black')
    plt.axvline(x=mu, color='r', linestyle='--', label=f'Valor Esperado = {mu}')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2, label=f'Aprox.Normal N({mu},{std})')
    plt.title('Distribución del Experimento Aleatorio')
    plt.xlabel('Resultados')
    plt.ylabel('Densidad')
    plt.grid(linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()


#-------------------------------------------------------------------------------------------------------------------
#------------------------------- Graficador de ejemplo de error estandar de la media -------------------------------
#-------------------------------------------------------------------------------------------------------------------
    

def graficar_eem(sample_means,population_mean, eem):
    plt.figure(figsize=(8, 4))
    plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')
    plt.axvline(population_mean, color='red', linestyle='dashed', linewidth=2, label='Media Poblacional')
    plt.axvline(population_mean + eem, color='green', linestyle='--', linewidth=2, label='±1 EEM')
    plt.axvline(population_mean - eem, color='green', linestyle='--', linewidth=2)
    plt.title('Distribución de Medias Muestrales y Error Estándar de la Media')
    plt.xlabel('Media Muestral')
    plt.ylabel('Densidad')
    plt.grid(linestyle='--', alpha=0.7)
    plt.legend()
    plt.show()
    
    
#-------------------------------------------------------------------------------------------------------------------
#------------------------------- Graficador de ejemplo intervalos de confianza media -------------------------------
#-------------------------------------------------------------------------------------------------------------------
    

def graficar_ID_normal(data, mu, ci):
    plt.figure(figsize=(8, 4))
    plt.hist(data, bins=30, density=True, alpha=0.6, color='blue', edgecolor='black')
    plt.axvline(mu, color='red', linestyle='--', label=f'Media Poblacional ({mu})')
    plt.axvline(ci[0], color='green', linestyle='--', label=f'IC 95% ({ci[0]:.2f}, {ci[1]:.2f})')
    plt.axvline(ci[1], color='green', linestyle='--')
    plt.title('Distribución de las Medias Muestrales con Intervalo de Confianza')
    plt.xlabel('Media Muestral')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()


#-------------------------------------------------------------------------------------------------------------------
#---------------------------------------- Graficador right-tail normal test ----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

  
def graficar_right_normal_test(x_min, x_max, mu_population, mu_sample, sem, critical_value):
    x = np.linspace(x_min, x_max, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.norm.pdf(x, loc=mu_population, scale=sem)
    plt.plot(x, y, label='Distribución Normal')
    plt.fill_between(x, y, where=(x >= critical_value), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(mu_sample, color='blue', linestyle='dashed', linewidth=2, label=f'Media Muestral = {mu_sample:.2f}')
    plt.axvline(critical_value, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico = {critical_value:.2f}')
    plt.title('Right-Tailed Test (Distribución Normal General)')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
  

#-------------------------------------------------------------------------------------------------------------------
#---------------------------------------- Graficador left-tail normal test -----------------------------------------
#-------------------------------------------------------------------------------------------------------------------
 

def graficar_left_normal_test(x_min, x_max, mu_population, mu_sample, sem, critical_value):
    x = np.linspace(x_min, x_max, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.norm.pdf(x, loc=mu_population, scale=sem)
    plt.plot(x, y, label='Distribución Normal')
    plt.fill_between(x, y, where=(x <= critical_value), color='blue', alpha=0.5, label='Región de rechazo')
    plt.axvline(mu_sample, color='red', linestyle='dashed', linewidth=2, label=f'Media Muestral = {mu_sample:.2f}')
    plt.axvline(critical_value, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico = {critical_value:.2f}')
    plt.title('Left-Tailed Test (Distribución Normal General)')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#---------------------------------------- Graficador two-tail normal test -----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

 
def graficar_two_normal_test(x_min, x_max, mu_population, mu_sample, sem, critical_value_lower, critical_value_upper):
    x = np.linspace(x_min, x_max, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.norm.pdf(x, loc=mu_population, scale=sem)
    plt.plot(x, y, label='Distribución Normal')
    plt.fill_between(x, y, where=(x <= critical_value_lower) | (x >= critical_value_upper), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(mu_sample, color='blue', linestyle='dashed', linewidth=2, label=f'Media Muestral = {mu_sample:.2f}')
    plt.axvline(critical_value_lower, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico Inferior = {critical_value_lower:.2f}')
    plt.axvline(critical_value_upper, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico Superior = {critical_value_upper:.2f}')
    plt.title('Two-Sided Test (Distribución Normal General)')
    plt.xlabel('Valor')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()


#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------ Graficador right-tail Z test -------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

  
def graficar_right_z_test(z_critical_value, z_statistic):
    x = np.linspace(-4, 4, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.norm.pdf(x, loc=0, scale=1)
    plt.plot(x, y, label='Distribución Z')
    plt.fill_between(x, y, where=(x >= z_critical_value), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(z_statistic, color='blue', linestyle='dashed', linewidth=2, label=f'Valor Z observado = {z_statistic:.2f}')
    plt.axvline(z_critical_value, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico = {z_critical_value:.2f}')
    plt.title('Right-Tailed Test (Distribución Z)')
    plt.xlabel('Valor Z')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------- Graficador left-tail Z test -------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
 

def graficar_left_z_test(z_critical_value, z_statistic):
    x = np.linspace(-4, 4, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.norm.pdf(x, loc=0, scale=1)
    plt.plot(x, y, label='Distribución Z')
    plt.fill_between(x, y, where=(x <= z_critical_value), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(z_statistic, color='blue', linestyle='dashed', linewidth=2, label=f'Valor Z observado = {z_statistic:.2f}')
    plt.axvline(z_critical_value, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico = {z_critical_value:.2f}')
    plt.title('Left-Tailed Test (Distribución Z)')
    plt.xlabel('Valor Z')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#---------------------------------------- Graficador two-tail normal test -----------------------------------------
#-------------------------------------------------------------------------------------------------------------------

 
def graficar_two_z_test(critical_value_lower, critical_value_upper, z_statistic):
    x = np.linspace(-4, 4, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.norm.pdf(x, loc=0, scale=1)
    plt.plot(x, y, label='Distribución Z')
    plt.fill_between(x, y, where=(x <= critical_value_lower) | (x >= critical_value_upper), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(z_statistic, color='blue', linestyle='dashed', linewidth=2, label=f'Valor Z observado = {z_statistic:.2f}')
    plt.axvline(critical_value_lower, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico Inferior = {critical_value_lower:.2f}')
    plt.axvline(critical_value_upper, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico Superior = {critical_value_upper:.2f}')
    plt.title('Two-Sided Test (Distribución Z)')
    plt.xlabel('Valor Z')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    
    
#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------ Graficador right-tail t test -------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

  
def graficar_right_t_test(t_critical_value, t_statistic, df):
    x = np.linspace(-4, 4, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.t.pdf(x, df)
    plt.plot(x, y, label='Distribución t-student')
    plt.fill_between(x, y, where=(x >= t_critical_value), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(t_statistic, color='blue', linestyle='dashed', linewidth=2, label=f'Valor t observado = {t_statistic:.2f}')
    plt.axvline(t_critical_value, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico = {t_critical_value:.2f}')
    plt.title('Right-Tailed Test (Distribución t-student)')
    plt.xlabel('Valor t')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#------------------------------------------- Graficador left-tail Z test -------------------------------------------
#-------------------------------------------------------------------------------------------------------------------
 

def graficar_left_t_test(t_critical_value, t_statistic, df):
    x = np.linspace(-4, 4, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.t.pdf(x, df)
    plt.plot(x, y, label='Distribución t-student')
    plt.fill_between(x, y, where=(x <= t_critical_value), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(t_statistic, color='blue', linestyle='dashed', linewidth=2, label=f'Valor t observado = {t_statistic:.2f}')
    plt.axvline(t_critical_value, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico = {t_critical_value:.2f}')
    plt.title('Left-Tailed Test (Distribución t-student)')
    plt.xlabel('Valor t')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#---------------------------------------- Graficador two-tail normal test ------------------------------------------
#-------------------------------------------------------------------------------------------------------------------

 
def graficar_two_t_test(critical_value_lower, critical_value_upper, t_statistic, df):
    x = np.linspace(-4, 4, 1000)
    plt.figure(figsize=(8, 4))
    y = stats.t.pdf(x, df)
    plt.plot(x, y, label='Distribución t-student')
    plt.fill_between(x, y, where=(x <= critical_value_lower) | (x >= critical_value_upper), color='red', alpha=0.5, label='Región de rechazo')
    plt.axvline(t_statistic, color='blue', linestyle='dashed', linewidth=2, label=f'Valor t observado = {t_statistic:.2f}')
    plt.axvline(critical_value_lower, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico Inferior = {critical_value_lower:.2f}')
    plt.axvline(critical_value_upper, color='green', linestyle='dashed', linewidth=2, label=f'Valor Crítico Superior = {critical_value_upper:.2f}')
    plt.title('Two-Sided Test (Distribución t-student)')
    plt.xlabel('Valor t')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(linestyle='--', alpha=0.7)
    plt.show()
    

#-------------------------------------------------------------------------------------------------------------------
#------------------------------------ Graficador violin segmentacion categórica ------------------------------------
#-------------------------------------------------------------------------------------------------------------------
  
    
def grafico_violin_segmentacion_categorica(df, variable_categorica, variable_numerica):
    plt.figure(figsize=(8, 4))
    sns.violinplot(x=df[variable_categorica], y=df[variable_numerica], inner='quartiles')

    for category in df[variable_categorica].unique():
   
        data_segment = df[df[variable_categorica] == category][variable_numerica]
        plt.boxplot(data_segment, positions=[list(df[variable_categorica].unique()).index(category)], widths=0.1,
                    patch_artist=True, boxprops=dict(facecolor='lightblue', color='black'),
                    medianprops=dict(color='red'),
                    capprops=dict(color='blue'))

    plt.xlabel(f'{variable_categorica}')
    plt.ylabel('Valores estandarizados')
    plt.title(f'Diagrama de Violín de {variable_numerica} segmentado por {variable_categorica}')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    

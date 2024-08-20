import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


def hello():
    print('Helloo! , module loaded')
    

# Create a scatter plot
def scatter(data,x,y):
    sns.scatterplot(x=x, y=y, data=data)
    plt.xlabel('x-label')
    plt.ylabel('y-label')
    plt.title('title')
    plt.show()


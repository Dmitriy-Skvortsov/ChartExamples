import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def plot_chart():
    np.random.seed(19680801)
    
    # Данные для графика
    
    mu = 100  
    sigma = 15  
    x = mu + sigma * np.random.randn(437)
    num_bins = 50
    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(x, num_bins, density=True)

    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
         np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    ax.plot(bins, y, '--')
    ax.set_xlabel('Сообразительность')
    ax.set_ylabel('Плотность вероятности')
    ax.set_title(r'Гистограмма для IQ: $\mu=100$, $\sigma=15$')
        
    fig.tight_layout()
    plt.show()


def plot_chart2():
    # Данные для графика
    sns.set()
    
    np.random.seed(33)
    normal_data_a = np.random.normal(size = 500, loc = 100, scale = 10)
    
    df_normal_a = pd.DataFrame(data = normal_data_a, columns=['score']).assign(group = 'Group A')
    
    sns.histplot(data=df_normal_a
                 , x='score'
                 , bins=50
                 , kde=True
                 )   
    plt.show()
    

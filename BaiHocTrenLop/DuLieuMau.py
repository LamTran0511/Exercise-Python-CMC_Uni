import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cities = pd.read_csv('california_cities.csv')
lat, lon = cities['latd'], cities['longd']
population = cities['population_total']
area = cities['area_total_km2']

plt.style.use('seaborn-v0_8')
plt.figure(figsize=(8,6))
plt.scatter(lon, lat, c=np.log10(population), cmap='viridis',
            s=area, linewidths=0, alpha=0.5)
plt.axis('equal')
plt.xlabel('longtitude')
plt.ylabel('latitude')
plt.title('California Cities: Population and Area Distribution')
plt.colorbar(label='log$_{10}$(population)')
plt.show()
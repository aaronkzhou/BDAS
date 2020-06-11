import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

hd_data = pd.read_csv(r'C:\Users\Monica\Desktop\iteration 3\heart.csv')

print(hd_data.shape)
print(hd_data.dtypes)
print(hd_data.head())
print(hd_data.describe())

plt.boxplot(hd_data["chol"])
plt.show()

plt.boxplot(hd_data["oldpeak"])
plt.show()

print(hd_data['chol'].quantile(0.50)) 
print(hd_data['chol'].quantile(0.95)) 
hd_data['chol'] = np.where(hd_data['chol'] > 330, 240, hd_data['chol'])
print(hd_data.describe())

plt.boxplot(hd_data["chol"])
plt.show()

print(hd_data['oldpeak'].quantile(0.50)) 
print(hd_data['oldpeak'].quantile(0.95)) 
hd_data['oldpeak'] = np.where(hd_data['oldpeak'] > 3.5, 0.8, hd_data['oldpeak'])
print(hd_data.describe())

plt.boxplot(hd_data["oldpeak"])
plt.show()




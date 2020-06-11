import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

gender_data = pd.read_csv('./gender.csv')

# print(gender_data.shape)

# print(gender_data.dtypes)

# print(gender_data.describe())

# print(gender_data.Category.value_counts())

# plt.figure(1,dpi=50) 
# plt.hist(gender_data['Occupation'])   
# plt.show()

# plt.figure(1,dpi=50)
# plt.hist(gender_data['Category'])   
# plt.show()

# plt.figure(1,dpi=50)
# gender_data.sort_values(by=['M_weekly'])
# plt.plot(gender_data['M_weekly'])
# plt.show()

gender_data.sort_values(by=['F_weekly'])
plt.plot(gender_data['F_weekly'])
plt.show()



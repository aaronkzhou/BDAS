import pandas as pd
import matplotlib.pyplot as plt

gender_data = pd.read_csv('./gender.csv')

newIncome = gender_data.loc[(gender_data['F_weekly']  != 'Na') & (gender_data['M_weekly'] != 'Na')]
newIncome['F_weekly'] = pd.to_numeric(newIncome['F_weekly'])
newIncome['M_weekly'] = pd.to_numeric(newIncome['M_weekly'])
del gender_data['F_weekly']
del gender_data['M_weekly']
del newIncome['M_workers']
del newIncome['F_workers']
del newIncome['All_workers']

print(gender_data.isnull().any())
print(newIncome.isnull().any())
print(gender_data.dtypes)
print(newIncome.dtypes)
print(gender_data)
print(newIncome)
print(gender_data.describe())
newIncome.describe()
# plt.plot(gender_data["F_workers"], gender_data["M_workers"], 'ro')
# plt.ylabel('M_workers numbers')
# plt.xlabel('F_workers numbers')
# plt.show()
# plt.plot(newIncome["F_weekly"], newIncome["M_weekly"], 'ro')
# plt.ylabel('M_weekly income')
# plt.xlabel('F_weekly income')
# plt.show()


import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
# m = ols('F_workers ~ M_workers',gender_data).fit()
# print(m.summary())
# sns.jointplot(x="F_workers", y="M_workers", data=gender_data, kind = 'reg',fit_reg= True, size = 7)
# plt.show()

n = ols('F_weekly ~ M_weekly',newIncome).fit()
print(n.summary())
sns.jointplot(x="F_weekly", y="M_weekly", data=newIncome, kind = 'reg',fit_reg= True, size = 7)
plt.show()

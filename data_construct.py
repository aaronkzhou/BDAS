import pandas as pd

gender_data = pd.read_csv('./gender.csv')

newIncome = gender_data.loc[(gender_data['F_weekly']  != 'Na') & (gender_data['M_weekly'] != 'Na')]
del gender_data['F_weekly']
del gender_data['M_weekly']
del newIncome['M_workers']
del newIncome['F_workers']
del newIncome['All_workers']

print(gender_data)
print(newIncome)

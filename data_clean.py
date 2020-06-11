import pandas as pd

gender_data = pd.read_csv('./gender.csv')

newIncome = gender_data.loc[(gender_data['F_weekly']  != 'Na') & (gender_data['M_weekly'] != 'Na')]
print(newIncome)


import pandas as pd

gender_data = pd.read_csv('./gender.csv')
gender_data['F_workers'] = pd.to_numeric(gender_data['F_workers'])
gender_data['M_workers'] = pd.to_numeric(gender_data['M_workers'])
gender_data['All_workers'] = pd.to_numeric(gender_data['All_workers'])

newIncome = gender_data.loc[(gender_data['F_weekly']  != 'Na') & (gender_data['M_weekly'] != 'Na')]
newIncome['F_weekly'] = pd.to_numeric(newIncome['F_weekly'])
newIncome['M_weekly'] = pd.to_numeric(newIncome['M_weekly'])
newIncome['is_male_high_income'] = newIncome['M_weekly'] > 1000
newIncome['is_female_high_income'] = newIncome['F_weekly'] > 1000
del gender_data['F_weekly']
del gender_data['M_weekly']
del newIncome['M_workers']
del newIncome['F_workers']
del newIncome['All_workers']
print(newIncome)
print(gender_data)
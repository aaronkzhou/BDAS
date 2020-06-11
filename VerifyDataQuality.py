import pandas as pd

gender_data = pd.read_csv('./gender.csv')
print(gender_data.loc[gender_data['Occupation'] != 'Na'].count())
print(gender_data.loc[gender_data['Category'] != 'Na'].count())
print(gender_data.loc[gender_data['All_workers'] != 'Na'].count())
print(gender_data.loc[gender_data['M_workers'] != 'Na'].count())
print(gender_data.loc[gender_data['F_workers'] != 'Na'].count())
print(gender_data.loc[gender_data['M_weekly'] != 'Na'].count())
print(gender_data.loc[gender_data['F_weekly'] != 'Na'].count())
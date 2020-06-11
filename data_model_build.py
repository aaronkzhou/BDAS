import pandas as pd

gender_data = pd.read_csv('./gender.csv')
gender_data['F_workers'] = pd.to_numeric(gender_data['F_workers'])
gender_data['M_workers'] = pd.to_numeric(gender_data['M_workers'])
gender_data['All_workers'] = pd.to_numeric(gender_data['All_workers'])

newIncome = gender_data.loc[(gender_data['F_weekly']  != 'Na') & (gender_data['M_weekly'] != 'Na')]
newIncome['F_weekly'] = pd.to_numeric(newIncome['F_weekly'])
newIncome['M_weekly'] = pd.to_numeric(newIncome['M_weekly'])
newIncome['is_male_high_income'] = (newIncome['M_weekly'] > 1000) * 1
newIncome['is_female_high_income'] = (newIncome['F_weekly'] > 1000) * 1
newIncome['income_ratio'] = newIncome['M_weekly'] / newIncome['F_weekly']
del gender_data['F_weekly']
del gender_data['M_weekly']
del newIncome['M_workers']
del newIncome['F_workers']
del newIncome['All_workers']
print(newIncome)
print(gender_data)

# model 1
# from pyspark import SparkContext 
# from pyspark.sql import SQLContext
# from pyspark.ml.linalg import Vectors
# from pyspark.ml.feature import VectorAssembler
# from pyspark.ml.classification import LogisticRegression
# sc = SparkContext()
# sqlContext = SQLContext(sc)
# sparkNewIncome=sqlContext.createDataFrame(newIncome)
# sparkGender_data=sqlContext.createDataFrame(gender_data)
# sparkNewIncome.show()
# from pyspark.ml.linalg import Vector
# from pyspark.ml.feature import VectorAssembler
# print(sparkNewIncome.columns)
# vec_assmebler=VectorAssembler(inputCols=['F_weekly'], outputCol='features')

# features_df=vec_assmebler.transform(sparkNewIncome)
# print(features_df)

# lr = LogisticRegression(labelCol='is_male_high_income')
# lr_f = LogisticRegression(labelCol='is_female_high_income')
# lrModel = lr.fit(features_df)

# print("Coefficients: " + str(lrModel.coefficients))
# print("Intercept: " + str(lrModel.intercept))

# lr_f = LogisticRegression(labelCol='is_female_high_income')

# lrModel_f = lr_f.fit(features_df)
# print("Coefficients: " + str(lrModel_f.coefficients))
# print("Intercept: " + str(lrModel_f.intercept))

# model 2
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import polyfit

# plt.scatter(gender_data['M_workers'], gender_data['F_workers'], color='red', s=30)
# plt.xlabel('M_workers')
# plt.ylabel('F_workers')
# plt.title('Linear Regression FOR ALL JOBS')
# p1 = polyfit(gender_data['M_workers'], gender_data['F_workers'], 1)
# plt.plot(gender_data['M_workers'], np.polyval(p1,gender_data['M_workers']), 'g-' )
# plt.show()

# model 3
# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import polyfit

# newGender_data = gender_data.loc[(gender_data['Category']  == 'MANAGEMENT')]
# plt.scatter(newGender_data['M_workers'], newGender_data['F_workers'], color='red', s=30)
# plt.xlabel('M_workers')
# plt.ylabel('F_workers')
# plt.title('Linear Regression for MANAGEMENT JOBS')
# p1 = polyfit(newGender_data['M_workers'], newGender_data['F_workers'], 1)
# plt.plot(newGender_data['M_workers'], np.polyval(p1,newGender_data['M_workers']), 'g-' )
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import polyfit

# newGender_data = gender_data.loc[(gender_data['Category']  == 'COMPUTATIONAL')]
# plt.scatter(newGender_data['M_workers'], newGender_data['F_workers'], color='red', s=30)
# plt.xlabel('M_workers')
# plt.ylabel('F_workers')
# plt.title('Linear Regression for COMPUTATIONAL JOBS')
# p1 = polyfit(newGender_data['M_workers'], newGender_data['F_workers'], 1)
# plt.plot(newGender_data['M_workers'], np.polyval(p1,newGender_data['M_workers']), 'g-' )
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# from numpy import polyfit

# newGender_data = gender_data.loc[(gender_data['Category']  == 'ARTS')]
# plt.scatter(newGender_data['M_workers'], newGender_data['F_workers'], color='red', s=30)
# plt.xlabel('M_workers')
# plt.ylabel('F_workers')
# plt.title('Linear Regression for ARTS JOBS')
# p1 = polyfit(newGender_data['M_workers'], newGender_data['F_workers'], 1)
# plt.plot(newGender_data['M_workers'], np.polyval(p1,newGender_data['M_workers']), 'g-' )
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from numpy import polyfit

newnewIncome = gender_data.loc[(newIncome['Category']  == 'ARTS')]
plt.scatter(newnewIncome['M_weekly'], newnewIncome['F_weekly'], color='red', s=30)
plt.xlabel('M_weekly')
plt.ylabel('F_weekly')
plt.title('Linear Regression for ARTS JOBS')
p1 = polyfit(newnewIncome['M_weekly'], newnewIncome['F_weekly'], 1)
plt.plot(newnewIncome['M_weekly'], np.polyval(p1,newnewIncome['M_weekly']), 'g-' )
plt.show()


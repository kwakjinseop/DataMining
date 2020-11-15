# https://www.kaggle.com/c/titanic/data
# 기초 통계 확인

import pandas as pd

data = pd.read_csv('../data/train.csv')
print(data.describe())
print(data['Fare'].mean())
print(data['Fare'].std())
print(data['Fare'].var())
print(data['Fare'].median())
print(data['Fare'].min)

#        PassengerId    Survived      Pclass  ...       SibSp       Parch        Fare
# count   891.000000  891.000000  891.000000  ...  891.000000  891.000000  891.000000
# mean    446.000000    0.383838    2.308642  ...    0.523008    0.381594   32.204208
# std     257.353842    0.486592    0.836071  ...    1.102743    0.806057   49.693429
# min       1.000000    0.000000    1.000000  ...    0.000000    0.000000    0.000000
# 25%     223.500000    0.000000    2.000000  ...    0.000000    0.000000    7.910400
# 50%     446.000000    0.000000    3.000000  ...    0.000000    0.000000   14.454200
# 75%     668.500000    1.000000    3.000000  ...    1.000000    0.000000   31.000000
# max     891.000000    1.000000    3.000000  ...    8.000000    6.000000  512.329200
#
# [8 rows x 7 columns]
#
# Process finished with exit code 0
#

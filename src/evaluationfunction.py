import pandas as pd
import numpy as np


backfit = pd.read_csv("backfit.csv")
train = pd.read_csv("../data/train_processed.csv",usecols = ['Id','Expected'])

print backfit.head()
print train.head()

backfit = backfit.groupby('Id').mean()
train = train.groupby('Id').mean()

print backfit.head()
print train.head()

#combined = pd.merge(backfit, train, on = ['Id'], how = "left")

combined = backfit.join(train)
combined['residual'] = abs(combined['Expected'] - combined['ExpectedForecast'])
print combined.head()

print("MAE =",np.mean(combined['residual']))

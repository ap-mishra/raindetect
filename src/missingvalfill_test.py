import pandas as pd
import numpy as np

test = pd.read_csv("../data/test.csv")

test.head()

def fillcol(df, col):
    print col.head()
    meancol = np.mean(col)
    col = col.fillna(meancol)
    print col.head()
    return col

for c in test.columns:
    test[c] = fillcol(test, test[c])

test.to_csv("test_processed.csv",index=False)
#fillcol(test, test['RhoHV'])


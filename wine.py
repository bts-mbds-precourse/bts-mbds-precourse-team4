import pandas as pd
import matplotlib
import numpy as np

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
df=pd.read_csv('/Users/cenliang/Downloads/winequality-data.csv')
df=df.drop(['id'],axis=1)
print(df.head(5))


fixedacid=df['fixed.acidity']
quality=df['quality']
volatileacid=df['volatile.acidity']
citricacid=df['citric.acid']
resisugar=df['residual.sugar']
chlorides=df['chlorides']
freeso=df['free.sulfur.dioxide']
totals0=df['total.sulfur.dioxide']
density=df['density']
ph=df['pH']
sulphates=df['sulphates']
alcohol=['alcohol']


import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('fixedacid')
plt.axis([0,10,4,11])
plt.scatter(quality, fixedacid, color='red',marker='.')
plt.suptitle("fixed acidity")
#plt.yticks(quality)

plt.show()
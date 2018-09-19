import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
totalso=df['total.sulfur.dioxide']
density=df['density']
ph=df['pH']
sulphates=df['sulphates']
alcohol=df['alcohol']




corr = df.corr()
sns.heatmap(corr, annot=True, annot_kws={"size": 6}, cmap="Reds")
plt.show()


def scatter(column):
    plt.xlabel('quality')
    plt.ylabel(column)
    plt.axis([0, 10, min(df[column]), df[column].max()])
    plt.scatter(quality, df[column], color='red')
    plt.suptitle(column)
    plt.show()


scatter('pH')

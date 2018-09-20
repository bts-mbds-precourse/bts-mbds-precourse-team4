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



#scatter functions

scatterlist=[i for i in list(df) if i!='quality']
print(list)

def scatter(column):
    plt.xlabel('quality')
    plt.ylabel(column)
    plt.axis([0, 10, min(df[column]), df[column].max()])
    plt.scatter(quality, df[column], alpha=0.4,marker='o',facecolors='none', edgecolors='r')
    plt.suptitle(column)
    plt.show()

pd.DataFrame(scatterlist).applymap(scatter)

#heatmaps

def heatmap(set,title=None):
    fig, ax = plt.subplots(figsize=(10, 10))
    corr = set.corr()
    sns.heatmap(corr, annot=True, annot_kws={"size": 10}, cmap="Reds",ax=ax)
    plt.title(title)
    plt.show()


heatmap(df,title="All Wine")

goodwine=df[df["quality"]>6]
heatmap(goodwine,title="Good Wine")

averagewine=df[(df["quality"]<=6 ) & (df["quality"]>5)]
heatmap(averagewine,title="Average Wine")

lowqualitywine=df[df["quality"]<5]
heatmap(lowqualitywine,title="Lowquality Wine")




#histgram

def hist(feature,bin=None):
    hist=df[feature].hist(bins=bin,grid=False, edgecolor='white', alpha=0.8)
    plt.xlabel(feature)
    plt.show()
    
hist('quality')

pd.DataFrame(list(df)).applymap(hist)


#for data in df:
 #   print(hist(data))





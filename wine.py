import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv('/Users/cenliang/Downloads/winequality-data.csv')
df=df.drop(['id'],axis=1) #use default index
df=df.drop(269,axis=0)   #outlier for residual sugar
quality=df['quality']    #data parsing


#histgram

def hist(feature, bin=None):
    hist = df[feature].hist(bins=bin, grid=False, edgecolor='white', alpha=0.8, facecolor='#fc8869', figsize=(15, 20))
    plt.ylabel(feature, fontsize=20)
    plt.xlabel('Quantity', fontsize=20)
    plt.show()
    
pd.DataFrame(list(df)).applymap(hist)


#scatter plot

scatterlist=[i for i in list(df) if i!='quality']
def scatter(column):
    plt.xlabel('quality')
    plt.ylabel(column)
    plt.axis([0, 10, min(df[column]), df[column].max()])
    plt.scatter(quality, df[column], alpha=0.4,marker='o',facecolors='none', edgecolors='r')
    plt.suptitle(column)
    plt.show()
    
pd.DataFrame(scatterlist).applymap(scatter)


#boxplots for all data

box1=df[['citric.acid', 'volatile.acidity', 'chlorides','density','sulphates']]
box2=df[['fixed.acidity','residual.sugar','pH','alcohol']]
box3=df[['total.sulfur.dioxide','free.sulfur.dioxide']]

sns.set(style="whitegrid")
box1 = sns.boxplot(data=box1,palette="Set1")
plt.show()
box2 = sns.boxplot(data=box2,palette="Set2")
plt.show()
box3 = sns.boxplot(data=box3,palette="Set3")
plt.show()



#heatmaps

def heatmap(set,title=None):
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(set.corr(), annot=True, annot_kws={"size": 10}, cmap="YlGnBu",ax=ax)
    plt.title(title)
    plt.show()

heatmap(df,title="All Wine")

goodwine=df[df["quality"]>6]
heatmap(goodwine,title="Good Wine")

averagewine=df[(df["quality"]<=6 ) & (df["quality"]>=5)]
heatmap(averagewine,title="Average Wine")

lowqualitywine=df[df["quality"]<5]
heatmap(lowqualitywine,title="Lowquality Wine")

#Scatter plots with joint regression for variables

from scipy import stats


df = df[(np.abs(stats.zscore(df['density'])) < 1.5
         )]

newdf = sns.JointGrid(x="density", y="total.sulfur.dioxide", data=df, size=6)
newdf = newdf.plot_joint(sns.regplot, scatter_kws={"s": 5})
newdf = newdf.plot_marginals(sns.distplot)



df = df[(np.abs(stats.zscore(df['chlorides'])) < 2
         )]

newdf = sns.JointGrid(x="chlorides", y="alcohol", data=df, size=6)
newdf = newdf.plot_joint(sns.regplot, scatter_kws={"s": 5})
newdf = newdf.plot_marginals(sns.distplot)



df = df[(np.abs(stats.zscore(df['residual.sugar'])) < 3
         
         )]
newdf = sns.JointGrid(x="density", y="residual.sugar", data=df, size=6)
newdf = newdf.plot_joint(sns.regplot, scatter_kws={"s": 5})
newdf = newdf.plot_marginals(sns.distplot)

#Compare different quality of wine

bins = pd.IntervalIndex.from_breaks([2.5,4.5,6.5,9.5])
wine=df.groupby(pd.cut(np.array(df['quality']), bins=bins)).mean()
wine.index=["bad", "average", "good"]
wine['volatile.acidity']*=10 #change the range only save the trend
wine['total.sulfur.dioxide']/=20 #change the range only save the trend
wine=wine.T
wine=wine.plot.bar(figsize=(20,20),color=['tan','red','darkred'])

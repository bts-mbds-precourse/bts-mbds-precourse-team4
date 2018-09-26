import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
red=pd.read_csv('/Users/cenliang/Downloads/winequality-red.csv',sep=";")
white=pd.read_csv('/Users/cenliang/Downloads/winequality-white.csv',sep=";")
red.head()

sns.set()
red.hist(figsize=(10,10), color='red')
white.hist(figsize=(10,10), color='blue')

plt.show()


red=red.groupby(by='quality').mean()
white=white.groupby(by='quality').mean()
badred=red[(red.index.values==3 )| (red.index.values==4)].mean()
badwhite=white[(white.index.values==3 )| (white.index.values==4)].mean()
bad=pd.concat([badwhite,badred], axis=1)


avered=red[(red.index.values==5 )| (red.index.values==6)].mean()
avewhite=white[(white.index.values==5 )| (white.index.values==6)].mean()
ave=pd.concat([avewhite,avered], axis=1)


goodred=red[(red.index.values==7 )| (red.index.values==8)| (red.index.values==9)].mean()
goodwhite=white[(white.index.values==7 )| (white.index.values==8)| (white.index.values==9)].mean()
bad=pd.concat([badwhite,badred], axis=1)


fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax2 = ax
badwhite[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']].plot(kind='bar',color='white',ax=ax,position=0,width=0.4,edgecolor='black')
badred[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']].plot(kind='bar',color='red',ax=ax2,position=1,width=0.4, edgecolor='black')


ax.set_ylabel('white')
ax2.set_ylabel('red')

plt.show()





fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax2 = ax

avewhite[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']].plot(kind='bar',color='white',ax=ax,position=0,width=0.4,edgecolor='black')
avered[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']].plot(kind='bar',color='red',ax=ax2,position=1,width=0.4, edgecolor='black')


ax.set_ylabel('white')
ax2.set_ylabel('red')

plt.show()




fig = plt.figure(figsize=(15,10))
ax = fig.add_subplot(111)
ax2 = ax

goodwhite[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']].plot(kind='bar',color='white',ax=ax,position=0,width=0.4,edgecolor='black')
goodred[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'density',
       'pH', 'sulphates', 'alcohol', 'quality']].plot(kind='bar',color='red',ax=ax2,position=1,width=0.4, edgecolor='black')


ax.set_ylabel('white')
ax2.set_ylabel('red')

plt.show()

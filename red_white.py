import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
red=pd.read_csv('/Users/cenliang/Downloads/winequality-red.csv',sep=";")
white=pd.read_csv('/Users/cenliang/Downloads/winequality-white.csv',sep=";")
red.index=['red']*len(red)
white.index=['white']*len(white)
allwine = pd.concat([red,white])
allwine.head()

#histogram for red and white
sns.set()
red.hist(figsize=(10,10), color='red')
white.hist(figsize=(10,10), color='blue')
plt.show()

#Groupby in the df way
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

#Comparing red and white wine
redwhite=allwine.groupby(allwine.index).mean()
redwhite['total sulfur dioxide']/=30
redwhite['free sulfur dioxide']/=10
redwhite['alcohol']/=10
redwhite['fixed acidity']/=5
redwhite['residual sugar']/=5
redwhite['chlorides']*=10
redwhite=redwhite.T
redwhite.plot.bar(color=['darkred','white'],edgecolor='black',figsize=(15,10))

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
df=pd.read_csv('/Users/Anastasia/Desktop/BTS/Python/Project/winequality-data.csv')
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
alcohol=['alcohol']

#1
import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('fixedacid')
plt.axis([0,10,4,11])
plt.scatter(quality, fixedacid, color='red',marker='.')
plt.suptitle("fixed acidity")
#plt.yticks(quality)
plt.show()

#2
import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('volatileacid')
plt.axis([0,10,min(volatileacid),max(volatileacid)])
plt.scatter(quality, volatileacid, color='blue',marker='.')
plt.suptitle("volatile acidity")
plt.show()


#3
import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('citricacid')
plt.axis([0,10,min(citricacid),max(citricacid)])
plt.scatter(quality, citricacid, color='green',marker='.')
plt.suptitle("citric acid")
plt.show()


#4
import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('resisugar')
plt.axis([0,10,min(resisugar),max(resisugar)])
plt.scatter(quality, resisugar, color='yellow',marker='.')
plt.suptitle("residual sugar")
plt.show()

#5
import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('chlorides')
plt.axis([0,10,min(chlorides),max(chlorides)])
plt.scatter(quality, chlorides, color='purple',marker='.')
plt.suptitle("chlorides")
plt.show()


#6
import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('freeso')
plt.axis([0,10,min(freeso),max(freeso)])
plt.scatter(quality, freeso, color='black',marker='.')
plt.suptitle("free sulfur dioxide")
plt.show()

#7

import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('totalso')
plt.axis([0,10,min(totalso),max(totalso)])
plt.scatter(quality, totalso, color='magenta',marker='.')
plt.suptitle("total sulfur dioxide")
plt.show()

#8

import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('density')
plt.axis([0,10,min(density),max(density)])
plt.scatter(quality, density, color='magenta',marker='.')
plt.suptitle("density")
plt.show()

#9

import matplotlib.pyplot as plt
plt.xlabel('quality')
plt.ylabel('ph')
plt.axis([0,10,min(ph),max(ph)])
plt.scatter(quality, ph, color='green',marker='.')
plt.suptitle("pH")
plt.show()

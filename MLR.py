import numpy as np
import pandas as pd

class MLR:
    
    def __init__(self, dataSet):

        self.dataSet = dataSet
        self.columns = len(dataSet.count())
        self.n = self.dataSet['Sales'].count()

        self.sumY = sum(dataSet['Sales'])
        self.sumX1 = sum(dataSet['TV'])
        self.sumX2 = sum(dataSet['Radio'])
        self.sumX3 = sum(dataSet['Newspaper'])

        self.sumX1sqr = sum(pow(dataSet['TV'],2))
        self.sumX2sqr = sum(pow(dataSet['Radio'],2))
        self.sumX3sqr = sum(pow(dataSet['Newspaper'],2))

        self.sumX1X2 = sum(dataSet['TV'] * dataSet['Radio'] ) 
        self.sumX1X3 = sum(dataSet['TV'] * dataSet['Newspaper'])
        self.sumX2X1 = sum(dataSet['Radio'] * dataSet['TV'])
        self.sumX2X3 = sum(dataSet['Radio'] * dataSet['Newspaper'])
        self.sumX3X1 = sum(dataSet['Newspaper'] * dataSet['TV'])
        self.sumX3X2 = sum(dataSet['Newspaper'] * dataSet['Radio'])

        self.sumX1Y = sum(dataSet['TV'] * dataSet['Sales'])
        self.sumX2Y = sum(dataSet['Radio'] * dataSet['Sales'])
        self.sumX3Y = sum(dataSet['Newspaper'] * dataSet['Sales'])

        self.data = {'col1': [self.n, self.sumX1, self.sumX2, self.sumX3] , 'col2': [self.sumX1, self.sumX1sqr, self.sumX1X2, self.sumX1X3 ] ,
                     'col3':[self.sumX2, self.sumX1X2, self.sumX2sqr, self.sumX2X3] , 'col4':[self.sumX3, self.sumX3X1, self.sumX3X2, self.sumX3sqr]}

        self.matrix = pd.DataFrame(data=self.data)
        self.vector = pd.DataFrame(data={'col':[self.sumY, self.sumX1Y, self.sumX2Y, self.sumX3Y]})

        self.staggeringMatrix = pd.DataFrame(data={'col1':[1,0,0,0],'col2':[0,1,0,0],'col3':[0,0,1,0],'col4':[0,0,0,1]})
        
    


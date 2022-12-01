import numpy as np
import pandas as pd

class MLR:

    def __init__(self, dataSet):

        self.dataSet = dataSet
        self.y = self.dataSet['Sales']
        self.x = self.dataSet[['TV','Radio','Newspaper']]
        self.x.insert(loc=0, column='Helper', value=1)
        
        # self.y = self.dataSet['col4']
        # self.x = self.dataSet[['col1','col2','col3']]
    
    def leastSquareEstimates(self):
        x_transposed = self.x.T

        result = np.dot(x_transposed,self.x)

        Inv = np.linalg.inv(result)

        y_trans = np.dot(x_transposed, self.y)

        result = np.dot(Inv, y_trans)

        print(result)
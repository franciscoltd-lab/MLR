import numpy as np
import pandas as pd
class MLR:

    # def __init__(self,x1, x2, x3, y):
    #      self.x1 = x1
    #      self.x2 = x2
    #      self.y = y

    #      self.sumY = np.array([]) #Sumatoria de Y
    #      self.sumX1 = np.array([]) #Sumatoria de Y
    #      self.sumX2 = np.array([]) #Sumatoria de Y
    #      self.sumX2 = np.array([]) #Sumatoria de Y
    #      self.sumX1sqr = np.array([]) #Sumatoria de x1^2
    #      self.sumX2sqr = np.array([]) #Sumatoria de x2^2
    #      self.sumYsqr = np.array([]) #Sumatoria de y^2
    #      self.sumX1X2 = np.array([]) #Sumatoria de X1 * X2
    #      self.sumX1Y = np.array([]) #Sumatoria de X1 * Y
    #      self.sumX2Y = np.array([]) #Sumatoria de X2 * Y
        
        #  self.avrgX = np.array([]) #Promedio de X
        #  self.avrgY = np.array([]) # Promedio de Y
        
        #  self.n = np.array([]) #Número de datos
        #  self.a = np.array([]) #Ordenada con el eje y
        #  self.b = np.array([]) #Pendiente de la recta
    
    def __init__(self, dataSet):
        self.dataSet = dataSet
        # self.n = len(self.dataSet.count()) - 1
        self.x = pd.DataFrame(dataSet[['TV', 'Radio', 'Newspaper']])
        self.sumY = sum(self.dataSet['Sales'])

    # def calculateSumY(self):

    def calculateSumX1(self):
        self.sumX1 = sum(self.x1)

    def calculateSumX2(self):
        self.sumX2 = sum(self.x2)

    def calculateSumX1sqr(self):
        self.sumX1sqr = pow(self.x1, 2)
        self.sumX1sqr = sum(self.sumX1sqr)
      
    def calculateSumX2sqr(self):
        self.sumX2sqr = pow(self.x2, 2)
        self.sumX2sqr = sum(self.sumX2sqr)
      
    def calculateSumX1X2(self):
        self.sumXY = sum(np.multiply(self.x1, self.y2))

    def calculateSumX1Y(self):
        self.sumXY = sum(np.multiply(self.x1, self.y))

    def calculateSumX2Y(self):
        self.sumXY = sum(np.multiply(self.x1, self.y))
       
    

    
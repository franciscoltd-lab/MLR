import MLR
import numpy as np
import pandas as pd

def main():

    # y = pd.read_csv('Advertising.csv', usecols = ['Sales'])
    # x1 = pd.read_csv('Advertising.csv', usecols = ['TV'])
    # x2 = pd.read_csv('Advertising.csv', usecols = ['Radio'])
    # x3 = pd.read_csv('Advertising.csv', usecols = ['Newspaper'])
    my_absolute_path = r'/home/fltd/Python/pade/examples/MLR/Advertising.csv'
    dataSet = pd.read_csv(my_absolute_path)

   

    advertising = MLR.MLR(dataSet)

    # print(advertising.sumY)
    # print(advertising.x['TV'])

if __name__ == '__main__':
    main()
    
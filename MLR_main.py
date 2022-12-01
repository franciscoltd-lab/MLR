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

    # print(advertising.n)

    # print(advertising.sumY)
    # print(advertising.sumX1)
    # print(advertising.sumX2)
    # print(advertising.sumX3)

    # print(advertising.sumX1sqr)
    # print(advertising.sumX2sqr)
    # print(advertising.sumX3sqr)

    # print('sumX1Y ',advertising.sumX1Y)
    # print(advertising.sumX2Y)
    # print(advertising.sumX3Y)

    # print('Columns: ', advertising.columns)

    print(advertising.matrix)
    print(advertising.vector)
    print(advertising.staggeringMatrix)


if __name__ == '__main__':
    main()
    
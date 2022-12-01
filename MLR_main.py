import MLR
import numpy as np
import pandas as pd

def main():

    # my_absolute_path = r'/home/fltd/Python/pade/examples/MLR/Advertising.csv'
    # columns=['col1', 'col2', 'col3', 'col4']
    # dataSet = pd.read_csv('DataSet.txt')
    dataSet = pd.read_csv('Advertising.csv')

    advertising = MLR.MLR(dataSet)
    advertising.leastSquareEstimates()


if __name__ == '__main__':
    main()
    
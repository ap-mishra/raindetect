import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import argparse
import subprocess
import sys
import os

class parserio():
    def __init__(self):
        pass

    def parser(self,train,args):
        field = train[args]
        parser = argparse.ArgumentParser(description = "Argument Parser : Enter Field you want to analyze")
        parser.add_argument('-exp',
                            '--exp',
                            type=str,
                            dest='Expected',
                            help=''
                           )
        options = parser.parse_args(args)
        print args
        return vars(options)

    def main(self):
        train_file = "../../data/train.short.csv"
        train = pd.read_csv(train_file)

        print("Argument passed =",sys.argv[1:])
        options = self.parser(train,sys.argv[1:])
        print("Options = ",options)
        #print(train[options].describe())

if __name__ == '__main__':
    cl = parserio()
    cl.main()
#    
#    #grouping based on id's to get rainfall mean
#    train_grouped = train.groupby(['Id'])
#    exp_rainfall = np.sort(np.array(train_grouped['Expected'].aggregate('mean')))
#    
#    print exp_rainfall
#    print("Shape of the rainfall")
#    print exp_rainfall.shape
#    print("scatter plot for rainfall distribution")
#    
#    plt.figure()
#    plt.scatter(np.arange(exp_rainfall.shape[0]), exp_rainfall)
#    plt.title("Scatterplot for Rainfall distibution in train")
#    plt.xlabel("ID ->>>> ")
#    plt.ylabel("Rainfall in mm")
#    plt.savefig("Scatter_Id_ExpectedRainfall.png")
#    plt.show()
#
#

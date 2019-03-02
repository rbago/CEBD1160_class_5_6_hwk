#!/usr/bin/env python

import os
import os.path as op
import numpy as np
import pandas as pd
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# Accept abritrary filename as argument
parser = ArgumentParser(description = 'A CSV reader + stats maker')
parser.add_argument('csvfile', help = 'Path to input csv file')

parsed_args = parser.parse_args()
# print(parsed_args.csvfile)

mainFilename =  parsed_args.csvfile

# load the file, accepts files space and comma seperated

filenameData = pd.read_csv(mainFilename, sep='\s+|,', header=None, engine='python')

# Obtains first row to identify header is string or numeric
headers = filenameData.iloc[0]
headers.name = ""

try:
    pd.to_numeric(headers)
except:
    filenameData = pd.DataFrame(filenameData.values[1:], columns=headers)

# Changes strings to numbers (self identifies for float or integer)
filenameData = filenameData.apply(pd.to_numeric)

# Obtains the mean and standard deviation of the columns with numpy
listMean = np.mean(filenameData)
listStd = np.std(filenameData)

# print(filenameData)

# Prints out the results
print('Mean for each column:')
for idx in filenameData.columns:
    print(idx,':',listMean[idx])

print()
print('Standard deviation for each column:')
for idx in filenameData.columns:
    print(idx,':',listStd[idx])

# Each column creates an histogram and saves it into a png file
try:
    os.mkdir("Histogram")
    os.mkdir("ScatterPlot")
except FileExistsError:
    print("Directory already exists")

for idx in filenameData.columns:

    # Use loc instead of iloc as column is identified by the name
    column = filenameData.loc[:,idx]
    histTitle = "Histogram of " + column.name

    n, bins, patches = plt.hist(x=column, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel(column.name)
    plt.ylabel('Frequency')
    plt.title(histTitle)
    plt.savefig("Histogram/" + column.name + ".png")
    plt.clf()

plt.close()
# Compare all columns with one another

#get the number of columns in int to better move around them
colNum = len(filenameData.columns)
yCount = 1

for idx in range(colNum):
    for jdx in range(colNum):

        if jdx == colNum-yCount:
            break
        x = filenameData.iloc[:,idx]
        y = filenameData.iloc[:,jdx+yCount]
        plt.scatter(x, y, marker="o")
        plt.xlabel(x.name)
        plt.ylabel(y.name)
        scatterTitle = "Scatter Plot for " + x.name + " and " + y.name
        plt.title(scatterTitle)
        plt.savefig("ScatterPlot/" + x.name + "_" + y.name + ".png")
        plt.clf()
        #plt.show()

    yCount = yCount + 1

plt.close()

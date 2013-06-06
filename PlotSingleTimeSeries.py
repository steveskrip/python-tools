"""
Generic time series generator for two columns of data
"""

import matplotlib.dates as md
import matplotlib.pyplot as plt
import matplotlib.mlab as ml
import numpy as np
#import datetime as dt
import dateutil.parser as dp
#import cPickle
#import scikits.timeseries as ts

PATH = 'data.csv'

#Common Options
SKIP_HEADER = 1
PLOT_TITLE = 'Structure 46'
X_AXIS_TITLE = 'Date'
Y_AXIS_TITLE = 'Flow, cfs'
HEADER_NAMES = ['Date','Data']

def openFile(path):
    #columns = {'names':('date','d10'),
    #           'formats':(object,np.float,np.float,np.float,np.float,np.float)}
    #data = cPickle.load(open(OUTDIR+"data.p"))
    def str2date(x):
        return dp.parse(x)
    print '...opening file'
    converter = {0:str2date}
    #dtype = columns,
    data = np.genfromtxt(path,converters = converter, delimiter=',',skip_header=SKIP_HEADER)
    #cPickle.dump(data, open(OUTDIR+"data.p","w"))
    data.dtype.names = HEADER_NAMES
    
    return data

def plotSingleTimeseries(data):
    """
    plots observed data and modeled data time series
    """
        
    print '...creating plot'
    fig = plt.figure(figsize=(11,8.5))
    ax = fig.add_subplot(111)
    for header in HEADER_NAMES[1:]:
        ax.plot(data[HEADER_NAMES[0]],data[header],label=header)
    #i, h = ax.get_legend_handles_labels()
    
    fig.autofmt_xdate()
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel(X_AXIS_TITLE)
    ax.set_ylabel(Y_AXIS_TITLE)
    ax.grid(True)
    ax.xaxis.set_major_formatter(md.DateFormatter('%m-%d-%Y %H:%M'))
    #print i,h
    ax.legend()
    plt.show()
    return i,h

if __name__=='__main__':
    data = openFile(PATH+FILE)
    i, h = plotSingleTimeseries(data)
    

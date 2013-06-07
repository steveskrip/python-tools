#PATH = r"/home/steve/Dropbox/Work/truck/50ptilePlots_2013-05-28/"
#PATH = r"C:\Users\sskripnik.LIMNO\Dropbox\Work\truck\50ptilePlots_2013-05-28\\"
#FILE = "Vista.csv"

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd
import os
from datetime import datetime


mpl.rc('lines', linewidth=1)
mpl.rc('font', size=9)
mpl.rc('axes', titlesize=15, labelsize=11, axisbelow=True)
mpl.rc('legend', fontsize=9) 

#File names
FNA_10 = 'PercentileCalcFNA_Q10.csv'
FNA_50 = 'PercentileCalcFNA_Q50.csv'

dir = os.path.dirname(__file__)

def cdir(nfile):
    return os.path.join(dir,nfile)

def get_ptile(dates,nfile,LOCAT):
    df_ptile = pd.read_csv(cdir(nfile), index_col=0, parse_dates=True)
    values = df_ptile[LOCAT].ix[dates].values
    return values

fig = plt.figure(figsize=[8.5,11])

##Read Location. Start here for individual location block
LOCAT = 'Farad'
PTILEHEADER = 'Farad'
InFile = 'Farad.csv'
df = pd.read_csv(cdir(InFile), index_col=0, usecols=[0,1,2,3,4,5,6,7,8], parse_dates = True)
#merge data - for each date in plot data, assign matching month/day to 10%-ile
months = df.index.month
days = df.index.day
adjusteddate = [datetime(1900,m,d) for m,d in zip(months,days)]
df['FNA 10%-ile']=get_ptile(adjusteddate,FNA_10,PTILEHEADER)
df['FNA 50%-ile']=get_ptile(adjusteddate,FNA_50,PTILEHEADER)

#


ax = fig.add_subplot(3,1,1)

l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1970'],'v-',label='FNA 1970')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1973'],'v-',label='FNA 1973')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1985'],'v-',label='FNA 1985')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1987'],'v-',label='FNA 1987')
l3, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1993'],'v-',label='FNA 1993')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 2000'],'v-',label='FNA 2000')
l1, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1977'],'-',label='FNA 1977',color='darkgrey')
l4, = ax.plot_date(df.index.to_pydatetime(),df['FNA 50%-ile'],'o',color='darkgrey',label='FNA 50%-ile')
l5, = ax.plot_date(df.index.to_pydatetime(),df['FNA 10%-ile'],'o',color='lightgrey',label='FNA 10%-ile')

#Settings
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
ax.xaxis.grid()
ax.yaxis.grid()
ax.legend()
plt.title('FNA Flow Comparison - Truckee River at '+LOCAT+'\n')
plt.xlabel('Month')
plt.ylabel('Flow (cfs)')
plt.tight_layout()

##Read Location. Start here for individual location block
LOCAT = 'Vista'
PTILEHEADER = 'Vista'
InFile = 'Vista.csv'
df = pd.read_csv(cdir(InFile), index_col=0, usecols=[0,1,2,3,4,5,6,7,8], parse_dates = True)
#merge data - for each date in plot data, assign matching month/day to 10%-ile
months = df.index.month
days = df.index.day
adjusteddate = [datetime(1900,m,d) for m,d in zip(months,days)]
df['FNA 10%-ile']=get_ptile(adjusteddate,FNA_10,PTILEHEADER)
df['FNA 50%-ile']=get_ptile(adjusteddate,FNA_50,PTILEHEADER)

#


ax = fig.add_subplot(3,1,2)

l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1970'],'v-',label='FNA 1970')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1973'],'v-',label='FNA 1973')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1985'],'v-',label='FNA 1985')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1987'],'v-',label='FNA 1987')
l3, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1993'],'v-',label='FNA 1993')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 2000'],'v-',label='FNA 2000')
l1, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1977'],'-',label='FNA 1977',color='darkgrey')
l4, = ax.plot_date(df.index.to_pydatetime(),df['FNA 50%-ile'],'o',color='darkgrey',label='FNA 50%-ile')
l5, = ax.plot_date(df.index.to_pydatetime(),df['FNA 10%-ile'],'o',color='lightgrey',label='FNA 10%-ile')

#Settings
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
ax.xaxis.grid()
ax.yaxis.grid()
ax.legend()
plt.title('FNA Flow Comparison - Truckee River at '+LOCAT+'\n')
plt.xlabel('Month')
plt.ylabel('Flow (cfs)')
plt.tight_layout()

##Read Location. Start here for individual location block
LOCAT = 'Below Derby'
PTILHEADER = 'BelowDerby'
InFile = 'BelowDerby.csv'
df = pd.read_csv(cdir(InFile), index_col=0, usecols=[0,1,2,3,4,5,6,7,8], parse_dates = True)
#merge data - for each date in plot data, assign matching month/day to 10%-ile
months = df.index.month
days = df.index.day
adjusteddate = [datetime(1900,m,d) for m,d in zip(months,days)]
df['FNA 10%-ile']=get_ptile(adjusteddate,FNA_10,PTILEHEADER)
df['FNA 50%-ile']=get_ptile(adjusteddate,FNA_50,PTILEHEADER)

#


ax = fig.add_subplot(3,1,3)
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1970'],'v-',label='FNA 1970')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1973'],'v-',label='FNA 1973')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1985'],'v-',label='FNA 1985')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1987'],'v-',label='FNA 1987')
l3, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1993'],'v-',label='FNA 1993')
l2, = ax.plot_date(df.index.to_pydatetime(),df['FNA 2000'],'v-',label='FNA 2000')
l1, = ax.plot_date(df.index.to_pydatetime(),df['FNA 1977'],'-',label='FNA 1977',color='darkgrey')
l4, = ax.plot_date(df.index.to_pydatetime(),df['FNA 50%-ile'],'o',color='darkgrey',label='FNA 50%-ile')
l5, = ax.plot_date(df.index.to_pydatetime(),df['FNA 10%-ile'],'o',color='lightgrey',label='FNA 10%-ile')

#Settings
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
ax.xaxis.grid()
ax.yaxis.grid()
ax.legend()
plt.title('FNA Flow Comparison - Truckee River at '+LOCAT+'\n')
plt.xlabel('Month')
plt.ylabel('Flow (cfs)')
plt.tight_layout()

#wrap it up
plt.savefig(dir+"/FNAPlots_AllYears.png",dpi=300)
plt.show()

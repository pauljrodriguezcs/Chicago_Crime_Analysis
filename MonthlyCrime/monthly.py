import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

print("loading time series1... ")
timeSeries = np.loadtxt('AssaultYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
labels = timeSeries[:,1]
plt.plot(monthly,'r-', label='assault')

# print("loading time series2... ")
# timeSeries = np.loadtxt('BatteryTS.txt',delimiter=',',dtype=float) # load data
# hourly = timeSeries[:,0]
# plt.plot(hourly,'b-', label='battery')

# print("loading time series3... ")
# timeSeries = np.loadtxt('CriminalDamageTS.txt',delimiter=',',dtype=float) # load data
# hourly = timeSeries[:,0]
# plt.plot(hourly,'m-', label='CriminalDamage')

# print("loading time series4... ")
# timeSeries = np.loadtxt('TarcoticsTS.txt',delimiter=',',dtype=float) # load data
# hourly = timeSeries[:,0]
# plt.plot(hourly,'c-', label='narcotics')

# print("loading time series5... ")
# timeSeries = np.loadtxt('TheftTS.txt',delimiter=',',dtype=float) # load data
# hourly = timeSeries[:,0]
# plt.plot(hourly,'k-', label='theft')

print("plotting...")
l = np.arange(2001,2018,step=12)
plt.xticks(np.arange(216),l)
plt.grid(True)
plt.legend()
plt.title('Crime per Month')
plt.show()
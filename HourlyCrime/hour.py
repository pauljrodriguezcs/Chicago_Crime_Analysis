import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

print("loading time series... ")
timeSeries = np.loadtxt('AssaultTS.txt',delimiter=',',dtype=float) # load data
print("done ... ")

hourly = timeSeries[:,0]
plt.plot(hourly,'r-', label='assault')

timeSeries = np.loadtxt('BatteryTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'b-', label='battery')

timeSeries = np.loadtxt('CriminalDamageTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'m-', label='CriminalDamage')

timeSeries = np.loadtxt('TarcoticsTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'c-', label='narcotics')

timeSeries = np.loadtxt('TheftTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'k-', label='theft')

plt.xticks(np.arange(0,24,step=1))
plt.grid(True)
plt.legend()
plt.title('Crime per Hour')
plt.show()
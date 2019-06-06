import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

print("loading time series... ")
plt.figure(figsize=(16,9))

timeSeries = np.loadtxt('TheftTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'r-', label='theft')

timeSeries = np.loadtxt('BatteryTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'g-', label='battery')

timeSeries = np.loadtxt('CriminalDamageTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'b-', label='CriminalDamage')

timeSeries = np.loadtxt('TarcoticsTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'c-', label='narcotics')

timeSeries = np.loadtxt('AssaultTS.txt',delimiter=',',dtype=float) # load data
hourly = timeSeries[:,0]
plt.plot(hourly,'m-', label='assault')

plt.xticks(np.arange(0,24,step=1))
plt.grid(True)
plt.legend()
plt.xlabel('Hour')
plt.ylabel('Total Crimes')
plt.title('Crime per Hour')
# plt.show()
plt.savefig('CrimePerHour.png',format='png',dpi=600)
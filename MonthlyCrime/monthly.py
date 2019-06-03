import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

'''
print("loading time series1... ")
timeSeries = np.loadtxt('TheftYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'r-', label='Theft')

print("loading time series2... ")
timeSeries = np.loadtxt('BatteryYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'g-', label='Battery')

print("loading time series3... ")
timeSeries = np.loadtxt('CriminalDamageYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'b-', label='CriminalDamage')
print("loading time series4... ")
timeSeries = np.loadtxt('NarcoticsYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'c-', label='Narcotics')
'''
print("loading time series5... ")
timeSeries = np.loadtxt('AssaultYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
labels = timeSeries[:,1]
plt.plot(monthly,'m-', label='Assault')

print("plotting...")
plt.xticks(np.arange(1,(12*18)+1,step=12))
plt.grid(True)
plt.legend()
plt.axis([1,216,0,10100])
plt.title('Crime per Month')
plt.show()
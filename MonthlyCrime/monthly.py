import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

l = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011'
,'2012','2013','2014','2015','2016','2017','2018','2019']

### Individual graphs

print("loading time series1... ")
plt.figure(figsize=(16,9))
timeSeries = np.loadtxt('TheftYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'r-', label='Theft')
plt.xticks(np.arange(1,(12*18)+2,step=12),l)
plt.grid(True)
plt.legend()
plt.axis([1,217,0,10100])
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.title('Crime per Year')
# plt.show()
plt.savefig('TheftperMonth.png',format='png',dpi=600)

print("loading time series2... ")
plt.figure(figsize=(16,9))
timeSeries = np.loadtxt('BatteryYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'g-', label='Battery')
plt.xticks(np.arange(1,(12*18)+2,step=12),l)
plt.grid(True)
plt.legend()
plt.axis([1,217,0,10100])
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.title('Crime per Year')
# plt.show()
plt.savefig('BatteryperMonth.png',format='png',dpi=600)


print("loading time series3... ")
plt.figure(figsize=(16,9))
timeSeries = np.loadtxt('CriminalDamageYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'b-', label='Criminal_Damage')
plt.xticks(np.arange(1,(12*18)+2,step=12),l)
plt.grid(True)
plt.legend()
plt.axis([1,217,0,10100])
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.title('Crime per Year')
# plt.show()
plt.savefig('CriminalDamageperMonth.png',format='png',dpi=600)


print("loading time series4... ")
plt.figure(figsize=(16,9))
timeSeries = np.loadtxt('NarcoticsYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'c-', label='Narcotics')
plt.xticks(np.arange(1,(12*18)+2,step=12),l)
plt.grid(True)
plt.legend()
plt.axis([1,217,0,10100])
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.title('Crime per Year')
# plt.show()
plt.savefig('NarcoticsperMonth.png',format='png',dpi=600)


print("loading time series5... ")
plt.figure(figsize=(16,9))
timeSeries = np.loadtxt('AssaultYearMonth.txt',delimiter=',',dtype=float) # load data
monthly = timeSeries[:,0]
plt.plot(monthly,'m-', label='Assault')
plt.xticks(np.arange(1,(12*18)+2,step=12),l)
plt.grid(True)
plt.legend()
plt.axis([1,217,0,10100])
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.title('Crime per Year')
# plt.show()
plt.savefig('AssaultperMonth.png',format='png',dpi=600)


### All Graphs in One

# print("plotting...")
# plt.figure(figsize=(16,9))

# timeSeries = np.loadtxt('TheftYearMonth.txt',delimiter=',',dtype=float) # load data
# monthly = timeSeries[:,0]
# plt.plot(monthly,'r-', label='Theft')

# timeSeries = np.loadtxt('BatteryYearMonth.txt',delimiter=',',dtype=float) # load data
# monthly = timeSeries[:,0]
# plt.plot(monthly,'g-', label='Battery')

# timeSeries = np.loadtxt('CriminalDamageYearMonth.txt',delimiter=',',dtype=float) # load data
# monthly = timeSeries[:,0]
# plt.plot(monthly,'b-', label='Criminal_Damage')

# timeSeries = np.loadtxt('NarcoticsYearMonth.txt',delimiter=',',dtype=float) # load data
# monthly = timeSeries[:,0]
# plt.plot(monthly,'c-', label='Narcotics')

# timeSeries = np.loadtxt('AssaultYearMonth.txt',delimiter=',',dtype=float) # load data
# monthly = timeSeries[:,0]
# plt.plot(monthly,'m-', label='Assault')

# plt.xticks(np.arange(1,(12*18)+2,step=12),l)
# plt.grid(True)
# plt.legend()
# plt.axis([1,217,0,10100])
# plt.xlabel('Year')
# plt.ylabel('Total Crimes')
# plt.title('Crime per Year')
# plt.show()
# plt.savefig('AllCrimes.png',format='png',dpi=600)
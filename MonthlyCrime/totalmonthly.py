import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

l = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011'
,'2012','2013','2014','2015','2016','2017','2018','2019']

### All Graphs in One

total_crime = None

timeSeries = np.loadtxt('TheftYearMonth.txt',delimiter=',',dtype=float) # load data
theft = timeSeries[:,0]

timeSeries = np.loadtxt('BatteryYearMonth.txt',delimiter=',',dtype=float) # load data
battery = timeSeries[:,0]

timeSeries = np.loadtxt('CriminalDamageYearMonth.txt',delimiter=',',dtype=float) # load data
criminal_damage = timeSeries[:,0]

timeSeries = np.loadtxt('NarcoticsYearMonth.txt',delimiter=',',dtype=float) # load data
narcotics = timeSeries[:,0]

timeSeries = np.loadtxt('AssaultYearMonth.txt',delimiter=',',dtype=float) # load data
assault = timeSeries[:,0]

total_crime = theft + battery + criminal_damage + narcotics + assault

# print(total_crime)

timeSeries = np.loadtxt('ArrestYearMonth.txt', delimiter=',',dtype=float)
arrest = timeSeries[:,0]

plt.figure(figsize=(16,9))
plt.plot(total_crime,'k-', label='Total Crimes')
plt.plot(arrest, 'r-',label='Total Arrests')
plt.xticks(np.arange(1,(12*18)+2,step=12),l)
plt.grid(True)
plt.legend()
plt.axis([1,217,0,32500])
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.title('Crime vs Arrests')
# plt.show()
plt.savefig('CrimesVsArrests.png',format='png',dpi=600)
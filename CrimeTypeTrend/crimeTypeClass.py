import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.linalg as la

print("loading CrimeMapPerMonth... ")
CrimeMap = np.loadtxt('LatLongZip.txt',delimiter=',',dtype=float) # load data
print("done ... ")

### Fall

print("loading ... ")
CrimePerZipcode = np.loadtxt('Fall2001to2006.txt',delimiter=',',dtype=float)
print("done ... ")

# 1: theft
# 2: battery
# 3: criminal damage
# 4: narcotics
# 5: assault
# 6: other

x_coord = []
y_coord = []
crimes = [1.0,2.0,3.0,4.0,5.0,6.0]

print("for loop ... ")
colors = ['r','b', 'g', 'c', 'y','k']

plt.figure()

for c in range(len(crimes)):
	print(crimes[c])
	# plt.subplot(2,3,(c+1))
	x = []
	y = []
	for i in range(CrimePerZipcode.shape[0]):
		crime = CrimePerZipcode[i][2]
		if(crime == crimes[c]):
			for j in range(CrimeMap.shape[0]):
				zipcode = CrimePerZipcode[i][1] 
				zc = CrimeMap[j][2]				
				if(zipcode == zc):
					x.append(CrimeMap[j][0])
					y.append(CrimeMap[j][1])

	x_coord.append(x)
	y_coord.append(y)

print("done ... ")
print("plotting ... ")
for ind in range(len(x_coord)):
	plt.plot(y_coord[ind],x_coord[ind],color=colors[ind],marker=',',linestyle='None')
plt.title("Fall 2001-2006")
plt.axis([-87.96,-87.49,41.6,42.1])
plt.show()

### Spring

print("loading ... ")
CrimePerZipcode = np.loadtxt('Spring2001to2006.txt',delimiter=',',dtype=float)
print("done ... ")

# 1: theft
# 2: battery
# 3: criminal damage
# 4: narcotics
# 5: assault
# 6: other

x_coord = []
y_coord = []
crimes = [1.0,2.0,3.0,4.0,5.0,6.0]

print("for loop ... ")
colors = ['r','b', 'g', 'c', 'y','k']

plt.figure()

for c in range(len(crimes)):
	print(crimes[c])
	# plt.subplot(2,3,(c+1))
	x = []
	y = []
	for i in range(CrimePerZipcode.shape[0]):
		crime = CrimePerZipcode[i][2]
		if(crime == crimes[c]):
			for j in range(CrimeMap.shape[0]):
				zipcode = CrimePerZipcode[i][1] 
				zc = CrimeMap[j][2]				
				if(zipcode == zc):
					x.append(CrimeMap[j][0])
					y.append(CrimeMap[j][1])

	x_coord.append(x)
	y_coord.append(y)

print("done ... ")
print("plotting ... ")
for ind in range(len(x_coord)):
	plt.plot(y_coord[ind],x_coord[ind],color=colors[ind],marker=',',linestyle='None')
plt.title("Spring 2001-2006")
plt.axis([-87.96,-87.49,41.6,42.1])
plt.show()

### Summer

print("loading ... ")
CrimePerZipcode = np.loadtxt('Summer2001to2006.txt',delimiter=',',dtype=float)
print("done ... ")

# 1: theft
# 2: battery
# 3: criminal damage
# 4: narcotics
# 5: assault
# 6: other

x_coord = []
y_coord = []
crimes = [1.0,2.0,3.0,4.0,5.0,6.0]

print("for loop ... ")
colors = ['r','b', 'g', 'c', 'y','k']

plt.figure()

for c in range(len(crimes)):
	print(crimes[c])
	# plt.subplot(2,3,(c+1))
	x = []
	y = []
	for i in range(CrimePerZipcode.shape[0]):
		crime = CrimePerZipcode[i][2]
		if(crime == crimes[c]):
			for j in range(CrimeMap.shape[0]):
				zipcode = CrimePerZipcode[i][1] 
				zc = CrimeMap[j][2]				
				if(zipcode == zc):
					x.append(CrimeMap[j][0])
					y.append(CrimeMap[j][1])

	x_coord.append(x)
	y_coord.append(y)

print("done ... ")
print("plotting ... ")
for ind in range(len(x_coord)):
	plt.plot(y_coord[ind],x_coord[ind],color=colors[ind],marker=',',linestyle='None')
plt.title("Summer 2001-2006")
plt.axis([-87.96,-87.49,41.6,42.1])
plt.show()

### Winter

print("loading ... ")
CrimePerZipcode = np.loadtxt('Winter2001to2006.txt',delimiter=',',dtype=float)
print("done ... ")

# 1: theft
# 2: battery
# 3: criminal damage
# 4: narcotics
# 5: assault
# 6: other

x_coord = []
y_coord = []
crimes = [1.0,2.0,3.0,4.0,5.0,6.0]

print("for loop ... ")
colors = ['r','b', 'g', 'c', 'y','k']

plt.figure()

for c in range(len(crimes)):
	print(crimes[c])
	# plt.subplot(2,3,(c+1))
	x = []
	y = []
	for i in range(CrimePerZipcode.shape[0]):
		crime = CrimePerZipcode[i][2]
		if(crime == crimes[c]):
			for j in range(CrimeMap.shape[0]):
				zipcode = CrimePerZipcode[i][1] 
				zc = CrimeMap[j][2]				
				if(zipcode == zc):
					x.append(CrimeMap[j][0])
					y.append(CrimeMap[j][1])

	x_coord.append(x)
	y_coord.append(y)

print("done ... ")
print("plotting ... ")
for ind in range(len(x_coord)):
	plt.plot(y_coord[ind],x_coord[ind],color=colors[ind],marker=',',linestyle='None')
plt.title("Winter 2001-2006")
plt.axis([-87.96,-87.49,41.6,42.1])
plt.show()


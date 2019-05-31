import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import scipy.linalg as la
from scipy import stats

def makepoly(X,d):
    if d==0:
        return np.ones(X.shape)
    Xdminus1 = makepoly(X,d-1)
    l = np.hstack((Xdminus1,X*Xdminus1[:,-1,np.newaxis]))
    return l

def learnfn(X,Y,d,lmbda=0.0):
    M = makepoly(X,d)
    I0 = np.eye(d+1)
    w = np.linalg.inv(M.T@M + I0*lmbda)@(M.T@Y)
    return lambda x : makepoly(x[:,np.newaxis],d)@w

def plotfn(f,ax,color=None):
    xs = np.linspace(-2,2,100)
    ys = f(xs)
    hs = ax.plot(xs,ys)
    if color is not None:
        for h in hs:
            h.set_color(color)
    return hs

D = np.loadtxt('newyearvscrime.txt',dtype=int) # load data
trainX = D[:,0:1] # split first column into X
trainY = D[:,-1] # and last column into Y

# trainX = stats.zscore(trainX)

testX = np.arange(2001,2025,step=1)
# testX = stats.zscore(testX)



# testing
# fun = learnfn(trainX,trainY,5,0.01)
# testY = fun(testX)
## hs = plotfn(learnfn(trainX,trainY,5,0.01),ax,'red')
# ax.plot(testX,testY,'r-')
# ax.plot(trainX,trainY,'bo')
## ax.axis([-2,2,0,500000])
# ax.set_xlabel('year')
# ax.set_ylabel('total crimes')
## ax.set_yticklabels(np.arange(0, 500000, step=100000))
## xticks = np.arange(1,25,step=1)
## ax.xaxis.set_major_locator(mticker.FixedLocator(xticks))
## ax.set_xlim(left=0,right=26)
## ax.set_xticklabels(np.arange(0,20,step=1))
# ax.set_title("Crime Rate Prediction")

# fig = plt.figure(figsize=(16,4))
# ax = fig.add_subplot(3,2,6)
# deg = np.arange(4,10,step=1)
# ind = 1
# for i in deg:
#     plt.subplot(3,2,ind)
#     fun = learnfn(trainX,trainY,i,1)
#     testY = fun(testX)
#     plt.plot(testX,testY,'r-')
#     plt.plot(trainX,trainY,'bo')
#     # plt.set_xlabel('year')
#     # plt.set_ylabel('total crimes')
#     ind += 1

fun = learnfn(trainX,trainY,6,1)
testY = fun(testX)
newX = testX[trainX.size:,]
newY = np.ceil(testY[trainY.size:,])

plt.plot(testX,testY,'r-')
plt.plot(trainX,trainY,'bo')
plt.plot(newX,newY,'go')

plt.axis([2000,2025,0,500000])
plt.xticks(np.arange(2000,2025,step=1))
plt.yticks(np.arange(0,500000,step=25000))
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.title("Crime Rate Prediction")


# working
# hs = plotfn(learnfn(trainX,trainY,5,0.01),ax,'red')
# ax.plot(trainX,trainY,'go')
# ax.axis([-2,2,0,500000])
# ax.set_xlabel('year')
# ax.set_ylabel('total crimes')
# ax.set_yticklabels(np.arange(0, 900000, step=100000))
# ax.set_xticklabels(np.arange(0,20,step=1))
# ax.set_title("Crime Rate Prediction")
plt.show()
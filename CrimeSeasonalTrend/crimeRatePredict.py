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


testX = np.arange(2001,2025,step=1)


fun = learnfn(trainX,trainY,6,1)
testY = fun(testX)
newX = testX[trainX.size:,]
newY = np.ceil(testY[trainY.size:,])

plt.figure(figsize=(16,9))

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

# plt.show()
plt.savefig('crimerateprediction.png',format='png',dpi=600)
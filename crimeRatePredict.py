import numpy as np
import matplotlib.pyplot as plt
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

D = np.loadtxt('yearvscrime.txt',dtype=int) # load data
trainX = D[:,0:1] # split first column into X
trainY = D[:,-1] # and last column into Y

trainX = stats.zscore(trainX)

fig = plt.figure(figsize=(12,4))
ax = fig.add_subplot(1,1,1)
hs = plotfn(learnfn(trainX,trainY,6,0.1),ax,'red')
ax.plot(trainX,trainY,'go')
ax.axis([-1.5,2,0,900000])
ax.set_xlabel('year')
ax.set_ylabel('total crimes')
ax.set_yticklabels(np.arange(0, 900000, step=100000))
ax.set_xticklabels([])
ax.set_title("Crime Rate Prediction")
plt.show()
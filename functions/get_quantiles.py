import numpy as np

def get_quantiles(X):
    q1=np.zeros([len(X),3])
    q99=np.zeros([len(X),3])
    for i in range(0,len(X)):
        q1[i]=[np.percentile(X[i,:,:,0],q=1,),np.percentile(X[i,:,:,1],q=1,),np.percentile(X[i,:,:,2],q=1,)]
        q99[i]=[np.percentile(X[i,:,:,0],q=99,),np.percentile(X[i,:,:,1],q=99,),np.percentile(X[i,:,:,2],q=99,)]
    return(q1, q99)
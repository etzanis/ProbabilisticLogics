# minimum common expansion 
# using numpy arrays

import numpy as np
a = np.array([[2,7,1,3], [4,2,1,5], [6,2,9,4]]); 
c=[None]*len(a)
def my_func(a, index, value): 
    if(a[index]!=value and a[index]-value>0):
            a=np.insert(a, (index+1), a[index]-value); a[index]=value;
    else:
        a=np.insert(a, a.shape, 0);

    return a

for x in range(len(a)*len(a)):
    temp=[]
    unique, counts = np.unique(np.sort(a[:, x]), return_counts=True)
    temp=dict(zip(unique, counts));
    # last current element for all rows has the same value
    if(counts[0]==len(a) or temp.get(0)==len(a)-1): break;
    index=0;
    for y in a: 
         z=a[np.asarray(np.nonzero(a[:,x]))][0];
         b=my_func(y,x,z[:,x].min(axis=0)); print('B',b); c[index]=b; index+=1;    
    a=np.asarray(c)
a

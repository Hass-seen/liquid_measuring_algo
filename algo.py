

import numpy as np




def  AgreedWay(l,x):
    a=x
    l= np.trim_zeros(l)
    a+= l.count(0)
    L=[i - 1 for i in l]
    l = [0 if i < 0 else i for i in L]
    if(len(list(filter(lambda x: (x > 0), l))) != 1):
        return AgreedWay(l,a)
    else:

        return a




l = [3,0,2,0,4]
print(AgreedWay(l,0))





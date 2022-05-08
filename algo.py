

import numpy as np




def  AgreedWay(l,x):
    a=x
    np.trim_zeros(l)
    print(l)
    a+= l.count(0)
    print(a)
    l=[i - 1 for i in l]
    if(len(list(filter(lambda x: (x >= 0), l))) != 0):
        AgreedWay(l,a)
    else:
        
        return a




l = [1,0,2,0,2,0]
print(AgreedWay(l,0))







import numpy as np




def  AgreedWay(l,x):
    a=x  #a is the counter of the aria of the body of water 
    l= np.trim_zeros(l) #removes leading and trailing Zeros from the list
    a+= l.count(0)  # counts the number of Zeros left and adds it to the aria
    L=[i - 1 for i in l]  # decriments every eliment of the list by 1
    l = [0 if i < 0 else i for i in L]  # replaces every negative number with a Zero
    if(len(list(filter(lambda x: (x > 0), l))) != 1): #if there is only one non zero value left the recursion stops
        return AgreedWay(l,a)
    else:

        return a #returns the aria of the body of water




l = [3,0,2,0,4]
print(AgreedWay(l,0))





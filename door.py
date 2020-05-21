import random
import numpy as np
n=0
a=[]

while n<100:
    q=(np.random.randint(2))
    # print(q)
    n+=1
    a.append(q)
n=0
for index,v in enumerate(a):
    if index%2 ==0:
        if v==0:
            a[index]=1
    else:
        if v==1:
            a[index]=0
for i in a:
    if i==1:
        n+=1
print(n)
x1=[int(x) for x in input().split()]
x2=[int(x) for x in input().split()]
a=0
b=0
for i in range(3):
    if x1[i]>x2[i]:
        a+=1
    elif x1[i]<x2[i]:
        b+=1
    
print(a,b)
x=[int(x) for x in input().split()]
print(x)
maxx=max(x)
minn=min(x)
mini=10000
new=[]
for i in range(len(x)-1):
    mini=min(mini,x[i+1]-x[i])

for i in range(round(maxx/minn)):
    temp=minn+(mini * (i))
    if temp not in x:
        new.append(minn+(mini * (i)))
print(new)
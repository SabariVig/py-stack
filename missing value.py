mini =10000
new=[]
n=[int(x) for x in input().split()]
maxl=max(n)
minl=min(n)

for i in range(len(n)-1):
    mini=min(mini,n[i+1]-n[i])

for i in range(round(maxl/minl)):
    temp=minl+(mini * (i))
    if temp not in n:
        new.append(minl+(mini * (i)))

print(new)
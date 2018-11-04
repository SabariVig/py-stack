n=int(input("Enter The No Of Towers"))
q=[int(x) for x in input().split()]
f,c,sum_p,s = 0 ,0,0,0
for i in range(0,n):
    if q[i] != 0:
        if not f:
            f=q[i]
        else:
            s=q[i]
    if q[i] == 0 and f:
        c+=1
    if f and s:
        sum_p += c * (min(f,s))
        c=0
        f=s
        s=0
    
print("Water Amount is  ",sum_p)






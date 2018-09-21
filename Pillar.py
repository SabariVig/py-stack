# import copy

# def set_var(a,b):
#     return a if a<b else b

# c=0
# n=int(input())
# x=[int(x) for x in input().split()]
# q=copy.deepcopy(x)
# for i in x:
#     print(i)
#     if i == 0:
#         x.pop(i)
# print(x)
# print(q)

# for i in q:
#     for j in x:
#         set_v=set_var(j,j+1)
#     if i == 0:
#         q[i]=set_v
#     print(i,j)

# print(q)



count=0
a=[int(x) for x in input().split()]
x=[x for x in a if x!=0]
print(x)
print(a)
mm=[x[i:i + 2] for i in range(0, len(x), 2)]
for i in a:
    for j in range(len(x)):
        for k in range(1,len(x),1):
            if i == 0:
                set_var = x[j] if x[j]<=x[k] else x[k]
                try:
                    n=a.index(i)
                    a[n]=set_var
                    count+=a[n]
                except:pass
print(a)
print(count)
print(mm)
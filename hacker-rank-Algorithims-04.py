q=input()
x=[x for x in input().split()]
x1=[x for x in input().split()]
x2=[x for x in input().split()]
# x=[11,2,4]
# x1=[4,5,6]
# x2=[10,8,-12]
a=0
b=0
x=[x,x1,x2]
for i in range(3):
    a+=x[i][i]
    b+=x[i][3-i-1]
print(abs(a-b))
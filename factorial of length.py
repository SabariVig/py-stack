def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

sum_p,no=0,0
n=input().split()
print(n)
for i in n:
    no=fact(len(i))
    sum_p+=no
print(sum_p)
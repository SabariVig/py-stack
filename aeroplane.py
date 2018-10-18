q=int(input("No Of Rows"))
w=[]
for i in range(q):
    p= [[int(x)  for x in (input(f"Enter  AxB For The {i+1}th  Row").split())]]
    w+=p
print("P =",p,"\n","W =",w)



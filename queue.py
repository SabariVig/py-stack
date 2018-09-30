import os
q=[]
output=""
while True:
    print(f"{output}")
    ch=int(input("1.Insert\n2.Remove\n3.Display\n4.Exit\nEnter Your Choice"))
    if ch == 1:
        if len(q)> 9: #The Queue Size Is 10 
            output=("Queue OverFlow")
        else:
            q.append(input("Enter The Variable"))
            output= f"Item Inserted is {q[-1]}"
    if ch == 2:
        if len(q) == 0:
            output="UnderFlow"
        else:
            output= f"{q.pop(0)} was removed"
    if ch == 3:
        if len(q) == 0:
            output="Queue Empty"
        else:
            output=(q)
    if ch==4:
        break
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")

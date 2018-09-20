import random
num=random.randint(1,10)
guess=int(input("Guess A No Between 1 To 10:"))
a=1
while num!=guess:
    a=a+1    
    if guess<num:
        print("Guess a Higher Number")
        guess=int(input("Enter A number"))

    else:        
        print("Guess A  Lower Number")
        guess=int(input("Enter A no"))                  
print("You Gussed The Correct No In",a,"No Of Tries")

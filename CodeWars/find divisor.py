##################  CODE WARS KATA ##################
#KYU LEVEL : 6
#KATA TITLE : Find The Minimum Number Divisible by Integers of an Array I
#KATA LINK :  https://www.codewars.com/kata/find-the-minimum-number-divisible-by-integers-of-an-array-i
#####################################################

def min_special_mult(arr):
    flag=1
    x=[]
    c=1
    #clean the list
    try:
        for i in arr:
            x.append(int(i))
    except:
        pass
    for _ in range(10000):
        for i in x:
            if c%i !=0:
                c +=1
    return(c) 








##################  TEST CASES  ##################
arr = [2, 3 ,4 ,5, 6, 7]
print(min_special_mult(arr), 420)
arr = [18, 22, 4, 3, 21, 6, 3]
print(min_special_mult(arr), 2772)

arr = [16, 15, 23, 'a', '&', '12']
print(min_special_mult(arr), "There are 2 invalid entries: ['a', '&']")

arr = [16, 15, 23, 'a', '&', '12', 'a']
print(min_special_mult(arr), "There are 3 invalid entries: ['a', '&', 'a']")
arr = [16, 15, 23, 'a', '12']
print(min_special_mult(arr), "There is 1 invalid entry: a")
arr = [16, 15, 23, '12']
print(min_special_mult(arr), 5520)
arr = [16, 15, 23, '012']
print(min_special_mult(arr), 5520)
arr = [18, 22, 4, None, 3, 21, 6, 3]
print(min_special_mult(arr), 2772)
arr = [18, 22, 4, None, 3, -21, 6, 3]
print(min_special_mult(arr), 2772)
arr = [16, 15, 23, '-012']
print(min_special_mult(arr), 5520)
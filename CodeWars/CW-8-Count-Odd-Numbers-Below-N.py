""" 
https://www.codewars.com/kata/count-odd-numbers-below-n/train/python

Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
 """
 
q=15023
print((q//2))

#Final Sol#
def odd_count(n):
    return (n//2)
##----##

print(odd_count(15),7)
print(odd_count(15023),7511)
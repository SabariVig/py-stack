"""
https://www.codewars.com/kata/simple-fun-number-176-reverse-letter/train/python
Task
Given a string str, reverse it omitting all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str

A string consists of lowercase latin letters, digits and symbols.

[output] a string """
st1=[]
def reverse_letter(string):
    # print(string)
    string=string.split()
    for i in string:
        if i.isalpha():
            st1=st1.append(i)


print(reverse_letter("krishan"),"nahsirk")
print(reverse_letter("ultr53o?n"),"nortlu")
print(reverse_letter("ab23c"),"cba")
print(reverse_letter("krish21an"),"nahsirk")
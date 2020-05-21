##################  CODE WARS KATA ##################
#KYU LEVEL : 6
#KATA TITLE : Framed Reflection
#KATA LINK :  https://www.codewars.com/kata/framed-reflection/train/python
#####################################################

def mirror(text):
   q=[]
   text=text.split()
   q.append("*"*(len(text[0])+4))
   for i in text:
       q.append(("* "+i[::-1]+" *"))
   q.append("*"*(len(text[0])+4))
   return("\n".join(q))







##################  TEST CASES  ##################
# mirror("Hello World")
print(mirror("Hello World"), "*********\n* olleH *\n* dlroW *\n*********");
# print(mirror("Codewars"), "************\n* srawedoC *\n************"); 


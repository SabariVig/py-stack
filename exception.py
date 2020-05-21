def fun(s,ss):
    c=0
    for i in range(len(s)-(len(ss)-1)):
        if(ss in s[i:i+len(ss)]):
            c+=1
    return(c)

fun("ABCDCDC","CDC") 